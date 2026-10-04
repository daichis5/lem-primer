"""Find the factor of safety of one slip surface by 2D slices (Practice 2).

As in Practice 1, x points right and z points up. The slope is that of Chapter 1,
Figure 1: the toe at x = 0, the crest at x = 15 m, 10 m high (a gradient of 1:1.5).
The soil slides to the left. Lengths are in m, forces in kN per 1 m of depth (kN/m).
"""

import math
from dataclasses import dataclass

import numpy as np

GAMMA_W = 9.81  # unit weight of water [kN/m³]
HEIGHT, CREST = 10.0, 15.0  # height of the slope and x of the crest [m]


def ground(x):
    """Height of the ground: 0 left of the toe and HEIGHT right of the crest."""
    return np.clip(x, 0.0, CREST) * HEIGHT / CREST


class Circle:
    """A circular slip surface with its center at center.

    It exits the ground on the left at x = exit_x and enters it right of the crest.
    """

    def __init__(self, center=(6.0, 18.0), exit_x=-1.0):
        self.center = np.array(center, dtype=float)
        cx, cz = self.center
        self.radius = math.hypot(exit_x - cx, float(ground(exit_x)) - cz)
        self.x0 = exit_x
        self.x1 = cx + math.sqrt(self.radius**2 - (cz - HEIGHT) ** 2)

    def z(self, x):
        cx, cz = self.center
        return cz - np.sqrt(self.radius**2 - (x - cx) ** 2)

    def slope(self, x):
        """Slope dz/dx of the slip surface."""
        cx, cz = self.center
        return (x - cx) / (cz - self.z(x))


class Ellipse:
    """An elliptical slip surface with center center and radii a across and b down.

    It exits the ground on the left at x = exit_x and enters it right of the crest.
    """

    def __init__(self, center=(6.0, 18.0), b=20.0, exit_x=-1.0):
        self.center = np.array(center, dtype=float)
        cx, cz = self.center
        self.b = b
        depth = (cz - float(ground(exit_x))) / b
        self.a = (cx - exit_x) / math.sqrt(1.0 - depth**2)
        self.x0 = exit_x
        self.x1 = cx + self.a * math.sqrt(1.0 - ((cz - HEIGHT) / b) ** 2)

    def z(self, x):
        cx, cz = self.center
        return cz - self.b * np.sqrt(1.0 - ((x - cx) / self.a) ** 2)

    def slope(self, x):
        s = (x - self.center[0]) / self.a
        return self.b * s / (self.a * np.sqrt(1.0 - s**2))


class Line:
    """A plane slip surface a vertical depth depth below the ground z = x tan(beta).

    Give beta_deg in degrees; the plane runs from x0 to x1. Pass line.ground as ground.
    """

    def __init__(self, beta_deg, depth, x0=0.0, x1=10.0):
        self.tan_beta = math.tan(math.radians(beta_deg))
        self.depth = depth
        self.x0, self.x1 = x0, x1

    def ground(self, x):
        return x * self.tan_beta

    def z(self, x):
        return x * self.tan_beta - self.depth

    def slope(self, x):
        return np.full_like(x, self.tan_beta)


@dataclass
class Slices:
    """The slice table. Each quantity is an array, from the leftmost slice."""

    x: np.ndarray  # x of the base point (the middle of the width) [m]
    z: np.ndarray  # z of the base point [m]
    b: np.ndarray  # width [m]
    # base inclination [rad], positive rising to the right; such a base slides soil left
    alpha: np.ndarray
    l: np.ndarray  # base length [m]
    n: np.ndarray  # outward unit normal of the base, shape (number of slices, 2)
    m: np.ndarray  # unit vector of the sliding direction, shape (number of slices, 2)
    W: np.ndarray  # weight [kN/m]
    u: np.ndarray  # pore water pressure on the base [kPa]
    c: np.ndarray  # cohesion c' [kPa]
    tan_phi: np.ndarray  # tan(phi')


def make_slices(
    surface, n, *, gamma=18.0, c=10.0, phi_deg=30.0, water_level=None, ground=ground
):
    """Split the slip surface into n slices of equal width and return the slice table.

    The middle point of each base and the tangent there represent the base. A water
    table water_level [m] makes the base pore pressure hydrostatic, with the depth
    measured vertically from it. A water table above the ground is cut to the ground,
    so no water stands on it. The soil weighs gamma above and below the water table.
    """
    edges = np.linspace(surface.x0, surface.x1, n + 1)
    x = 0.5 * (edges[:-1] + edges[1:])
    b = np.diff(edges)
    z = surface.z(x)
    alpha = np.arctan(surface.slope(x))
    W = gamma * b * (ground(x) - z)  # uses the heights at the middle of the width
    if water_level is None:
        u = np.zeros(n)
    else:
        level = np.minimum(water_level, ground(x))
        u = GAMMA_W * np.clip(level - z, 0.0, None)
    return Slices(
        x=x,
        z=z,
        b=b,
        alpha=alpha,
        l=b / np.cos(alpha),
        n=np.stack([np.sin(alpha), -np.cos(alpha)], axis=1),
        m=np.stack([-np.cos(alpha), -np.sin(alpha)], axis=1),
        W=W,
        u=u,
        c=np.full(n, c),
        tan_phi=np.full(n, math.tan(math.radians(phi_deg))),
    )


