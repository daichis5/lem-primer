"""Find the factor of safety of one slip surface by 3D columns (Practice 3).

x points right, y points horizontally away from the viewer, and z points up. The
slope is that of Practice 2 extended in y, and the soil slides toward negative x.
The normal vector n points out of the sliding mass. Lengths are in m, forces in kN.
"""

import math
from dataclasses import dataclass

import numpy as np

import slices

GRAVITY = np.array([0.0, 0.0, -1.0])  # direction of gravity


def ground(x, y):
    """Height of the ground: the slope of Practice 2, extended in y."""
    return slices.ground(x)


class Ellipsoid:
    """An ellipsoid with axes along x, y and z. Its lower half is the slip surface."""

    def __init__(self, center, radii):
        self.center = np.array(center, dtype=float)
        self.radii = np.array(radii, dtype=float)
        cx, cy, _ = self.center
        rx, ry, _ = self.radii
        # the plan area the slip surface can cover
        self.bounds = (cx - rx, cx + rx, cy - ry, cy + ry)

    def z(self, x, y):
        """Height where a vertical line meets the lower surface; nan where it misses."""
        cx, cy, cz = self.center
        rx, ry, rz = self.radii
        q = 1.0 - ((x - cx) / rx) ** 2 - ((y - cy) / ry) ** 2
        return np.where(q > 0.0, cz - rz * np.sqrt(np.abs(q)), np.nan)

    def normal(self, x, y, z):
        """Outward unit normal of the ellipsoid (out of the sliding mass).

        The shape is (number of points, 3).
        """
        g = (np.stack([x, y, z], axis=-1) - self.center) / self.radii**2
        return g / np.linalg.norm(g, axis=-1, keepdims=True)


class Cylinder:
    """The circle of Practice 2 extended a length length in y, as a slip surface.

    Vertical planes cut its two ends.
    """

    def __init__(self, length, circle=None):
        self.circle = circle or slices.Circle()
        self.length = length
        self.bounds = (self.circle.x0, self.circle.x1, -length / 2, length / 2)

    def z(self, x, y):
        c = self.circle
        inside = (x > c.x0) & (x < c.x1) & (np.abs(y) < self.length / 2)
        return np.where(inside, c.z(np.clip(x, c.x0, c.x1)), np.nan)

    def normal(self, x, y, z):
        cx, cz = self.circle.center
        g = np.stack([x - cx, np.zeros_like(x), z - cz], axis=-1)
        return g / np.linalg.norm(g, axis=-1, keepdims=True)


class Plane:
    """A plane slip surface a vertical depth depth below the ground z = x tan(beta).

    Give beta_deg in degrees; the plane covers the plan area bounds = (x0, x1, y0, y1).
    Pass plane.ground as ground.
    """

    def __init__(self, beta_deg, depth, bounds=(0.0, 20.0, 0.0, 20.0)):
        self.tan_beta = math.tan(math.radians(beta_deg))
        self.depth = depth
        self.bounds = bounds

    def ground(self, x, y):
        return x * self.tan_beta

    def z(self, x, y):
        return x * self.tan_beta - self.depth

    def normal(self, x, y, z):
        n = np.array([self.tan_beta, 0.0, -1.0]) / math.hypot(self.tan_beta, 1.0)
        return np.tile(n, (len(x), 1))


@dataclass
class Columns:
    """The column table. Each quantity is an array in the order of the columns."""

    # base point on the central vertical and the slip surface; shape (columns, 3)
    base: np.ndarray
    top: np.ndarray  # where the same vertical meets the ground
    n: np.ndarray  # outward unit normal of the base
    A: np.ndarray  # base area [m²]
    W: np.ndarray  # weight [kN]
    u: np.ndarray  # pore water pressure on the base [kPa]
    c: np.ndarray  # cohesion c' [kPa]
    tan_phi: np.ndarray  # tan(phi')


def centres(lo, hi, h):
    """Centers of intervals of width h that cover lo to hi.

    The intervals are symmetric about the midpoint of lo and hi.
    """
    k = math.ceil((hi - lo) / (2 * h))
    return 0.5 * (lo + hi) + h * (np.arange(-k, k) + 0.5)


