---
title: "What is the limit equilibrium method? What assumptions does each method use to determine the remaining unknowns?"
lang: en
series: "2 of 3"
translated_from: "4396db4"
translated_on: 2026-10-05
---

# What is the limit equilibrium method?

**What assumptions does each method use to determine the remaining unknowns?**

Chapter 1 derived the equation for the forces on a slice base. That equation alone, however, determines neither the magnitude of the base forces nor the factor of safety. This chapter compares 2D and 3D limit equilibrium methods (LEM) by asking which assumption each method uses to supply the missing conditions. The aim is not to memorize each method's formula. Instead, the chapter sets each method against the full statics problem, with all its forces, and sorts out what the method satisfies, what it simplifies and what it leaves unsolved.

This chapter assumes that you have read [Chapter 1](continuum-mechanics-to-lem-start.md). The terms and symbols are collected in the [Glossary](lem-glossary.md).

```{admonition} Key points of this chapter
Limit equilibrium methods do not differ only in the form of their formulas. Once a continuum is divided into slices or columns, the equilibrium equations alone cannot determine the internal forces. This state is called **static indeterminacy**. The methods differ in **which assumption about the internal forces, and which equilibrium conditions, they use to resolve this indeterminacy**.
```

---

(what-section-0)=

## 0. Scope and terms of this chapter

This chapter uses the word "rigorous" in two separate senses.

1. **Rigor as continuum mechanics**: solving a boundary value problem for the stress and displacement fields that satisfies the constitutive law, compatibility and the boundary conditions all at once
2. **Static rigor within LEM**: satisfying all the required force and moment equilibrium conditions under the assumed {term}`slip surface`, the assumed way strength is mobilized, and the assumed model of interslice or intercolumn forces

The Spencer and Morgenstern–Price methods are sometimes called "rigorous methods." Here "rigorous" mostly has the second sense. These methods are not continuum analyses either: they do not solve for displacement compatibility or for the stress–strain relation of the soil.

From here on, unless stated otherwise, strength follows the {term}`Mohr–Coulomb failure criterion` in terms of effective stress. The symbols are as follows.

| Symbol | Meaning |
|---|---|
| $F_s$ | Factor of safety |
| $c_i',\phi_i'$ | Effective cohesion and effective angle of internal friction on the base of element $i$ |
| $A_i$ | Base area of element $i$. In 2D, the base area for a unit depth |
| $N_i$ | Total normal force on the base |
| $U_i$ | Resultant of the pore water pressure on the base |
| $T_i$ | Magnitude of the shear force mobilized along the base |
| $W_i$ | Weight. External loads and seismic inertia forces are added separately when needed |
| $E,X$ | 2D interslice normal and shear forces. $E$ is the component normal to the boundary, $X$ the component along it |
| $\boldsymbol{n}_i$ | Unit normal vector of the base of element $i$, pointing out of the sliding mass |
| $\boldsymbol{m}_i$ | Unit vector of the local direction of sliding assumed on the base of element $i$ |

---

## The starting point of 2D LEM

(what-section-1)=

### 1. What is known, and what is not yet known

Chapter 1 arrived at the following equation.

$$
T_i
=
\frac{
c_i' A_i + (N_i-U_i)\tan\phi_i'
}{F_s}
$$ (eq-what-base-shear)

This equation assumes that the whole slip surface is in a limit state, with the {term}`shear strength` reduced to

$$
c_{m,i}'=\frac{c_i'}{F_s},
\qquad
\tan\phi_{m,i}'=\frac{\tan\phi_i'}{F_s}
$$ (eq-what-mobilized-parameters)

By Eq. {eq}`eq-what-base-shear`, $T_i$ is not an independent unknown: it follows once $N_i$ and $F_s$ are known. That alone, however, does not solve the problem.

#### Known quantities

- The shape of the slope, the boundaries between soil layers, and the assumed slip surface
- The weight $W_i$ of each slice
- $c_i',\phi_i'$ and the base area $A_i$
- $U_i$, found from the distribution of {term}`pore water pressure`
- Applied external loads, seismic inertia forces, anchor forces and so on

#### Quantities not yet known

- The {term}`base normal force` $N_i$ of each slice
- The {term}`factor of safety` $F_s$, common to the whole slip surface
- The magnitude and direction of the interslice forces
- If moment equilibrium of each slice is considered, the point where the resultant interslice force acts

Of these, forces that neighboring slices exert on each other across their boundary, such as the interslice forces, are called **internal forces**.

So the real starting point of LEM is not Eq. {eq}`eq-what-base-shear` itself, but the following question.

> **What assumptions turn a statics problem with unknown internal forces into one with a unique solution?**

---

(what-section-2)=

### 2. The forces a 2D slice really carries

```{figure} ./figures/fig_01_2d_slice_forces.svg
:name: fig-01-2d-slice-forces
:alt: Free-body diagram of a slice with vertical sides, showing its weight, the normal and shear forces on the base, and the interslice forces on the left and right

Free-body diagram of a 2D slice. It shows $N_i$ and $T_i$ on the base, $E$ and $X$ on the left and right boundaries, the weight $W_i$, the base inclination $\alpha_i$, and the height $h$ at which the interslice force acts. The arrow lengths are drawn to satisfy force equilibrium
```

When slice $i$ is cut out of the soil mass, at least the following forces must be considered.

- The weight $W_i$
- The base normal force $N_i$
- The {term}`base shear force` $T_i$
- The interslice normal force $E_{i-1}$ and shear force $X_{i-1}$ on the left boundary
- The interslice normal force $E_i$ and shear force $X_i$ on the right boundary
- As needed, water pressure, external loads, seismic inertia forces and reinforcement forces

Each slice, taken out as a rigid body, has three independent equilibrium equations in the plane.

$$
\sum F_x=0,
\qquad
\sum F_z=0,
\qquad
\sum M_y=0
$$ (eq-what-2d-equilibrium)

From the viewpoint of continuum mechanics, however, the boundary between slices (an internal boundary) does not carry a single arrow. It carries a distribution of {term}`traction` that varies with position:

$$
\boldsymbol{t}(\boldsymbol{x})
=
\boldsymbol{\sigma}(\boldsymbol{x})\boldsymbol{n}
$$ (eq-what-cauchy)

LEM lumps this distribution into the resultants $E$ and $X$ and, if needed, the point where they act. At this stage, a **discretization** has already taken place: the continuous stress field has been replaced by a finite number of resultants.

---

### 3. Why the equilibrium equations alone cannot solve the problem

```{figure} ./figures/fig_02_indeterminacy.svg
:name: fig-02-indeterminacy
:alt: Five slices, showing where the normal force on each base, the interslice forces and their points of action on each boundary, and the single factor of safety for the whole mass act

The unknowns left for $n=5$ slices. Each base has $N$, each boundary between slices has $E$, $X$ and $h$, and there is one $F_s$ for the whole mass: 18 in all
```

(what-section-3-1)=

