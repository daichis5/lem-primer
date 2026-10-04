---
title: "Glossary"
lang: en
translated_from: "56298d2"
translated_on: 2026-10-04
---

# Glossary

This page collects the terms and symbols that the three chapters of Theory and the practice pages share. Each definition gives the meaning this primer uses. Some references write a term differently or use other sign conventions.

Before its definition, each entry gives the symbol (when there is one), the English term and the Japanese term. The (→) at the end links to the sections of the text that explain the term.

## The LEM framework

```{glossary}
limit equilibrium method
  limit equilibrium method (LEM)（極限平衡法）

  A method that discretizes an assumed failure mechanism, sets how strength is mobilized and how {term}`internal forces <internal force>` are determined, and finds the {term}`factor of safety` from static equilibrium in the limit state. This primer abbreviates it to LEM (→[Chapter 1, "Overview of LEM"](#overview), [Chapter 2, Section 13.5](#what-section-13-5))

slip surface
  slip surface（すべり面）

  The surface inside a slope along which the soil is assumed to slide when it fails. It may be a circle, an ellipsoid, a composite surface or a free-form surface, depending on the method and its implementation. LEM fixes this surface first and then computes the {term}`factor of safety` (→[Chapter 1, "Overview of LEM"](#overview))

sliding mass
  sliding mass（すべり土塊）

  The soil above the slip surface. It is assumed to move along the slip surface (→[Chapter 1, "Overview of LEM"](#overview))

slice
  slice（スライス）

  In a 2D analysis, one of the vertical strips the sliding mass is divided into (→[Chapter 1, "Overview of LEM"](#overview), [Chapter 2, Section 7](#what-section-7))

column
  column（カラム）

  In a 3D analysis, one of the vertical prisms the sliding mass is divided into, along two horizontal directions. It is the 3D form of a slice (→[Chapter 1, "Overview of LEM"](#overview), [Chapter 2, Section 7](#what-section-7))

spatial discretization
  spatial discretization（空間の離散化）

  Representing continuous shapes, loads and stress distributions by a finite number of slices or columns and resultant forces (→[Chapter 1, Section 9](#section-9), [Chapter 2, Section 10](#what-section-10))

general slip surface
  general slip surface（一般形状のすべり面）

  A slip surface that need not be circular: an ellipse, a polyline, a composite surface and so on. It is also called an arbitrary slip surface. It must still meet some conditions: for example, it can be divided into slices or columns, and each base has a definite area, normal and tangent (→[Chapter 3, Section 3](#practice-section-3), [Section 4](#practice-section-4))

critical slip surface
  critical slip surface（臨界すべり面）

  The surface with the smallest {term}`factor of safety` among the family of slip surfaces searched. Computing the factor of safety and searching for the critical slip surface are separate problems (→[Chapter 3, Section 12.4](#practice-section-12-4))

infinite slope
  infinite slope（無限斜面）

  A model of a slope with the same inclination that extends without end. The slip surface is a plane parallel to the ground surface. The forces on the two sides of a vertical strip cancel, so equilibrium alone fixes the forces on the base, with no assumption about the {term}`interslice forces <interslice force>` (→[Practice 1, Section 2](#infinite-section-2))
```

## Stress and strength

