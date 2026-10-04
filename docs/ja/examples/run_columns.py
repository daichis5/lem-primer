"""実践3の数値を表示する．"""

import math

import numpy as np

import columns
import slices
from infinite_slope import base_stresses, factor_of_safety

D = np.array([-1.0, 0.0, 0.0])  # 全体すべり方向：斜面を下る向き
AXIS = np.cross(D, [0.0, 0.0, 1.0])  # 回転軸：d に直交する水平な軸（y 方向）
CENTRE = np.array([6.0, 0.0, 18.0])  # 実践2の円の中心を，y = 0 に置く
R = slices.Circle().radius


def methods(col, centre):
    return (
        columns.hovland(col, columns.section_directions(col, D)),
        columns.hovland_moment(col, centre, AXIS),
        columns.bishop(col, centre, AXIS),
    )


print("1. a plane 5 m under a planar slope of 30 deg (h = 0.5 m)")
plane = columns.Plane(30.0, 5.0)
col = columns.make_columns(plane, 0.5, ground=plane.ground)
fs = methods(col, np.array([10.0, 10.0, 30.0]))
expected = factor_of_safety(*base_stresses(30.0, 18.0 * 5.0), 0.0, 10.0, 30.0)
print(f"   {len(col.W)} columns:", end=" ")
print(f"Hovland {fs[0]:.4f}, moment form {fs[1]:.4f}, Bishop {fs[2]:.4f}")
print(f"   infinite slope (practice 1) {expected:.4f}")

print("2. the circle of practice 2 as a cylinder 10 m long (h = 0.25 m)")
col = columns.make_columns(columns.Cylinder(10.0), 0.25)
fs = methods(col, CENTRE)
s = slices.make_slices(slices.Circle(), 200)
print(f"   {len(col.W)} columns:", end=" ")
print(f"Hovland {fs[0]:.4f}, moment form {fs[1]:.4f}, Bishop {fs[2]:.4f}")
print(f"   2D, n = 200: Fellenius {slices.fellenius(s):.4f},", end=" ")
print(f"Bishop {slices.bishop(s):.4f}")

print("3. ellipsoids with semi-axes (R, B, R) and centre (6, 0, 18) (h = 0.25 m)")
print("      B  columns  Hovland  moment   Bishop")
for k in (1, 2, 5):
    col = columns.make_columns(columns.Ellipsoid(CENTRE, (R, k * R, R)), 0.25)
    fs = methods(col, CENTRE)
    print(f"   {k:2d} R  {len(col.W):7d}   {fs[0]:.4f}  {fs[1]:.4f}  {fs[2]:.4f}")

sphere = columns.make_columns(columns.Ellipsoid(CENTRE, (R, R, R)), 0.25)

print("4. Hovland on the sphere, with and without the lateral tilt of the bases")
hyp = np.hypot(sphere.n[:, 0], sphere.n[:, 2])  # 横に傾いていない底面では 1
N = sphere.W * (sphere.n @ columns.GRAVITY)
driving = np.sum(sphere.W * sphere.n[:, 0] / hyp)
for label, A, N_i in (
    ("A and N of the untilted section", sphere.A * hyp, N / hyp),
    ("only A of the tilted base", sphere.A, N / hyp),
    ("only N of the tilted base", sphere.A * hyp, N),
    ("both (Hovland)", sphere.A, N),
):
    resisting = np.sum(sphere.c * A + N_i * sphere.tan_phi)
    print(f"   {label:31s}  {resisting / driving:.4f}")

print("5. base normal force on the sphere by lateral tilt of the base")
m = columns.rotation_directions(sphere, AXIS)
n_bishop = columns.vertical_normal_force(
    sphere, m, columns.bishop(sphere, CENTRE, AXIS)
)
tilt = np.degrees(np.arcsin(np.abs(sphere.n[:, 1])))
print("   tilt [deg]  columns  sum N, Bishop / Hovland")
for lo, hi in ((0, 10), (10, 30), (30, 90)):
    k = (tilt >= lo) & (tilt < hi)
    ratio = n_bishop[k].sum() / N[k].sum()
    print(f"   {lo:2d} - {hi:2d}    {k.sum():7d}  {ratio:.3f}")
negative = n_bishop - sphere.u * sphere.A < 0.0
height = sphere.top[negative, 2] - sphere.base[negative, 2]
print(f"   columns with N - U < 0: Bishop {negative.sum()},", end=" ")
print(f"all at most {height.max():.2f} m tall;", end=" ")
print(f"Hovland {np.sum(N - sphere.u * sphere.A < 0.0)}")

print("6. local direction of sliding on the sphere (Hovland)")
section = columns.hovland(sphere, columns.section_directions(sphere, D))
projected = columns.hovland(sphere, columns.projected_directions(sphere, D))
print(f"   in the vertical plane through d  {section:.4f}")
print(f"   d projected onto each base       {projected:.4f}")

print("7. azimuth of d on the sphere (Hovland)")
print("   azimuth [deg]  section  projected")
for deg in (-30, -15, 0, 15, 30):
    t = math.radians(deg)
    d = np.array([-math.cos(t), math.sin(t), 0.0])
    section = columns.hovland(sphere, columns.section_directions(sphere, d))
    projected = columns.hovland(sphere, columns.projected_directions(sphere, d))
    print(f"   {deg:+13d}  {section:7.4f}  {projected:9.4f}")

print("8. column size on the sphere")
print("   h [m]  columns  Hovland   Bishop")
for h in (1.0, 0.5, 0.25):
    col = columns.make_columns(columns.Ellipsoid(CENTRE, (R, R, R)), h)
    fs = methods(col, CENTRE)
    print(f"   {h:5.2f}  {len(col.W):7d}   {fs[0]:.4f}  {fs[2]:.4f}")
