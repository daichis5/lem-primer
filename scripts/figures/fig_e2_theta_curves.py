"""Practice 2: F_m(theta) and F_f(theta) for the circle of Chapter 1's Figure 1.

The values are read from docs/ja/examples/output/run_slices.txt, which
`make examples` writes from the practice code, so this figure and the table on
the page come from one computation. Both languages read the Japanese output: the
numbers are the same. Run `make examples` first.
"""

import re

from figlib import DOCS, INK, MUTED, RULE, SMALL, Figure, L

SOURCE = DOCS / "ja" / "examples" / "output" / "run_slices.txt"
T0, T1 = 0.0, 30.0  # theta [deg]
F0, F1 = 1.8, 2.3  # F_s
X0, X1 = 92.0, 700.0  # plot area [px]
Y0, Y1 = 300.0, 36.0


def read():
    lines = SOURCE.read_text(encoding="utf-8").splitlines()
    start = lines.index("theta_deg,F_m,F_f") + 1
    rows = []
    for line in lines[start:]:
        if not re.fullmatch(r"-?[0-9.]+,-?[0-9.]+,-?[0-9.]+", line):
            break
        rows.append(tuple(float(v) for v in line.split(",")))
    meet = re.search(r"theta = (-?[0-9.]+) deg, Fs = (-?[0-9.]+) \(Spencer\)", SOURCE.read_text(encoding="utf-8"))
    if meet is None:
        raise SystemExit(f"{SOURCE} has no Spencer line: run `make examples` first")
    spencer = (float(meet.group(1)), float(meet.group(2)))
    # The axes are fixed, so stop rather than draw outside them if the output changes.
    thetas = [r[0] for r in rows] + [spencer[0]]
    values = [f for r in rows for f in r[1:]] + [spencer[1]]
    if not rows or rows[0][0] != T0 or rows[-1][0] != T1 or not (
        min(thetas) >= T0 and max(thetas) <= T1 and min(values) >= F0 and max(values) <= F1
    ):
        raise SystemExit(f"{SOURCE}: the values leave the axes (theta {T0}-{T1}, F_s {F0}-{F1})")
    return rows, spencer


def px(theta, fs):
    return (X0 + (theta - T0) / (T1 - T0) * (X1 - X0), Y0 + (fs - F0) / (F1 - F0) * (Y1 - Y0))


rows, (theta_s, fs_s) = read()

fig = Figure(
    "fig_e2_theta_curves",
    360,
    L("スライス間力の合力の傾きと，2つのつり合いから求めた安全率",
      "The inclination of the interslice resultant, and the factors of safety from two equilibria"),
    L("第1章の図1の円弧で，スライス間力の合力の傾き θ を決定して，モーメントのつり合いから求めた安全率 F_m と，"
      "力のつり合いから求めた安全率 F_f を描いた図．θ = 0 の F_m は簡易Bishop法，F_f は簡易Janbu法の値で，"
      "2本の曲線が交わる点がSpencer法の解である．",
      "For the circle of Figure 1 in Chapter 1, the inclination θ of the resultant interslice force is "
      "fixed, and the factor of safety F_m from moment equilibrium and F_f from force equilibrium are "
      "plotted against it. At θ = 0, F_m is the value of the simplified Bishop method and F_f that of "
      "the simplified Janbu method. The point where the two curves cross is the Spencer solution."),
)

for k in range(6):
    fs = F0 + 0.1 * k
    y = px(T0, fs)[1]
    fig.line((X0, y), (X1, y), RULE, 1.0)
    fig.text((X0 - 10, y), f"{fs:.1f}", SMALL, MUTED, "end", vcenter=True)
for theta in range(0, 31, 5):
    x = px(theta, F0)[0]
    fig.line((x, Y0), (x, Y0 + 5), MUTED, 1.0)
    fig.text((x, Y0 + 22), f"{theta}", SMALL, MUTED, "middle")
fig.line((X0, Y0), (X1, Y0), INK, 1.4)
fig.line((X0, Y0), (X0, Y1), INK, 1.4)
fig.math((X0 + (X1 - X0) / 2, Y0 + 48),
         L(r"\t{スライス間力の合力の傾き }θ\t{ [°]}", r"\t{inclination of the interslice resultant }θ\t{ [°]}"),
         15, MUTED, anchor="middle")
fig.math((X0 - 52, Y1 - 12), "F_s", 15, MUTED)

fig.polyline([px(t, fm) for t, fm, _ in rows], INK, 2.4)
fig.polyline([px(t, ff) for t, _, ff in rows], INK, 2.4, dash="9 6")
last = rows[-1]
# A hair space keeps the colon off the italic subscript.
fig.math((px(last[0], last[1])[0] - 6, px(last[0], last[1])[1] + 26),
         L(r"F_m\t{：モーメントのつり合い}", r"F_m\t{" "\u200a" r": moment equilibrium}"),
         15, INK, anchor="end")
fig.math((px(last[0], last[2])[0] - 6, px(last[0], last[2])[1] - 14),
         L(r"F_f\t{：力のつり合い}", r"F_f\t{" "\u200a" r": force equilibrium}"),
         15, INK, anchor="end")

first = rows[0]
for (theta, fs), label, dx, dy, anchor in (
    ((first[0], first[1]), L("簡易Bishop法", "simplified Bishop method"), 12, -14, "start"),
    ((first[0], first[2]), L("簡易Janbu法", "simplified Janbu method"), 12, 20, "start"),
    ((theta_s, fs_s), L("Spencer法", "Spencer method"), -10, -16, "end"),
):
    p = px(theta, fs)
    fig.circle(p, 5.0, "#fff", INK, 2.0)
    fig.text((p[0] + dx, p[1] + dy), label, SMALL, INK, anchor)

if __name__ == "__main__":
    fig.save()
