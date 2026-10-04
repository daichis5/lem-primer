"""Chapter 3, Sections 7 and 8: the global sliding direction and its projection onto a
column's base.

Left, in plan: the long axis of the slip surface and the global sliding
direction d, which need not coincide. Right, in 3D: d projected onto the
base's tangent plane, p = (I - n n^T) d, computed here; the dotted line
from d to p runs along n. m is p made unit length, and T acts against m.
"""

import math

from figlib import (FAINT, INK, MUTED, RESIST, SMALL, SOIL, UNIT, Figure, L, Oblique, add, add3, dot3,
                    mul, mul3, sub3, unit3)

fig = Figure(
    "fig_s03_sliding_direction",
    380,
    L("全体すべり方向と，カラムの底面での局所すべり方向",
      "The direction of sliding, and the local direction of sliding at a column's base"),
    L("左は平面図で，すべり面の長軸と全体すべり方向 d が一致するとは限らないことを示す．"
      "右は1つのカラムの底面の接平面で，d を接平面に射影したベクトル p を計算して描く．"
      "局所すべり方向 m は p の向きの単位ベクトルで，底面のせん断力 T はその逆向きに働く．",
      "Left, in plan: the long axis of the slip surface and the direction of sliding d need not "
      "coincide. Right: the tangent plane of one column's base, with the vector p, the projection of d "
      "onto that plane, computed and drawn. The local direction of sliding m is the unit vector along "
      "p, and the base shear force T acts opposite to it."),
)

# Left: plan view.
C = (170, 172)
A_LONG, B_SHORT, AXIS = 128, 78, math.radians(14)
THETA = math.radians(-24)


def ell(t):
    x, y = A_LONG * math.cos(t), B_SHORT * math.sin(t)
    return (C[0] + x * math.cos(AXIS) - y * math.sin(AXIS), C[1] - (x * math.sin(AXIS) + y * math.cos(AXIS)))


fig.polygon([ell(2 * math.pi * k / 90) for k in range(90)], fill=SOIL, color=INK, width=2)
ax = (math.cos(AXIS), -math.sin(AXIS))
fig.line(add(C, mul(ax, -150)), add(C, mul(ax, 150)), INK, 1.3, "8 5")
fig.text(add(C, add(mul(ax, 150), (-8, -12))), L("長軸", "long axis"), SMALL, INK)
d2 = (math.cos(THETA), -math.sin(THETA))
fig.arrow(C, add(C, mul(d2, 104)), UNIT, 2.2, "6 4")
fig.math(add(C, add(mul(d2, 104), (6, 14))), r"\v{d}", 17, UNIT)
fig.line(C, add(C, (70, 0)), FAINT, 1.1, "3 3")
fig.angle_arc(C, 52, math.degrees(THETA), 0, MUTED)
fig.math(add(C, (58, 24)), "θ", 15, MUTED)
fig.circle(C, 3, INK)
fig.text((C[0], 336), L("平面図：長軸と全体すべり方向", "plan: long axis and direction of sliding"), SMALL, MUTED, "middle")

# Right: one column's base plane z = -0.5 x + 0.15 y around P, in 3D.
pr = Oblique(92, (548, 196), depth=0.62)
P = (0.0, 0.0, 0.0)


def plane_z(x, y):
    return -0.5 * x + 0.15 * y


n = unit3((-0.5, 0.15, -1.0))  # outward normal of the base: downward
d = (math.cos(THETA), math.sin(THETA), 0.0)  # plan direction as above
p = sub3(d, mul3(n, dot3(d, n)))
m = unit3(p)
LEN = 1.5
patch = [(-1.5, -1.0), (1.5, -1.0), (1.5, 1.0), (-1.5, 1.0)]
fig.polygon([pr.p((x, y, plane_z(x, y))) for x, y in patch], fill="#ece4d0", color="#c9b88f", width=1.3)
fig.text(pr.p((-1.5, -1.0, plane_z(-1.5, -1.0) - 0.15)), L("底面の接平面", "tangent plane of the base"), SMALL, MUTED)
d_tip, p_tip = add3(P, mul3(d, LEN)), add3(P, mul3(p, LEN))
fig.unit_vector(pr.p(P), pr.p(add3(P, mul3(n, 0.9))))
fig.math(add(pr.p(add3(P, mul3(n, 0.9))), (8, 8)), r"\v{n}_i", 16, UNIT)
fig.line(pr.p(d_tip), pr.p(p_tip), FAINT, 1.3, "2 3")
fig.arrow(pr.p(P), pr.p(d_tip), UNIT, 2, "6 4")
fig.math(add(pr.p(d_tip), (8, -2)), r"\v{d}", 17, UNIT)
fig.arrow(pr.p(P), pr.p(p_tip), MUTED, 2.4)
fig.math(add(pr.p(p_tip), (8, 14)), r"\v{p}_i", 17, MUTED)
fig.arrow(pr.p(P), pr.p(add3(P, mul3(m, -1.25))), RESIST, 2.6)
fig.math(add(pr.p(add3(P, mul3(m, -1.25))), (-8, -6)), r"\v{T}_i", 17, RESIST, "end")
fig.circle(pr.p(P), 3, INK)
P_M = r"\v{p}_i = (\v{I} − \v{n}_i\v{n}_i^{\r{T}})\v{d}{sep}\v{m}_i = \v{p}_i / ‖\v{p}_i‖"
fig.math((560, 322), L(P_M.replace("{sep}", "，　"), P_M.replace("{sep}", ",\u2003")), 16, INK, "middle")
fig.line((350, 20), (350, 360), "#e2e8f0", 1)

if __name__ == "__main__":
    fig.save()
    print("p", [round(x, 3) for x in p], "|p|", round(math.sqrt(dot3(p, p)), 3), "m", [round(x, 3) for x in m])