```{glossary}
stress tensor
  $\boldsymbol{\sigma}$　stress tensor（応力テンソル）

  A second-order tensor defined at each point. It is not the force on any one plane, but the force on every plane can be obtained from it (→[Chapter 1, Section 1](#section-1), [Section 2](#section-2))

traction
  $\boldsymbol{t}$　traction（表面力）

  The force per unit area acting on a plane, as a vector. Cauchy's formula $\boldsymbol{t}=\boldsymbol{\sigma}\boldsymbol{n}$ gives it from the {term}`stress tensor` and the outward unit normal vector $\boldsymbol{n}$ (→[Chapter 1, Section 2](#section-2))

normal stress
  $\sigma_n$　normal stress（垂直応力）

  The magnitude of the normal component of the {term}`traction`. Following geotechnical practice, this primer takes compression as positive (→[Chapter 1, "Notation and sign conventions"](#notation), [Section 3](#section-3))

pore water pressure
  $u$　pore water pressure（間隙水圧）

  The pressure of the water filling the pores of the soil. It acts equally in all directions, so it does not directly change the shear component of the {term}`traction` (→[Chapter 1, Section 4](#section-4))

effective normal stress
  $\sigma_n'$　effective normal stress（有効垂直応力）

  The {term}`total normal stress <normal stress>` minus the {term}`pore water pressure`, $\sigma_n'=\sigma_n-u$. It is the normal stress the soil skeleton actually carries, and it controls the {term}`shear strength` (→[Chapter 1, Section 4](#section-4))

shear strength
  $\tau_f$　shear strength（せん断強度）

  The largest shear resistance the soil can develop at failure. It is not the shear stress acting now (→[Chapter 1, Section 5](#section-5))

Mohr–Coulomb failure criterion
  Mohr–Coulomb failure criterion（Mohr–Coulomb則）

  The failure criterion $\tau_f=c'+\sigma_n'\tan\phi'$, which gives the {term}`shear strength` available under the current {term}`effective normal stress`. Here $c'$ is the effective cohesion and $\phi'$ the effective angle of internal friction (→[Chapter 1, Section 5](#section-5))

mobilized shear stress
  $\tau_m$　mobilized shear stress（動員せん断応力）

  The shear stress that actually acts to keep equilibrium. It shows how much of the strength is in use (→[Chapter 1, Section 6](#section-6))
```

## Factor of safety

```{glossary}
factor of safety
  $F_s$　factor of safety（安全率）

  The ratio $F_s=\tau_f/\tau_m$ of the {term}`shear strength` $\tau_f$ to the {term}`mobilized shear stress` $\tau_m$. Standard LEM assumes one value shared by the whole slip surface. Introductions explain it as the ratio of the {term}`resisting force` to the {term}`driving force`. What the ratio is taken of depends on the method, though: the Fellenius method (ordinary method of slices) and the simplified Bishop method take the ratio of moments about the center of the circle (→[Chapter 1, "Overview of LEM"](#overview), [Section 6](#section-6))

resisting force
  resisting force（抵抗力）

  The largest shear force the slip surface can develop. It is the numerator when the {term}`factor of safety` is explained as resisting force ÷ {term}`driving force` (→[Chapter 1, "Overview of LEM"](#overview))

driving force
  driving force（滑動力）

  The force that tends to make the sliding mass slide, such as the component of its weight along the slip surface. For a mass in equilibrium, it equals in magnitude the shear force the slip surface mobilizes (→[Chapter 1, "Overview of LEM"](#overview))
```

## Forces on slices and columns

```{glossary}
base normal force
  $N_i$　base normal force（底面垂直力）

  The {term}`total normal stress <normal stress>` integrated over the base of element $i$. As a vector, the force it exerts on the sliding mass is $-N_i\boldsymbol{n}_i$ (→[Chapter 1, Section 8](#section-8))

pore water force on the base
  $U_i$　pore water force on the base（底面の間隙水圧の合力）

  The {term}`pore water pressure` integrated over the base of element $i$. $N_i-U_i$ is the effective normal force (→[Chapter 1, Section 8](#section-8))

base shear force
  $T_i$　base shear force（底面せん断力）

  The magnitude of the shear force mobilized on the base of element $i$. It is the resultant of the {term}`shear strength` available on the base, divided by the {term}`factor of safety` (→[Chapter 1, Section 8](#section-8))

internal force
  internal force（内力）

  As in mechanics of materials, the force that the two sides of an imaginary cut through a body exert on each other. In LEM it means only the {term}`interslice forces <interslice force>` and intercolumn forces on the boundaries of slices or columns. LEM does not treat the stress inside each element (→[Chapter 2, Section 1](#what-section-1))

interslice force
  $E$，$X$　interslice force（スライス間力）

  The {term}`internal force` that neighboring slices exert on each other. In 2D it is split into the component normal to the boundary, $E$ (the interslice normal force), and the shear component $X$. In 3D it is taken on the boundaries in each of the two directions and called the intercolumn force (→[Chapter 2, Section 2](#what-section-2), [Section 7.2](#what-section-7-2))

line of thrust
  line of thrust（内力線）

  The line through the points of action of the {term}`interslice forces <interslice force>`. Even when a numerical solution exists, if this line passes outside the slices, the distribution of {term}`internal forces <internal force>` is not mechanically sound (→[Chapter 2, Section 10](#what-section-10), [Chapter 3, Section 0](#practice-section-0), [Section 5.2](#practice-section-5-2))
```

