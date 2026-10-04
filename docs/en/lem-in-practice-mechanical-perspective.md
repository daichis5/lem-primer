---
title: "Using the limit equilibrium method in practice: slip surfaces other than circles, the direction of sliding, and checking results"
lang: en
series: "3 of 3"
translated_from: "56298d2"
translated_on: 2026-10-04
---

# Using the limit equilibrium method in practice

**Slip surfaces other than circles, the direction of sliding, and checking results**

By the end of Chapter 2, the sliding mass had been discretized into slices or columns, and a strength equation and assumptions on the internal forces turned equilibrium at the limit state into a problem that can be solved. This chapter takes up the questions that arise when that theory is used in actual calculations. In particular, it looks at what inputs such as the shape of the slip surface, the direction of sliding and the discretization determine mechanically, and what they approximate. It keeps this apart from the impression that a method's name gives.

This chapter assumes that you have read [Chapter 1](continuum-mechanics-to-lem-start.md) and [Chapter 2](what-is-limit-equilibrium-method.md). The terms and symbols are collected in the [Glossary](lem-glossary.md).

```{admonition} Key points of this chapter
Even when an {term}`LEM <limit equilibrium method>` was derived for circular slips, its assumptions on the {term}`internal forces <internal force>` and its equilibrium equations can be applied to a general slip surface, and the {term}`factor of safety` can be computed numerically.

However, **being able to compute**, **being the same method as the original**, and **keeping the same properties as the original** are separate questions.
```

This chapter takes up the following five questions.

- Why can a method derived for circles also be used for elliptical slip surfaces and slip surfaces of any shape?
- When the shape is generalized, what remains and what is lost?
- In 3D LEM, what does setting the direction of sliding decide in the calculation?
- How much of the mechanics can be judged from the method name that software displays?
- Once a factor of safety is obtained as a number, what should be checked?

---

(practice-section-0)=

## 0. Four stages to keep apart from the start

When LEM is used in practice, think of the following four stages separately.

| Stage | Question | Example of the check |
|---|---|---|
| The shape can be entered | Can the slip surface be divided into slices? | A circle, an ellipse, a polyline or a composite surface can be divided into slices |
| It can be computed | Does the iteration give $F_s$? | The residuals converge and a numerical solution is returned |
| It satisfies equilibrium | Does it satisfy the required force and moment equilibrium? | For Spencer-type and Morgenstern–Price-type methods, check both force and moment equilibrium |
| It is mechanically sound | Are the assumed internal forces, the mechanism of deformation and the direction of sliding realistic? | Check the line of thrust (the line through the points of action of the interslice forces), the base normal forces, and whether the mass can deform that way |

For example, suppose a Bishop-type factor of safety converges for a non-circular surface. That alone does not show any of the following.

- It is derived in the same way as the classical Bishop equation for circles
- It satisfies horizontal force equilibrium for the whole mass
- It does not depend on the choice of the center of moments
- The soil mass can move along that surface as a rigid body
- The distribution of internal forces it gives is close to the actual stress field

This distinction is the yardstick for the whole chapter.

---

## Why a method for circles can still compute general shapes

(practice-section-1)=

### 1. The minimum quantities an LEM calculation needs

Let an arbitrary 2D {term}`slip surface` be

$$
z=s(x)
$$ (eq-practice-surface-2d)

If it can be divided into the bases of a finite number of {term}`slices <slice>`, the following quantities can be set for each base.

- The base length $l_i$ or the base area $A_i$
- The base inclination $\alpha_i$
- The assumed local direction of sliding $\boldsymbol{m}_i$
- The local normal direction $\boldsymbol{n}_i$
- The weight $W_i$
- The {term}`pore water force <pore water force on the base>` $U_i$
- The position vector $\boldsymbol{r}_i$ from an arbitrary reference point to the resultant on the base

Here $\boldsymbol{n}_i$ points outward from the {term}`sliding mass`, and $\boldsymbol{m}_i$ points in the assumed direction of sliding. With these directions, the compressive normal force and the shear force resisting sliding that the base exerts on the sliding mass are $-N_i\boldsymbol{n}_i$ and $-T_i\boldsymbol{m}_i$.

The resultant force on the base can be written as follows.

$$
\boldsymbol{R}_{b,i}
=-N_i\boldsymbol{n}_i-T_i\boldsymbol{m}_i
$$ (eq-practice-base-force)

With strength from the {term}`Mohr–Coulomb failure criterion` and a common factor of safety, the magnitude of the {term}`base shear force` is

