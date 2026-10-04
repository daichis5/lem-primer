"""第2資料 3.1節: where the unknowns live, for n = 5 slices.

N on every base, E, X and the height h on every boundary between two
slices, and one F_s for the whole surface. The arrows only mark where an
unknown acts; their lengths are all the same, because their sizes are what
is unknown.
"""

import math

from figlib import (GROUND, INK, INTER, LABEL, MUTED, NORMAL, SMALL, SOIL, SOIL_EDGE, Figure, Slope, View,
                    add, mul, unit)

s = Slope(n=5)
L = 22  # px: every unknown's arrow, since only its place is known
v = View(24.5, (100, 290))
fig = Figure(
    "fig_02_indeterminacy",
    370,
    "5つのスライスに残る未知量",
    "5つのスライスに分けたすべり土塊で，未知量が働く場所を示す．各底面に垂直力 N が1つずつ，"
    "スライスの間の4つの境界に E，X，作用位置 h が1つずつあり，安全率 Fs は全体で1つである．"
    "未知量は18個で，つり合い式の15本より多い．",
)

left, right, bottom = -3.8, 26.6, -2.6
fig.polygon([v.p(p) for p in s.ground_pts(left, right) + [(right, bottom), (left, bottom)]], fill=GROUND)
fig.polygon([v.p(p) for p in s.mass()], fill=SOIL)
for k in range(1, s.n):
    x = s.x0 + k * s.b
    fig.line(v.p((x, s.slip(x))), v.p((x, s.ground(x))), SOIL_EDGE, 1.4)
fig.polyline([v.p(p) for p in s.ground_pts(left, right)], SOIL_EDGE, 2)
fig.polyline([v.p(p) for p in s.arc_pts(s.x0, s.x1)], INK, 3)

# N on each base: a fixed-length arrow into the slice, normal to the chord.
for k in range(s.n):
    mid, alpha = s.chord(k)
    d = unit(v.d((-math.sin(alpha), math.cos(alpha))))
    fig.arrow(v.p(mid), add(v.p(mid), mul(d, L)), NORMAL, 2.4)
    out = add(v.p(mid), mul(d, -20))
    fig.math((out[0], out[1] + 8), f"N_{k + 1}", 16, NORMAL, "middle")

# E, X and h on each boundary between slices, and the line through the h's.
thrust = [v.p((s.x0, s.slip(s.x0)))]
for k in range(1, s.n):
    x = s.x0 + k * s.b
    h = 0.45 * (s.ground(x) - s.slip(x))
    p = v.p((x, s.slip(x) + h))
    thrust.append(p)
    fig.arrow(p, add(p, (L, 0)), INTER, 2.2, head=0.8)
    fig.arrow(p, add(p, (0, -L)), INTER, 2.2, head=0.8)
    fig.circle(p, 3.2, INTER)
    fig.math(add(p, (L + 5, 6)), f"E_{k}", 15, INTER)
    fig.math(add(p, (-5, -12)), f"X_{k}", 15, INTER, "end")
    base = v.p((x, s.slip(x)))
    fig.line(add(base, (-6, 0)), add(p, (-6, 0)), MUTED, 1)
    fig.math(add(base, (-10, (p[1] - base[1]) / 2 + 5)), f"h_{k}", 15, MUTED, "end")
thrust.append(v.p((s.x1, s.slip(s.x1))))
fig.polyline(thrust, INTER, 1.2, "4 4")

fig.math(add(v.p((s.x1, s.h)), (-104, -12)), "F_s", 17, INK)
fig.text(add(v.p((s.x1, s.h)), (-82, -12)), "は全体で1つ", SMALL, INK)

# The count, in the open space above the slope.
fig.text((28, 52), "未知量　5 + 4 + 4 + 4 + 1 = 18個", LABEL, INK)
fig.text((28, 76), "つり合い式　3 × 5 = 15本", LABEL, INK)

if __name__ == "__main__":
    fig.save()
