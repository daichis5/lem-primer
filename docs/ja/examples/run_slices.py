"""実践2の数値を表示する．"""

import math

import numpy as np

from infinite_slope import base_stresses, factor_of_safety
from slices import (
    Circle,
    Ellipse,
    Line,
    base_forces,
    bishop,
    cross,
    fellenius,
    fellenius_about,
    fs_force,
    fs_moment,
    janbu,
    make_slices,
    spencer,
)

CENTRE = (6.0, 18.0)

print("1. slice table of figure 1 (n = 6)")
s = make_slices(Circle(), 6)
print("    i       x       z       b   alpha       W       l")
for i in range(6):
    alpha = math.degrees(s.alpha[i])
    print(f"   {i + 1:2d}  {s.x[i]:6.2f}  {s.z[i]:6.2f}  {s.b[i]:6.3f}", end="")
    print(f"  {alpha:6.2f}  {s.W[i]:6.1f}  {s.l[i]:6.3f}")
r = np.stack([s.x - CENTRE[0], s.z - CENTRE[1]], axis=1)
print(f"   largest |r x n| about the centre: {np.abs(cross(r, s.n)).max():.1e} m")

print("2. factor of safety on the circle, dry")
print("     n  Fellenius  Bishop   Janbu  Spencer  theta [deg]")
for n in (6, 12, 25, 50, 100, 200):
    s = make_slices(Circle(), n)
    fs, theta = spencer(s, CENTRE)
    print(f"   {n:3d}     {fellenius(s):.4f}  {bishop(s):.4f}  {janbu(s):.4f}", end="")
    print(f"  {fs:.4f}  {math.degrees(theta):6.2f}")

print("3. one framework, theta = 0 (n = 50)")
s = make_slices(Circle(), 50)
print(f"   Bishop by its formula {bishop(s):.6f},", end=" ")
print(f"F_m(theta = 0) {fs_moment(s, 0.0, CENTRE):.6f}")
print(f"   Janbu by its formula  {janbu(s):.6f}, F_f(theta = 0) {fs_force(s, 0.0):.6f}")

print("4. F_m and F_f against theta (n = 50)")
print("theta_deg,F_m,F_f")
for deg in np.arange(0.0, 30.1, 2.5):
    t = math.radians(deg)
    print(f"{deg:.1f},{fs_moment(s, t, CENTRE):.4f},{fs_force(s, t):.4f}")
fs, theta = spencer(s, CENTRE)
print(
    f"   the two meet at theta = {math.degrees(theta):.2f} deg, Fs = {fs:.4f} (Spencer)"
)

print("5. water table at z = 4 m (n = 50)")
s = make_slices(Circle(), 50, water_level=4.0)
fs, theta = spencer(s, CENTRE)
print(f"   Fellenius, N' = W cos(a) - u l     {fellenius(s):.3f}")
weight = fellenius(s, effective_weight=True)
print(f"   Fellenius, N' = (W - u b) cos(a)   {weight:.3f}")
print(f"   Bishop                             {bishop(s):.3f}")
print(f"   Janbu                              {janbu(s):.3f}")
print(f"   Spencer                            {fs:.3f}", end=" ")
print(f"(theta = {math.degrees(theta):.1f} deg)")

print("6. slices with a negative effective normal force N - U (n = 50)")
for label, level in (("dry", None), ("water at z = 4 m", 4.0)):
    s = make_slices(Circle(), 50, water_level=level)
    fs, theta = spencer(s, CENTRE)
    normal = (
        ("Fellenius", s.W * np.cos(s.alpha)),
        ("Bishop", base_forces(s, bishop(s), 0.0)[0]),
        ("Spencer", base_forces(s, fs, theta)[0]),
    )
    found = []
    for name, N in normal:
        x = s.x[N - s.u * s.l < 0.0]
        found.append(name + " " + (", ".join(f"x = {v:.2f}" for v in x) or "none"))
    print(f"   {label}: " + "; ".join(found))
s = make_slices(Circle(), 50)
alpha = math.degrees(s.alpha[-1])
pull = s.c[-1] * s.l[-1] * math.sin(s.alpha[-1]) / bishop(s)
print(f"   the last slice, dry: alpha = {alpha:.1f} deg,", end=" ")
print(f"W = {s.W[-1]:.1f}, c l sin(alpha) / F = {pull:.1f} [kN/m]")

print("7. a plane 5 m under a planar slope of 30 deg (n = 8)")
line = Line(30.0, 5.0)
s = make_slices(line, 8, ground=line.ground)
expected = factor_of_safety(*base_stresses(30.0, 18.0 * 5.0), 0.0, 10.0, 30.0)
print(f"   Fellenius {fellenius(s):.4f}, Bishop {bishop(s):.4f}, Janbu {janbu(s):.4f}")
print(f"   infinite slope (practice 1) {expected:.4f}")

print("8. an ellipse through the same exit (n = 50)")
s = make_slices(Ellipse(), 50)
print(f"   Bishop's circle formula with the ellipse's angles  {bishop(s):.3f}")
bishop_about = fs_moment(s, 0.0, CENTRE)
print(f"   Bishop, moments about the centre (6, 18)           {bishop_about:.3f}")
print(f"   Fellenius's circle formula                         {fellenius(s):.3f}")
fellenius_o = fellenius_about(s, CENTRE)
print(f"   Fellenius, moments about the centre (6, 18)        {fellenius_o:.3f}")

print("9. moving the moment centre on the ellipse (n = 50)")
print("   centre       Fellenius  Bishop  Spencer")
for centre in ((6.0, 18.0), (6.0, 25.0), (10.0, 18.0)):
    label = f"({centre[0]:.0f}, {centre[1]:.0f})"
    fs = (fellenius_about(s, centre), fs_moment(s, 0.0, centre), spencer(s, centre)[0])
    print(f"   {label:10s}     {fs[0]:.3f}   {fs[1]:.3f}    {fs[2]:.3f}")