def make_columns(
    surface, h, *, gamma=18.0, c=10.0, phi_deg=30.0, water_level=None, ground=ground
):
    """Split the plan into squares of side h and return the column table.

    A square becomes a column where the slip surface at its center is below the ground.
    The point on the central vertical and the tangent plane there represent each base.
    A water table water_level [m] makes the base pore pressure hydrostatic, measured
    vertically. A water table above the ground is cut to it; the soil weighs gamma.
    """
    x0, x1, y0, y1 = surface.bounds
    X, Y = np.meshgrid(centres(x0, x1, h), centres(y0, y1, h))
    x, y = X.ravel(), Y.ravel()
    z, zg = surface.z(x, y), ground(x, y)
    keep = np.isfinite(z) & (z < zg)
    x, y, z, zg = x[keep], y[keep], z[keep], zg[keep]
    n = surface.normal(x, y, z)
    if water_level is None:
        u = np.zeros(len(x))
    else:
        u = slices.GAMMA_W * np.clip(np.minimum(water_level, zg) - z, 0.0, None)
    return Columns(
        base=np.stack([x, y, z], axis=1),
        top=np.stack([x, y, zg], axis=1),
        n=n,
        A=h * h / np.abs(n[:, 2]),
        W=gamma * h * h * (zg - z),
        u=u,
        c=np.full(len(x), c),
        tan_phi=np.full(len(x), math.tan(math.radians(phi_deg))),
    )


def rotation_directions(col, axis):
    """Local direction of sliding on each base for a rotation about the axis axis.

    It is the direction of axis × n.
    """
    m = np.cross(axis, col.n)
    return m / np.linalg.norm(m, axis=1, keepdims=True)


def section_directions(col, d):
    """Direction along each base, toward d, in the vertical plane containing d.

    This is the choice of Hovland (1977). It equals the direction of rotation about
    the horizontal axis normal to d.
    """
    return rotation_directions(col, np.cross(d, [0.0, 0.0, 1.0]))


def projected_directions(col, d):
    """d projected onto the tangent plane of each base (Chapter 3, Section 8.2)."""
    p = d - (col.n @ d)[:, None] * col.n
    return p / np.linalg.norm(p, axis=1, keepdims=True)


def hovland(col, m):
    """Factor of safety by the Hovland method. m is the local direction of sliding.

    It ignores intercolumn forces and divides the summed resisting by driving forces.
    """
    N = col.W * (col.n @ GRAVITY)  # normal component of the weight
    S = col.c * col.A + (N - col.u * col.A) * col.tan_phi  # mobilizable shear force
    return np.sum(S) / np.sum(col.W * (m @ GRAVITY))


def arms(col, m, center, axis):
    """Moment arms of unit forces about the axis axis through the point center.

    In order: base shear force (direction m), weight (acting at mid-height of the
    column), and base normal force (direction n).
    """
    rb = col.base - center
    rg = 0.5 * (col.base + col.top) - center
    return (
        np.cross(rb, m) @ axis,
        np.cross(rg, np.broadcast_to(GRAVITY, rg.shape)) @ axis,
        np.cross(rb, col.n) @ axis,
    )


def hovland_moment(col, center, axis):
    """Ratio of moments about the axis axis, with the N of the Hovland method."""
    m = rotation_directions(col, axis)
    l_t, l_w, l_n = arms(col, m, center, axis)
    N = col.W * (col.n @ GRAVITY)
    S = col.c * col.A + (N - col.u * col.A) * col.tan_phi
    return np.sum(S * l_t) / np.sum(col.W * l_w - N * l_n)


def vertical_normal_force(col, m, fs):
    """Base normal force N from vertical force equilibrium of each column.

    Intercolumn forces are horizontal. m is the local direction of sliding.
    """
    nz, mz = col.n[:, 2], m[:, 2]
    U = col.u * col.A
    m_alpha = -nz - mz * col.tan_phi / fs
    if np.any(m_alpha <= 0.0):
        raise ValueError("m_alpha is zero or negative for some column")
    return (col.W + mz * (col.c * col.A - U * col.tan_phi) / fs) / m_alpha


def bishop(col, center, axis, fs=1.5, tol=1e-10, max_iter=100):
    """Factor of safety by the 3D simplified Bishop method (Hungr, 1987).

    N comes from vertical force equilibrium of each column, then the ratio of moments
    about the axis axis. F_s is on both sides, so it is iterated.
    """
    m = rotation_directions(col, axis)
    l_t, l_w, l_n = arms(col, m, center, axis)
    for _ in range(max_iter):
        N = vertical_normal_force(col, m, fs)
        S = col.c * col.A + (N - col.u * col.A) * col.tan_phi
        new = np.sum(S * l_t) / np.sum(col.W * l_w - N * l_n)
        if abs(new - fs) < tol:
            return new
        fs = new
    raise RuntimeError("the 3D simplified Bishop iteration does not converge")


def save_columns(path, col, center, axis):
    """Save the column table in .npz format.

    It also saves the center of moments center and the axis of rotation axis.
    """
    np.savez(
        path,
        base=col.base,
        top=col.top,
        normal=col.n,
        area=col.A,
        weight=col.W,
        pore_pressure=col.u,
        cohesion=col.c,
        friction_angle_deg=np.degrees(np.arctan(col.tan_phi)),
        center=np.asarray(center, dtype=float),
        axis=np.asarray(axis, dtype=float),
    )
