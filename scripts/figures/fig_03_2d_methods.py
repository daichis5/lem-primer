"""第2資料 4節: what Fellenius, simplified Bishop and simplified Janbu keep.

The same slice as fig_01 in all three panels. Forces a method ignores are
drawn faint and dashed. N follows from the balance each method uses:
Fellenius balances forces normal to the base without interslice forces
(N = W cos alpha); Bishop and Janbu balance vertical forces with X ignored
(N cos alpha + T sin alpha = W). T is drawn the same in every panel: it
depends on F_s, which the methods find from different equations.
"""

import math

from figlib import (FAINT, INK, INTER, MUTED, NORMAL, RESIST, SMALL, SOIL, SOIL_EDGE, WEIGHT, Figure,
                    SliceModel, View, add, mul, text_width, unit)

FORCE = 0.34  # px per kN
sm = SliceModel()
s, c = math.sin(sm.alpha), math.cos(sm.alpha)
T = sm.T
METHODS = [
    ("Fellenius法", False, sm.W * c, ["—", "—", "✓"], "スライス間力 E，X を無視"),
    ("簡易Bishop法", True, (sm.W - T * s) / c, ["✓", "—", "✓"], "スライス間のせん断力 X を無視"),
    ("簡易Janbu法", True, (sm.W - T * s) / c, ["✓", "✓", "—"], "スライス間のせん断力 X を無視"),
]
ROWS = ["各スライスの鉛直方向の力", "全体の水平方向の力", "全体のモーメント"]

fig = Figure(
    "fig_03_2d_methods",
    420,
    "Fellenius法，簡易Bishop法，簡易Janbu法の比較",
    "同じスライスで，3つの簡便法が無視する内力と，使うつり合いを比べる．無視する力は薄い破線で示す．"
    "Fellenius法はスライス間力を無視し，全体のモーメントのつり合いを使う．"
    "簡易Bishop法はスライス間のせん断力を無視し，各スライスの鉛直方向の力と全体のモーメントのつり合いを使う．"
    "簡易Janbu法はスライス間のせん断力を無視し，力のつり合いを使う．",
)


def panel(x0, name, keep_e, N, checks, note):
    v = View(40, (x0 + 60, 262))
    fig.text((x0 + 120, 28), name, 15, INK, "middle", weight="bold")
    fig.polygon([v.p(p) for p in sm.pts], fill=SOIL, color=SOIL_EDGE, width=1.6)
    ta = math.tan(sm.alpha)
    fig.line(v.p((-0.9, -0.9 * ta)), v.p((sm.b + 0.9, (sm.b + 0.9) * ta)), INK, 2.6)
    g, mid = v.p(sm.g), v.p(sm.mid)
    fig.arrow(g, add(g, (0, sm.W * FORCE)), WEIGHT, 2.4)
    fig.circle(g, 2.6, WEIGHT)
    fig.arrow(mid, add(mid, mul(unit(v.d((-s, c))), N * FORCE)), NORMAL, 2.4)
    fig.arrow(mid, add(mid, mul(unit(v.d((c, s))), T * FORCE)), RESIST, 2.4)
    pl, pr = (v.p(p) for p in sm.thrust_points())
    (e_l, e_r), (x_l, x_r) = sm.E, sm.X
    e_col, e_dash = (INTER, None) if keep_e else (FAINT, "4 3")
    fig.arrow(add(pl, (4, 0)), add(pl, (4 + e_l * FORCE, 0)), e_col, 2.2, e_dash)
    fig.arrow(add(pr, (-4, 0)), add(pr, (-4 - e_r * FORCE, 0)), e_col, 2.2, e_dash)
    fig.arrow(add(pl, (4, 0)), add(pl, (4, -x_l * FORCE)), FAINT, 2.2, "4 3", head=0.8)
    fig.arrow(add(pr, (-4, 0)), add(pr, (-4, x_r * FORCE)), FAINT, 2.2, "4 3", head=0.8)
    fig.math(add(pl, (4 + 0.5 * e_l * FORCE, 20)), "E", 15, e_col, "middle")
    fig.math(add(pr, (-8 - e_r * FORCE, 5)), "E", 15, e_col, "end")
    fig.math(add(pl, (-6, -6)), "X", 15, FAINT, "end")
    fig.math(add(pr, (6, 14)), "X", 15, FAINT)
    fig.math(add(g, (8, 0.62 * sm.W * FORCE)), "W", 15, WEIGHT)
    fig.math(add(mid, add(mul(unit(v.d((-s, c))), N * FORCE), (-8, 0))), "N", 15, NORMAL, "end")
    fig.math(add(mid, add(mul(unit(v.d((c, s))), T * FORCE), (6, 16))), "T", 15, RESIST)
    fig.text((x0 + 120, 300), note, SMALL, MUTED, "middle")
    for k, (row, mark) in enumerate(zip(ROWS, checks)):
        y = 334 + 24 * k
        fig.text((x0 + 12, y), row, SMALL, INK)
        ok = mark == "✓"
        fig.text((x0 + 228, y), mark, 15, RESIST if ok else FAINT, "end", weight="bold" if ok else None)


for i, method in enumerate(METHODS):
    x0 = 10 + 250 * i
    if i:
        fig.line((x0 - 5, 20), (x0 - 5, 400), "#e2e8f0", 1)
    panel(x0, *method)

if __name__ == "__main__":
    fig.save()
    for name, _, N, _, _ in METHODS:
        print(name, round(N, 1))
