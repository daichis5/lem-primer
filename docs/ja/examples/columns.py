"""3次元のカラム法で，1つのすべり面の安全率を求める（実践3）．

x を水平右向き，y を水平奥向き，z を鉛直上向きにとる．斜面は，実践2の
斜面を y 方向に延ばしたもので，土塊は x の負の向きへすべる．法線ベクトル n
は，すべり土塊の外向きにとる．長さは m，力は kN で表す．
"""

import math
from dataclasses import dataclass

import numpy as np

import slices

GRAVITY = np.array([0.0, 0.0, -1.0])  # 重力の向き


def ground(x, y):
    """地表の高さ．実践2の斜面を y 方向に延ばす．"""
    return slices.ground(x)


class Ellipsoid:
    """3つの軸が座標軸に平行な楕円体．その下の面をすべり面とする．"""

    def __init__(self, center, radii):
        self.center = np.array(center, dtype=float)
        self.radii = np.array(radii, dtype=float)
        cx, cy, _ = self.center
        a, b, _ = self.radii
        # 平面図で，すべり面がありうる範囲
        self.bounds = (cx - a, cx + a, cy - b, cy + b)

    def z(self, x, y):
        """鉛直線と，楕円体の下の面との交点の高さ．交わらないところは nan．"""
        cx, cy, cz = self.center
        a, b, c = self.radii
        q = 1.0 - ((x - cx) / a) ** 2 - ((y - cy) / b) ** 2
        return np.where(q > 0.0, cz - c * np.sqrt(np.abs(q)), np.nan)

    def normal(self, x, y, z):
        """楕円体の外向き（すべり土塊の外向き）の単位法線ベクトル．

        形は (点の数, 3) である．
        """
        g = (np.stack([x, y, z], axis=-1) - self.center) / self.radii**2
        return g / np.linalg.norm(g, axis=-1, keepdims=True)


class Cylinder:
    """実践2の円弧を，y 方向に長さ length だけ延ばしたすべり面．

    両端は鉛直の面で切る．
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
    """地表 z = x tan(beta) から，鉛直に depth の深さにある平面のすべり面．

    beta_deg は度で与え，平面図の範囲 bounds = (x0, x1, y0, y1) を使う．
    地表には plane.ground を渡す．
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
    """カラムの表．どの量も，カラムの順に並べた配列である．"""

    # 底面の代表点．カラムの中心を通る鉛直線と，すべり面の交点．形は (カラムの数, 3)
    base: np.ndarray
    top: np.ndarray  # 同じ鉛直線と地表の交点
    n: np.ndarray  # 底面の外向きの単位法線ベクトル
    A: np.ndarray  # 底面積 [m²]
    W: np.ndarray  # 重さ [kN]
    u: np.ndarray  # 底面の間隙水圧 [kPa]
    c: np.ndarray  # 粘着力 c' [kPa]
    tan_phi: np.ndarray  # tan(phi')


def centres(lo, hi, h):
    """lo から hi までを覆う，幅 h の区間の中心．

    区間の並びは，lo と hi の中点について対称にする．
    """
    k = math.ceil((hi - lo) / (2 * h))
    return 0.5 * (lo + hi) + h * (np.arange(-k, k) + 0.5)


def make_columns(
    surface, h, *, gamma=18.0, c=10.0, phi_deg=30.0, water_level=None, ground=ground
):
    """平面図を一辺 h の正方形に分け，カラムの表を返す．

    中心ですべり面が地表より下にある正方形を，カラムにする．各底面は，中心の
    鉛直線上の点と，そこでの接平面で代表させる．地下水位 water_level [m] を
    与えると，底面の間隙水圧を，地下水位から鉛直に測った深さの静水圧とする．
    地表より高い地下水位は地表に合わせ，土の重さは gamma のままとする．
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
    """水平な軸 axis のまわりに土塊が回るときの，各底面の局所すべり方向．

    axis × n の向きである．
    """
    m = np.cross(axis, col.n)
    return m / np.linalg.norm(m, axis=1, keepdims=True)


def dip_directions(col, d):
    """全体すべり方向 d を含む鉛直面の中で，各底面が下る向き．

    Hovland (1977) の取り方で，d に直交する水平な軸のまわりの回転の向きと
    同じになる．
    """
    return rotation_directions(col, np.cross(d, [0.0, 0.0, 1.0]))


def projected_directions(col, d):
    """全体すべり方向 d を，各底面の接平面に射影した向き（第3資料 8.2節）．"""
    p = d - (col.n @ d)[:, None] * col.n
    return p / np.linalg.norm(p, axis=1, keepdims=True)


def hovland(col, m):
    """Hovland法の安全率．m は各底面の局所すべり方向．

    カラム間力を無視し，各カラムの抵抗力と滑動力を足し合わせて比をとる．
    """
    N = col.W * (col.n @ GRAVITY)  # 自重の法線方向の成分
    S = col.c * col.A + (N - col.u * col.A) * col.tan_phi  # 発揮できるせん断力
    return np.sum(S) / np.sum(col.W * (m @ GRAVITY))


def arms(col, m, center, axis):
    """点 center を通る軸 axis のまわりの，単位の力のモーメントの腕．

    底面のせん断力（向き m），重さ（カラムの高さの中央に働く），底面の
    法線方向の力（向き n）の順に返す．
    """
    rb = col.base - center
    rg = 0.5 * (col.base + col.top) - center
    return (
        np.cross(rb, m) @ axis,
        np.cross(rg, np.broadcast_to(GRAVITY, rg.shape)) @ axis,
        np.cross(rb, col.n) @ axis,
    )


def hovland_moment(col, center, axis):
    """Hovland法と同じ N を使い，軸 axis のまわりのモーメントの比をとる形．"""
    m = rotation_directions(col, axis)
    l_t, l_w, l_n = arms(col, m, center, axis)
    N = col.W * (col.n @ GRAVITY)
    S = col.c * col.A + (N - col.u * col.A) * col.tan_phi
    return np.sum(S * l_t) / np.sum(col.W * l_w - N * l_n)


def vertical_normal_force(col, m, fs):
    """各カラムの鉛直方向の力のつり合いから求めた底面垂直力 N．

    カラム間力は水平とする．m は各底面の局所すべり方向．
    """
    nz, mz = col.n[:, 2], m[:, 2]
    U = col.u * col.A
    m_alpha = -nz - mz * col.tan_phi / fs
    if np.any(m_alpha <= 0.0):
        raise ValueError("m_alpha が 0 以下になるカラムがある")
    return (col.W + mz * (col.c * col.A - U * col.tan_phi) / fs) / m_alpha


def bishop(col, center, axis, fs=1.5, tol=1e-10, max_iter=100):
    """3次元の簡易Bishop法（Hungr, 1987）の安全率．

    各カラムの鉛直方向の力のつり合いから N を求め，軸 axis のまわりの
    モーメントの比をとる．右辺にも F_s が現れるので，反復して求める．
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
    raise RuntimeError("3次元の簡易Bishop法の反復が収束しない")


def save_columns(path, col, center, axis):
    """カラムの表を，.npz 形式で保存する．

    モーメントの基準点 center と回転軸 axis も，一緒に保存する．
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
