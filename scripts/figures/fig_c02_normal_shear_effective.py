"""Chapter 1, Sections 3 and 4: splitting the traction, and the effective normal stress.

Uses the numbers of Section 6's worked example: sigma_n = 100 kPa, u = 40 kPa,
tau = 30 kPa. The traction is drawn as the vector sum of its normal and
shear components, and the normal stress as the sum of sigma_n' and u.
"""

import math

from figlib import (FAINT, GROUND, INK, MUTED, NORMAL, RESIST, SMALL, SOIL, UNIT, WATER, Figure, L, add, lerp,
                    mul)

SIGMA_N, U, TAU = 100.0, 40.0, 30.0  # kPa
K = 1.45  # px per kPa
TILT = math.radians(18)  # the surface rises to the right

fig = Figure(
    "fig_c02_normal_shear_effective",
    380,
    L("表面力の分解と有効垂直応力", "Splitting the traction, and the effective normal stress"),
    L("左は，面にはたらく表面力を，法線成分とせん断成分の和に分解した図．"
      "右は，同じ面で，垂直応力が有効垂直応力と間隙水圧の和になることと，間隙水圧がせん断成分を変えないことを示す図．",
      "Left: the traction on a plane, split into the sum of its normal and shear components. Right: on "
      "the same plane, the normal stress is the sum of the effective normal stress and the pore water "
      "pressure, and the pore water pressure does not change the shear component."),
)

t_hat = (math.cos(TILT), -math.sin(TILT))  # along the surface, screen coordinates
n_out = (math.sin(TILT), math.cos(TILT))  # outward normal: out of the soil above, downward


def surface(c, x0, x1, top=40, bottom=330):
    """A cut through the soil: the surface through c, soil above, ground below."""
    slope = t_hat[1] / t_hat[0]
    a = (x0, c[1] + (x0 - c[0]) * slope)
    b = (x1, c[1] + (x1 - c[0]) * slope)
    fig.polygon([a, b, (x1, top), (x0, top)], fill=SOIL)
    fig.polygon([a, b, (x1, bottom), (x0, bottom)], fill=GROUND)
    fig.line(a, b, INK, 2.6)


def panel_left(c):
    surface(c, 20, 360)
    normal = mul(n_out, -SIGMA_N * K)  # -sigma_n n, into the soil
    shear = mul(t_hat, TAU * K)
    t = add(normal, shear)
    tip_n, tip_s, tip_t = add(c, normal), add(c, shear), add(c, t)
    fig.line(tip_n, tip_t, FAINT, 1.2, "4 4")
    fig.line(tip_s, tip_t, FAINT, 1.2, "4 4")
    fig.arrow(c, tip_n, NORMAL)
    fig.arrow(c, tip_s, RESIST)
    fig.arrow(c, tip_t, INK, width=2.8)
    fig.unit_vector(c, add(c, mul(n_out, 46)))
    fig.math(add(c, add(mul(n_out, 46), (8, 12))), r"\v{n}", color=UNIT)
    fig.math(add(tip_t, (8, -4)), r"\v{t}", color=INK)
    fig.math(add(tip_n, (-10, 4)), r"−σ_n\v{n}", color=NORMAL, anchor="end")
    fig.math(add(tip_s, (6, 22)), r"\v{τ}", color=RESIST)
    fig.circle(c, 3.4, INK)
    fig.text((c[0], 360), L("表面力 = 法線成分 + せん断成分", "traction = normal component + shear component"),
             SMALL, MUTED, "middle")


def panel_right(c):
    surface(c, 400, 740)
    up = mul(n_out, -1)
    total = mul(up, SIGMA_N * K)
    # sigma_n drawn twice side by side: once whole, once as sigma_n' + u.
    off = mul(t_hat, -26)
    a0 = add(c, off)
    fig.arrow(a0, add(a0, total), NORMAL)
    fig.math(add(add(a0, total), (-8, 2)), r"σ_n = 100 \r{kPa}", color=NORMAL, anchor="end")
    b0 = add(c, mul(t_hat, 4))
    mid = add(b0, mul(up, (SIGMA_N - U) * K))
    fig.line(b0, mid, NORMAL, 2.6)
    fig.arrow(mid, add(b0, total), WATER)
    fig.circle(mid, 2.6, NORMAL)
    fig.math(add(lerp(b0, mid, 0.5), (10, 6)), "σ′_n = 60", 15, NORMAL)
    fig.math(add(lerp(mid, add(b0, total), 0.5), (10, 6)), "u = 40", 15, WATER)
    shear = mul(t_hat, TAU * K)
    s0 = add(c, mul(t_hat, 40))
    fig.arrow(s0, add(s0, shear), RESIST)
    fig.math(add(add(s0, shear), (6, 20)), r"\v{τ}", color=RESIST)
    # English takes two lines to stay inside the panel.
    fig.text(L((c[0], 360), (c[0], 350)),
             L("垂直応力 = 有効垂直応力 + 間隙水圧", "normal stress = effective normal stress"), SMALL, MUTED, "middle")
    fig.text((c[0], 370), L("", "+ pore water pressure"), SMALL, MUTED, "middle")


panel_left((190, 252))
panel_right((585, 252))

if __name__ == "__main__":
    fig.save()
