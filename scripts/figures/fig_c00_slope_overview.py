"""Chapter 1, overview of LEM: a slope, a circular slip surface, slices, and the
forces on one slice.

The slip surface is a true circle. The highlighted slice carries W at its
centroid and N, T at the middle of its base chord, with N = W cos(alpha) and
T = W sin(alpha), so the three arrows close into a triangle (interslice
forces are left out of this overview).
"""

import math

from figlib import (GROUND, INK, MUTED, NORMAL, RESIST, SMALL, SOIL, SOIL_EDGE, UNIT, WEIGHT, Figure,
                    L, Slope, View, add, centroid, mul, unit)

GAMMA = 18.0  # unit weight [kN/m3]
PICK = 3  # the slice that carries the forces

s = Slope(n=6)
v = View(19.5, (178, 268))
fig = Figure(
    "fig_c00_slope_overview",
    330,
    L("LEMが対象とする斜面，すべり面，スライス", "The slope, slip surface and slices that LEM deals with"),
    L("斜面の中に円弧のすべり面を仮定し，その上のすべり土塊を鉛直なスライスに分ける．"
      "1つのスライスに，自重と，底面に働く垂直力とせん断力を示す．",
      "A circular slip surface is assumed in the slope, and the sliding mass above it is cut into "
      "vertical slices. One slice shows its weight and the normal and shear forces on its base."),
)

left, right, bottom = -9.0, 29.5, -3.0
fig.polygon([v.p(p) for p in s.ground_pts(left, right) + [(right, bottom), (left, bottom)]], fill=GROUND)
fig.polygon([v.p(p) for p in s.mass()], fill=SOIL)
for k in range(1, s.n):
    x = s.x0 + k * s.b
    fig.line(v.p((x, s.slip(x))), v.p((x, s.ground(x))), SOIL_EDGE, 1, "4 4")
pts = s.slice(PICK)
fig.polygon([v.p(p) for p in pts], fill="#ead39c", color=SOIL_EDGE, width=1.6)
fig.polyline([v.p(p) for p in s.ground_pts(left, right)], SOIL_EDGE, 2)
fig.polyline([v.p(p) for p in s.arc_pts(s.x0, s.x1)], INK, 3)

g, area = centroid(pts)
W = GAMMA * area
mid, alpha = s.chord(PICK)
N, T = W * math.cos(alpha), W * math.sin(alpha)
# Scale forces so that W ends just above the base: the arrows stay inside.
base_under_g = mid[1] + (g[0] - mid[0]) * math.tan(alpha)
FORCE = 0.82 * (g[1] - base_under_g) * v.k / W

fig.arrow(v.p(g), add(v.p(g), (0, W * FORCE)), WEIGHT)
fig.circle(v.p(g), 3, WEIGHT)
into = unit(v.d((-math.sin(alpha), math.cos(alpha))))
up_slope = unit(v.d((math.cos(alpha), math.sin(alpha))))
fig.arrow(v.p(mid), add(v.p(mid), mul(into, N * FORCE)), NORMAL)
fig.arrow(v.p(mid), add(v.p(mid), mul(up_slope, T * FORCE)), RESIST)

wl = add(v.p(g), (8, 0.36 * W * FORCE))
fig.math(wl, "W_i", color=WEIGHT)
fig.text(add(wl, (0, 17)), L("自重", "weight"), SMALL, WEIGHT)
nl = add(v.p(mid), add(mul(into, N * FORCE), (-12, -6)))
fig.math(nl, "N_i", color=NORMAL, anchor="end")
fig.text(L(add(nl, (0, 18)), add(nl, (-8, 18))), L("垂直力", "normal force"), SMALL, NORMAL, "end")
tl = add(v.p(mid), add(mul(up_slope, T * FORCE), (6, -8)))
fig.math(tl, "T_i", color=RESIST)
fig.text(add(tl, (24, -1)), L("せん断力", "shear force"), SMALL, RESIST)

# Names of the parts.
xa, xb = s.edges(PICK)
top_mid = v.p(((xa + xb) / 2, s.ground((xa + xb) / 2)))
fig.line(add(top_mid, (0, -6)), add(top_mid, (0, -30)), MUTED, 1)
fig.math(add(top_mid, (0, -36)), L(r"\t{スライス }i", r"\t{slice }i"), 15, INK, "middle")
fig.line(v.p((21.2, 8.8)), v.p((22.4, 11.2)), MUTED, 1)
fig.text(add(v.p((22.4, 11.2)), (0, -6)), L("すべり土塊", "sliding mass"), SMALL, INK, "middle")
fig.text(v.p((5.0, 7.3)), L("斜面", "slope"), SMALL, MUTED, "middle")
fig.line(v.p((6.2, 6.6)), v.p((8.4, 5.2)), MUTED, 1)
fig.text(v.p((21.5, -1.9)), L("地盤", "ground"), SMALL, MUTED, "middle")
fig.text(add(v.p((10.0, s.slip(10.0))), (0, 30)),
         L("すべり面（仮定する曲面）", "slip surface (an assumed surface)"), SMALL, INK, "middle")

# The direction the mass slides, beside the slip surface near the toe.
pa = v.p((s.x0 + 4.6, s.slip(s.x0 + 4.6) + 0.5))
pb = v.p((s.x0 + 2.0, s.slip(s.x0 + 2.0) + 0.5))
fig.arrow(pa, pb, UNIT, width=2, dash="5 4")
fig.text(add(pb, (-12, -14)), L("すべる向き", "direction the mass slides"), SMALL, MUTED, "end")

if __name__ == "__main__":
    fig.save()
    print(f"alpha={math.degrees(alpha):.1f} W={W:.0f} N={N:.0f} T={T:.0f}")
