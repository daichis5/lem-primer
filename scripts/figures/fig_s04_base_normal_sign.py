"""Chapter 3, Section 12.1: why a base normal force turns negative, read from
the slice's vertical balance.

On a dry slope the simplified Bishop vertical balance is linear in N:

    m_alpha N + c l sin(alpha) / F = W

The left side, the upward force the base gives the slice, is a line in N with
slope m_alpha (the denominator) and intercept c l sin(alpha) / F; N is where
the line meets the level W. Three schematic cases, each with a small sketch of
its slice: an ordinary slice (positive slope, intercept below W, N > 0); a
head slice whose intercept exceeds W (N < 0: the numerator is negative); an
toe slice whose slope is negative (N < 0: the denominator is negative). The
lines are drawn to scale from the values passed to panel(), which are not
printed; each slope follows from its sketch's alpha.
"""

import math

from figlib import GROUND, INK, MUTED, NORMAL, RULE, SMALL, SOIL, SOIL_EDGE, WEIGHT, Figure, L, View

N_RANGE, Y_RANGE = (-10.0, 10.0), (-4.0, 14.0)
TAN_PHI = math.tan(math.radians(30.0))
SHADE = "#fdf0ef"  # the side N < 0
SHADE_TEXT = "#b45309"

fig = Figure(
    "fig_s04_base_normal_sign",
    362,
    L("底面垂直力が負になる2つの原因（模式図）", "The two ways a base normal force turns negative (schematic)"),
    L("鉛直方向のつり合いで，底面がスライスを上向きに支える力は底面垂直力の1次式になり，"
      "底面垂直力はその直線が自重の高さと交わる点で決まる．左のふつうのスライスでは，交点は正の側にある．"
      "中央の頭部のスライスでは，切片が自重を超えるので，交点は負の側にある．これは分子が負のときである．"
      "右の末端部のスライスでは，傾きが負なので，交点は負の側にある．これは分母が負のときである．",
      "In the vertical balance, the upward force the base gives the slice is linear in the base normal force, "
      "and the base normal force is where that line meets the weight. Left: an ordinary slice, crossing on the "
      "positive side. Middle: a head slice whose intercept exceeds the weight, crossing on the negative side: the "
      "numerator is negative. Right: a toe slice whose slope is negative, crossing on the negative side: the "
      "denominator is negative."),
)


def sketch(c, alpha, kind, box=(110.0, 62.0)):
    """A small slice centred on c (pixels) on a base inclined at alpha, with the ground below the base,
    scaled to fit box (pixels)."""
    ta = math.tan(alpha)
    if kind == "head":  # a triangle whose base meets the level crest
        top = 1.2
        b = top / ta
        pts, a, e = [(0.0, 0.0), (b, top), (0.0, top)], (-0.3, -0.3 * ta), (b, top)
    elif kind == "exit":  # a wedge whose base leaves the level toe
        b = 0.8
        pts, a, e = [(0.0, 0.0), (b, b * ta), (b, 0.0)], (0.0, 0.0), (b + 0.3, (b + 0.3) * ta)
    else:  # a slice in the middle of the slip surface
        b = 1.0
        pts, a, e = [(0.0, 0.0), (b, b * ta), (b, b * ta + 1.0), (0.0, 0.8)], (-0.3, -0.3 * ta), (b + 0.3, (b + 0.3) * ta)
    strip = [a, e, (e[0], e[1] - 0.35), (a[0], a[1] - 0.35)]
    xs, zs = [p[0] for p in pts + strip], [p[1] for p in pts + strip]
    k = min(box[0] / (max(xs) - min(xs)), box[1] / (max(zs) - min(zs)))
    v = View(k, (c[0] - k * (max(xs) + min(xs)) / 2, c[1] + k * (max(zs) + min(zs)) / 2))
    fig.polygon([v.p(p) for p in strip], fill=GROUND)
    fig.polygon([v.p(p) for p in pts], fill=SOIL, color=SOIL_EDGE, width=1.5)
    fig.line(v.p(a), v.p(e), INK, 2.2)