#### 3.1 Counting the unknowns

For $n$ slices, even after Eq. {eq}`eq-what-base-shear` expresses the base shear force $T_i$ in terms of $N_i$ and $F_s$, a typical formulation still has the following unknowns.

| Unknown | Count |
|---|---:|
| Base normal force $N_i$ | $n$ |
| Interslice normal force $E_i$ | $n-1$ |
| Interslice shear force $X_i$ | $n-1$ |
| Point of action of the resultant interslice force $h_i$ | $n-1$ |
| Factor of safety $F_s$ | $1$ |
| **Total** | **$4n-2$** |

Applying Eq. {eq}`eq-what-2d-equilibrium` to each slice, on the other hand, gives $3n$ equations. The count of unknowns changes with how the resultants and their positions are represented, and with whether global equilibrium is counted separately. Every count, however, leads to the same conclusion.

$$
\boxed{
\text{Equilibrium and the base strength equation alone do not determine the distribution of internal forces uniquely}
}
$$ (eq-what-indeterminacy)

This is the static indeterminacy mentioned at the start of this chapter.

```{note}
This table does not count the point where the base normal force $N_i$ acts as an unknown. That amounts to adopting, in advance, the customary assumption that $N_i$ acts at the middle of the base. Textbook counts that include these points of action, together with the Mohr–Coulomb equations, give $6n-2$ unknowns and $4n$ equations. If $n$ of the $2n-2$ missing conditions are supplied by assuming that $N_i$ acts at the middle of the base, $n-2$ remain, which agrees with the count in this table.
```

#### 3.2 What a continuum analysis adds

A continuum boundary value problem solves, besides equilibrium, at least the following conditions together.

- The strain–displacement relation
- The constitutive law (the stress–strain relation)
- Displacement compatibility
- Stress and displacement boundary conditions
- The elastoplastic history and the yield condition at each point

LEM usually does not solve these. Instead, it assumes the direction, ratio or point of action of the interslice forces, or which of their components can be ignored.

(what-section-3-3)=

#### 3.3 What does it mean to "close" the indeterminacy?

This chapter calls the step that makes an indeterminate problem solvable **closure**. Closure commonly takes one of three forms.

1. Ignore part of the internal forces
2. Assume the direction of the internal forces, or the ratio of their components
3. Use only part of the equilibrium conditions, and leave the rest unsatisfied

