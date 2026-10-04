"""2次元のスライス法で，1つのすべり面の安全率を求める（実践2）．

座標は実践1と同じく，x を水平右向き，z を鉛直上向きにとる．斜面は第1資料の
図1と同じで，のり尻が x = 0，のり肩が x = 15 m，高さが 10 m（勾配 1:1.5）
である．土塊は左へすべる．長さは m，力は奥行き 1 m あたりの kN（kN/m）で表す．
"""

import math
from dataclasses import dataclass

import numpy as np

GAMMA_W = 9.81  # 水の単位体積重量 [kN/m³]
HEIGHT, CREST = 10.0, 15.0  # 斜面の高さと，のり肩の x [m]


def ground(x):
    """地表の高さ．のり尻より左は 0，のり肩より右は HEIGHT である．"""
    return np.clip(x, 0.0, CREST) * HEIGHT / CREST


class Circle:
    """中心 center の円弧のすべり面．

    x = exit_x で左の地表に出て，のり肩より右の地表に入る．
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
        """すべり面の傾き dz/dx．"""
        cx, cz = self.center
        return (x - cx) / (cz - self.z(x))


class Ellipse:
    """中心 center，水平の半径 a，鉛直の半径 b の楕円のすべり面．

    x = exit_x で左の地表に出て，のり肩より右の地表に入る．
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
    """地表 z = x tan(beta) から，鉛直に depth の深さにある平面のすべり面．

    beta_deg は度で与え，x0 から x1 までを使う．地表には line.ground を渡す．
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
    """スライスの表．どの量も，左のスライスから順に並べた配列である．"""

    x: np.ndarray  # 底面の代表点（幅の中央）の x [m]
    z: np.ndarray  # 底面の代表点の z [m]
    b: np.ndarray  # 幅 [m]
    # 底面の傾き [rad]．右上がりを正とし，正の底面は土塊を左へすべらせる
    alpha: np.ndarray
    l: np.ndarray  # 底面の長さ [m]
    n: np.ndarray  # 底面の外向きの単位法線ベクトル．形は (スライスの数, 2)
    m: np.ndarray  # すべる向きの単位ベクトル．形は (スライスの数, 2)
    W: np.ndarray  # 重さ [kN/m]
    u: np.ndarray  # 底面の間隙水圧 [kPa]
    c: np.ndarray  # 粘着力 c' [kPa]
    tan_phi: np.ndarray  # tan(phi')


def make_slices(
    surface, n, *, gamma=18.0, c=10.0, phi_deg=30.0, water_level=None, ground=ground
):
    """すべり面を n 本の等幅のスライスに分け，スライスの表を返す．

    各底面は，幅の中央の点と，そこでの接線で代表させる．地下水位
    water_level [m] を与えると，底面の間隙水圧を，地下水位から鉛直に
    測った深さの静水圧とする．地表より高い地下水位は地表に合わせ，地表の
    上に水はためない．土の重さは，地下水位の上でも下でも gamma のままとする．
    """
    edges = np.linspace(surface.x0, surface.x1, n + 1)
    x = 0.5 * (edges[:-1] + edges[1:])
    b = np.diff(edges)
    z = surface.z(x)
    alpha = np.arctan(surface.slope(x))
    W = gamma * b * (ground(x) - z)  # 幅の中央の高さを使う
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
    """Fellenius法（簡便分割法）の安全率．

    円弧の中心まわりのモーメントの比をとる．底面の有効垂直力は，既定では
    W cos(alpha) - u l とする．effective_weight=True なら，有効重量 W - u b を
    底面の法線方向に分けた (W - u b) cos(alpha) とする．
    """
    if effective_weight:
        n_eff = (s.W - s.u * s.b) * np.cos(s.alpha)
    else:
        n_eff = s.W * np.cos(s.alpha) - s.u * s.l
    resisting = np.sum(s.c * s.l + n_eff * s.tan_phi)
    return resisting / np.sum(s.W * np.sin(s.alpha))


def bishop(s, fs=1.0, tol=1e-10, max_iter=100):
    """簡易Bishop法の安全率．右辺にも F_s が現れるので，反復して求める．"""
    for _ in range(max_iter):
        m_alpha = np.cos(s.alpha) + np.sin(s.alpha) * s.tan_phi / fs
        if np.any(m_alpha <= 0.0):
            raise ValueError("m_alpha が 0 以下になるスライスがある")
        resisting = np.sum((s.c * s.b + (s.W - s.u * s.b) * s.tan_phi) / m_alpha)
        new = resisting / np.sum(s.W * np.sin(s.alpha))
        if abs(new - fs) < tol:
            return new
        fs = new
    raise RuntimeError("簡易Bishop法の反復が収束しない")


def janbu(s, fs=1.0, tol=1e-10, max_iter=100):
    """補正係数を掛けない簡易Janbu法の安全率．

    水平方向の力のつり合いから求める．右辺にも F_s が現れるので，反復する．
    """
    for _ in range(max_iter):
        m_alpha = np.cos(s.alpha) + np.sin(s.alpha) * s.tan_phi / fs
        if np.any(m_alpha <= 0.0):
            raise ValueError("m_alpha が 0 以下になるスライスがある")
        strength = s.c * s.b + (s.W - s.u * s.b) * s.tan_phi
        resisting = np.sum(strength / (np.cos(s.alpha) * m_alpha))
        new = resisting / np.sum(s.W * np.tan(s.alpha))
        if abs(new - fs) < tol:
            return new
        fs = new
    raise RuntimeError("簡易Janbu法の反復が収束しない")


def cross(r, f):
    """2次元のベクトル r と f の外積 r_x f_z - r_z f_x．

    反時計回りのモーメントを正とする．
    """
    return r[..., 0] * f[..., 1] - r[..., 1] * f[..., 0]


def fellenius_about(s, center):
    """点 center まわりのモーメントの比をとる Fellenius法の安全率．

    底面垂直力には，Fellenius法と同じ N = W cos(alpha) を使う．円弧の中心を
    center にすれば fellenius と同じ値になり，円弧以外では N のモーメントも
    式に入る．
    """
    r = np.stack([s.x - center[0], s.z - center[1]], axis=1)
    N = s.W * np.cos(s.alpha)
    S = s.c * s.l + (N - s.u * s.l) * s.tan_phi  # 底面が発揮できるせん断力
    weight = np.array([0.0, -1.0])
    driving = s.W * cross(r, weight) + N * cross(r, -s.n)
    return np.sum(S * cross(r, -s.m)) / -np.sum(driving)


def base_forces(s, fs, theta):
    """スライス間力の合力の傾きを theta [rad] とし，各スライスの N と T を求める．

    合力に直交する向き p で各スライスの力のつり合いをとると，合力が式から
    消え，N が1本の式で決まる．theta = 0 なら p は鉛直で，D は m_alpha になる．
    """
    p = np.array([-math.sin(theta), math.cos(theta)])
    e = -s.m  # すべりに抵抗する向き
    U = s.u * s.l
    D = -(s.n @ p) + s.tan_phi / fs * (e @ p)
    if np.any(D <= 0.0):
        raise ValueError("分母 D が 0 以下になるスライスがある．F_s か theta を見直す")
    N = (s.W * p[1] - (s.c * s.l - U * s.tan_phi) / fs * (e @ p)) / D
    T = (s.c * s.l + (N - U) * s.tan_phi) / fs
    return N, T


def residuals(s, fs, theta, center):
    """力の残差と，点 center まわりのモーメントの残差を返す．

    各スライスに働くスライス間力の合力 Q（向き d）を求め，その和を力の残差，
    center まわりのモーメントの和をモーメントの残差とする．
    """
    N, T = base_forces(s, fs, theta)
    d = np.array([math.cos(theta), math.sin(theta)])
    Q = N * (s.n @ d) - T * (-s.m @ d) + s.W * d[1]
    r = np.stack([s.x - center[0], s.z - center[1]], axis=1)
    return float(np.sum(Q)), float(np.sum(Q * cross(r, d)))


def secant(f, x0, x1, tol=1e-10, max_iter=100):
    """f(x) = 0 の解を割線法で求める．"""
    f0, f1 = f(x0), f(x1)
    for _ in range(max_iter):
        if f1 == f0:
            raise RuntimeError("割線法で，2点の値が同じになった")
        x0, x1 = x1, x1 - f1 * (x1 - x0) / (f1 - f0)
        if abs(x1 - x0) < tol:
            return x1
        f0, f1 = f1, f(x1)
    raise RuntimeError("割線法が収束しない")


def fs_moment(s, theta, center, fs=1.5):
    """theta を決めたとき，center まわりのモーメントの残差を 0 にする F_s．"""
    return secant(lambda f: residuals(s, f, theta, center)[1], fs, 1.1 * fs)


def fs_force(s, theta, fs=1.5):
    """theta を決めたとき，力の残差を 0 にする F_s．"""
    return secant(lambda f: residuals(s, f, theta, (0.0, 0.0))[0], fs, 1.1 * fs)


def spencer(s, center, fs=1.5):
    """力とモーメントの残差をともに 0 にする F_s と theta [rad]（Spencer法）．"""

    def gap(theta):
        return fs_moment(s, theta, center, fs) - fs_force(s, theta, fs)

    theta = secant(gap, 0.0, 0.1, tol=1e-9)
    return fs_moment(s, theta, center, fs), theta
