"""無限斜面の安全率を，すべり面に働く表面力から求める（実践1）．

x を水平右向き，z を鉛直上向きにとる．地表は右に上がり，土塊は左下へすべる．
法線ベクトル n は，第1章と同じく，すべり土塊の外向き（すべり面より下の
地盤の側）にとる．長さは m，応力は kPa で表す．
"""

import math

import numpy as np

GAMMA_W = 9.81  # 水の単位体積重量 [kN/m³]


def plane_vectors(beta_deg: float) -> tuple[np.ndarray, np.ndarray]:
    """傾き beta の面の，外向きの単位法線ベクトル n と，すべる向き m を返す．"""
    b = math.radians(beta_deg)
    n = np.array([math.sin(b), -math.cos(b)])
    m = np.array([-math.cos(b), -math.sin(b)])
    return n, m


def split_traction(t: np.ndarray, n: np.ndarray) -> tuple[float, np.ndarray]:
    """表面力 t を，外向きの単位法線ベクトル n の面について分ける．

    圧縮を正とする垂直応力 sigma_n = -n·t と，せん断成分 (I - n nᵀ) t を返す．
    """
    t_n = float(n @ t)
    return -t_n, t - t_n * n


def base_stresses(beta_deg: float, w: float) -> tuple[float, float]:
    """柱の重さが，傾き beta のすべり面に生む垂直応力 sigma_n とせん断応力 tau を返す．

    w は柱の水平面積あたりの重さ [kPa]．乾いた土なら gamma z である．
    """
    n, _ = plane_vectors(beta_deg)
    weight = np.array([0.0, -w])  # 幅 1 m，奥行き 1 m の柱の重さ [kN]
    area = 1.0 / math.cos(math.radians(beta_deg))  # その柱の下のすべり面の面積 [m²]
    t = -weight / area  # 下の地盤から柱に働く表面力．両隣の柱から受ける力は打ち消し合う
    sigma_n, shear = split_traction(t, n)
    return sigma_n, float(np.linalg.norm(shear))


def column_weight(
    z: float, gamma: float, h_w: float = 0.0, gamma_sat: float | None = None
) -> float:
    """深さ z の柱の，水平面積あたりの重さ [kPa]．

    地下水位がすべり面から鉛直に h_w の高さにあるとき，地下水位より下の土を
    gamma_sat，上の土を gamma とする．
    """
    if not 0.0 <= h_w <= z:
        raise ValueError(f"h_w は 0 以上 z 以下にする: h_w = {h_w}, z = {z}")
    if gamma_sat is None:
        gamma_sat = gamma
    return gamma * (z - h_w) + gamma_sat * h_w


def pore_pressure(h_w: float, beta_deg: float, rule: str) -> float:
    """すべり面から鉛直に h_w の高さに地下水位があるときの，すべり面の間隙水圧 [kPa]．

    rule="parallel"：地下水が斜面に平行に流れる．u = gamma_w h_w cos²beta
    rule="vertical"：地下水位から鉛直に測った深さで静水圧とする．u = gamma_w h_w
    """
    if rule == "parallel":
        return GAMMA_W * h_w * math.cos(math.radians(beta_deg)) ** 2
    if rule == "vertical":
        return GAMMA_W * h_w
    raise ValueError(f"rule は 'parallel' か 'vertical' にする: {rule!r}")


def factor_of_safety(
    sigma_n: float, tau: float, u: float, c: float, phi_deg: float
) -> float:
    """せん断強度 tau_f = c' + (sigma_n - u) tan(phi') と，tau の比を返す．"""
    tau_f = c + (sigma_n - u) * math.tan(math.radians(phi_deg))
    return tau_f / tau
