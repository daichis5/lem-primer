"""Chapter 3, Sections 2 and 3: normals on a circle meet at its centre; on an ellipse
they do not.

Left: a circular arc. Every base normal force N acts along the radius, so
its line passes through O and M_O(N) = 0; every base shear has the same
arm R. Right: an elliptical arc. The normals miss the centre O', so N has
an arm d about O' and a moment N d; and the tangent no longer matches the
direction in which a rotation about O' moves a point of the base.
"""

import math

from figlib import (FAINT, INK, MUTED, NORMAL, RESIST, SMALL, SOIL, UNIT, Figure, L, View, add, lerp, mul,
                    sub, unit)

fig = Figure(
    "fig_s02_circle_general_surface",
    350,
    L("円弧のすべり面と楕円のすべり面での，底面垂直力の向き",
      "The direction of the base normal forces on a circular and an elliptical slip surface"),
    L("左の円弧では，底面垂直力の作用線がすべて中心 O を通るので，O まわりのモーメントは0になる．"
      "底面のせん断力の腕は，どれも半径 R である．右の楕円では，作用線が中心 O′ を通らない．"
      "そのため，底面垂直力は O′ まわりに腕 d をもつ．また，接線の方向が，O′ まわりに回転したときに底面の点が移動する方向と，一般に一致しない．",
      "On the circle (left), the lines of action of the base normal forces all pass through the center "
      "O, so their moment about O is zero. Every base shear force has the same arm, the radius R. On "
      "the ellipse (right), the lines of action miss the center O′. The base normal force therefore has "
      "an arm d about O′. Also, a rotation about O′ does not, in general, move the points of the base "
      "along the tangent."),
)


def right_angle(p, u, w, size=9):
    a = add(p, mul(u, size))
    b = add(a, mul(w, size))
    c = add(p, mul(w, size))
    fig.polyline([a, b, c], MUTED, 1.1)


# Left: a circle of radius R about O.
R = 9.0
vl = View(16, (186, 66))
angles = [212, 238, 268, 300, 326]
arc = [vl.p((R * math.cos(math.radians(t)), R * math.sin(math.radians(t)))) for t in range(205, 336, 2)]
fig.polygon(arc, fill=SOIL)
fig.polyline(arc, INK, 3)
O = vl.p((0, 0))
for k, t in enumerate(angles):
    p = vl.p((R * math.cos(math.radians(t)), R * math.sin(math.radians(t))))
    u = unit(sub(O, p))
    tip = add(p, mul(u, 50))
    fig.line(tip, O, FAINT, 1, "3 4")
    fig.arrow(p, tip, NORMAL, 2.4)
    if k == 3:
        # One base shear and its arm R: the radius, perpendicular to the shear.
        tan = (-u[1], u[0])
        if tan[0] < 0:
            tan = (-tan[0], -tan[1])
        fig.arrow(p, add(p, mul(tan, 46)), RESIST, 2.4)
        fig.math(add(p, (40, 26)), "T_i", 16, RESIST)
        right_angle(p, u, tan)
fig.circle(O, 4, INK)
fig.math(add(O, (8, -6)), "O", 17, INK)
fig.math(add(vl.p((R * math.cos(math.radians(300)), R * math.sin(math.radians(300)))), (-34, -62)), "R", 16, MUTED)
fig.math(add(vl.p((R * math.cos(math.radians(212)), R * math.sin(math.radians(212)))), (-6, 22)), "N_i", 16, NORMAL, "end")
fig.math((186, 282),
         L(r"\t{作用線はすべて }O\t{ を通る}", r"\t{All lines of action pass through }O"), 15, INK, "middle")
fig.math((186, 305), "M_O(N_i) = 0", 15, INK, "middle")
fig.math((186, 328),
         L(r"\t{せん断力の腕は，どれも }R", r"\t{Every shear force has the arm }R"), 15, INK, "middle")

# Right: an ellipse with semi-axes AX, BY about O'.
AX, BY = 11.0, 6.0
vr = View(14.5, (574, 70))


def ell(t):
    return (AX * math.cos(math.radians(t)), BY * math.sin(math.radians(t)))


def inward(t):
    x, y = ell(t)
    return unit((-x / AX**2, -y / BY**2))  # model frame, toward the inside


arc2 = [vr.p(ell(t)) for t in range(200, 341, 2)]
fig.polygon(arc2, fill=SOIL)
fig.polyline(arc2, INK, 3)
O2 = vr.p((0, 0))
for k, t in enumerate([214, 240, 260, 294]):
    p = vr.p(ell(t))
    u = unit(vr.d(inward(t)))
    tip = add(p, mul(u, 50))
    reach = (p[1] - (O2[1] - 22)) / -u[1]  # extend each line up to just above O'
    fig.line(tip, add(p, mul(u, reach)), FAINT, 1, "3 4")
    fig.arrow(p, tip, NORMAL, 2.4)
    if k == 1:
        # The arm d of this N about O': the perpendicular from O' to its line.
        foot = add(p, mul(u, (O2[0] - p[0]) * u[0] + (O2[1] - p[1]) * u[1]))
        fig.line(O2, foot, INK, 1.4)
        right_angle(foot, unit(sub(O2, foot)), (-u[0], -u[1]))
        fig.math(add(lerp(O2, foot, 0.5), (-4, -8)), "d", 16, INK, "end")
        fig.math(add(p, (-8, 20)), "N_i", 16, NORMAL, "end")
    if k == 3:
        # Tangent (dashed) against the direction a rotation about O' moves the point (grey).
        r = sub(p, O2)
        motion = unit((r[1], -r[0]))
        if motion[0] < 0:
            motion = (-motion[0], -motion[1])
        tg = (-u[1], u[0])
        if tg[0] < 0:
            tg = (-tg[0], -tg[1])
        fig.line(sub(p, mul(tg, 20)), add(p, mul(tg, 60)), UNIT, 1.3, "5 4")
        fig.arrow(p, add(p, mul(motion, 50)), MUTED, 2)
        tv, tt = add(p, mul(motion, 50)), add(p, mul(tg, 60))
        # Above and right of the arrowhead, clear of the normal arrow, its dashed line and the arc.
        # English is wider: higher and further right.
        fig.text(L(add(tv, (10, -24)), add(tv, (14, -30))),
                 L("移動方向", "direction of motion"), SMALL, MUTED, "middle")
        fig.text(add(tt, (4, 16)), L("接線", "tangent"), SMALL, UNIT)


fig.circle(O2, 4, INK)
fig.math(add(O2, (8, -6)), "O′", 17, INK)
fig.math((574, 282),
         L(r"\t{作用線は }O′\t{ を通らない}", r"\t{The lines of action miss }O′"), 15, INK, "middle")
fig.math((574, 305), "M_{O′}(N_i) = N_i d ≠ 0", 15, INK, "middle")
fig.math((574, 328),
         L(r"\t{接線と，}O′\t{ まわりの回転による移動方向が異なる}", r"\t{Rotation about }O′\t{ does not follow the tangent}"),
         15, INK, "middle")
fig.line((380, 20), (380, 330), "#e2e8f0", 1)

if __name__ == "__main__":
    fig.save()
