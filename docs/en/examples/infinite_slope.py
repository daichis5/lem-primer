"""Find the factor of safety of an infinite slope from the traction (Practice 1).

x points right and z points up. The ground rises to the right, and the soil slides
down to the left. As in Chapter 1, the normal vector n points out of the sliding mass
(toward the ground below the slip surface). Lengths are in m and stresses in kPa.
"""

import math

import numpy as np

GAMMA_W = 9.81  # unit weight of water [kN/m³]


def plane_vectors(beta_deg: float) -> tuple[np.ndarray, np.ndarray]:
    """Return the outward unit normal n and sliding direction m of a plane at beta."""
    b = math.radians(beta_deg)
    n = np.array([math.sin(b), -math.cos(b)])
    m = np.array([-math.cos(b), -math.sin(b)])
    return n, m


def split_traction(t: np.ndarray, n: np.ndarray) -> tuple[float, np.ndarray]:
    """Split the traction t on a plane with the outward unit normal n.

    Return sigma_n = -n·t (compression positive) and the shear part (I - n nᵀ) t.
    """
    t_n = float(n @ t)
    return -t_n, t - t_n * n


def base_stresses(beta_deg: float, w: float) -> tuple[float, float]:
    """Return the stresses sigma_n and tau on a slip plane at beta under a column.

    w is the column's weight per unit horizontal area [kPa]: gamma z for dry soil.
    """
    n, _ = plane_vectors(beta_deg)
    weight = np.array([0.0, -w])  # weight of a column 1 m wide and 1 m deep [kN]
    area = 1.0 / math.cos(math.radians(beta_deg))  # area of the plane under it [m²]
    t = -weight / area  # traction from the ground below; the neighbors' forces cancel
    sigma_n, shear = split_traction(t, n)
    return sigma_n, float(np.linalg.norm(shear))


def column_weight(
    z: float, gamma: float, h_w: float = 0.0, gamma_sat: float | None = None
) -> float:
    """Weight per unit horizontal area of a column of depth z [kPa].

    With the water table h_w above the slip surface, measured vertically, the soil
    below the water table weighs gamma_sat and the soil above it gamma.
    """
    if not 0.0 <= h_w <= z:
        raise ValueError(f"h_w must be between 0 and z: h_w = {h_w}, z = {z}")
    if gamma_sat is None:
        gamma_sat = gamma
    return gamma * (z - h_w) + gamma_sat * h_w


def pore_pressure(h_w: float, beta_deg: float, rule: str) -> float:
    """Pore water pressure on the slip surface, the water table h_w above it [kPa].

    rule="parallel": groundwater flows parallel to the slope. u = gamma_w h_w cos²beta
    rule="vertical": hydrostatic, the depth measured vertically. u = gamma_w h_w
    """
    if rule == "parallel":
        return GAMMA_W * h_w * math.cos(math.radians(beta_deg)) ** 2
    if rule == "vertical":
        return GAMMA_W * h_w
    raise ValueError(f"rule must be 'parallel' or 'vertical': {rule!r}")


def factor_of_safety(
    sigma_n: float, tau: float, u: float, c: float, phi_deg: float
) -> float:
    """Return the ratio of the shear strength c' + (sigma_n - u) tan(phi') to tau."""
    tau_f = c + (sigma_n - u) * math.tan(math.radians(phi_deg))
    return tau_f / tau