def panel(x, title, alpha, fs, intercept, weight, kind, slope_at):
    """One case: its title, its slice, the line m N + c against the level W, and what decides the sign.

    slope_at is where (N, upward force) the label on the slope starts; the label on the intercept sits
    beside the intercept. The condition that makes N negative is drawn in SHADE_TEXT. The slope is
    m_alpha = cos(alpha) + sin(alpha) tan(phi) / F at phi = 30 deg; the intercept c l sin(alpha) / F is
    given directly and has the sign of sin(alpha)."""
    slope = math.cos(alpha) + math.sin(alpha) * TAN_PHI / fs
    cx = x + 114
    fig.rect(x, 6, 228, 348, fill="none", color=RULE, width=1.2)
    fig.text((cx, 30), title, 15, INK, "middle", weight="bold")
    sketch((cx, 80), alpha, kind)
    gx, gy, gw, gh = x + 18, 146, 176, 160  # N across N_RANGE, the upward force up Y_RANGE

    def px(n):
        return gx + (n - N_RANGE[0]) / (N_RANGE[1] - N_RANGE[0]) * gw

    def py(y):
        return gy + gh - (y - Y_RANGE[0]) / (Y_RANGE[1] - Y_RANGE[0]) * gh

    fig.polygon([(px(N_RANGE[0]), gy), (px(0), gy), (px(0), gy + gh), (px(N_RANGE[0]), gy + gh)], fill=SHADE)
    fig.math((px(N_RANGE[0]) + 6, gy + 17), "N_i < 0", 13, SHADE_TEXT)
    fig.line((gx, py(0)), (gx + gw, py(0)), MUTED, 1.2)
    fig.line((px(0), gy), (px(0), gy + gh), MUTED, 1.2)
    fig.math((gx + gw + 4, py(0) + 5), "N_i", 14, MUTED)
    fig.text((px(0), gy - 8), L("上向きの力", "upward force"), SMALL, MUTED, "middle")
    fig.line((gx, py(weight)), (gx + gw, py(weight)), WEIGHT, 1.8, "6 4")
    fig.math((gx + gw + 4, py(weight) + 5), "W_i", 14, WEIGHT)
    # The line m N + c, clipped to the graph.
    ends = [(n, slope * n + intercept) for n in N_RANGE if Y_RANGE[0] <= slope * n + intercept <= Y_RANGE[1]]
    ends += [((y - intercept) / slope, y) for y in Y_RANGE if N_RANGE[0] < (y - intercept) / slope < N_RANGE[1]]
    ends.sort()
    fig.line((px(ends[0][0]), py(ends[0][1])), (px(ends[-1][0]), py(ends[-1][1])), INK, 2.4)
    fig.circle((px(0), py(intercept)), 3.5, fill=INK)
    n = (weight - intercept) / slope
    fig.circle((px(n), py(weight)), 5.5, fill=NORMAL)
    sign = ">" if slope > 0 else "<"
    fig.math((px(slope_at[0]), py(slope_at[1])), L(fr"\t{{傾き }}m_{{α,i}} {sign} 0", fr"\t{{slope }}m_{{α,i}} {sign} 0"),
             13, SHADE_TEXT if slope < 0 else INK)
    above = intercept > weight
    sign = ">" if above else "<"
    # Beside the intercept, on the side the line leaves free: above it where the line falls to the right.
    fig.math((px(0) + 8, py(intercept) + (5 if above else (18 if slope > 0 else -30))),
             L(fr"\t{{切片 }}{sign} W_i", fr"\t{{intercept }}{sign} W_i"), 13, SHADE_TEXT if above else INK)
    sign = ">" if n > 0 else "<"
    fig.math((cx, 336), L(fr"\t{{交点は }}N_i {sign} 0", fr"\t{{They meet at }}N_i {sign} 0"), 14, INK, "middle")


panel(14, L("ふつうのスライス", "An ordinary slice"), math.radians(20.0), 1.5, 3.0, 9.0, "middle", (0.8, -2.6))
panel(266, L("頭部：分子が負", "Head: negative numerator"), math.radians(60.0), 1.2, 13.0, 9.0, "head", (0.8, 2.0))
panel(518, L("末端部：分母が負", "Toe: negative denominator"), math.radians(-60.0), 0.3, -1.5, 8.0, "exit",
      (0.8, 12.0))

if __name__ == "__main__":
    fig.save()
