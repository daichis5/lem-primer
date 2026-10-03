"""第1資料 7節・8節: from the traction on a curved base to its resultants.

Left: normal and shear tractions along a curved base, both acting on the
soil above (normal ones point into it). Middle: the normal forces added
head to tail; the resultant is shorter than the sum of their sizes, which
is 7節's inequality. Right: LEM's model of the base, one plane with N_i and
T_i, whose sizes are the sums of sizes (N_i = ∫σ_n dA, as 8節 defines it),
so the model's N_i is longer than the curved base's true resultant. The
middle panel adds the left panel's own vectors.
"""

import math

from figlib import (GROUND, INK, MUTED, NORMAL, RESIST, SMALL, SOIL, UNIT, Figure, add, mul, norm, sub,
                    unit)

LIGHT = "#93c5fd"  # each point's share, before adding
SPAN = 100.0  # degrees of arc covered by the base (strongly curved, to show 7節's point)
POINTS = 7
fig = Figure(
    "fig_c04_surface_integration",
    330,
    "曲面の底面に働く表面力から，底面の合力へ",
    "左は，曲面の底面に沿って分布する表面力の法線成分とせん断成分．中は，各点の垂直力をベクトルとして"
    "つないだ図．向きを考えて足した合力は，大きさだけを足した値より短い．"
    "右は，LEMが底面を1つの平面と1つの向きで表し，大きさだけを足した Ni と Ti を置いたモデル．",
)

# Left: the curved base. Screen coordinates, y down; the centre is above.
C, Rr = (172, 92), 150.0


def on_arc(th):  # th in degrees, 90 = straight below the centre
    r = math.radians(th)
    return (C[0] + Rr * math.cos(r), C[1] + Rr * math.sin(r))


ths = [90 - SPAN / 2 + SPAN * (k + 0.5) / POINTS for k in range(POINTS)]
arc = [on_arc(90 + SPAN / 2 - SPAN * k / 60) for k in range(61)]
fig.polygon(arc + [(arc[-1][0], 40), (arc[0][0], 40)], fill=SOIL)
fig.polygon(arc + [(arc[-1][0], 312), (arc[0][0], 312)], fill=GROUND)
fig.polyline(arc, INK, 3)


def sigma(k):  # larger in the middle of the base [kPa]
    return 62 + 30 * math.sin(math.pi * (k + 0.5) / POINTS)


K = 0.62  # px per kPa
inward = []
for k, th in enumerate(ths):
    p = on_arc(th)
    n_in = unit(sub(C, p))
    t_res = (math.sin(math.radians(th)), -math.cos(math.radians(th)))  # to the right, along the base
    inward.append(n_in)
    fig.arrow(p, add(p, mul(n_in, sigma(k) * K)), NORMAL, 2.2, head=0.85)
    fig.arrow(p, add(p, mul(t_res, 0.33 * sigma(k) * K)), RESIST, 2.2, head=0.85)
fig.math((arc[30][0], arc[30][1] + 30), "S_i", 16, INK, "middle")
fig.text((C[0], 30), "曲面の底面に分布する表面力", SMALL, MUTED, "middle")

# Middle: the same normal forces head to tail (equal area per point), at a
# force scale shared with the right panel.
SCALE = 0.22  # px per kPa of one point's share
start = (420, 246)
tip = start
for k, n_in in enumerate(inward):
    nxt = add(tip, mul(n_in, sigma(k) * SCALE))
    fig.arrow(tip, nxt, LIGHT, 1.8, head=0.65)
    tip = nxt
fig.arrow(start, tip, NORMAL, 2.8)
fig.math((tip[0] + 10, tip[1] + 6), r"\v{N}_i", 16, NORMAL)
chain = sum(sigma(k) * SCALE for k in range(POINTS))
resultant = norm(sub(tip, start))
by = 272
bx = 362
fig.line((bx, by), (bx + chain, by), LIGHT, 6, cap="butt")
fig.math((bx + chain + 8, by + 5), "∫σ_n dA", 15, "#3b82f6")
fig.line((bx, by + 18), (bx + resultant, by + 18), NORMAL, 6, cap="butt")
fig.math((bx + resultant + 8, by + 23), r"‖\v{N}_i‖", 15, NORMAL)
fig.text((462, 30), "ベクトルとして足す", SMALL, MUTED, "middle")

# In LEM's model the base forces are sums of sizes: N_i = ∫σ_n dA, and T_i alike.
shear_sum = sum(0.33 * sigma(k) * SCALE for k in range(POINTS))

# Right: LEM's model, one plane and one direction for the base.
pc = (668, 214)
chord = unit(sub(on_arc(90 - SPAN / 2), on_arc(90 + SPAN / 2)))
a, b = sub(pc, mul(chord, 82)), add(pc, mul(chord, 82))
fig.polygon([a, b, (b[0], 40), (a[0], 40)], fill=SOIL)
fig.polygon([a, b, (b[0], 312), (a[0], 312)], fill=GROUND)
fig.line(a, b, INK, 3)
n_tip = add(pc, (0, -chain))
fig.arrow(pc, n_tip, NORMAL, 2.6)
t_tip = add(pc, mul(chord, shear_sum))
fig.arrow(pc, t_tip, RESIST, 2.6)
fig.unit_vector(pc, add(pc, (0, 40)))
fig.math((n_tip[0] - 10, n_tip[1] + 14), r"\v{N}_i = −N_i\v{n}_i", 16, NORMAL, "end")
fig.math((t_tip[0] + 2, t_tip[1] + 22), r"\v{T}_i", 16, RESIST)
fig.math((pc[0] + 8, pc[1] + 52), r"\v{n}_i", 16, UNIT)
fig.text((pc[0], 30), "LEMのモデル：1つの平面", SMALL, MUTED, "middle")

if __name__ == "__main__":
    fig.save()
    print(f"sum of sizes {chain:.1f} px, resultant {resultant:.1f} px ({resultant / chain:.3f})")