$$
T_i
=
\frac{
c_i'A_i+(N_i-U_i)\tan\phi_i'
}{F_s}
$$ (eq-practice-base-shear)

So whether the surface is a circle, an ellipse or a polyline, the forces and moments can be summed once the local normals, the tangents and the moment arms can be computed.

$$
\sum_i \boldsymbol{R}_{b,i}
+\sum \boldsymbol{F}_{\mathrm{external}}
=\boldsymbol{0}
$$ (eq-practice-force-balance)

$$
\sum_i
\boldsymbol{r}_i\times\boldsymbol{R}_{b,i}
+\sum \boldsymbol{M}_{\mathrm{external}}
=\boldsymbol{0}
$$ (eq-practice-moment-balance)

In this sense, **the operation of computing a factor of safety is not itself limited to circles**.

In a generalized LEM framework, the differences between methods such as Fellenius, Bishop, Janbu, Spencer and Morgenstern–Price can be expressed mainly by a combination of the following.

1. How the {term}`interslice forces <interslice force>` are assumed
2. Which of force equilibrium and moment equilibrium is used
3. Which unknowns are found by iteration

In other words, the mechanical character of a method is not determined by "the input shape of a circle" alone. It is determined by **the assumptions on the internal forces and the equilibrium conditions used**. [Zhu, Lee and Jiang (2003)](https://doi.org/10.1680/geot.2003.53.4.377) give a formulation that treats general slip surfaces in a unified way.

---

(practice-section-2)=

### 2. Circles have special geometric properties

```{figure} ./figures/fig_s02_circle_general_surface.svg
:name: fig-s02-circle-general-surface
:alt: A circular slip surface, on which the lines of action of all base normal forces pass through the center, and an elliptical slip surface, on which they do not

Left: on a circle, the lines of action of all base normal forces pass through the center $O$. Every shear force has the radius $R$ as its arm. Right: on an ellipse, the lines of action do not pass through $O'$, so the normal forces have an arm $d$. The tangent directions also differ from the directions of velocity for a rotation about $O'$
```

Being able to compute general shapes does not put circles on the same footing as other curves. A circle has properties that suit methods using moment equilibrium particularly well.

#### 2.1 The base normal forces pass through a common center

Let $O$ be the center of the circle. When each base is approximated by a short arc of the circle, the line of action of the {term}`base normal force` $N_i$ passes through $O$.

$$
M_O(N_i)=0
$$ (eq-practice-circle-normal-moment)

So the unknown base normal forces do not appear directly in the moment equation about the center of the circle.

(practice-section-2-2)=

#### 2.2 The arms of the base shear forces are a common radius

If $R$ is the radius of the circle, the moment of a base shear force can be written schematically as

$$
M_O(T_i)=R\,T_i
$$ (eq-practice-circle-shear-moment)

This makes the moment equation for the whole mass simple.

#### 2.3 It is easy to read as a rigid-body rotation

The direction of the tangent along a circle matches the direction of velocity for a rotation about the common center. This fits the picture of the sliding mass rotating as one rigid body.

Because of these properties, on a circular surface the moment equilibrium is often relatively insensitive to the assumption on the interslice shear forces. This is one reason why even the simplified Bishop method tends to give a reasonable factor of safety for circular slips. [Krahn (2003)](https://doi.org/10.1139/t03-024) shows that the sensitivity to the internal-force assumptions differs between circular, planar, composite and block-shaped surfaces.

It is worth being clear here about what a term "missing" from the factor-of-safety equation means. About the center of a circle, $M_O(N_i)=0$, so the moment terms of the base normal forces drop out of the equilibrium equation. As a result, they may not appear as separate moment terms in the final factor-of-safety equation either. This does not mean that the base normal forces do not physically exist, or that they do not affect the factor of safety. Through the {term}`shear strength` $c_i'A_i+(N_i-U_i)\tan\phi_i'$, $N_i$ governs how large the resistance is. What is zero is only their contribution to the moment about the center, and that comes from geometry specific to circles: their lines of action pass through a common center.

So care is needed when a final factor-of-safety equation from a paper or a textbook is used for a slip surface of a different shape. It has to be checked whether a term left out of the equation is unnecessary under general mechanical assumptions, or whether it dropped out during the derivation because of a property specific to circles. If only the local angles and coordinates of an ellipse, a composite surface or a surface of any shape are substituted into an equation of the latter kind, it may lose the moments of the base normal forces, the moment arms that differ from base to base, and the link to a motion about one center of rotation. To extend it to general shapes, the original equation cannot simply be reused. The formulation has to be rebuilt from force and moment equilibrium, including the lost terms.

---

(practice-section-3)=

### 3. What changes when it is extended to ellipses, composite surfaces and any shape

On surfaces other than circles, Eqs. {eq}`eq-practice-base-force` to {eq}`eq-practice-moment-balance` can still be computed. However, the special properties of the circle are in general lost.

#### 3.1 The base normal forces do not pass through a common point

The normals of an ellipse, or the local normals of a general curve, usually do not meet at one center. So for an arbitrarily chosen center of moments $O$,

$$
M_O(N_i)\neq 0
$$ (eq-practice-general-normal-moment)

Some implementations take the center of a circle that approximates the slip surface as the center of moments. However, as long as the surface is computed as non-circular, the normals of the bases do not meet at that center either. So an implementation that uses moment equilibrium on a general shape has to find the arm of each normal force and include its moment in the equation, whatever point it chooses as the center.

(practice-section-3-2)=

#### 3.2 The moment arms of the shear forces are not constant

The moment of the shear force on each base has to be computed base by base, as in

$$
M_O(T_i)
=
\boldsymbol{e}_y\cdot
\left(
\boldsymbol{r}_i\times\left(-T_i\boldsymbol{m}_i\right)
\right)
$$ (eq-practice-general-shear-moment)

The simplification with the common radius $R$ of a circle is not available.

#### 3.3 It cannot be read as a rotation about one center

The tangent directions of an ellipse do not match the directions of velocity of a rigid body rotating about one fixed point. On composite and polyline surfaces, the local direction changes even more abruptly.

LEM can still assign shear resistance to each base and compute a factor of safety, because it does not solve displacement compatibility. However, a factor of safety does not mean that the soil mass can actually move along that surface as one rigid body.

#### 3.4 The sensitivity to the interslice shear forces changes

On circular surfaces, the simplified Bishop method and {term}`complete equilibrium methods <complete equilibrium method>` often give close factors of safety. On planar, composite and block-shaped surfaces, on the other hand, force equilibrium and moment equilibrium differ in their sensitivity to the interslice shear forces.

As a result, on a general surface, which of

$$
F_s^{\mathrm{Bishop}}
\lessgtr
F_s^{\mathrm{Spencer/MP}}
$$ (eq-practice-method-difference)

holds cannot be decided once and for all. In other words, a {term}`simplified method` is neither always on the safe side nor always on the unsafe side.

---

(practice-section-4)=

### 4. What "it can compute any shape" means exactly

```{note}
In this chapter, "any shape" does not mean that every mathematical curve or surface is allowed without conditions. "It can be applied to any shape" means that the internal-force assumptions and the equilibrium equations can be rebuilt in a generalized LEM framework. Substituting only the coordinates of the shape into a classical formula for circles does not guarantee that the properties of the original method still hold.
```

To be treated as a general slip surface in LEM, a surface must satisfy at least the following conditions.

- It can be divided stably into slices or {term}`columns <column>`
- The area, the normal and the tangent of each base can be set
- It contains no self-intersecting parts and no elements of zero area
- The side assumed to move and the side that resists can be told apart
- The solver in use can represent the shape
- A strength criterion and {term}`pore water pressure` can be assigned to each base
- The numerical solution converges under the assumed internal forces

Stated precisely, then, the claim is as follows.

> **Even an LEM derived for circular slips can compute the factor of safety for a slip surface of any shape, once its internal-force assumptions and equilibrium conditions are generalized. However, the surface must allow {term}`discretization <spatial discretization>`, and must be a candidate along which the soil mass can move.**

When interpreting the results, check whether the geometric simplifications and the accuracy assessments that held for the original method still hold.

---

## Check the actual formulation rather than the method name

### 5. Common methods applied to general shapes

| Method | Shape it originally suits | Calculation on general shapes | Main assumption that remains | Main things lost or to check |
|---|---|---|---|---|
| Fellenius method (ordinary method of slices) | Circle | A reference value can be computed with generalized equations | Ignores the interslice forces | The center of the circle as center of moments, force equilibrium, assurance of accuracy |
| Simplified Bishop method | Circle | The Bishop-type assumption can be applied to general shapes | Simplifies the interslice shear forces, and uses vertical force equilibrium and moment equilibrium | The common center, the zero moment of the normal forces, horizontal force equilibrium |
| Simplified Janbu method | Any shape | Easy to apply from the start | Simplifies the interslice shear forces, and uses force equilibrium | Moment equilibrium, whether the correction factor applies |
| Spencer method | Can be extended to general shapes | Can be applied | The resultant interslice force has a constant inclination | The assumed direction of the internal forces, displacement compatibility |
| Morgenstern–Price method, GLE (general limit equilibrium) | Any shape | Can be applied | Ratio of internal forces $X/E=\lambda f(x)$ | The choice of the internal-force function, displacement compatibility |

(practice-section-5-1)=

#### 5.1 Two meanings of "computed a non-circular surface with Bishop"

This phrase can be read in at least two ways.

1. The local angles of a non-circular surface were substituted into the classical Bishop equation for circles
2. Bishop's internal-force assumption was kept and extended to force and moment equations for general shapes

The two are not the same. The second can be a mechanically consistent generalization. For the first, on the other hand, whether it is valid cannot be judged without checking which terms were left out.

The same holds for names such as Fellenius-type, Spencer-type and 3D Bishop-type. A name displayed by software may refer not to the original method proposed in the paper but to **an implementation that inherits the internal-force assumption characteristic of that method**.

(practice-section-5-2)=

#### 5.2 A factor of safety alone is not a verification

Even when the iteration converges and $F_s$ is output, check at least the following separately.

- The force residuals and the moment residuals
- The effective normal force on each base, $N_i-U_i$
- The magnitude and direction of the interslice forces
- Whether the line of thrust falls outside the slices
- Whether negative normal forces appear in a material that cannot carry tension
- Whether the factor of safety stays the same when the number of divisions is increased
- Whether the factor of safety differs greatly from that of methods with other internal-force assumptions

---

(practice-section-6)=

### 6. Why the choice of the center of moments or the axis of rotation matters

When the point about which moments are taken moves from $O$ to $O'$, the moment changes as follows.

$$
\boldsymbol{M}_{O'}
=
\boldsymbol{M}_O
-\boldsymbol{a}\times\sum\boldsymbol{F},
\qquad
\boldsymbol{a}=\overrightarrow{OO'}
$$ (eq-practice-moment-transfer)

So for a rigid system that satisfies force equilibrium for the whole mass ($\sum\boldsymbol{F}=\boldsymbol{0}$), moving the point does not change the result.

On the other hand, in methods that do not satisfy all of force equilibrium, such as the simplified Bishop method and the Fellenius method,

$$
\sum\boldsymbol{F}\neq\boldsymbol{0}
$$ (eq-practice-unbalanced-force)

may hold. In that case, changing the center of moments also changes the moment residual, unless $\boldsymbol{a}$ is parallel to $\sum\boldsymbol{F}$.

On a circle, the center of the circle serves as the reference point. A general shape has no such fixed point, so the following must be checked.

- How the center of moments was chosen
- Whether the center of a circle approximating the slip surface is used
- Whether the moments of the normal forces are included
- In 3D, about which axes moment equilibrium is satisfied
- Whether the factor of safety changes greatly when the reference point or axis is changed

These points matter especially when the simplified Bishop method or the Fellenius method is applied to a surface of general shape.

---

## What the assumed direction of sliding decides

### 7. In 2D the direction is set implicitly; in 3D it is an unknown

```{figure} ./figures/fig_s03_sliding_direction.svg
:name: fig-s03-sliding-direction
:alt: The long axis of a slip surface and the direction of sliding in plan view, and the projection onto the tangent plane of a column base

Left: the long axis of the slip surface and the direction of sliding $\boldsymbol{d}$ do not necessarily coincide. Right: the direction of $\boldsymbol{p}_i$, the projection of $\boldsymbol{d}$ onto the tangent plane of the base, is the local direction of sliding $\boldsymbol{m}_i$. $\boldsymbol{T}_i$ acts in the opposite direction
```

In a 2D analysis, motion is confined to the section being analyzed. Of the two directions along the tangent to the slip surface, the base shear force takes the one that opposes the assumed sliding, almost automatically.

In 3D, the tangent plane of a base contains infinitely many directions. The strength equation

$$
\|\boldsymbol{T}_i\|
=
\frac{
c_i'A_i+(N_i-U_i)\tan\phi_i'
}{F_s}
$$ (eq-practice-shear-magnitude)

sets only the magnitude of the shear force, not its direction.

So each column needs a unit direction vector $\boldsymbol{m}_i$ to form

$$
\boldsymbol{T}_i
=
-\|\boldsymbol{T}_i\|\boldsymbol{m}_i
$$ (eq-practice-shear-vector)

---

(practice-section-8)=

### 8. Three meanings of "direction of sliding"

This chapter calls the representative direction of the whole soil mass the **direction of sliding** (the overall direction), and the direction at the base of each column the **local direction of sliding**.

(practice-section-8-1)=

#### 8.1 The representative direction of sliding of the whole mass

This is the representative direction in which the whole sliding mass moves. It is expressed, for example, by an azimuth $\theta$ in the horizontal plane.

$$
\boldsymbol{d}
=
\begin{bmatrix}
\cos\theta & \sin\theta & 0
\end{bmatrix}^{\mathsf{T}}
$$ (eq-practice-global-direction)

On a symmetric slope, the plane of symmetry gives a candidate. On asymmetric slopes, under lateral loads, or with complex strata, however, it is not obvious.

(practice-section-8-2)=

#### 8.2 The local direction of shear at the base of each column

In a formulation that projects the overall direction $\boldsymbol{d}$ onto the tangent plane perpendicular to the base normal $\boldsymbol{n}_i$, the local direction is obtained as

$$
\boldsymbol{p}_i
=
\left(
\boldsymbol{I}
-\boldsymbol{n}_i\boldsymbol{n}_i^{\mathsf{T}}
\right)
\boldsymbol{d}
$$ (eq-practice-projection)

$$
\boldsymbol{m}_i
=
\frac{\boldsymbol{p}_i}{\|\boldsymbol{p}_i\|}
$$ (eq-practice-local-direction)

So even with a single direction of sliding, the local direction of shear on a curved surface differs from column to column.

#### 8.3 Directions and principal axes used when searching for slip surfaces

These include the direction of the long axis of an ellipsoid or a NURBS surface, the orientation of the search range, and the axis of rotation. They are related to the direction of sliding, but do not necessarily coincide with it.

For example, the direction of the long axis describes the shape of the sliding mass in plan. The direction of sliding, on the other hand, is the azimuth in which the mass moves, determined by force equilibrium. Fixing the two as the same thing may narrow the search range more than necessary.

---

(practice-section-9)=

### 9. What setting the direction of sliding decides in the calculation

The direction of sliding is not a marker added to a figure but a variable that enters the calculation. It determines at least the following.

1. The $x,y,z$ components of the base shear forces
2. The {term}`resisting forces <resisting force>` and {term}`driving forces <driving force>` along each horizontal axis
3. The moments of the base shear forces about each axis
4. The base normal forces found from force equilibrium
5. The magnitude and direction of the intercolumn forces required
6. The factor of safety for each direction, or a common factor of safety
7. How the iteration converges

Written schematically, the relation is as follows.

$$
\text{direction of sliding}
\longrightarrow
\boldsymbol{m}_i
\longrightarrow
\boldsymbol{T}_i
\longrightarrow
\begin{cases}
\sum\boldsymbol{F}\\
\sum\boldsymbol{M}
\end{cases}
\longrightarrow
N_i,\ \text{intercolumn forces},\ F_s
$$ (eq-practice-direction-chain)

So if the direction of sliding is not appropriate, resistance is distributed in the wrong directions, and the factor of safety may be misjudged either too high or too low.

3D methods set the direction of sliding in ways such as the following.

- Take it from the plane of symmetry
- Let the user specify it
- Try several azimuths and find the one that gives the minimum factor of safety
- Solve for it as an unknown of force and moment equilibrium

[Cheng and Yip (2007)](https://doi.org/10.1061/%28ASCE%291090-0241%282007%29133%3A12%281544%29) treated the direction of sliding explicitly for asymmetric 3D slopes. [Kalatehjari et al. (2014)](https://doi.org/10.1016/j.enggeo.2014.06.002) examine a way to determine a unique direction of sliding.

---

### 10. Ways to set the direction of sliding, and what each loses

#### Using one direction for all columns

The calculation tends to be stable, and the soil mass is easy to treat as one body. On the other hand, it is hard to follow strata whose dip varies from place to place, the orientation of weak layers, or complex bends.

#### Using a separate direction for each column

This fits each base more easily. However, neighboring columns may separate, overlap or move in different directions, and the displacement compatibility of the whole mass may break down.

#### Searching for the direction with the minimum factor of safety

This reduces the room for the user to choose a direction arbitrarily. However, the shape of the slip surface and the direction of sliding are optimized together, so the result depends on local minima, the search range, the angle increment and the convergence criteria.

#### Solving for the direction from equilibrium

This improves consistency with equilibrium. However, a separate assumption for {term}`closure` is still needed. Also, the direction obtained does not necessarily satisfy compatibility of the displacement field.

---

## How to check the results of an actual calculation

### 11. What to check when using general surfaces

#### 11.1 Formulation

- Does the method name refer to the classical original method, or to a generalized "type"?
- Which components of the interslice or intercolumn forces are ignored?
- In which directions is force equilibrium satisfied?
- About which points or axes is moment equilibrium satisfied?
- Is one factor of safety shared by all bases?

#### 11.2 Shape of the slip surface

- Is it a circle, an ellipse, a composite surface or a free-form surface?
- On a general surface, are the moments of the normal forces included?
- Is a circle or an axis of rotation that approximates the shape used?
- Does the range of the parameters describing the shape cover the expected failure mechanisms well enough?

#### 11.3 Direction of sliding in 3D

- Is it given by the user, set from the plane of symmetry, or found by the analysis?
- How is the overall direction linked to the local directions at the bases?
- Is the direction of sliding taken to be the same as the long axis of the slip surface?
- Can the direction change when a lateral external force is applied?

(practice-section-11-4)=

#### 11.4 Numerical solution

- Have the force and moment residuals converged, and not just the factor of safety?
- Are there negative effective normal forces or extreme internal forces?
- How were tension cracks and surfaces with zero resistance handled?
- Have cases that did not converge been replaced with another factor of safety?
- Has the search for the critical slip surface stopped at a local minimum?

(practice-section-11-5)=

#### 11.5 Sensitivity analysis

Vary at least the following and compare the results.

1. The number of slices or columns
2. Simplified methods and complete equilibrium methods
3. The internal-force function, or the direction of the internal forces
4. The center of moments, or the axis of rotation
5. The azimuth of the 3D direction of sliding
6. The type of slip surface shape
7. The handling of tensile forces and negative effective normal forces

On a general surface, the results are more reliable if the factor of safety of a simplified method is close to that of Spencer-type or Morgenstern–Price-type methods, and if it stays the same when the divisions, the axes and the direction are changed. Conversely, if the factor of safety changes greatly, check whether the failure mechanism and the formulation match before fine-tuning the soil parameters.

---

### 12. Cases that need care even when a number is obtained

(practice-section-12-1)=

#### 12.1 Negative effective normal force on a base

$$
N_i-U_i<0
$$ (eq-practice-negative-normal)

On a base where this holds, the result depends on whether the frictional resistance is kept as a negative value, the contact is released, or a tension crack is introduced. If the model assumes that soil cannot carry tension, the base needs a treatment consistent with the contact condition.

#### 12.2 Extremely small slices or columns

At sharp kinks or thin edge parts, the base angle, the normal force and the ratio of internal forces may become numerically unstable. Finer division does not always help. It may be necessary to smooth the shape or to set a minimum element width.

#### 12.3 Composite surfaces along which motion is physically difficult

Even when the factor-of-safety equation can be computed, the soil mass may not be able to move as one rigid body on a surface whose parts need different centers of rotation or directions of motion. An LEM calculation does not check this displacement compatibility directly.

(practice-section-12-4)=

#### 12.4 A converged local minimum

Even if $F_s$ converges for a given slip surface, it is not necessarily the minimum factor of safety for the whole slope. The surface with the minimum factor of safety among the family of slip surfaces searched is called the **critical slip surface**. Computing the factor of safety and searching for the critical slip surface are separate problems.

---

### 13. Guidelines for judgment in practice

| Situation | What to do first | What to check as well |
|---|---|---|
| A 2D slope that is nearly homogeneous, where circular failure is plausible | Compute with the simplified Bishop method and compare with the Spencer method or the Morgenstern–Price method | The search range for circles, pore water pressure, dependence on the number of divisions |
| A composite or non-circular surface along a weak layer | Use the Spencer method, the Morgenstern–Price method or the generalized Janbu method | The internal-force function, the difference from simplified methods, whether the mass can deform that way |
| Extending a method for circles to general shapes | Check the specification of the generalized equations | The center of moments, the moments of the normal forces, the equilibrium not satisfied |
| A symmetric 3D slope | Use the plane of symmetry as the initial value of the direction of sliding | Sensitivity to fixing the direction |
| An asymmetric 3D slope, or one with lateral loads | Use a 3D method that searches for or solves for the direction of sliding | The overall direction and the local directions, the force residuals in three directions |
| Factors of safety differ greatly between methods | Review the failure mechanism and the internal-force assumptions | Convergence, negative normal forces, sensitivity to the axes, the direction and the divisions |

---

## Summary

### 14. Conclusions of this chapter

#### 14.1 The factor of safety can be computed on general surfaces too

Even a method derived for circles can compute the factor of safety for ellipses, composite surfaces, polyline surfaces and others. To do so, discretize the slip surface, set the normal, the tangent and the moment arm of each base, and generalize the internal-force assumptions and the equilibrium conditions.

#### 14.2 However, the special properties of the circle are lost

- The base normal forces do not pass through a common center
- The moment arms of the shear forces are not constant
- The motion cannot be read as a rotation about one fixed center
- In methods that do not satisfy all of force equilibrium, the result may change with the choice of the center of moments or the axis of rotation
- The result may become more sensitive to the assumption on the interslice shear forces

#### 14.3 A method name alone does not reveal the formulation

Even when "Bishop," "Spencer" or "3D Bishop" is displayed, it has to be checked whether it is the classical original method or a generalized implementation that inherits only its internal-force assumption.

#### 14.4 The direction of sliding decides how forces are distributed

The 3D direction of sliding is not a marker added to a figure. It is a variable of the formulation that determines the components of the base shear forces, the base normal forces, the intercolumn forces, the moments and the factor of safety.

#### 14.5 What to check at the end

$$
\boxed{
\begin{aligned}
&\text{Could the factor of safety be computed?}\\
&\quad\downarrow\\
&\text{Under which assumptions was it computed?}\\
&\quad\downarrow\\
&\text{Which equilibrium and which mechanical meaning are kept?}
\end{aligned}
}
$$ (eq-practice-summary)

When LEM is used in practice, the fine value of the factor of safety matters less than **being able to explain whether the shape of the slip surface, the internal-force assumptions, the moment axes, the direction of sliding and the numerical treatment match the expected failure mechanism**.

---

## Review questions

Click a question to see its answer.

:::{dropdown} Q1. Why can a method derived for circles compute the factor of safety of an elliptical slip surface or one of any shape?
:icon: question

Once the normal, the tangent and the moment arm of each base can be computed, the forces and moments can be summed whatever the shape of the surface. The mechanical character of a method is not determined by the input shape of a circle alone, but by the internal-force assumptions and the equilibrium conditions used. (→[Section 1](#practice-section-1))
:::

:::{dropdown} Q2. Why do the base normal forces not appear directly in the moment equation about the center of a circle? Does this mean that they do not affect the factor of safety?
:icon: question

Because the lines of action of the base normal forces pass through the center $O$ of the circle, so their moments about $O$ are zero. This does not mean they do not affect the factor of safety. Through the shear strength $c_i'A_i+(N_i-U_i)\tan\phi_i'$, $N_i$ governs how large the resistance is. (→[Section 2](#practice-section-2))
:::

:::{dropdown} Q3. Why can the phrase "computed a non-circular surface with Bishop" be read in two ways? Which reading needs care?
:icon: question

Because it may mean that the angles of a non-circular surface were simply substituted into the classical equation for circles, or that Bishop's internal-force assumption was kept and extended to equations for general shapes. The first needs care. It may drop terms that vanished because of properties specific to circles, such as the moments of the base normal forces. (→[Section 2](#practice-section-2), [Section 5.1](#practice-section-5-1))
:::

:::{dropdown} Q4. In a method that does not satisfy all of force equilibrium, why can changing the center of moments change the result?
:icon: question

In such methods, $\sum\boldsymbol{F}\neq\boldsymbol{0}$ may hold. Then moving the center by $\boldsymbol{a}$ changes the moment residual by $-\boldsymbol{a}\times\sum\boldsymbol{F}$. If $\boldsymbol{a}$ is parallel to $\sum\boldsymbol{F}$, however, this change is zero. (→[Section 6](#practice-section-6))
:::

:::{dropdown} Q5. In 3D, what does setting the direction of sliding decide in the calculation? Name three things.
:icon: question

For example, the $x,y,z$ components of the base shear forces, the moments of the base shear forces about each axis, and the base normal forces found from force equilibrium. It also decides the resisting and driving forces along each horizontal axis, the magnitude and direction of the intercolumn forces, the factor of safety, and how the iteration converges. (→[Section 9](#practice-section-9))
:::

:::{dropdown} Q6. When the iteration converges and gives $F_s$, what should be checked besides the factor of safety?
:icon: question

- The force and moment residuals
- Whether the effective normal force on each base, $N_i-U_i$, is negative
- The magnitude and direction of the interslice forces, and whether the line of thrust falls outside the slices
- Whether the factor of safety stays the same when the number of divisions is increased
- Whether the factor of safety differs greatly from that of methods with other internal-force assumptions

(→[Section 5.2](#practice-section-5-2))
:::

:::{dropdown} Q7. $F_s$ has converged for a given slip surface. Can it be taken as the factor of safety of the slope?
:icon: question

Not as it is. The converged $F_s$ is the value for the given slip surface, and is not necessarily the minimum factor of safety for the whole slope. The critical slip surface is searched for separately from computing the factor of safety. (→[Section 12.4](#practice-section-12-4))
:::

:::{dropdown} Q8. (Calculate) For a circular slip with radius $R=20$ m, the base shear forces of the slices sum to $\sum_i T_i=300$ kN/m. What is the moment of the base shear forces about the center of the circle?
:icon: question

The arm of the shear force on every base is the radius $R$. So $M_O=R\sum_i T_i=20\times 300=6000$ kN·m/m. On a surface other than a circle, the arms differ from base to base, so they cannot be gathered under one $R$ like this. (→[Section 2.2](#practice-section-2-2), [Section 3.2](#practice-section-3-2))
:::

---

## What to read next

This chapter looked at what slip surfaces other than circles, the direction of sliding and discretization decide in computing the factor of safety. The ideas so far can be checked with numbers by writing code. Start with [Practice 1, "Computing the factor of safety of an infinite slope"](practice-infinite-slope.md); Practice 2 then implements four 2D methods, and Practice 3 two 3D methods. Practice 2 shows how much the center of moments from this chapter changes the factor of safety, and Practice 3 does the same for the local direction of sliding.

## References

### General and non-circular slip surfaces

1. Bishop, A. W. (1955). “The use of the slip circle in the stability analysis of slopes.” *Géotechnique*, 5(1), 7–17. [https://doi.org/10.1680/geot.1955.5.1.7](https://doi.org/10.1680/geot.1955.5.1.7)
2. Fredlund, D. G., and Krahn, J. (1977). “Comparison of slope stability methods of analysis.” *Canadian Geotechnical Journal*, 14(3), 429–439. [https://doi.org/10.1139/t77-045](https://doi.org/10.1139/t77-045)
3. Morgenstern, N. R., and Price, V. E. (1965). “The analysis of the stability of general slip surfaces.” *Géotechnique*, 15(1), 79–93. [https://doi.org/10.1680/geot.1965.15.1.79](https://doi.org/10.1680/geot.1965.15.1.79)
4. Spencer, E. (1967). “A method of analysis of the stability of embankments assuming parallel inter-slice forces.” *Géotechnique*, 17(1), 11–26. [https://doi.org/10.1680/geot.1967.17.1.11](https://doi.org/10.1680/geot.1967.17.1.11)
5. Zhu, D. Y., Lee, C. F., and Jiang, H. D. (2003). “Generalised framework of limit equilibrium methods for slope stability analysis.” *Géotechnique*, 53(4), 377–395. [https://doi.org/10.1680/geot.2003.53.4.377](https://doi.org/10.1680/geot.2003.53.4.377)
6. Krahn, J. (2003). “The 2001 R. M. Hardy Lecture: The limits of limit equilibrium analyses.” *Canadian Geotechnical Journal*, 40(3), 643–660. [https://doi.org/10.1139/t03-024](https://doi.org/10.1139/t03-024)
7. Duncan, J. M., and Wright, S. G. (1980). “The accuracy of equilibrium methods of slope stability analysis.” *Engineering Geology*, 16(1–2), 5–17. [https://doi.org/10.1016/0013-7952(80)90003-4](https://doi.org/10.1016/0013-7952%2880%2990003-4)

### Direction of sliding in 3D

8. Cheng, Y. M., and Yip, C. J. (2007). “Three-Dimensional Asymmetrical Slope Stability Analysis—Extension of Bishop's, Janbu's, and Morgenstern–Price's Techniques.” *Journal of Geotechnical and Geoenvironmental Engineering*, 133(12), 1544–1555. [https://doi.org/10.1061/(ASCE)1090-0241(2007)133:12(1544)](https://doi.org/10.1061/%28ASCE%291090-0241%282007%29133%3A12%281544%29)
9. Kalatehjari, R., Rashid, A. S. A., Hajihassani, M., Kholghifard, M., and Ali, N. (2014). “Determining the unique direction of sliding in three-dimensional slope stability analysis.” *Engineering Geology*, 182, 97–108. [https://doi.org/10.1016/j.enggeo.2014.06.002](https://doi.org/10.1016/j.enggeo.2014.06.002)
