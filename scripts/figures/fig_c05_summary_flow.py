"""Chapter 1, Section 9: the path from the stress field to the factor of safety.

One box per step, in the order of Sections 1 to 9: the section, the quantity
and its formula, in three columns shared by all boxes. Arrows run down the
boxes' common centre line, each labelled with what the step does. Two panels
group the steps: Sections 1 to 6 work with the stress at each point,
Sections 7 to 9 with the resultants on each base.
"""

from figlib import INK, LABEL, MATH, MUTED, RULE, SMALL, TINT, Figure, L

STEPS = [  # (section, quantity, formula, label of the arrow into the next step)
    (L("1節", "§1"), L("応力場と各点のつり合い", "equilibrium at each point"),
     r"\v{σ},  ∇·\v{σ} + ρ\v{b} = \v{0}", L(r"\t{Cauchyの公式}", r"\t{Cauchy's formula}")),
    (L("2節", "§2"), L("すべり面上の表面力", "traction on the slip surface"),
     r"\v{t} = \v{σ}\v{n}", L(r"\t{法線方向と面内に分ける}", r"\t{split along and across the surface}")),
    (L("3節", "§3"), L("垂直応力とせん断応力", "normal and shear stress"),
     r"σ_n,  \v{τ}", L(r"\t{間隙水圧 }u\t{ を引く}", r"\t{subtract the pore pressure }u")),
    (L("4節", "§4"), L("有効垂直応力", "effective normal stress"),
     r"σ′_n = σ_n − u", L(r"\t{Mohr–Coulomb則}", r"\t{Mohr–Coulomb failure criterion}")),
    (L("5節", "§5"), L("せん断強度", "shear strength"),
     r"τ_f = c′ + σ′_n \r{tan} ϕ′", L(r"\t{安全率 }F_s\t{ で割る}", r"\t{divide by the factor of safety }F_s")),
    (L("6節", "§6"), L("動員せん断応力", "mobilized shear stress"),
     r"τ_m = τ_f / F_s", L(r"\t{面積分と，底面ごとのモデル化}", r"\t{integrate over each base, and model it}")),
    (L("7・8節", "§7–8"), L("底面に働く合力", "resultant forces on a base"),
     r"N_i,  U_i,  T_i", L(r"\t{つり合い式と，LEMに固有の仮定}", r"\t{equilibrium equations and LEM's assumptions}")),
    (L("9節", "§9"), L("安全率と各合力", "factor of safety and the forces"), r"F_s", None),
]
POINT_STEPS = 6  # Sections 1 to 6 are in the first panel

BOX_X, BOX_W, BOX_H = 120, 520, 44
NAME_X, FORMULA_X = BOX_X + 76, BOX_X + 324
GAP = 40  # between two boxes in one panel
PAD_TOP, PAD_BOTTOM, PANEL_GAP = 34, 14, 28
PANEL_X, PANEL_W = BOX_X - 24, BOX_W + 48
CX = BOX_X + BOX_W / 2

# Box tops, top to bottom; the second panel starts after the first one's padding.
tops, y = [], 16 + PAD_TOP
for k in range(len(STEPS)):
    if k == POINT_STEPS:
        y += PAD_BOTTOM + PANEL_GAP + PAD_TOP - GAP
    tops.append(y)
    y += BOX_H + GAP
height = tops[-1] + BOX_H + PAD_BOTTOM + 16

fig = Figure(
    "fig_c05_summary_flow",
    height,
    L("連続体の応力から安全率までの流れ", "From the stress in a continuum to the factor of safety"),
    L("1節から9節の段階を，上から順に箱で示す．各箱は，節，量，式を並べる．箱の間の矢印には，"
      "その段階で行うことを書いている．1節から6節は点ごとの応力を，7節から9節は底面ごとの合力を扱う．",
      "The steps of Sections 1 to 9, as boxes from top to bottom. Each box gives the section, the "
      "quantity and its formula. The arrow between two boxes is labelled with what that step does. "
      "Sections 1 to 6 work with the stress at each point, Sections 7 to 9 with the resultants on "
      "each base."),
)

panels = [
    (tops[0] - PAD_TOP, tops[POINT_STEPS - 1] + BOX_H + PAD_BOTTOM, L("点ごとの応力", "stress at each point")),
    (tops[POINT_STEPS] - PAD_TOP, tops[-1] + BOX_H + PAD_BOTTOM, L("底面ごとの合力", "resultants on each base")),
]
for top, bottom, label in panels:
    fig.rect(PANEL_X, top, PANEL_W, bottom - top, fill=TINT, color=RULE)
    fig.text((PANEL_X + 14, top + 22), label, SMALL, MUTED)

for top, (section, name, formula, step) in zip(tops, STEPS):
    mid = top + BOX_H / 2
    fig.rect(BOX_X, top, BOX_W, BOX_H, fill="#fff", color=RULE, r=6)
    fig.text((BOX_X + 16, mid), section, SMALL, MUTED, vcenter=True)
    fig.text((NAME_X, mid), name, LABEL, INK, vcenter=True)
    fig.math((FORMULA_X, mid), formula, MATH, INK, vcenter=True)

for k, (*_, step) in enumerate(STEPS[:-1]):
    y0, y1 = tops[k] + BOX_H + 4, tops[k + 1] - 4
    fig.arrow((CX, y0), (CX, y1), MUTED, width=1.8)
    # The arrow between the panels has its label in the gap between them.
    label_y = tops[k + 1] - PAD_TOP - PANEL_GAP / 2 if k + 1 == POINT_STEPS else (y0 + y1) / 2
    fig.math((CX + 14, label_y), step, SMALL, MUTED, vcenter=True)

if __name__ == "__main__":
    fig.save()
