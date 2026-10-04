"""Practice 1: the forces on a column of an infinite slope, and the two rules for
the pore pressure on its slip plane.

The slope rises to the right at beta and the soil slides down to the left, as
in the practice code. The weight W, the base normal force N and the base shear
force T are drawn to one scale, so N and T are W's components along -n and -m.
The head on the right follows from the equipotential through P, which is
normal to the slope when the water flows parallel to it.
"""

import math

from figlib import (FAINT, GROUND, INK, INTER, MUTED, NORMAL, RESIST, RULE, SMALL, SOIL, SOIL_EDGE, UNIT, WATER,
                    WEIGHT, Figure, L, View, add, mul, sub)

BETA = math.radians(30.0)
Z = 4.4  # vertical depth of the slip plane [m]
B = 2.4  # width of the column [m]
H_W = 2.6  # height of the water table above the slip plane, measured vertically [m]
BAND = 1.5  # ground drawn below the slip plane [m]
X0, X1 = -3.0, 5.0  # extent of the slope in each panel [m]
K = 28.0  # px per m
W_PX = 52.0  # length of the weight arrow

TAN = math.tan(BETA)
n_out = (math.sin(BETA), -math.cos(BETA))  # outward normal of the soil above the slip plane
m_dir = (-math.cos(BETA), -math.sin(BETA))  # down the slope


def screen(vec):
    return (vec[0], -vec[1])


fig = Figure(
    "fig_e1_infinite_slope",
    330,
    L("無限斜面の柱に働く力と，すべり面の間隙水圧",
      "Forces on a column of an infinite slope, and the pore water pressure on the slip surface"),
    L("左は，無限斜面から取り出した柱に働く力．自重 W を，すべり面の垂直力 N とせん断力 T が支え，"
      "両側の面に働く力は打ち消し合う．右は，地下水位がすべり面から鉛直に h_w の高さにあるときの，"
      "すべり面の点 P の間隙水圧の2つの決め方．斜面に平行に浸透するときは，等ポテンシャル線が斜面に直交するので，"
      "P の圧力水頭は h_w cos²β になる．",
      "Left: the forces on a column taken from an infinite slope. The normal force N and the shear "
      "force T on the slip surface carry the weight W, and the forces on the two sides cancel. Right: "
      "two ways to find the pore water pressure at point P on the slip surface when the water table "
      "stands h_w above it, measured vertically. When the water seeps parallel to the slope, the "
      "equipotential lines are normal to the slope, so the pressure head at P is h_w cos²β."),
)


def dimension(a, b):
    """A vertical dimension line from a to b (pixels) with a tick at each end."""
    fig.line(a, b, MUTED, 1.0)
    for y in (a[1], b[1]):
        fig.line((a[0] - 4, y), (a[0] + 4, y), MUTED, 1.0)


def slope(v, water=False):
    """Ground surface and slip plane from X0 to X1, soil between, a band of ground below."""
    g = [(x, x * TAN) for x in (X0, X1)]
    s = [(x, x * TAN - Z) for x in (X0, X1)]
    b = [(x, x * TAN - Z - BAND) for x in (X0, X1)]
    fig.polygon([v.p(s[0]), v.p(s[1]), v.p(b[1]), v.p(b[0])], fill=GROUND)
    fig.polygon([v.p(g[0]), v.p(g[1]), v.p(s[1]), v.p(s[0])], fill=SOIL)
    if water:
        w = [(x, x * TAN - Z + H_W) for x in (X0, X1)]
        fig.polygon([v.p(w[0]), v.p(w[1]), v.p(s[1]), v.p(s[0])], fill=WATER, opacity=0.1)
        fig.line(v.p(w[0]), v.p(w[1]), WATER, 1.6)
    fig.line(v.p(g[0]), v.p(g[1]), INK, 2.2)
    fig.line(v.p(s[0]), v.p(s[1]), INK, 2.6, "9 5")


