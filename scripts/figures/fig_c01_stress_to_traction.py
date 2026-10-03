"""第1資料 2節: the stress tensor at a point, and the traction on two planes.

One stress state (tension positive, kPa) is cut by two planes through the
same point. t = sigma n is computed for each, so the figure shows the two
tractions really differ in direction and size.
"""

import math

from figlib import (FAINT, GROUND, INK, MUTED, NORMAL, RESIST, SMALL, SOIL, UNIT, Figure, add, fmt,
                    mul, norm, sub)

SXX, SZZ, TXZ = -60.0, -100.0, -35.0  # kPa, tension positive (the soil is in compression)
KE = 0.6  # px per kPa on the element
K = 1.0  # px per kPa


def traction(n):
    return (SXX * n[0] + TXZ * n[1], TXZ * n[0] + SZZ * n[1])


fig = Figure(
    "fig_c01_stress_to_traction",
    330,
    "応力テンソルと，面に働く表面力",
    "左は，1つの点の応力の状態を，小さな要素の面に働く応力の成分で表した図．"
    "中と右は，同じ点を向きの違う2つの面で切り，それぞれの面に働く表面力を同じ応力から計算して描いた図．"
    "面の向きが変わると，表面力の向きと大きさも変わる．",
)


def S(p):  # model (x right, z up) to screen offset
    return (p[0], -p[1])


# Left: the stress element, compression arrows pointing into the faces.
c = (120, 175)
h = 46
fig.rect(c[0] - h, c[1] - h, 2 * h, 2 * h, fill="#f1f5f9", color=INK, width=1.6, r=2)
fig.circle(c, 3, INK)
for sign in (1, -1):
    # faces normal to x: normal stress and the shear along z
    fx = c[0] + sign * h
    fig.arrow((fx + sign * (4 - SXX * KE), c[1]), (fx + sign * 4, c[1]), NORMAL, 2.4)
    sh = -TXZ * KE  # shear arrows sit beside the face's centre, in a pinwheel
    fig.arrow((fx + sign * 9, c[1] - sign * (11 + sh)), (fx + sign * 9, c[1] - sign * 11), RESIST, 2, head=0.75)
    # faces normal to z
    fz = c[1] - sign * h
    fig.arrow((c[0], fz - sign * (4 - SZZ * KE)), (c[0], fz - sign * 4), NORMAL, 2.4)
    fig.arrow((c[0] - sign * 11, fz - sign * 9), (c[0] - sign * (11 + sh), fz - sign * 9), RESIST, 2, head=0.75)
fig.math((c[0] + h + 8 - SXX * KE, c[1] - 8), "σ_{xx}", 16, NORMAL)
fig.math((c[0] + 10, c[1] - h - 8 + SZZ * KE + 18), "σ_{zz}", 16, NORMAL)
fig.math((c[0] + h + 16, c[1] - 30), "τ_{xz}", 16, RESIST)
fig.text((c[0], 300), "点の応力の状態", SMALL, MUTED, "middle")
fig.text((c[0] - 70, 50), "z", SMALL, MUTED)
fig.arrow((c[0] - 96, 92), (c[0] - 96, 56), MUTED, 1.4, head=0.7)
fig.arrow((c[0] - 96, 92), (c[0] - 60, 92), MUTED, 1.4, head=0.7)
fig.text((c[0] - 52, 97), "x", SMALL, MUTED)


def plane_panel(center, deg, label, name):
    """The plane through the point, rising at deg, with the soil above it."""
    a = math.radians(deg)
    t_hat = (math.cos(a), math.sin(a))  # along the plane, model frame
    n = (math.sin(a), -math.cos(a))  # outward from the soil above: downward
    half = 112
    p0 = add(center, S(mul(t_hat, -half)))
    p1 = add(center, S(mul(t_hat, half)))
    top, bottom = center[1] - 130, center[1] + 40
    fig.polygon([p0, p1, (p1[0], top), (p0[0], top)], fill=SOIL)
    fig.polygon([p0, p1, (p1[0], bottom), (p0[0], bottom)], fill=GROUND)
    fig.line(p0, p1, "#172033", 2.4)
    t = traction(n)
    tip = add(center, S(mul(t, K)))
    fig.arrow(center, tip, INK, 2.8)
    fig.unit_vector(center, add(center, S(mul(n, 40))))
    fig.circle(center, 3, INK)
    nl = add(center, S(mul(n, 40)))
    fig.math(add(nl, (8, 14)), rf"\v{{n}}_{label}", 16, UNIT)
    side, anchor = (10, "start") if t[0] >= 0 else (-10, "end")
    fig.math(add(tip, (side, 0)), rf"\v{{t}}(\v{{n}}_{label})", 16, INK, anchor)
    fig.text(add(tip, (side, 18)), f"{round(norm(t))} kPa", SMALL, MUTED, anchor)
    fig.text((center[0], 300), name, SMALL, MUTED, "middle")


plane_panel((375, 210), 0, "1", "面1：水平な面")
plane_panel((610, 210), 32, "2", "面2：傾いた面")

if __name__ == "__main__":
    fig.save()
    for deg in (0, 32):
        a = math.radians(deg)
        n = (math.sin(a), -math.cos(a))
        print(deg, [round(x, 1) for x in traction(n)])
