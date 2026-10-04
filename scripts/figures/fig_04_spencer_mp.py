"""Chapter 2, Section 5: the interslice resultants of Spencer and Morgenstern–Price.

Both panels use the same slices and the same E on each boundary. The
resultant on boundary k leans at theta_k with tan(theta_k) = X/E: constant
for Spencer, lambda * f(x_k) for Morgenstern–Price with a half-sine f.
Under each mass, f(x) is drawn on the same x, so each arrow's lean can be
read off the curve. Spencer is the case f(x) = 1.
"""

import math

from figlib import FAINT, GROUND, INK, INTER, MUTED, SOIL, SOIL_EDGE, Figure, L, Slope, View, add

s = Slope(n=8)
THETA_SPENCER = math.radians(25)
LAMBDA = math.tan(math.radians(40))
E_LEN = 40.0  # px for the largest E


def f_half_sine(x):
    return math.sin(math.pi * (x - s.x0) / (s.x1 - s.x0))


fig = Figure(
    "fig_04_spencer_mp",
    360,
    L("Spencer法とMorgenstern–Price法の，スライス間力の向きの仮定",
      "The direction of the interslice forces assumed by the Spencer and Morgenstern–Price methods"),
    L("同じスライスの境界に働くスライス間力の合力を，2つの手法で比べる．Spencer法では，すべての境界で合力が同じ角度 θ で傾く．"
      "Morgenstern–Price法では，合力の傾き X/E が λf(x) に従って場所ごとに変わる．"
      "下のグラフは，それぞれの f(x) を同じ横軸で示す．Spencer法は f(x)=1 の場合にあたる．",
      "The resultant interslice forces on the same slice boundaries under two methods. In the Spencer "
      "method, the resultant leans at the same angle θ on every boundary. In the Morgenstern–Price "
      "method, its inclination X/E varies from place to place as λf(x). The graphs below show each "
      "f(x) on the same horizontal axis. The Spencer method is the case f(x)=1."),
)


def panel(x_off, title, formula, f, label_f):
    v = View(13.4, (x_off + 22, 214))
    fig.text((x_off + 180, 26), title, 15, INK, "middle", weight="bold")
    fig.math((x_off + 180, 50), formula, 16, INTER, "middle")
    fig.polygon([v.p(p) for p in s.ground_pts(-1.6, 24.8) + [(24.8, -2.0), (-1.6, -2.0)]], fill=GROUND)
    fig.polygon([v.p(p) for p in s.mass()], fill=SOIL)
    thrust = [v.p((s.x0, s.slip(s.x0)))]
    for k in range(1, s.n):
        x = s.x0 + k * s.b
        fig.line(v.p((x, s.slip(x))), v.p((x, s.ground(x))), SOIL_EDGE, 1.2)
        p = v.p((x, s.slip(x) + 0.36 * (s.ground(x) - s.slip(x))))
        thrust.append(p)
        theta = math.atan(f(x) * (math.tan(THETA_SPENCER) if f is ONE else LAMBDA))
        e = E_LEN * math.sin(math.pi * k / s.n)
        r = e / math.cos(theta)
        tip = add(p, (r * math.cos(theta), -r * math.sin(theta)))
        fig.arrow(p, tip, INTER, 2.4, head=0.85)
        fig.circle(p, 2.6, INTER)
        if k == 2:
            fig.line(p, add(p, (46, 0)), FAINT, 1, "3 3")
            fig.angle_arc(p, 30, 0, math.degrees(theta), MUTED)
            fig.math(add(p, (36, 14)), "θ" if f is ONE else "θ_2", 15, MUTED)
    thrust.append(v.p((s.x1, s.slip(s.x1))))
    fig.polyline(thrust, "#c4b5fd", 1, "3 4")
    fig.polyline([v.p(p) for p in s.ground_pts(-1.6, 24.8)], SOIL_EDGE, 1.8)
    fig.polyline([v.p(p) for p in s.arc_pts(s.x0, s.x1)], INK, 2.6)

    # f(x) on the same x as the slices.
    y0, amp = 322, 46
    xa, xb = v.p((s.x0, 0))[0], v.p((s.x1, 0))[0]
    fig.line((xa - 6, y0), (xb + 10, y0), INK, 1.1)
    fig.line((xa, y0 + 4), (xa, y0 - amp - 10), INK, 1.1)
    pts = []
    for j in range(61):
        x = s.x0 + (s.x1 - s.x0) * j / 60
        pts.append((v.p((x, 0))[0], y0 - amp * f(x)))
    fig.polyline(pts, INTER, 2)
    for k in range(1, s.n):
        x = s.x0 + k * s.b
        px = v.p((x, 0))[0]
        fig.line((px, y0), (px, y0 - amp * f(x)), FAINT, 1, "2 3")
        fig.circle((px, y0 - amp * f(x)), 2.6, INTER)
    fig.math((xa - 8, y0 - amp + 4), "1", 13, MUTED, "end")
    fig.math((xb + 14, y0 + 5), "x", 15, MUTED)
    fig.math((xa + 8, y0 - amp - 14), label_f, 15, MUTED)


def ONE(x):
    return 1.0


panel(10, L("Spencer法", "Spencer method"),
      L(r"X/E = \r{tan} θ\t{（一定）}", r"X/E = \r{tan} θ\t{ (constant)}"), ONE,
      L(r"f(x) = 1\t{（一定）}", r"f(x) = 1\t{ (constant)}"))
panel(390, L("Morgenstern–Price法", "Morgenstern–Price method"), "X/E = λ f(x)", f_half_sine,
      L(r"f(x)\t{：正弦の半波}", r"f(x)\t{: half sine wave}"))
fig.line((380, 16), (380, 345), "#e2e8f0", 1)

if __name__ == "__main__":
    fig.save()
