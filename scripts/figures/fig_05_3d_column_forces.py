"""第2資料 7節: the forces on one 3D column.

The column has vertical sides over a square footprint and a base plane
z = GX x + GY y, inclined in both directions. n is the base's outward
normal; m is the global sliding direction d projected onto the base plane.
N acts along -n and T along -m; the dashed circle in the base plane marks
the directions T could take, which the strength equation leaves open.
"""

import math

from figlib import (FAINT, INK, INTER, MUTED, NORMAL, RESIST, SMALL, SOIL, SOIL_EDGE, UNIT, WEIGHT,
                    Figure, Oblique, add, add3, cross3, dot3, mul3, sub3, unit3)

A = 2.6  # footprint side [m]
GX, GY = 0.45, 0.18  # base slopes: dz/dx, dz/dy
TOP0, TOP_GX = 3.4, 0.2  # ground surface z = TOP0 + TOP_GX x


def base_z(x, y):
    return GX * x + GY * y


def top_z(x, y):
    return TOP0 + TOP_GX * x


pr = Oblique(64, (150, 396), depth=0.6)
fig = Figure(
    "fig_05_3d_column_forces",
    470,
    "3次元のカラムに働く力",
    "傾いた底面をもつ3次元のカラムに，自重，底面の垂直力とせん断力，側面のカラム間力が働く．"
    "底面のせん断力は接平面の中のベクトルで，その向きは強度の式からは決まらない．"
    "点線の円は，接平面の中で向きがとりうる範囲を示す．",
)

n = unit3((GX, GY, -1.0))  # outward: out of the column, downward
d = unit3((-1.0, -0.35, 0.0))  # global sliding direction (down the slope)
m = unit3(sub3(d, mul3(n, dot3(d, n))))  # d projected onto the base plane
e2 = cross3(n, m)
P = (A / 2, A / 2, base_z(A / 2, A / 2))

# The base plane around the column, then the column's hidden edges.
patch = [(-0.9, -0.7), (A + 0.9, -0.7), (A + 0.9, A + 0.7), (-0.9, A + 0.7)]
fig.polygon([pr.p((x, y, base_z(x, y))) for x, y in patch], fill="#ece4d0", color="#c9b88f", width=1.2)
fig.text(pr.p((A + 0.95, -0.7, base_z(A + 0.9, -0.7) - 0.25)), "底面の接平面", SMALL, MUTED)
corners = [(0, 0), (A, 0), (A, A), (0, A)]
B = {c: (c[0], c[1], base_z(*c)) for c in corners}
T = {c: (c[0], c[1], top_z(*c)) for c in corners}
for a_, b_ in (((0, A), (0, 0)), ((0, A), (A, A))):
    fig.line(pr.p(B[a_]), pr.p(B[b_]), SOIL_EDGE, 1.2, "4 4")
fig.line(pr.p(B[(0, A)]), pr.p(T[(0, A)]), SOIL_EDGE, 1.2, "4 4")

# The visible faces, lightly filled so the base shows through.
for face in (
    [B[(0, 0)], B[(A, 0)], T[(A, 0)], T[(0, 0)]],
    [B[(A, 0)], B[(A, A)], T[(A, A)], T[(A, 0)]],
    [T[(0, 0)], T[(A, 0)], T[(A, A)], T[(0, A)]],
):
    fig.polygon([pr.p(q) for q in face], fill=SOIL, color=SOIL_EDGE, width=1.6, opacity=0.42)

# At the base: the circle of possible directions, n, m, N and T.
circle = [pr.p(add3(P, add3(mul3(m, 0.8 * math.cos(t)), mul3(e2, 0.8 * math.sin(t)))))
          for t in [2 * math.pi * k / 72 for k in range(73)]]
