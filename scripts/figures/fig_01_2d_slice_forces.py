"""第2資料 2節: the free-body diagram of one 2D slice.

The slice has vertical sides and a straight base inclined at alpha. W, E
and X are chosen; N and T follow from the slice's force balance (see
SliceModel), so the arrows drawn here close into a force polygon.
"""

import math

from figlib import (FAINT, GROUND, INK, INTER, MUTED, NORMAL, RESIST, SMALL, SOIL, SOIL_EDGE, UNIT,
                    WEIGHT, Figure, SliceModel, View, add, mul, unit)

FORCE = 0.5  # px per kN
sm = SliceModel()
v = View(66, (300, 470))
fig = Figure(
    "fig_01_2d_slice_forces",
    600,
    "2次元のスライスに働く力の自由物体図",
    "側面が鉛直で底面が傾いたスライスに，自重，底面の垂直力とせん断力，左右の境界のスライス間力が働く．"
    "底面の傾き，スライスの幅，スライス間力が働く高さ，外向きの法線と仮定したすべり方向も示す．",
)

# Ground under the slip surface, the neighbouring slices, and the slice itself.
ta = math.tan(sm.alpha)
ext = 1.3
slip_l, slip_r = (-ext, -ext * ta), (sm.b + ext, (sm.b + ext) * ta)
fig.polygon([v.p(slip_l), v.p(slip_r), v.p((slip_r[0], slip_r[1] - 1.1)), v.p((slip_l[0], slip_l[1] - 1.1))],
            fill=GROUND)
slope = (sm.top_r[1] - sm.top_l[1]) / sm.b
for x0, x1 in ((-ext, 0.0), (sm.b, sm.b + ext)):
    pts = [(x0, x0 * ta), (x1, x1 * ta), (x1, sm.top_l[1] + slope * x1), (x0, sm.top_l[1] + slope * x0)]
    fig.polygon([v.p(p) for p in pts], fill="#faf6ea")
fig.polygon([v.p(p) for p in sm.pts], fill=SOIL, color=SOIL_EDGE, width=2)
fig.line(v.p(slip_l), v.p(slip_r), INK, 3.2)
fig.text(add(v.p(slip_r), (6, 4)), "すべり面", SMALL, MUTED)

# Unit vectors at the base midpoint: n outward (into the ground), m along the base.
mid = sm.mid
fig.unit_vector(v.p(mid), add(v.p(mid), mul(v.d(sm.n), 0.9)))
fig.math(add(v.p(add(mid, mul(sm.n, 0.9))), (8, 10)), r"\v{n}_i", color=UNIT)
m_from = add(mid, mul(sm.n, 0.18))
fig.unit_vector(v.p(m_from), v.p(add(m_from, sm.m)))
fig.math(add(v.p(add(m_from, sm.m)), (-6, 18)), r"\v{m}_i", color=UNIT, anchor="end")

# Base forces: N along -n, T up the base (against sliding along m).
s, c = math.sin(sm.alpha), math.cos(sm.alpha)
n_tip = add(v.p(mid), mul(unit(v.d((-s, c))), sm.N * FORCE))
fig.arrow(v.p(mid), n_tip, NORMAL)
fig.math(add(n_tip, (-12, -4)), "N_i", color=NORMAL, anchor="end")
t_tip = add(v.p(mid), mul(unit(v.d((c, s))), sm.T * FORCE))
fig.arrow(v.p(mid), t_tip, RESIST)
fig.math(add(t_tip, (4, 22)), "T_i", color=RESIST)

# Weight at the centroid.
fig.arrow(v.p(sm.g), add(v.p(sm.g), (0, sm.W * FORCE)), WEIGHT)
fig.math(add(v.p(sm.g), (10, 0.55 * sm.W * FORCE)), "W_i", color=WEIGHT)
fig.circle(v.p(sm.g), 3.2, fill=WEIGHT)

# Interslice forces at heights h above each base corner.
pl, pr = sm.thrust_points()
(e_l, e_r), (x_l, x_r) = sm.E, sm.X
inset = 5
fig.arrow(add(v.p(pl), (inset, 0)), add(v.p(pl), (inset + e_l * FORCE, 0)), INTER)
fig.math(add(v.p(pl), (inset + 0.5 * e_l * FORCE, 24)), "E_{i−1}", color=INTER, anchor="middle")
fig.arrow(add(v.p(pl), (inset, 0)), add(v.p(pl), (inset, -x_l * FORCE)), INTER)
fig.math(add(v.p(pl), (inset + 6, -x_l * FORCE - 4)), "X_{i−1}", color=INTER)
fig.arrow(add(v.p(pr), (-inset, 0)), add(v.p(pr), (-inset - e_r * FORCE, 0)), INTER)
fig.math(add(v.p(pr), (-inset - e_r * FORCE - 8, 6)), "E_i", color=INTER, anchor="end")
fig.arrow(add(v.p(pr), (-inset, 0)), add(v.p(pr), (-inset, x_r * FORCE)), INTER)
fig.math(add(v.p(pr), (-inset - 6, x_r * FORCE + 16)), "X_i", color=INTER, anchor="end")
fig.circle(v.p(pl), 3, fill=INTER)
fig.circle(v.p(pr), 3, fill=INTER)


def dim_vertical(x_px, y0, y1, label, side):
    fig.line((x_px, y0), (x_px, y1), MUTED, 1.1)
    for y in (y0, y1):
        fig.line((x_px - 4, y), (x_px + 4, y), MUTED, 1.1)
    fig.math((x_px + (-8 if side == "left" else 8), (y0 + y1) / 2 + 6), label, 15, MUTED,
             "end" if side == "left" else "start")


dim_vertical(v.p(sm.base_l)[0] - 16, v.p(sm.base_l)[1], v.p(pl)[1], "h_{i−1}", "left")
dim_vertical(v.p(sm.base_r)[0] + 16, v.p(sm.base_r)[1], v.p(pr)[1], "h_i", "right")

# Width b_i above the slice.
yb = v.p(sm.top_r)[1] - 22
xl, xr = v.p(sm.top_l)[0], v.p(sm.top_r)[0]
fig.line((xl, yb), (xr, yb), MUTED, 1.1)
for x, top in ((xl, sm.top_l), (xr, sm.top_r)):
    fig.line((x, yb - 4), (x, yb + 4), MUTED, 1.1)
    fig.line((x, yb + 6), (x, v.p(top)[1] - 4), FAINT, 1, "2 3")
fig.math(((xl + xr) / 2, yb - 8), "b_i", 15, MUTED, "middle")

# Base inclination alpha, outside the slice at its left corner.
corner = v.p(sm.base_l)
fig.line(corner, add(corner, (-84, 0)), FAINT, 1.1, "4 3")
fig.angle_arc(corner, 64, 180, 180 + math.degrees(sm.alpha), MUTED)
fig.math(add(corner, (-74, 22)), "α_i", 15, MUTED, anchor="end")

fig.legend(
    40,
    575,
    [(WEIGHT, False, "自重"), (NORMAL, False, "垂直力"), (RESIST, False, "すべりに抵抗するせん断力"),
     (INTER, False, "スライス間力"), (UNIT, True, "単位ベクトル")],
    gap=18,
)

if __name__ == "__main__":
    fig.save()
    print(f"W={sm.W:.1f} N={sm.N:.1f} T={sm.T:.1f} kN/m")
