"""Chapter 1, Sections 5 and 6: the Mohr–Coulomb line and the worked example
of Section 6.

c' = 10 kPa, phi' = 30 deg. Before: sigma_n' = 60 kPa (u = 40); after the
water rises: sigma_n' = 40 kPa (u = 60). tau_m = 30 kPa in both. The axes
share one scale, so the line is drawn at its true angle phi'.
"""

import math

from figlib import FAINT, INK, MUTED, NORMAL, RESIST, SMALL, WATER, Figure, L

C, PHI = 10.0, math.radians(30)
TAU_M = 30.0
STATES = [60.0, 40.0]  # sigma_n' before and after the water rises
K = 5.4  # px per kPa, on both axes
O = (92, 330)  # origin of the plot
XMAX, YMAX = 105.0, 55.0


def P(s, tau):
    return (O[0] + s * K, O[1] - tau * K)


def tau_f(s):
    return C + s * math.tan(PHI)


fig = Figure(
    "fig_c03_strength_mobilization",
    390,
    L("Mohr–Coulomb則によるせん断強度と，動員せん断応力",
      "Shear strength by the Mohr–Coulomb failure criterion, and the mobilized shear stress"),
    L("有効垂直応力とせん断応力の図に，c′=10 kPa，ϕ′=30° のMohr–Coulomb則の直線を引く．"
      "6節の数値例の2つの状態について，発揮できるせん断強度 τf と，動員せん断応力 τm=30 kPa を示す．"
      "水位が上がって有効垂直応力が60 kPaから40 kPaに下がると，τf は44.6 kPaから33.1 kPaに下がり，"
      "安全率は1.49から1.10に下がる．",
      "The Mohr–Coulomb line for c′=10 kPa, ϕ′=30°, on a plot of shear stress against effective normal "
      "stress. For the two states of the worked example in Section 6, it shows the available shear "
      "strength τf and the mobilized shear stress τm=30 kPa. When the water table rises and the "
      "effective normal stress falls from 60 kPa to 40 kPa, τf falls from 44.6 kPa to 33.1 kPa, and "
      "the factor of safety falls from 1.49 to 1.10."),
)

# Axes with ticks.
fig.line(O, P(XMAX, 0), INK, 1.4)
fig.line(O, P(0, YMAX), INK, 1.4)
fig.arrow(P(XMAX - 1, 0), P(XMAX + 3, 0), INK, 1.4, head=0.8)
fig.arrow(P(0, YMAX - 1), P(0, YMAX + 3), INK, 1.4, head=0.8)
for s in range(20, 101, 20):
    fig.line(P(s, 0), (P(s, 0)[0], O[1] + 5), INK, 1.2)
    fig.text((P(s, 0)[0], O[1] + 21), str(s), SMALL, MUTED, "middle")
for tau in range(10, 51, 10):
    fig.line(P(0, tau), (O[0] - 5, P(0, tau)[1]), INK, 1.2)
    fig.text((O[0] - 9, P(0, tau)[1] + 5), str(tau), SMALL, MUTED, "end")
fig.math((P(XMAX + 4, 0)[0], O[1] + 6), "σ′_n", 17, INK)
fig.text((P(XMAX + 4, 0)[0] + 2, O[1] + 26), "[kPa]", SMALL, MUTED)
fig.math((O[0] + 10, P(0, YMAX + 3)[1] + 6), "τ", 17, INK)
fig.text((O[0] + 24, P(0, YMAX + 3)[1] + 6), "[kPa]", SMALL, MUTED)

# The Mohr–Coulomb line, and the level the slope needs: tau_m.
S_END = (YMAX - 2 - C) / math.tan(PHI)
fig.line(P(0, C), P(S_END, tau_f(S_END)), INK, 2.6)
fig.math((P(S_END, tau_f(S_END))[0] + 10, P(S_END, tau_f(S_END))[1] + 6),
         r"τ_f = c′ + σ′_n \r{tan} ϕ′", 16, INK)
fig.line(P(0, TAU_M), P(XMAX - 4, TAU_M), RESIST, 1.8, "7 5")
fig.math((P(XMAX - 4, TAU_M)[0], P(XMAX - 4, TAU_M)[1] - 8), "τ_m = 30", 16, RESIST, "end")
fig.math((O[0] + 8, P(0, C)[1] + 18), "c′ = 10", 15, MUTED)
# phi' drawn near the intercept, against a horizontal guide.
a0 = P(8, tau_f(8))
fig.line(a0, (a0[0] + 70, a0[1]), FAINT, 1.1, "4 3")
fig.angle_arc(a0, 58, 0, math.degrees(PHI), MUTED)
fig.math((a0[0] + 64, a0[1] - 8), "ϕ′ = 30°", 15, MUTED)

# The two states.
for s in STATES:
    tf = tau_f(s)
    fs = tf / TAU_M
    base, top, mid = P(s, 0), P(s, tf), P(s, TAU_M)
    fig.line(base, top, FAINT, 1.1, "3 3")
    fig.circle(top, 4.6, INK)
    fig.circle(mid, 4.6, RESIST)
    fig.circle(base, 4, NORMAL)
    # Labels sit on the open side of the line: below it on the right, above it on the left.
    if s > 50:
        at, anchor = (top[0] + 12, top[1] + 22), "start"
    else:
        at, anchor = (top[0] - 14, top[1] - 32), "end"
    fig.math(at, rf"τ_f = {tf:.1f}", 15, INK, anchor)
    fig.math((at[0], at[1] + 21), rf"F_s = {tf:.1f} / 30 = {fs:.2f}", 15, INK, anchor)

# The change: u rises, so sigma_n' falls from 60 to 40 and tau_f with it.
a, b = P(58, 4.5), P(42, 4.5)
fig.arrow(a, b, WATER, 2.4)
fig.math((P(60, 0)[0] + 8, a[1] + 5), L(r"u\t{ が上がる}", r"u\t{ rises}"), 15, WATER)

if __name__ == "__main__":
    fig.save()
    for s in STATES:
        print(s, round(tau_f(s), 2), round(tau_f(s) / TAU_M, 3))