## Indeterminacy and methods

```{glossary}
static indeterminacy
  static indeterminacy（静力学的不静定性）

  The state in which there are more unknowns than independent equilibrium equations, so equilibrium alone does not fix a unique distribution of {term}`internal forces <internal force>` (→[Chapter 2, Section 3.1](#what-section-3-1))

closure
  closure（不静定性の解消）

  Adding assumptions so the problem can be solved: ignoring some {term}`internal forces <internal force>`, assuming their directions or the ratios of their components, or using only some of the equilibrium conditions. The methods differ mainly here (→[Chapter 1, Section 9](#section-9), [Chapter 2, Section 3.3](#what-section-3-3))

simplified method
  simplified method（つり合いの一部だけを満たす方法）

  The class of methods that ignore some or all {term}`internal forces <internal force>` and satisfy only some of the equilibrium conditions, such as the Fellenius method, the simplified Bishop method and the simplified Janbu method. In Japanese standards and practice documents, 簡便法 (simplified method) often means the Fellenius method (ordinary method of slices) alone (→[Chapter 2, Section 4](#what-section-4), [Section 6](#what-section-6))

complete equilibrium method
  complete equilibrium method（静力学的に完全な方法）

  A method that assumes the directions of the {term}`internal forces <internal force>` and then satisfies all force and moment equilibrium, such as the Spencer method and the Morgenstern–Price method. It is also called a rigorous method. "Complete" and "rigorous" hold only within the assumed model of internal forces, though: they do not mean an exact solution for a continuum (→[Chapter 2, Section 0](#what-section-0), [Section 5.1](#what-section-5-1))

general limit equilibrium
  general limit equilibrium (GLE)（一般極限平衡法）

  A framework that writes the ratio of the shear to the normal component of the {term}`interslice force` as $X/E=\lambda f(x)$ and satisfies both force and moment equilibrium. It writes the ratio the same way as the Morgenstern–Price method, so this primer treats the two as one family (→[Chapter 2, Section 5.2](#what-section-5-2), [Section 8.4](#what-section-8-4))
```

## Center of moments and direction of sliding

```{glossary}
center of moments
  center of moments（モーメントの中心）

  The reference point for moment equilibrium. For a circle, the center of the circle is used. In 3D, the axis (the axis of rotation) about which moment equilibrium is taken must also be chosen. In methods that do not satisfy all force equilibrium, the {term}`factor of safety` can change with this choice (→[Chapter 3, Section 6](#practice-section-6))

direction of sliding
  $\boldsymbol{d}$　direction of sliding（全体すべり方向）

  In 3D, the representative direction in which the whole sliding mass is assumed to move. It is not just a marker added to a figure: it is a variable in the formulation and affects the {term}`factor of safety` (→[Chapter 3, Section 8](#practice-section-8), [Section 9](#practice-section-9))

local direction of sliding
  $\boldsymbol{m}_i$　local direction of sliding（局所すべり方向）

  The direction of sliding assumed in the tangent plane of the base of each column. One way to set it is to project the {term}`direction of sliding` onto the tangent plane of the base (→[Chapter 1, Section 3](#section-3), [Chapter 3, Section 8](#practice-section-8))
```