def fellenius(s, *, effective_weight=False):
    """Factor of safety by the Fellenius method (ordinary method of slices).

    It takes the ratio of moments about the center of the circle. The effective
    normal force on a base is W cos(alpha) - u l by default. effective_weight=True
    makes it (W - u b) cos(alpha), the effective weight W - u b resolved along n.
    """
    if effective_weight:
        n_eff = (s.W - s.u * s.b) * np.cos(s.alpha)
    else:
        n_eff = s.W * np.cos(s.alpha) - s.u * s.l
    resisting = np.sum(s.c * s.l + n_eff * s.tan_phi)
    return resisting / np.sum(s.W * np.sin(s.alpha))


def bishop(s, fs=1.0, tol=1e-10, max_iter=100):
    """Simplified Bishop factor of safety. F_s is on both sides, so it is iterated."""
    for _ in range(max_iter):
        m_alpha = np.cos(s.alpha) + np.sin(s.alpha) * s.tan_phi / fs
        if np.any(m_alpha <= 0.0):
            raise ValueError("m_alpha is zero or negative for some slice")
        resisting = np.sum((s.c * s.b + (s.W - s.u * s.b) * s.tan_phi) / m_alpha)
        new = resisting / np.sum(s.W * np.sin(s.alpha))
        if abs(new - fs) < tol:
            return new
        fs = new
    raise RuntimeError("the simplified Bishop iteration does not converge")


def janbu(s, fs=1.0, tol=1e-10, max_iter=100):
    """Simplified Janbu factor of safety, without the correction factor.

    It comes from horizontal force equilibrium. F_s is on both sides, so it is iterated.
    """
    for _ in range(max_iter):
        m_alpha = np.cos(s.alpha) + np.sin(s.alpha) * s.tan_phi / fs
        if np.any(m_alpha <= 0.0):
            raise ValueError("m_alpha is zero or negative for some slice")
        strength = s.c * s.b + (s.W - s.u * s.b) * s.tan_phi
        resisting = np.sum(strength / (np.cos(s.alpha) * m_alpha))
        new = resisting / np.sum(s.W * np.tan(s.alpha))
        if abs(new - fs) < tol:
            return new
        fs = new
    raise RuntimeError("the simplified Janbu iteration does not converge")


def cross(r, f):
    """Cross product r_x f_z - r_z f_x of the 2D vectors r and f.

    A counterclockwise moment is positive.
    """
    return r[..., 0] * f[..., 1] - r[..., 1] * f[..., 0]


def fellenius_about(s, center):
    """Fellenius factor of safety from the ratio of moments about the point center.

    The base normal force is N = W cos(alpha), as in the Fellenius method. With the
    center of a circle as center it equals fellenius; on other shapes the moment of
    N enters too.
    """
    r = np.stack([s.x - center[0], s.z - center[1]], axis=1)
    N = s.W * np.cos(s.alpha)
    S = s.c * s.l + (N - s.u * s.l) * s.tan_phi  # shear force the base can mobilize
    weight = np.array([0.0, -1.0])
    driving = s.W * cross(r, weight) + N * cross(r, -s.n)
    return np.sum(S * cross(r, -s.m)) / -np.sum(driving)


def base_forces(s, fs, theta):
    """Find N and T of each slice with the resultant interslice force at theta [rad].

    Force equilibrium of a slice in the direction p normal to the resultant drops the
    resultant, so one equation gives N. With theta = 0, p is vertical and D is m_alpha.
    """
    p = np.array([-math.sin(theta), math.cos(theta)])
    e = -s.m  # direction resisting sliding
    U = s.u * s.l
    D = -(s.n @ p) + s.tan_phi / fs * (e @ p)
    if np.any(D <= 0.0):
        raise ValueError("D is zero or negative for some slice; check F_s and theta")
    N = (s.W * p[1] - (s.c * s.l - U * s.tan_phi) / fs * (e @ p)) / D
    T = (s.c * s.l + (N - U) * s.tan_phi) / fs
    return N, T


def residuals(s, fs, theta, center):
    """Return the force residual and the moment residual about the point center.

    It finds the resultant interslice force Q (direction d) on each slice. Their sum
    is the force residual, and the sum of their moments about center the moment one.
    """
    N, T = base_forces(s, fs, theta)
    d = np.array([math.cos(theta), math.sin(theta)])
    Q = N * (s.n @ d) - T * (-s.m @ d) + s.W * d[1]
    r = np.stack([s.x - center[0], s.z - center[1]], axis=1)
    return float(np.sum(Q)), float(np.sum(Q * cross(r, d)))


def secant(f, x0, x1, tol=1e-10, max_iter=100):
    """Solve f(x) = 0 by the secant method."""
    f0, f1 = f(x0), f(x1)
    for _ in range(max_iter):
        if f1 == f0:
            raise RuntimeError("secant method: the two points have the same value")
        x0, x1 = x1, x1 - f1 * (x1 - x0) / (f1 - f0)
        if abs(x1 - x0) < tol:
            return x1
        f0, f1 = f1, f(x1)
    raise RuntimeError("the secant method does not converge")


def fs_moment(s, theta, center, fs=1.5):
    """F_s that makes the moment residual about center zero, for a given theta."""
    return secant(lambda f: residuals(s, f, theta, center)[1], fs, 1.1 * fs)


def fs_force(s, theta, fs=1.5):
    """F_s that makes the force residual zero, for a given theta."""
    return secant(lambda f: residuals(s, f, theta, (0.0, 0.0))[0], fs, 1.1 * fs)


def spencer(s, center, fs=1.5):
    """F_s and theta [rad] that make both force and moment residuals zero (Spencer)."""

    def gap(theta):
        return fs_moment(s, theta, center, fs) - fs_force(s, theta, fs)

    theta = secant(gap, 0.0, 0.1, tol=1e-9)
    return fs_moment(s, theta, center, fs), theta