def panel_forces(v):
    slope(v)
    top_l, top_r = (0.0, 0.0), (B, B * TAN)
    bot_l, bot_r = (0.0, -Z), (B, B * TAN - Z)
    fig.polygon([v.p(top_l), v.p(top_r), v.p(bot_r), v.p(bot_l)], fill="#ead6a6", color=SOIL_EDGE, width=1.4)

    # Side forces: equal and opposite, so they cancel. Each acts a third of the way up
    # its face, where the resultant of a stress growing linearly with depth acts.
    along = screen((math.cos(BETA), math.sin(BETA)))
    for face, sign in ((0.0, 1.0), (B, -1.0)):
        mid = v.p((face, face * TAN - 2 * Z / 3))
        fig.arrow(add(mid, mul(along, -sign * 40.0)), add(mid, mul(along, -sign * 3.0)), INTER, width=2.2)

    centroid = v.p((B / 2, B / 2 * TAN - Z / 2))
    fig.arrow(centroid, add(centroid, (0.0, W_PX)), WEIGHT)
    fig.circle(centroid, 3.0, WEIGHT)
    fig.math(add(centroid, (14, 30)), "W", color=WEIGHT)

    base = v.p((B / 2, B / 2 * TAN - Z))
    tip_n = add(base, mul(screen((-n_out[0], -n_out[1])), W_PX * math.cos(BETA)))
    tip_t = add(base, mul(screen((-m_dir[0], -m_dir[1])), W_PX * math.sin(BETA)))
    fig.line(tip_n, add(tip_n, sub(tip_t, base)), FAINT, 1.2, "4 4")
    fig.line(tip_t, add(tip_t, sub(tip_n, base)), FAINT, 1.2, "4 4")
    fig.arrow(base, tip_n, NORMAL)
    fig.arrow(base, tip_t, RESIST)
    fig.math(add(tip_n, (-4, 4)), "N", color=NORMAL, anchor="end")
    fig.math(add(tip_t, (4, 16)), "T", color=RESIST)

    n_tip = add(base, mul(screen(n_out), 34))
    m_tip = add(base, mul(screen(m_dir), 34))
    fig.unit_vector(base, n_tip)
    fig.unit_vector(base, m_tip)
    fig.math(add(n_tip, (6, 8)), r"\v{n}", color=UNIT)
    fig.math(add(m_tip, (-2, 18)), r"\v{m}", color=UNIT, anchor="end")
    fig.circle(base, 3.0, INK)

    # Depth of the slip plane, measured vertically; it is the same anywhere along the slope.
    x_dim = 4.3
    top, bot = v.p((x_dim, x_dim * TAN)), v.p((x_dim, x_dim * TAN - Z))
    dimension(top, bot)
    fig.math((top[0] + 7, (top[1] + bot[1]) / 2), "z", color=MUTED, vcenter=True)

    # Inclination of the ground, at its left end.
    corner = v.p((X0, X0 * TAN))
    fig.line(corner, add(corner, (62, 0)), RULE, 1.2)
    fig.angle_arc(corner, 44, 0, 30)
    fig.math(add(corner, (50, -9)), "β", vcenter=True)
    # English is wider: end it where the Japanese label sits, so the ground line falls away below it.
    fig.text(L(v.p((2.9, 2.9 * TAN + 0.45)), v.p((3.7, 3.7 * TAN + 0.45))), L("地表", "ground surface"), SMALL,
             MUTED, L("middle", "end"))
    # English does not fit in the band: set it past the end of the slip plane.
    fig.text(L(v.p((4.0, 4.0 * TAN - Z - BAND / 2)), add(v.p((X1, X1 * TAN - Z)), (8, 0))),
             L("すべり面", "slip surface"), SMALL, MUTED, L("middle", "start"), vcenter=True)
    fig.text((206, 282), L("両側の面の力（紫）は", "The side forces (purple) are"), SMALL, INTER)
    fig.text((206, 302), L("大きさが同じで打ち消し合う", "equal in size and cancel"), SMALL, INTER)


def panel_water(v):
    slope(v, water=True)
    xp = 2.6
    p = v.p((xp, xp * TAN - Z))
    q = v.p((xp - H_W * math.cos(BETA) * math.sin(BETA), xp * TAN - Z + H_W * math.cos(BETA) ** 2))
    top = v.p((xp, xp * TAN - Z + H_W))
    fig.line(p, q, WATER, 1.4, "5 4")
    # h_w: from P straight up to the water table.
    dimension(p, top)
    fig.math((p[0] + 7, (p[1] + top[1]) / 2), "h_w", color=MUTED, vcenter=True)
    # h_w cos^2(beta): from P up to the level where P's equipotential meets the water table.
    x_left = q[0] - 12
    fig.line(q, (x_left - 4, q[1]), WATER, 1.2, "2 3")
    fig.line(p, (x_left - 4, p[1]), RULE, 1.0)
    dimension((x_left, p[1]), (x_left, q[1]))
    # Set low, at P's end of the dimension, so the water table above clears the label.
    fig.math((x_left - 6, p[1] + 4), r"h_w \r{cos}^2β", 15, MUTED, anchor="end")
    fig.circle(p, 3.0, INK)
    fig.circle(q, 2.6, WATER)
    fig.math(add(p, (7, 17)), "P")

    a = v.p((-1.4, -1.4 * TAN - Z + 0.8))
    fig.arrow(a, add(a, mul(screen(m_dir), 34)), WATER, width=1.6)
    fig.text(v.p((-2.0, -2.0 * TAN - Z + H_W - 0.9)), L("地下水位", "water table"), SMALL, WATER, "middle", vcenter=True)

    fig.math((404, 32), L(r"\t{斜面に平行な浸透：}u = γ_w h_w \r{cos}^2β",
                          r"\t{Parallel seepage: }u = γ_w h_w \r{cos}^2β"), 15, INK)
    fig.math((404, 56), L(r"\t{鉛直の静水圧：}u = γ_w h_w", r"\t{Hydrostatic (vertical): }u = γ_w h_w"), 15, INK)


panel_forces(View(K, (138, 112)))
panel_water(View(K, (520, 112)))

if __name__ == "__main__":
    fig.save()