Each method can be classified by its combination of these three. [Fredlund and Krahn (1977)](https://doi.org/10.1139/t77-045) compares the 2D methods within a single framework.

---

## What 2D LEM simplifies

(what-section-4)=

### 4. How to compare the 2D methods

```{figure} ./figures/fig_03_2d_methods.svg
:name: fig-03-2d-methods
:alt: The same slice drawn for the Fellenius method, the simplified Bishop method and the simplified Janbu method, comparing the internal forces each ignores and the equilibrium each uses

Comparison of the Fellenius, simplified Bishop and simplified Janbu methods. The same slice shows the internal forces each ignores (pale dashes) and the equilibrium each uses
```

The rest of this part compares the methods from four viewpoints.

1. How the method treats the interslice forces
2. Which equilibrium conditions it satisfies
3. What constraints it puts on the shape of the slip surface
4. As a result, what becomes easy to compute, and what is no longer guaranteed

The three methods in Sections 4.1 to 4.3 all ignore some or all of the internal forces and satisfy only part of the equilibrium conditions. This primer groups them as **simplified methods** (methods that satisfy only part of equilibrium), and sets them apart from the complete equilibrium methods of Section 5.

#### 4.1 Fellenius method (ordinary method of slices)

The Fellenius method (ordinary method of slices) ignores the effect of the normal and shear forces from neighboring slices when it finds the base normal force. It then finds the factor of safety from global moment equilibrium for a circular slip surface. In English it is also called the Ordinary Method of Slices or the Swedish Circle Method. Japanese standards and practice documents often call it simply *kanben-hō* (簡便法, "simplified method"), using the word for this one method only.

For a unit depth and a circular slip surface, with the horizontal slice width $b_i$, the base length $l_i$ and the base inclination $\alpha_i$, a typical form of the equation is the following.

$$
F_s
=
\frac{
\displaystyle\sum_i
\left[
c_i'l_i+\left(W_i\cos\alpha_i-U_i\right)\tan\phi_i'
\right]
}{
\displaystyle\sum_i W_i\sin\alpha_i
}
$$ (eq-what-fellenius)

```{note}
How the water pressure term is written depends on the choice of symbols.
```

##### How it closes the indeterminacy

- Ignores the effect of the interslice forces
- Uses global moment equilibrium about the center of the circle
- Does not satisfy horizontal and vertical force equilibrium of each slice at the same time

##### Mechanical meaning

It is an approximation that leaves the effect of the resultant interslice forces out of the factor of safety. For this reason, it is not suited to finding the base normal force or the internal forces of each slice.

```{note}
This approximation does not treat the interslice forces as physically absent. The interslice forces exist; their effect is simply left out of the factor-of-safety calculation.
```

**Original sources**: Fellenius's method goes back to works from the 1920s. One source whose bibliographic details could be checked is W. Fellenius, *Erdstatische Berechnungen mit Reibung und Kohäsion (Adhäsion) und unter Annahme kreiszylindrischer Gleitflächen*, Ernst & Sohn, Berlin, 1927 ([Bibliographic record](https://books.google.com/books?id=yHhHAAAAIAAJ)). Another is “Calculation of the Stability of Earth Dams,” *Proceedings of the Second Congress on Large Dams*, Vol. 4, pp. 445–462, 1936 ([Bibliographic record](https://cir.nii.ac.jp/crid/1573950399306830336)). Neither has a modern DOI that could be verified.

---

#### 4.2 Simplified Bishop method

The simplified Bishop method keeps the interslice normal force $E_i$ and simplifies the resultant interslice shear force. It usually sets $X_i-X_{i-1}=0$, and implementations set $X_i=0$ on each boundary. It then combines vertical force equilibrium of each slice with global moment equilibrium about the center of the circle.

A typical form is the following.

$$
F_s
=
\frac{
\displaystyle\sum_i
\frac{
c_i'b_i+(W_i-u_i b_i)\tan\phi_i'
}{
\cos\alpha_i+\dfrac{\sin\alpha_i\tan\phi_i'}{F_s}
}
}{
\displaystyle\sum_i W_i\sin\alpha_i
}
$$ (eq-what-bishop)

$F_s$ also appears on the right-hand side, so it is found by iteration.

##### How it closes the indeterminacy

- Keeps the interslice normal force
- Simplifies the interslice shear force
- Finds $N_i$ from vertical force equilibrium of each slice
- Finds $F_s$ from global moment equilibrium
- In general does not strictly satisfy global horizontal force equilibrium

##### Mechanical meaning

It finds the base normal force better than the Fellenius method does, but it does not solve for the direction of the internal forces. The classical formulation is for circular slip surfaces. This is because, for a circle, the moment equation about the common center is especially simple.

**Original paper**: [A. W. Bishop (1955), “The use of the slip circle in the stability analysis of slopes,” *Géotechnique*, 5(1), 7–17. DOI: 10.1680/geot.1955.5.1.7](https://doi.org/10.1680/geot.1955.5.1.7)

---

#### 4.3 Simplified Janbu method

The Janbu family of methods developed toward handling {term}`slip surfaces of arbitrary shape <general slip surface>` easily and finding the factor of safety mainly from force equilibrium. The simplified Janbu method simplifies the interslice shear force and finds the factor of safety mainly from global horizontal force equilibrium.

##### How it closes the indeterminacy

- Usually ignores or simplifies the interslice shear force
- Uses force equilibrium
- Does not fully satisfy global moment equilibrium
- Has a simple form that uses an empirical correction factor $f_0$ to make up for the unbalanced moment

##### Compared with the simplified Bishop method

$$
\begin{array}{c|c}
\text{Simplified Bishop method} & \text{Simplified Janbu method} \\
\hline
\text{Suits circular slip surfaces} & \text{Handles slip surfaces of arbitrary shape easily} \\
\text{Emphasizes global moment equilibrium} & \text{Emphasizes global force equilibrium} \\
\text{Does not satisfy horizontal force equilibrium} & \text{Does not satisfy moment equilibrium}
\end{array}
$$ (eq-what-bishop-janbu)

```{note}
Applying the correction factor does not make the unsatisfied moment equilibrium strictly satisfied. The correction factor reduces the bias of the factor of safety under particular assumptions and an empirical fit.
```

**Early sources**: N. Janbu (1954), “Application of composite slip surfaces for stability analysis,” *Proceedings of the European Conference on Stability of Earth Slopes*, Stockholm, Vol. 3, pp. 43–49 ([Bibliographic record](https://cir.nii.ac.jp/crid/1570009750148611712)). It has no DOI that could be verified. A widely cited work that generalizes and organizes the method is N. Janbu (1973), “Slope Stability Computations,” in *Embankment-Dam Engineering: Casagrande Volume*, pp. 47–86.

---

### 5. Methods that assume the direction of the internal forces and satisfy both force and moment equilibrium

```{figure} ./figures/fig_04_spencer_mp.svg
:name: fig-04-spencer-mp
:alt: Comparison of the inclination of the resultant on the slice boundaries, and of the function f(x), for the Spencer method and the Morgenstern–Price method

In the Spencer method, the resultant has the same inclination on every boundary. In the Morgenstern–Price method, the inclination varies as $\lambda f(x)$. The graph below shows each $f(x)$ on the same horizontal axis
```

(what-section-5-1)=

#### 5.1 Spencer method

The Spencer method assumes that the resultant forces on the slice boundaries are parallel to each other, that is, that they have a constant angle $\theta$.

$$
\frac{X_i}{E_i}=\tan\theta
=\text{constant}
$$ (eq-what-spencer)

With $F_s$ and $\theta$ as unknowns, it satisfies both global force equilibrium and global moment equilibrium.

##### How it closes the indeterminacy

- Does not ignore the interslice forces
- Assumes that the resultant interslice forces have **the same direction on every boundary**
- Finds $F_s$ and $\theta$ so that force and moment equilibrium are satisfied together

##### What "rigorous" means

Under the assumed direction of the internal forces, the Spencer method satisfies all force and moment equilibrium. A method that satisfies all equilibrium in this way is called a **complete equilibrium method**. The constant angle $\theta$, however, is an assumption; it is not derived from the actual stress field of the continuum. So even for a complete equilibrium method, the distribution of internal forces it gives is not necessarily the unique physical solution.

**Original paper**: [E. Spencer (1967), “A method of analysis of the stability of embankments assuming parallel inter-slice forces,” *Géotechnique*, 17(1), 11–26. DOI: 10.1680/geot.1967.17.1.11](https://doi.org/10.1680/geot.1967.17.1.11)

---

(what-section-5-2)=

#### 5.2 Morgenstern–Price method

The Morgenstern–Price method expresses the ratio of the interslice shear force to the interslice normal force as a function $f(x)$ of position $x$, whose shape is given, times an unknown scale factor $\lambda$.

$$
X(x)=\lambda f(x)E(x),
\qquad
\frac{X(x)}{E(x)}=\lambda f(x)
$$ (eq-what-morgenstern-price)

$f(x)$ is chosen from shapes such as half-sine, trapezoidal and constant, and $\lambda$ is determined in the analysis. $F_s$ and $\lambda$ are adjusted until force equilibrium, moment equilibrium and the conditions at both ends are satisfied.

##### How it closes the indeterminacy

- Does not ignore the interslice forces
- Assumes, as $f(x)$, **how the direction of the internal forces varies with position**
- Solves for $\lambda$, which sets their size, and for the factor of safety $F_s$
- Satisfies force and moment equilibrium together

##### Relation to the Spencer method

With $f(x)=1$, $X/E=\lambda$ is constant. In other words, the Spencer method can be seen as the special case of the Morgenstern–Price method whose internal-force function is constant.

##### What remains

Even if several reasonable choices of $f(x)$ give similar factors of safety, the distributions of interslice forces and base normal forces can differ. A matching factor of safety does not mean that the internal stress field has been pinned down.

**Original paper**: [N. R. Morgenstern and V. E. Price (1965), “The analysis of the stability of general slip surfaces,” *Géotechnique*, 15(1), 79–93. DOI: 10.1680/geot.1965.15.1.79](https://doi.org/10.1680/geot.1965.15.1.79)

**Numerical solution**: [N. R. Morgenstern and V. E. Price (1967), “A numerical method for solving the equations of stability of general slip surfaces,” *The Computer Journal*, 9(4), 388–393. DOI: 10.1093/comjnl/9.4.388](https://doi.org/10.1093/comjnl/9.4.388)

---

(what-section-6)=

### 6. The 2D methods side by side

| Method | Main slip surface | Treatment of interslice forces | Equilibrium mainly satisfied | Equilibrium not satisfied, main assumption | Role |
|---|---|---|---|---|---|
| Fellenius method | Circular | Effect ignored | Global moment | Force equilibrium, internal forces | Simplest |
| Simplified Bishop method | Mainly circular | Normal force kept, shear force simplified | Vertical force of each slice + global moment | Global horizontal force | Emphasizes moment equilibrium |
| Simplified Janbu method | Arbitrary shape | Shear force simplified | Global force | Global moment | Emphasizes force equilibrium |
| Spencer method | Circular; extends to general shapes | Direction of the resultant assumed constant | Force + moment | Constant direction of internal forces | Complete equilibrium LEM |
| Morgenstern–Price method | Arbitrary shape | $X/E=\lambda f(x)$ | Force + moment | Internal-force function $f(x)$ | Generalized LEM |

```{note}
"Equilibrium mainly satisfied" summarizes the standard formulations. Software implementations of a method with the same name differ in details: extended equations, and the treatment of seismic loads, reinforcement and non-circular surfaces. Before using a program, check the equations and the convergence criteria given in its manual.
```

---

## What 3D adds

(what-section-7)=

### 7. From slices to columns

```{figure} ./figures/fig_05_3d_column_forces.svg
:name: fig-05-3d-column-forces
:alt: The weight, the normal and shear forces on the base, and the intercolumn forces on the sides of a 3D column with an inclined base

Forces on a 3D column. The base shear force $\boldsymbol{T}_i$ is a vector in the tangent plane, and the strength equation does not fix its direction (dotted circle). Each side carries a normal component and two shear components
```

In 2D, the {term}`sliding mass` is divided in one direction only, and each element is called a "slice." In 3D, it is divided in two directions in plan, so each element becomes a prism-shaped "column."

(what-section-7-1)=

#### 7.1 The base force becomes a vector

On the base of column $i$, take the unit normal vector $\boldsymbol{n}_i$ pointing out of the sliding mass. Let $\boldsymbol{m}_i$ be the unit vector of the assumed {term}`local direction of sliding`, and define the base shear force vector that resists sliding as follows.

$$
\boldsymbol{T}_i=-T_i\boldsymbol{m}_i
$$

The resultant force that the sliding mass receives from its base then splits as follows.

$$
\boldsymbol{R}_{b,i}
=
-N_i\boldsymbol{n}_i+\boldsymbol{T}_i,
\qquad
\boldsymbol{T}_i\cdot\boldsymbol{n}_i=0
$$ (eq-what-column-base-force)

$\boldsymbol{T}_i$ is a vector in the tangent plane of the base, and in general it has two independent components.

The Mohr–Coulomb failure criterion gives directly only its **magnitude**.

$$
\|\boldsymbol{T}_i\|
=
\frac{
c_i'A_i+(N_i-U_i)\tan\phi_i'
}{F_s}
$$ (eq-what-column-shear)

Eq. {eq}`eq-what-column-shear` alone, however, does not fix the **direction** in the tangent plane. 3D LEM therefore needs at least one of the following.

- Assume a direction of sliding that is common to all columns, or that follows a rule
- Use the direction of steepest slope at each point
- Solve for the direction, as an unknown, so that it agrees with global equilibrium
- Take the direction from a velocity field or a kinematic mechanism

In 2D, the direction of the shear force is effectively fixed within the cross section, so this problem goes unnoticed. In 3D, the formulation includes not only the factor of safety but also **the direction in which the mass is assumed to slide**.

(what-section-7-2)=

#### 7.2 Internal boundaries come in two sets

When columns are laid out along the orthogonal $x$ and $y$ directions, the internal boundaries fall into two sets. On each vertical side of a column, the following quantities must in general be considered.

- The resultant of the component normal to the face (the normal force)
- The vertical component of the shear force in the face
- The horizontal component of the shear force in the face
- The point where each resultant acts

So it is not enough to have more copies of the 2D $E$ and $X$. The resultant internal forces gain freedom in their direction, and their contributions to the moment equations increase.

#### 7.3 There are six equilibrium equations, but even more unknowns

A 3D rigid body has the following six equilibrium conditions.

$$
\sum F_x=0,
\quad
\sum F_y=0,
\quad
\sum F_z=0
$$ (eq-what-3d-force)

$$
\sum M_x=0,
\quad
\sum M_y=0,
\quad
\sum M_z=0
$$ (eq-what-3d-moment)

Each column, however, adds the direction of its base shear force and two sets of intercolumn forces to the unknowns. Raising the number of equilibrium equations from three to six therefore does not make the problem solvable.

$$
\boxed{
\text{Extending 2D to 3D}
\neq
\text{multiplying the same equations by a width in depth}
}
$$ (eq-what-3d-not-extrusion)

A 3D extension must deal at once with the extra internal boundaries, the freedom in the direction of the base shear force, and the choice of an {term}`axis of rotation <center of moments>` and a {term}`direction of sliding`.

---

### 8. How was LEM extended to 3D?

Most 3D methods were not built separately from scratch. The typical line of thought is the following.

1. Replace slices with columns
2. Extend the internal-force assumptions made in 2D to the column boundaries in two directions
3. Replace the moment about the center of the circle with the moment about a 3D axis of rotation
4. Add the direction of sliding, implicit in 2D, as a plane of symmetry, a main direction of sliding, or an unknown parameter

The rest of this section follows the development of the main methods from this viewpoint.

---

(what-section-8-1)=

#### 8.1 Hovland method: a direct extension of the Fellenius type

The Hovland method is an early general 3D method. It divides the sliding mass into vertical columns, and it can handle a 3D base shape and the effect of the lateral ends. Its mechanical framework can be seen as an extension of the Fellenius type that ignores the intercolumn forces.

##### How it extends 2D

- Replaces 2D slices with 3D columns
- Uses the inclination and area of each column's base
- Ignores the intercolumn forces and finds the base normal force from the weight
- Sums the {term}`resisting force` and the {term}`driving force` along the assumed direction of sliding

##### What it gains and what it loses

It can represent the effect of a sliding mass of finite width, of a non-uniform 3D shape, and of shapes that include the ends. On the other hand, because it ignores the internal forces, it in general does not fully satisfy force equilibrium in three directions or moment equilibrium. In other words, going to 3D does not by itself make an analysis statically more rigorous.

**Original paper**: [H. J. Hovland (1977), “Three-Dimensional Slope Stability Analysis Method,” *Journal of the Geotechnical Engineering Division*, 103(9), 971–986. DOI: 10.1061/AJGEB6.0000493](https://doi.org/10.1061/AJGEB6.0000493)

---

(what-section-8-2)=

#### 8.2 Hungr and Ugai: extending the simplified Bishop method and others to the column method

Hungr extended the simplified Bishop method directly to 3D. Ugai et al. also carried out a series of studies that extended the ordinary method of slices, the simplified Bishop method, the simplified Janbu method and the Spencer method to 3D.

##### The idea of the 3D simplified Bishop method

- As in 2D, ignores the vertical component of the intercolumn shear force
- Finds the base normal force from vertical force equilibrium of each column
- Finds $F_s$ from global moment equilibrium about the assumed axis of rotation
- In general does not satisfy force equilibrium in the two horizontal directions

This extension keeps the simplified Bishop method easy to compute, while capturing the effects of finite width, the ends and the plan shape. For problems with a non-rotational mechanism, strong asymmetry or a complex direction of base shear, however, whether the original assumption is appropriate must be checked separately.

##### Where Ugai et al. stand

Ugai et al. first presented the 3D ordinary method of slices, then extended the simplified Bishop, simplified Janbu and Spencer methods to 3D. This shows that 3D LEM did not develop into a single 3D formula. Instead, it consists of **several lineages, each carrying a 2D way of closing the indeterminacy over to an assembly of columns**.

**Main primary papers**:

- [O. Hungr (1987), “An extension of Bishop's simplified method of slope stability analysis to three dimensions,” *Géotechnique*, 37(1), 113–117. DOI: 10.1680/geot.1987.37.1.113](https://doi.org/10.1680/geot.1987.37.1.113)
- [O. Hungr, F. M. Salgado and P. M. Byrne (1989), “Evaluation of a three-dimensional method of slope stability analysis,” *Canadian Geotechnical Journal*, 26(4), 679–686. DOI: 10.1139/t89-079](https://doi.org/10.1139/t89-079)
- [K. Ugai, K. Hosobori, H. Nagase and M. Enokido (1986), “Three-dimensional stability analysis of slopes by simple slice method,” *土木学会論文集*, No. 376/III-6, 267–276. DOI: 10.2208/jscej.1986.376_267](https://doi.org/10.2208/jscej.1986.376_267)
- [K. Ugai and K. Hosobori (1988), “Extension of simplified Bishop method, simplified Janbu method and Spencer's method to three dimensions,” *土木学会論文集*, No. 394/III-9, 21–26. DOI: 10.2208/jscej.1988.394_21](https://doi.org/10.2208/jscej.1988.394_21)

---

#### 8.3 The 3D Spencer method: extending the constant-direction assumption to plan and space

In the 2D Spencer method, the resultant interslice forces share a common angle of inclination. A 3D extension expresses this idea of "parallel internal forces" as the direction of the resultants on column boundaries in two directions, or as a plane of common direction.

##### What the extension newly needs

- A main direction of sliding, or an axis of rotation
- The relation between the directions of the two sets of intercolumn forces
- The direction of the shear force in the tangent plane of the base
- Force equilibrium in three directions, and the moment equilibrium conditions to be used

3D Spencer-type methods aim to satisfy more equilibrium conditions than the Hovland method or the 3D simplified Bishop method, under an assumption about the direction of the intercolumn forces. How to extend the single angle that makes "all internal forces parallel" in 2D to 3D, however, has no single answer. Papers and programs differ in which components they take as parallel and about which axes they use moment equilibrium.

Jiang and Yamagami extended the factor-of-safety equation of the 2D Spencer method to the column method, and combined it with a dynamic programming search for the 3D {term}`critical slip surface`.

**Representative primary paper**: [J.-C. Jiang and T. Yamagami (2004), “Three-Dimensional Slope Stability Analysis Using an Extended Spencer Method,” *Soils and Foundations*, 44(4), 127–135. DOI: 10.3208/sandf.44.4_127](https://doi.org/10.3208/sandf.44.4_127)

---

(what-section-8-4)=

#### 8.4 Lam–Fredlund's 3D GLE: a generalization of the Morgenstern–Price type

Lam and Fredlund extended the 2D general limit equilibrium (GLE) method to the column method. In 3D, the internal boundaries run in two directions, so a function is needed for the direction of the resultant intercolumn force on each set.

In outline, the method assumes relations like the following for the internal boundaries in the two directions.

$$
\text{Ratio of shear to normal force on boundaries in the } x \text{ direction}
=\lambda_x f_x(x,y)
$$ (eq-what-3d-lambda-x)

$$
\text{Ratio of shear to normal force on boundaries in the } y \text{ direction}
=\lambda_y f_y(x,y)
$$ (eq-what-3d-lambda-y)

The actual symbols for the components and the way the functions are set up differ between formulations. The central idea, however, is the same.

##### How it extends 2D

- Generalizes the 2D $X/E=\lambda f(x)$ to functions for intercolumn forces in two directions
- Represents the change in direction of the resultant intercolumn forces by functions of any shape
- Searches for the factor of safety and scale factors that satisfy force and moment equilibrium together
- Models the slope, the soil layers, the slip surface and the pore water pressure in 3D space

This approach makes 3D LEM more general. On the other hand, it adds internal-force functions that must be assumed, unknown scale factors and iterative calculation. With more freedom, the effect of the input assumptions on the results needs careful checking.

**Original paper**: [L. Lam and D. G. Fredlund (1993), “A general limit equilibrium model for three-dimensional slope stability analysis,” *Canadian Geotechnical Journal*, 30(6), 905–919. DOI: 10.1139/t93-089](https://doi.org/10.1139/t93-089)

---

#### 8.5 Cheng–Yip: generalization to asymmetric 3D slopes

Many early 3D methods implicitly assumed a plane of symmetry or a known main direction of sliding. Cheng and Yip extended the ideas of the simplified Bishop, simplified Janbu and Morgenstern–Price methods to asymmetric 3D slopes.

##### Key ideas

- Does not presume that the plan shape and the slip surface are symmetric
- Writes out the base forces and intercolumn forces explicitly for two horizontal axis directions
- Maps each 2D method's choice of "what to ignore and what to balance" onto 3D
- In the Morgenstern–Price type, adds internal-force functions and coefficients for two directions

This work shows that the key to a 3D extension is not only making the shape solid. It lies in **redefining in space the internal-force assumption and the direction of sliding, both of which were one-directional in 2D**.

**Original paper**: [Y. M. Cheng and C. J. Yip (2007), “Three-Dimensional Asymmetrical Slope Stability Analysis—Extension of Bishop's, Janbu's, and Morgenstern–Price's Techniques,” *Journal of Geotechnical and Geoenvironmental Engineering*, 133(12), 1544–1555. DOI: 10.1061/(ASCE)1090-0241(2007)133:12(1544)](https://doi.org/10.1061/%28ASCE%291090-0241%282007%29133%3A12%281544%29)

---

(what-section-9)=

### 9. The 3D methods side by side

| Method or family | Corresponding 2D idea | Intercolumn forces | Main equilibrium | Features and limits | Primary source |
|---|---|---|---|---|---|
| Hovland method | Fellenius type | Ignored | Mainly sums global resisting and driving forces | Simple, but not a complete equilibrium method | Hovland (1977) |
| Hungr's 3D simplified Bishop method | Simplified Bishop method | Vertical component of shear force simplified | Vertical force of each column + global moment | Suits rotational, fairly symmetric problems | Hungr (1987) |
| Ugai et al.'s family | Simplified Bishop, simplified Janbu and Spencer methods | Assumed to match the original 2D method | Differs by method | Extends each 2D family to 3D | Ugai et al. (1986); Ugai & Hosobori (1988) |
| Spencer method extended to 3D | Spencer method | Assumed parallel in space | Force + the moment conditions used | How "parallel" is defined in 3D differs by implementation | Jiang & Yamagami (2004) |
| Lam–Fredlund's 3D GLE | Morgenstern–Price method, GLE | Expressed by functions in two directions | Force + moment | Very general, but with more assumptions and unknowns | Lam & Fredlund (1993) |
| Cheng–Yip | Simplified Bishop, simplified Janbu and Morgenstern–Price methods | Each 2D assumption extended to two directions | Differs by method | Handles asymmetric 3D shapes directly | Cheng & Yip (2007) |

#### Reading 3D factors of safety

A 3D analysis adds the resistance of the lateral ends, so in many cases it gives a higher factor of safety than a 2D analysis of the same central cross section. If the following conditions differ, however, the two cannot simply be compared.

- Whether the slip surfaces found in 2D and 3D represent the same failure mechanism
- Whether the direction of sliding assumed in 3D is appropriate
- How far the intercolumn forces were taken into account
- Whether the strength on the sides has been counted twice
- How the unit depth in 2D was matched to the finite width in 3D
- Whether the 3D distributions of soil layers, pore water pressure and external loads agree with the 2D analysis

```{warning}
So this tendency must not be used as a rule that "the 3D factor of safety is always larger than the 2D one." Any difference must be explained in terms of shape, strength, internal-force assumptions and the failure mechanisms searched.
```

---

## The layers of approximation in LEM

(what-section-10)=

### 10. Approximation is not only in the internal-force assumptions

The approximations in LEM are easier to see when arranged as layers stacked from the bottom up.

#### Layer 1: geometric discretization

The continuous soil mass is replaced with a finite number of slices or columns.

- A curved surface is approximated by small plane pieces or simple bases
- Distributed loads and stresses are replaced with resultants
- The number and orientation of the divisions introduce a discretization error

#### Layer 2: assumed failure mechanism

The slip surface, or the family of slip surfaces that can be searched, is fixed in advance.

- Circular, composite, non-circular, ellipsoidal, NURBS surfaces and so on
- The actual progressive failure, or a failure that links several surfaces, may lie outside the search range
- The minimum factor of safety found is the minimum within the family of surfaces searched

#### Layer 3: assumed mobilization of strength

A single factor of safety $F_s$ is shared by the whole slip surface, and strength is taken to be mobilized everywhere at the same time and in the same proportion.

$$
\tau_{m,i}
=
\frac{
c_i'+(\sigma_{n,i}-u_i)\tan\phi_i'
}{F_s}
$$ (eq-what-mobilized-stress)

This assumption does not directly represent differences in strain from place to place, softening from peak to residual strength, or progressive failure.

#### Layer 4: how the internal forces are determined

- Ignore components of the internal forces
- Take the direction of the internal forces as constant
- Assume, as a function, how the ratio of the internal forces varies with position
- Assume or compute the points where the internal forces act

The names of the methods mostly describe this layer.

#### Layer 5: the 3D direction of sliding and axis of rotation

In 3D, the direction of the base shear force vector, the direction of sliding and the axis for moments must also be chosen. In a symmetric problem, the geometry gives candidates. In an asymmetric problem, they become unknowns or search variables.

#### Layer 6: numerical solution and search

- How $F_s$, the internal-force scale factor and the internal-force angle are solved by iteration
- The search for the critical slip surface
- Convergence criteria and local solutions
- Handling of unreasonable base normal forces, negative effective normal forces, and a line of thrust (the line through the points where the interslice forces act) that leaves the slices

Even with the same theoretical equations, different numerical implementations or search methods can give different results.

---

### 11. The roles of LEM and continuum analysis

| Question | LEM | Continuum analysis such as FEM or FDM |
|---|---|---|
| Global factor of safety | Well suited | Found by strength reduction and similar methods |
| Resisting and driving forces on an assumed slip surface | Found directly | Found from the stress field in post-processing |
| Magnitude of displacement | In principle not found | Found |
| Stress redistribution | Represented indirectly through the internal-force assumptions | Found through the constitutive law |
| Progressive failure | In principle not represented directly | Needs softening laws, nonlocal regularization and the like |
| 3D end effects | Found with 3D LEM | Found with a 3D model |
| Effort for input and computation | Relatively small | Generally large |
| What is mainly read from the results | Factor of safety and sliding mechanism | Stresses, displacements, plastic zones, failure process |

Neither one is simply better than the other. LEM evaluates global stability for an assumed failure mechanism with mechanics that are easy to follow. Continuum analysis, on the other hand, can handle deformation and stress redistribution. Its results, however, depend on the constitutive law, the mesh, the boundary conditions and the strength reduction procedure.

In practice, the two work best as complements. First compare several methods and several slip surfaces with LEM. Then, as needed, check deformation, local stresses, the construction sequence and progressive failure with a continuum analysis.

---

## Lineage and summary

### 12. The lineage of LEM

The lineage from the 2D methods to the 3D methods runs as follows.

```text
Continuum mechanics
    ↓ discretization + assumed slip surface
2D methods of slices
    ├─ Fellenius method ──────────────→ Hovland-type 3D method
    ├─ Simplified Bishop method ──────→ 3D simplified Bishop method of Hungr and Ugai
    ├─ Simplified Janbu method ───────→ 3D simplified Janbu method of Ugai and Cheng–Yip
    ├─ Spencer method ────────────────→ 3D Spencer method of Ugai and Jiang–Yamagami
    └─ Morgenstern–Price method, GLE → 3D GLE of Lam–Fredlund and Cheng–Yip
```

This lineage is not a chronological history of inventions. It is a conceptual map of **how the mechanical assumptions were passed on**.

---

### 13. A final summary

#### 13.1 The starting point of LEM

In LEM, even with the following equation known, $N_i$, $F_s$ and the interslice or intercolumn forces are still unknown.

$$
T_i
=
\frac{c_i'A_i+(N_i-U_i)\tan\phi_i'}{F_s}
$$ (eq-what-summary-shear)

#### 13.2 Key points in 2D

- Each slice carries its base forces and the interslice forces on its left and right
- Force and moment equilibrium alone do not determine the distribution of internal forces uniquely
- The Fellenius, simplified Bishop, simplified Janbu, Spencer and Morgenstern–Price methods differ in how they close the indeterminacy
- "Simplified methods" (the Fellenius, simplified Bishop and simplified Janbu methods) ignore some or all of the internal forces
- "Complete equilibrium methods" assume the direction of the internal forces and then satisfy all force and moment equilibrium

#### 13.3 What 3D adds

- Slices become columns
- Internal boundaries run in two directions instead of one
- The base shear force becomes a vector in the tangent plane
- Assumptions are needed about the direction of sliding, the axis of rotation and the intercolumn forces in two directions
- Six rigid-body equilibrium equations are not enough on their own, because the internal forces gain even more freedom

#### 13.4 How LEM was extended to 3D

- Hovland extended the Fellenius-type simplification to the column method
- Hungr and Ugai et al. carried the 2D assumptions of the simplified Bishop method and others over to 3D
- 3D Spencer-type methods extended the idea of parallel internal forces into space
- Lam–Fredlund generalized the internal-force functions of the Morgenstern–Price method and GLE to column boundaries in two directions
- Cheng–Yip extended the ideas of the simplified Bishop, simplified Janbu and Morgenstern–Price methods to asymmetric 3D slopes

(what-section-13-5)=

#### 13.5 Reading analysis results

When reading analysis results, check the following points, not only the name of the method.

1. How the slip surface was assumed and how it was searched
2. How strength and the factor of safety were defined
3. Which components of the internal forces were ignored, and which were expressed as functions
4. Which force and moment equilibrium conditions were satisfied
5. In 3D, how the direction of sliding and the axis of rotation were chosen
6. Whether the distributions of normal forces and internal forces in the converged solution are physically reasonable

In short, LEM is not simply "a method that divides the resisting force by the driving force."

$$
\boxed{
\begin{aligned}
&\text{LEM discretizes an assumed failure mechanism,}\\
&\text{sets how strength is mobilized and how the internal forces are determined,}\\
&\text{and finds the factor of safety from static equilibrium in the limit state.}
\end{aligned}
}
$$ (eq-what-summary)

---

## Review questions

Click a question to see its answer.

:::{dropdown} Q1. The base of "Working through the numbers" in Chapter 1, Section 6 has $c'=10$ kPa, $\phi'=30^\circ$, $\sigma_n'=60$ kPa and $\tau_m=30$ kPa, which give $F_s=1.49$. Reduce the strength by the factor $F_s$ and find $c_m'$ and $\phi_m'$. What does the Mohr–Coulomb failure criterion give on this base with these $c_m'$ and $\phi_m'$?
:icon: question

$c_m'=10/1.49=6.71$ kPa and $\tan\phi_m'=\tan 30^\circ/1.49=0.3875$, so $\phi_m'=21.2^\circ$. $F_s$ divides $\tan\phi'$, not $\phi'$, so $\phi_m'$ is not $\phi'/F_s=20.1^\circ$. Put into the Mohr–Coulomb failure criterion, they give $c_m'+\sigma_n'\tan\phi_m'=6.71+60\times0.3875=30.0$ kPa, equal to the mobilized shear stress $\tau_m$. In other words, reducing the strength by the factor $F_s$ puts this base exactly at the limit state. (→[Section 1](#what-section-1), [Chapter 1, Section 6](#section-6))
:::

:::{dropdown} Q2. Why can equilibrium and the base strength equation alone not determine the distribution of internal forces?
:icon: question

Because there are more unknowns than independent equilibrium equations. For $n$ slices, there are $4n-2$ unknowns but only $3n$ equilibrium equations, three per slice. (→[Section 3.1](#what-section-3-1))
:::

:::{dropdown} Q3. If the sliding mass is divided into $n=10$ slices, how many unknowns and equations are there, counted as in the table of Section 3.1? How many conditions are missing?
:icon: question

There are $4n-2=38$ unknowns. There are $3n=30$ equilibrium equations, so $n-2=8$ conditions are missing. The finer the division into slices, the more conditions are missing. (→[Section 3.1](#what-section-3-1))
:::

:::{dropdown} Q4. What three operations does "closing the indeterminacy" mean in concrete terms?
:icon: question

Ignoring part of the internal forces; assuming the direction of the internal forces or the ratio of their components; and using only part of the equilibrium conditions. Each method can be classified by its combination of these. (→[Section 3.3](#what-section-3-3))
:::

:::{dropdown} Q5. What does each of the Fellenius, simplified Bishop and simplified Janbu methods ignore, and which equilibrium does it use?
:icon: question

- Fellenius method: ignores the effect of the interslice forces and uses global moment equilibrium about the center of the circle
- Simplified Bishop method: keeps the interslice normal force and simplifies the shear force ($X_i=0$ in implementations). It uses vertical force equilibrium of each slice and global moment equilibrium
- Simplified Janbu method: ignores or simplifies the interslice shear force and uses force equilibrium

(→[Section 4](#what-section-4), [Section 6](#what-section-6))
:::

:::{dropdown} Q6. In what sense is the Spencer method called a "complete equilibrium method"?
:icon: question

In the sense that, under the assumed direction of the internal forces (the same angle $\theta$ on every boundary), it satisfies all force and moment equilibrium. The Spencer method's solution, however, is not an exact continuum solution. Nor is the distribution of internal forces it gives necessarily the unique physical solution. (→[Section 5.1](#what-section-5-1))
:::

:::{dropdown} Q7. In the Morgenstern–Price method's $X/E=\lambda f(x)$, how are $f(x)$ and $\lambda$ each determined? If several choices of $f(x)$ give nearly the same factor of safety, is the distribution of internal forces then pinned down?
:icon: question

$f(x)$ is a function that describes how the direction of the internal forces varies with position. It is assumed, chosen from shapes such as half-sine and trapezoidal. $\lambda$, on the other hand, is the scale factor that sets the size of $X/E$. It is solved for together with $F_s$ from force and moment equilibrium. Nearly the same factor of safety does not pin down the distribution of internal forces, because a different $f(x)$ can give different distributions of interslice forces and base normal forces. With $f(x)=1$, the method becomes the Spencer method. (→[Section 5.2](#what-section-5-2))
:::

:::{dropdown} Q8. What quantities must newly be chosen in 3D? Why are six equilibrium equations still not enough?
:icon: question

The direction of the base shear force in the tangent plane, the direction of sliding and the axis of rotation must newly be chosen. The equilibrium equations rise to six, but the unknowns rise by more. Because the internal boundaries run in two directions, there are more components and points of action of intercolumn forces. The direction of the base shear force is also added to the unknowns. (→[Section 7](#what-section-7))
:::

:::{dropdown} Q9. Is the 3D Hovland method statically more rigorous than the 2D Spencer method?
:icon: question

No. The Hovland method is an extension of the Fellenius type that ignores the intercolumn forces, so it in general does not fully satisfy force equilibrium in three directions or moment equilibrium. The 2D Spencer method, by contrast, assumes the direction of the internal forces and then satisfies all force and moment equilibrium. In other words, static rigor depends not on whether the analysis is 2D or 3D, but on how it treats the internal forces and which equilibrium it satisfies. (→[Section 5.1](#what-section-5-1), [Section 8.1](#what-section-8-1))
:::

:::{dropdown} Q10. Why can't one say outright that "the 3D factor of safety is larger than the 2D one"?
:icon: question

Because the conditions being compared in 2D and 3D are not necessarily the same. If they differ on points such as whether the slip surfaces found represent the same failure mechanism, whether the direction of sliding is appropriate, how far the intercolumn forces were considered, and whether the strength on the sides was counted twice, the two cannot simply be compared. (→[Section 9](#what-section-9))
:::

:::{dropdown} Q11. What does using a single factor of safety $F_s$ for the whole slip surface assume about strength? What can that assumption not represent directly?
:icon: question

It assumes that strength is mobilized everywhere on the slip surface at the same time and in the same proportion. So it does not directly represent differences in strain from place to place, softening from peak to residual strength, or progressive failure. (→[Section 10](#what-section-10))
:::

:::{dropdown} Q12. What does the name of a method not tell you?
:icon: question

The assumed slip surface and how it was searched; how strength and the factor of safety were defined; which internal-force components were ignored or expressed as functions; which equilibrium was satisfied; in 3D, how the direction of sliding and the axis of rotation were chosen; and whether the converged solution is physically reasonable. Of the layers of approximation in Section 10, a method's name mainly describes the layer of how the internal forces are determined. Even within that layer, the details of methods with the same name differ between implementations. (→[Section 10](#what-section-10), [Section 13.5](#what-section-13-5))
:::

---

## What to read next

This chapter sorted out how each method closes the static indeterminacy. In actual analyses, however, the shape of the slip surface, the direction of sliding, the way of discretizing and the search range also affect what the results mean. [Chapter 3, "Using the limit equilibrium method in practice"](lem-in-practice-mechanical-perspective.md) covers how to read these mechanically.

## References

### Original papers by method

The original papers discussed in the text and representative primary sources are listed by method. A DOI is given only where it could be matched against the publisher's or Crossref's bibliographic data. Fellenius (1927, 1936) and Janbu (1954, 1973), whose DOIs could not be verified, have none. Where a bibliographic page was found, a link to it is given.

#### 2D methods

##### Fellenius method (ordinary method of slices)

1. Fellenius, W. (1927). *Erdstatische Berechnungen mit Reibung und Kohäsion (Adhäsion) und unter Annahme kreiszylindrischer Gleitflächen*. Berlin: Ernst & Sohn. [Bibliographic record](https://books.google.com/books?id=yHhHAAAAIAAJ).
2. Fellenius, W. (1936). “Calculation of the Stability of Earth Dams.” *Proceedings of the Second Congress on Large Dams*, Vol. 4, pp. 445–462. [Bibliographic record](https://cir.nii.ac.jp/crid/1573950399306830336).

##### Simplified Bishop method

3. Bishop, A. W. (1955). “The use of the slip circle in the stability analysis of slopes.” *Géotechnique*, 5(1), 7–17. [https://doi.org/10.1680/geot.1955.5.1.7](https://doi.org/10.1680/geot.1955.5.1.7)

##### Janbu method

4. Janbu, N. (1954). “Application of composite slip surfaces for stability analysis.” *Proceedings of the European Conference on Stability of Earth Slopes*, Stockholm, Vol. 3, pp. 43–49. [Bibliographic record](https://cir.nii.ac.jp/crid/1570009750148611712).
5. Janbu, N. (1973). “Slope Stability Computations.” In R. C. Hirschfeld and S. J. Poulos (eds.), *Embankment-Dam Engineering: Casagrande Volume*, pp. 47–86. New York: Wiley.

##### Spencer method

6. Spencer, E. (1967). “A method of analysis of the stability of embankments assuming parallel inter-slice forces.” *Géotechnique*, 17(1), 11–26. [https://doi.org/10.1680/geot.1967.17.1.11](https://doi.org/10.1680/geot.1967.17.1.11)

##### Morgenstern–Price method and GLE

7. Morgenstern, N. R., and Price, V. E. (1965). “The analysis of the stability of general slip surfaces.” *Géotechnique*, 15(1), 79–93. [https://doi.org/10.1680/geot.1965.15.1.79](https://doi.org/10.1680/geot.1965.15.1.79)
8. Morgenstern, N. R., and Price, V. E. (1967). “A numerical method for solving the equations of stability of general slip surfaces.” *The Computer Journal*, 9(4), 388–393. [https://doi.org/10.1093/comjnl/9.4.388](https://doi.org/10.1093/comjnl/9.4.388)

##### Comparison of methods

9. Fredlund, D. G., and Krahn, J. (1977). “Comparison of slope stability methods of analysis.” *Canadian Geotechnical Journal*, 14(3), 429–439. [https://doi.org/10.1139/t77-045](https://doi.org/10.1139/t77-045)

#### 3D methods

##### Hovland method

10. Hovland, H. J. (1977). “Three-Dimensional Slope Stability Analysis Method.” *Journal of the Geotechnical Engineering Division*, 103(9), 971–986. [https://doi.org/10.1061/AJGEB6.0000493](https://doi.org/10.1061/AJGEB6.0000493)

##### Hungr (3D simplified Bishop method)

11. Hungr, O. (1987). “An extension of Bishop's simplified method of slope stability analysis to three dimensions.” *Géotechnique*, 37(1), 113–117. [https://doi.org/10.1680/geot.1987.37.1.113](https://doi.org/10.1680/geot.1987.37.1.113)
12. Hungr, O., Salgado, F. M., and Byrne, P. M. (1989). “Evaluation of a three-dimensional method of slope stability analysis.” *Canadian Geotechnical Journal*, 26(4), 679–686. [https://doi.org/10.1139/t89-079](https://doi.org/10.1139/t89-079)

##### Ugai et al.

13. Ugai, K., Hosobori, K., Nagase, H., and Enokido, M. (1986). “Three-dimensional stability analysis of slopes by simple slice method.” *土木学会論文集*, No. 376/III-6, 267–276. [https://doi.org/10.2208/jscej.1986.376_267](https://doi.org/10.2208/jscej.1986.376_267)
14. Ugai, K. (1987). “Three-dimensional slope stability analysis by simplified Janbu method.” *地すべり*, 24(3), 8–14. [https://doi.org/10.3313/jls1964.24.3_8](https://doi.org/10.3313/jls1964.24.3_8)
15. Ugai, K., and Hosobori, K. (1988). “Extension of simplified Bishop method, simplified Janbu method and Spencer's method to three dimensions.” *土木学会論文集*, No. 394/III-9, 21–26. [https://doi.org/10.2208/jscej.1988.394_21](https://doi.org/10.2208/jscej.1988.394_21)

##### 3D GLE (Morgenstern–Price type)

16. Lam, L., and Fredlund, D. G. (1993). “A general limit equilibrium model for three-dimensional slope stability analysis.” *Canadian Geotechnical Journal*, 30(6), 905–919. [https://doi.org/10.1139/t93-089](https://doi.org/10.1139/t93-089)

##### Spencer method extended to 3D

17. Jiang, J.-C., and Yamagami, T. (2004). “Three-Dimensional Slope Stability Analysis Using an Extended Spencer Method.” *Soils and Foundations*, 44(4), 127–135. [https://doi.org/10.3208/sandf.44.4_127](https://doi.org/10.3208/sandf.44.4_127)

##### 3D extension to asymmetric slopes

18. Cheng, Y. M., and Yip, C. J. (2007). “Three-Dimensional Asymmetrical Slope Stability Analysis—Extension of Bishop's, Janbu's, and Morgenstern–Price's Techniques.” *Journal of Geotechnical and Geoenvironmental Engineering*, 133(12), 1544–1555. [https://doi.org/10.1061/(ASCE)1090-0241(2007)133:12(1544)](https://doi.org/10.1061/%28ASCE%291090-0241%282007%29133%3A12%281544%29)