fig.polyline(circle, MUTED, 1.2, "2 4")
fig.unit_vector(pr.p(P), pr.p(add3(P, mul3(n, 0.9))))
fig.math(pr.p(add3(P, mul3(n, 0.9))), r"  \v{n}_i", 16, UNIT)
fig.unit_vector(pr.p(P), pr.p(add3(P, mul3(m, 0.8))))
fig.math(add(pr.p(add3(P, mul3(m, 0.8))), (-6, 16)), r"\v{m}_i", 16, UNIT, "end")
fig.arrow(pr.p(P), pr.p(add3(P, mul3(n, -1.9))), NORMAL)
fig.math(add(pr.p(add3(P, mul3(n, -1.9))), (-8, -6)), "N_i", 17, NORMAL, "end")
fig.arrow(pr.p(P), pr.p(add3(P, mul3(m, -0.8))), RESIST)
fig.math(add(pr.p(add3(P, mul3(m, -0.8))), (8, 14)), r"\v{T}_i", 17, RESIST)
fig.circle(pr.p(P), 3, INK)

# Weight at mid-height above the base centre.
G = (A / 2, A / 2, (P[2] + top_z(A / 2, A / 2)) / 2)
fig.arrow(pr.p(G), pr.p(add3(G, (0, 0, -1.3))), WEIGHT)
fig.circle(pr.p(G), 3, WEIGHT)
fig.math(add(pr.p(add3(G, (0, 0, -0.8))), (10, 0)), "W_i", 17, WEIGHT)

# Forces from the neighbouring column on the right face (normal to x): its
# normal component and two shear components. The other faces carry the same kind.
Q = (A, A / 2, base_z(A, A / 2) + 0.38 * (top_z(A, A / 2) - base_z(A, A / 2)))
fig.arrow(pr.p(add3(Q, (0.9, 0, 0))), pr.p(Q), INTER)
fig.arrow(pr.p(Q), pr.p(add3(Q, (0, 0, -0.75))), INTER, 2.2, head=0.85)
fig.arrow(pr.p(Q), pr.p(add3(Q, (0, 0.8, 0))), INTER, 2.2, head=0.85)
fig.circle(pr.p(Q), 3, INTER)
fig.text(add(pr.p(add3(Q, (0.9, 0, 0))), (8, 5)), "垂直成分", SMALL, INTER)
fig.text(add(pr.p(add3(Q, (0, 0.8, 0))), (6, -10)), "水平のせん断成分", SMALL, INTER)
fig.text(add(pr.p(add3(Q, (0, 0, -0.75))), (8, 12)), "鉛直のせん断成分", SMALL, INTER)
fig.text(add(pr.p(T[(A, 0)]), (12, -8)), "x方向の隣との境界", SMALL, MUTED)
fig.line(add(pr.p(T[(A, 0)]), (10, -12)), add(pr.p(T[(A, 0)]), (-2, 30)), MUTED, 1)
fig.text(add(pr.p(T[(0, 0)]), (-14, -10)), "y方向の隣との境界", SMALL, MUTED, "end")
fig.line(add(pr.p(T[(0, 0)]), (-12, -14)), add(pr.p(T[(0, 0)]), (24, 30)), MUTED, 1)

# Axes.
o = (604, 446)
for vec, name in (((1, 0, 0), "x"), ((0, 1, 0), "y"), ((0, 0, 1), "z")):
    tip = add(o, (pr.p(vec)[0] - pr.p((0, 0, 0))[0], pr.p(vec)[1] - pr.p((0, 0, 0))[1]))
    tip = add(o, ((tip[0] - o[0]) * 0.55, (tip[1] - o[1]) * 0.55))
    fig.arrow(o, tip, MUTED, 1.4, head=0.7)
    fig.math(add(tip, (4, -2)), name, 15, MUTED)

fig.text((470, 330), "点線の円：底面のせん断力が", SMALL, MUTED)
fig.text((470, 350), "接平面の中でとりうる向き", SMALL, MUTED)

if __name__ == "__main__":
    fig.save()
    print("n", [round(x, 3) for x in n], "m", [round(x, 3) for x in m])
