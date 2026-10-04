---
title: "From continuum mechanics to where the limit equilibrium method begins: deriving the forces on a slice base from stress"
lang: en
series: "1 of 3"
translated_from: "9b11256"
translated_on: 2026-10-04
---

# From continuum mechanics to where the limit equilibrium method begins

**Deriving the forces on a slice base from stress**

This chapter starts from the stress tensor of continuum mechanics and derives the forces $N_i$, $U_i$ and $T_i$ that the limit equilibrium method (LEM) uses on the base of a slice. Along the way, it splits the force on the slip surface into a normal component and a shear component, then brings in effective stress and the shear strength given by the Mohr–Coulomb failure criterion.

The terms and symbols are collected in the [Glossary](lem-glossary.md).

(overview)=

## Overview of LEM

To check whether a slope will fail, LEM sets up the problem as follows.

```{figure} ./figures/fig_c00_slope_overview.svg
:name: fig-c00-slope-overview
:alt: A circular slip surface assumed in a slope, the sliding mass, six slices, and the weight, normal force and shear force acting on one slice

The setting LEM deals with. A slip surface is assumed in the slope, the soil above it is divided into slices, and the analysis handles the forces on each base. Interslice forces are omitted
```

1. Assume one surface in the slope along which it may fail (the **slip surface**)
2. Divide the soil above the slip surface (the **sliding mass**) into vertical strips. In 2D a strip is called a **slice**; in 3D, a **column**
3. The ground below the slip surface exerts a force on the base of each slice. Split this force into a component normal to the base, $N_i$ (the **normal force**), and a component along the base, $T_i$ (the **shear force**)

The **factor of safety** $F_s$ is then defined as the ratio of the largest shear force the base can develop (the **shear strength**) to the shear force actually acting on the base in its current state. The shear force actually acting is the part of the strength in use, so it is also called the **mobilized** shear force.

$$
F_s=\frac{\text{maximum shear force that can be developed}}{\text{mobilized shear force}}
$$ (eq-start-fs-definition)

$F_s$ measures the stability of the assumed slip surface. For example, $F_s=2$ means the available shear strength is twice the mobilized shear force. If $F_s<1$, equilibrium cannot be maintained along that surface.

Textbooks and guides on LEM sometimes treat the numerator of Eq. {eq}`eq-start-fs-definition` (the shear strength) as the **resisting force** and the denominator (the mobilized shear force) as the **driving force** (the force that tends to make the soil slide), and write:

$$
F_s=\frac{\text{resisting force}}{\text{driving force}}
$$ (eq-start-fs-definition-mod)

Strictly speaking, the mobilized shear force in the denominator is not the driving force itself. It is a force that **resists** movement along the slip surface. However, consider the **force equilibrium** of a sliding mass at rest: the shear force mobilized on the slip surface balances the driving force from the weight and other loads. So the two are equal in magnitude, and treating the denominator as the driving force does not change the value of the factor of safety. For this reason, Eq. {eq}`eq-start-fs-definition-mod` is often used as the more intuitive form.

```{note}
"Force" in Eqs. {eq}`eq-start-fs-definition` and {eq}`eq-start-fs-definition-mod` is a loose way of speaking, because some methods take a ratio of quantities that are not forces. For example, the simplified Bishop method finds the factor of safety as a ratio of **moments** about the center of the circle. This chapter, too, rewrites the definition in Section 6 as the ratio of the available shear strength to the shear stress needed to maintain equilibrium.
```

The rest of this chapter explains how $N_i$ and $T_i$ in the figure are built from the stress at each point in the ground. It also traces where the Mohr–Coulomb failure criterion, which describes the strength of the soil itself, turns into $T_i$ on the base. The end point is the following equation.

$$
T_i
=
\frac{c_i'A_i+(N_i-U_i)\tan\phi_i'}{F_s}
$$ (eq-start-goal)

Sections 1 to 9 explain, step by step, how to derive this equation and why it is **the starting point of LEM**.

---


(notation)=

## Notation and sign conventions

To keep the equations of continuum mechanics and the strength equations of geotechnical engineering apart, the rest of this chapter uses the following notation and sign conventions.

- $\boldsymbol{\sigma}$: the Cauchy stress tensor, with tension positive
- $\boldsymbol{n}$: the unit normal vector, pointing outward from the sliding mass
- $\boldsymbol{t}(\boldsymbol{n})=\boldsymbol{\sigma}\boldsymbol{n}$: the traction vector that the surrounding ground exerts on the sliding mass across a surface with normal $\boldsymbol{n}$
- $\sigma_n$: the normal stress. Following geotechnical practice, compression is positive ($\sigma_n\ge 0$ under compression)
- $u\ge 0$: the pore water pressure
- $\boldsymbol{m}$: the unit vector of the local direction of sliding, assumed to lie in the tangent plane of the slip surface
- $\tau_m$: the magnitude of the mobilized shear stress (defined in Section 6)
- $c'$, $\phi'$: the cohesion and the angle of internal friction in terms of effective stress
- $F_s$: the factor of safety

Under these conventions, the traction on the sliding mass has a compressive normal component $-\sigma_n\boldsymbol{n}$ and a shear component $-\tau_m\boldsymbol{m}$ that resists sliding. The supplement below shows how the expressions change under the other sign convention.

:::{dropdown} Supplement A: tension-positive and compression-positive sign conventions
With the tension-positive convention that is standard in continuum mechanics, Cauchy's formula is

$$
\boldsymbol{t}=\boldsymbol{\sigma}\boldsymbol{n}
$$

The normal component of the traction, sign included, is

$$
t_n=\boldsymbol{n}^{\mathsf T}\boldsymbol{\sigma}\boldsymbol{n}
$$

Under compression, $t_n<0$.

Geotechnical engineering takes compression as positive. The normal stress is then

$$
\sigma_n=-t_n
$$

If the compression-positive stress tensor is defined as

$$
\boldsymbol{\sigma}^{(c)}=-\boldsymbol{\sigma}
$$

then

$$
\sigma_n
=
\boldsymbol{n}^{\mathsf T}\boldsymbol{\sigma}^{(c)}\boldsymbol{n}
$$

In this case, however, the actual traction is

$$
\boldsymbol{t}=-\boldsymbol{\sigma}^{(c)}\boldsymbol{n}
$$

```{note}
Some references use a compression-positive $\sigma_n$ but define the direction of the force separately and handle the sign outside the equations. This chapter uses the compression-positive magnitude $\sigma_n$ in the strength equations and states the direction of the force, $-\boldsymbol{n}$, explicitly in the vector equations.
```
:::

---

(section-1)=

## 1. The exact starting point in continuum mechanics

The state of stress in the ground is described by the Cauchy stress tensor at each point $\boldsymbol{x}$:

$$
\boldsymbol{\sigma}=\boldsymbol{\sigma}(\boldsymbol{x})
$$ (eq-start-stress-field)

The distribution of stress along the slip surface is an unknown function even before discretization. Finding it as a continuum problem takes not only the equilibrium equations but also a constitutive law, displacement compatibility, boundary conditions and more. Instead of solving this whole boundary value problem, LEM usually divides the sliding mass into a finite number of slices or columns and works with the resultant forces on each and their equilibrium.

```{note}
**The link to continuum mechanics**

In a continuum at rest, equilibrium of forces at each point reads

$$
\nabla\!\cdot\!\boldsymbol{\sigma}+\rho\boldsymbol{b}=\boldsymbol{0}
$$

Here $\rho\boldsymbol{b}$ is the body force per unit volume; with gravity alone, $\boldsymbol{b}=\boldsymbol{g}$. In an ordinary continuum without couple stresses, the balance of angular momentum also gives $\boldsymbol{\sigma}=\boldsymbol{\sigma}^{\mathsf T}$.

The rest of this chapter, however, uses only Cauchy's formula $\boldsymbol{t}=\boldsymbol{\sigma}\boldsymbol{n}$ from the next section. The two equations above are given to show where in continuum mechanics this chapter's starting point connects.
```

---

(section-2)=

## 2. Extracting the traction from the stress tensor

At a point $\boldsymbol{x}$ on the slip surface, let $\boldsymbol{n}(\boldsymbol{x})$ be the outward unit normal vector. The force per unit area acting on this surface is called the **traction**. Cauchy's formula gives the traction as follows.

$$
\boxed{
\boldsymbol{t}(\boldsymbol{x},\boldsymbol{n})
=
\boldsymbol{\sigma}(\boldsymbol{x})\boldsymbol{n}(\boldsymbol{x})
}
$$ (eq-start-cauchy)

The stress tensor $\boldsymbol{\sigma}$ is a second-order tensor, while the traction $\boldsymbol{t}$ on a given surface is a vector. Depending on context, the word "stress" can mean the tensor, the traction or one of their components. For this reason, this chapter keeps them apart.

```{figure} ./figures/fig_c01_stress_to_traction.svg
:name: fig-c01-stress-to-traction
:alt: An element representing the stress at one point, and the tractions on two surfaces of different orientation cut through the same point

The stress tensor at a point and the tractions $\boldsymbol{t}=\boldsymbol{\sigma}\boldsymbol{n}$ on two surfaces of different orientation. When the orientation of the surface changes, the direction and magnitude of the traction change too
```

---

(section-3)=

## 3. Normal and shear components of the traction

Write the normal component of the traction, sign included, as follows.

$$
t_n
=
\boldsymbol{n}^{\mathsf T}\boldsymbol{t}
=
\boldsymbol{n}^{\mathsf T}\boldsymbol{\sigma}\boldsymbol{n}
$$ (eq-start-normal-component)

Under the tension-positive convention, compression gives $t_n<0$. So the compression-positive **normal stress** $\sigma_n$ used in geotechnical engineering is defined as follows.

$$
\boxed{
\sigma_n=-t_n
=
-\boldsymbol{n}^{\mathsf T}\boldsymbol{\sigma}\boldsymbol{n}
}
$$ (eq-start-sigma-n)

Under compression, $\sigma_n\ge 0$. How to handle soil in tension, or a negative effective normal stress, is treated as a numerical issue in [Chapter 3](lem-in-practice-mechanical-perspective.md).

The traction splits uniquely into a normal component and a shear component in the tangent plane.

$$
\boxed{
\boldsymbol{t}
=
-\sigma_n\boldsymbol{n}+\boldsymbol{\tau}
}
$$ (eq-start-traction-split)

Here the shear component $\boldsymbol{\tau}$ satisfies the following equation.

$$
\boldsymbol{\tau}\cdot\boldsymbol{n}=0
$$ (eq-start-tau-tangential)

:::{dropdown} Supplement B: splitting into normal and shear components, and projection matrices
Let $\|\boldsymbol{n}\|=1$. The matrices that project onto the normal direction and onto the tangent plane are:

$$
\boldsymbol{P}_n=\boldsymbol{n}\boldsymbol{n}^{\mathsf T},
\qquad
\boldsymbol{P}_t=\boldsymbol{I}-\boldsymbol{n}\boldsymbol{n}^{\mathsf T}
$$

The vector component of the traction in the normal direction is

$$
\begin{aligned}
\boldsymbol{t}_n
&=(\boldsymbol{n}^{\mathsf T}\boldsymbol{t})\boldsymbol{n}\\
&=\boldsymbol{n}\boldsymbol{n}^{\mathsf T}\boldsymbol{t}\\
&=\boldsymbol{P}_n\boldsymbol{t}
\end{aligned}
$$

and the shear component is

$$
\begin{aligned}
\boldsymbol{\tau}
&=\boldsymbol{t}-\boldsymbol{t}_n\\
&=(\boldsymbol{I}-\boldsymbol{n}\boldsymbol{n}^{\mathsf T})\boldsymbol{t}\\
&=(\boldsymbol{I}-\boldsymbol{n}\boldsymbol{n}^{\mathsf T})
\boldsymbol{\sigma}\boldsymbol{n}
\end{aligned}
$$

Since

$$
\boldsymbol{n}^{\mathsf T}\boldsymbol{\tau}=0
$$

holds, $\boldsymbol{\tau}$ lies in the tangent plane. Under the tension-positive convention, $\boldsymbol{t}_n=t_n\boldsymbol{n}=-\sigma_n\boldsymbol{n}$.
:::

In 2D, the tangent direction is unique up to its sense (sign). In 3D, by contrast, the tangent plane contains infinitely many directions. For this reason, the basis of the tangent plane must be kept apart from the local direction of sliding that is actually assumed. This chapter takes the local direction of sliding to be a vector $\boldsymbol{m}$ that satisfies

$$
\|\boldsymbol{m}\|=1,
\qquad
\boldsymbol{m}\cdot\boldsymbol{n}=0
$$ (eq-start-slip-direction)

The shear component that resists sliding is written as follows.

$$
\boxed{
\boldsymbol{\tau}_m=-\tau_m\boldsymbol{m}
}
$$ (eq-start-shear-traction)

:::{dropdown} Supplement C: the basis of the tangent plane in 3D, and the assumed local direction of sliding
In 3D, the tangent plane is

$$
\left\{
\boldsymbol{v}\mid \boldsymbol{v}\cdot\boldsymbol{n}=0
\right\}
$$

With an orthogonal tangent basis $\boldsymbol{t}_1,\boldsymbol{t}_2$, any vector in the tangent plane can be written as

$$
\boldsymbol{v}=a\boldsymbol{t}_1+b\boldsymbol{t}_2
$$

In other words, $\boldsymbol{n}$ alone does not determine $\boldsymbol{m}$.

One approach, for example, assumes a direction $\boldsymbol{d}$ in which the whole mass moves and projects it onto the tangent plane at each point. Call the projected vector

$$
\boldsymbol{d}_{\mathrm{tan}}
=
(\boldsymbol{I}-\boldsymbol{n}\boldsymbol{n}^{\mathsf T})\boldsymbol{d}
$$

and, when $\boldsymbol{d}_{\mathrm{tan}}\ne\boldsymbol{0}$, define

$$
\boxed{
\boldsymbol{m}
=
\frac{\boldsymbol{d}_{\mathrm{tan}}}
{\|\boldsymbol{d}_{\mathrm{tan}}\|}
}
$$

This is only one possible choice, though. In 3D LEM, the assumed local direction of sliding and the way the shear resistance is projected can differ from method to method.
:::

---

(section-4)=

## 4. From total stress to effective stress

Apply Terzaghi's principle of effective stress to a saturated soil. If the compression-positive total stress tensor is $\boldsymbol{\sigma}^{(c)}=-\boldsymbol{\sigma}$, the effective stress tensor is:

$$
\boxed{
\boldsymbol{\sigma}'^{(c)}
=
\boldsymbol{\sigma}^{(c)}-u\boldsymbol{I}
}
$$ (eq-start-effective-tensor)

Projecting this onto the normal direction of the slip surface gives the **effective normal stress**.

$$
\boxed{
\sigma_n'
=
\sigma_n-u
}
$$ (eq-start-effective-normal)

In other words, "effective stress" originally refers to the whole tensor, and $\sigma_n'$ is the normal component of the effective stress on one particular surface. Pore water pressure acts equally in all directions, so it does not directly change the shear component of the traction.

:::{dropdown} Supplement D: the effective normal stress from the effective stress tensor
For the compression-positive total stress tensor, let

$$
\boldsymbol{\sigma}'^{(c)}
=
\boldsymbol{\sigma}^{(c)}-u\boldsymbol{I}
$$

Projecting this onto the direction of the unit normal vector $\boldsymbol{n}$ gives:

$$
\begin{aligned}
\sigma_n'
&=\boldsymbol{n}^{\mathsf T}
\boldsymbol{\sigma}'^{(c)}\boldsymbol{n}\\
&=\boldsymbol{n}^{\mathsf T}
(\boldsymbol{\sigma}^{(c)}-u\boldsymbol{I})\boldsymbol{n}\\
&=\boldsymbol{n}^{\mathsf T}
\boldsymbol{\sigma}^{(c)}\boldsymbol{n}
-u\boldsymbol{n}^{\mathsf T}\boldsymbol{n}\\
&=\sigma_n-u
\end{aligned}
$$

As in Supplement A, the actual traction is $\boldsymbol{t}=-\boldsymbol{\sigma}^{(c)}\boldsymbol{n}$. Substituting $\boldsymbol{\sigma}^{(c)}=\boldsymbol{\sigma}'^{(c)}+u\boldsymbol{I}$, the traction due to the $u\boldsymbol{I}$ part is

$$
-u\boldsymbol{I}\boldsymbol{n}=-u\boldsymbol{n}
$$

This traction always acts in the direction $-\boldsymbol{n}$, that is, it pushes on the sliding mass. For this reason, an isotropic pore water pressure has no shear component in the tangent plane.
:::

```{figure} ./figures/fig_c02_normal_shear_effective.svg
:name: fig-c02-normal-shear-effective
:alt: A diagram splitting the traction into the sum of a normal component and a shear component, and a diagram showing that the normal stress is the sum of the effective normal stress and the pore water pressure

Left: the traction $\boldsymbol{t}$ is the sum of the normal component $-\sigma_n\boldsymbol{n}$ and the shear component $\boldsymbol{\tau}$. Right: the normal stress $\sigma_n$ is the sum of the effective normal stress $\sigma_n'$ and the pore water pressure $u$. The values are from the example in Section 6
```

---

(section-5)=

## 5. Shear strength from the Mohr–Coulomb failure criterion

The Mohr–Coulomb failure criterion in terms of effective stress gives the **shear strength** $\tau_f$ that can be developed under the current effective normal stress $\sigma_n'$:

$$
\boxed{
\tau_f
=
c'+\sigma_n'\tan\phi'
=
c'+(\sigma_n-u)\tan\phi'
}
$$ (eq-start-mohr-coulomb)

$\tau_f$ is not the shear stress acting now. It is the upper limit of the shear resistance that can be developed at failure. For the same soil, a larger $\sigma_n'$ increases the frictional resistance between particles, and $\tau_f$ grows. Conversely, even with the same total normal stress $\sigma_n$, a rise in the pore water pressure $u$ lowers $\tau_f$, as follows.

$$
u\uparrow
\quad\Longrightarrow\quad
\sigma_n'\downarrow
\quad\Longrightarrow\quad
\tau_f\downarrow
$$ (eq-start-pore-pressure-effect)

---

(section-6)=

## 6. The factor of safety and the mobilized shear stress

In LEM, the factor of safety is the ratio of the available shear strength $\tau_f$ to the shear stress $\tau_m$ mobilized to maintain equilibrium.

$$
\boxed{
F_s=\frac{\tau_f}{\tau_m}
}
$$ (eq-start-fs-stress)

Solving this for $\tau_m$ and substituting Eq. {eq}`eq-start-mohr-coulomb` for $\tau_f$ gives:

$$
\boxed{
\tau_m
=
\frac{c'+(\sigma_n-u)\tan\phi'}{F_s}
}
$$ (eq-start-mobilized-stress)

As a vector, with its direction included, the shear component that resists sliding is:

$$
\boxed{
\boldsymbol{\tau}_m
=
-\frac{c'+(\sigma_n-u)\tan\phi'}{F_s}\boldsymbol{m}
}
$$ (eq-start-mobilized-vector)

```{note}
Eqs. {eq}`eq-start-mobilized-stress` and {eq}`eq-start-mobilized-vector` do not mean that the current $\tau_m$ is measured first and the ratio taken afterward. First, how much of the shear strength is mobilized is expressed in terms of the unknown $F_s$. Then $F_s$ and the other unknown forces are found together so that the mass loaded by this traction satisfies force and moment equilibrium.
```

```{figure} ./figures/fig_c03_strength_mobilization.svg
:name: fig-c03-strength-mobilization
:alt: A plot of shear stress against effective normal stress showing the Mohr–Coulomb line and the two states of the numerical example in Section 6

The Mohr–Coulomb line and the numerical example of Section 6. When the water level rises and $\sigma_n'$ drops from 60 kPa to 40 kPa, $\tau_f$ drops from 44.6 kPa to 33.1 kPa, and $F_s=\tau_f/\tau_m$ drops from 1.49 to 1.10
```

```{admonition} Working through the numbers
On a certain base, let the total normal stress be $\sigma_n=100$ kPa, the pore water pressure $u=40$ kPa, $c'=10$ kPa and $\phi'=30^\circ$. Then

$$
\sigma_n'=100-40=60\ \text{kPa},
\qquad
\tau_f=10+60\tan 30^\circ=44.6\ \text{kPa}
$$

If the shear stress needed to maintain equilibrium is $\tau_m=30$ kPa, the factor of safety is

$$
F_s=\frac{44.6}{30}=1.49
$$

Now suppose the water level rises so that $u=60$ kPa, while the $\tau_m$ needed for equilibrium stays the same. Then

$$
\sigma_n'=40\ \text{kPa},
\qquad
\tau_f=10+40\tan 30^\circ=33.1\ \text{kPa},
\qquad
F_s=\frac{33.1}{30}=1.10
$$

The strength parameters $c'$ and $\phi'$ of the soil have not changed at all, yet the factor of safety drops from 1.49 to 1.10. In other words, this checks numerically the relation $u\uparrow\Rightarrow\tau_f\downarrow$ from Section 5.
```

---

(section-7)=

## 7. From stress at a point to the resultant on a base with area

Let $S_i$ be the base of column $i$, and let its area be

$$
A_i=\int_{S_i}dA
$$ (eq-start-base-area)

The resultant of all the tractions on the base is given exactly by the following equation.

$$
\boxed{
\boldsymbol{R}_i
=
\int_{S_i}\boldsymbol{t}\,dA
}
$$ (eq-start-resultant)

The resultant of the compressive normal components of the traction and the resultant of the shear components that resist sliding can each be written as a vector, as follows.

$$
\boxed{
\boldsymbol{N}_i
=
-\int_{S_i}\sigma_n(\boldsymbol{x})\boldsymbol{n}(\boldsymbol{x})\,dA
}
$$ (eq-start-normal-resultant)

$$
\boxed{
\boldsymbol{T}_i
=
-\int_{S_i}\tau_m(\boldsymbol{x})\boldsymbol{m}(\boldsymbol{x})\,dA
}
$$ (eq-start-shear-resultant)

The equation for $\boldsymbol{R}_i$ is exact. By contrast, $\boldsymbol{T}_i$ can be written in the form of Eq. {eq}`eq-start-shear-resultant` only under the assumption that the shear component at every point points in the direction $-\boldsymbol{m}(\boldsymbol{x})$, that is, that the base is in the mobilized state of Section 6. Under this assumption,

$$
\boldsymbol{R}_i=\boldsymbol{N}_i+\boldsymbol{T}_i
$$ (eq-start-resultant-split)

holds.

On a curved surface, $\boldsymbol{n}$ varies from place to place. For this reason, the following inequality holds in general.

$$
\left\|\boldsymbol{N}_i\right\|
\le
\int_{S_i}\sigma_n\,dA
$$ (eq-start-resultant-bound)

Equality holds only in cases such as when the normal has the same direction over the whole base. In other words, the scalar obtained by simply adding up the magnitudes of the normal force at each point must be kept apart from the magnitude of the vector resultant, which accounts for direction.

:::{dropdown} Supplement E: vector resultants and scalar integrals on a curved surface
On a curved surface $S_i$, in general $\boldsymbol{n}=\boldsymbol{n}(\boldsymbol{x})$. The resultant of the compressive normal components of the traction, summed as vectors, is

$$
\boldsymbol{N}_i
=
-\int_{S_i}\sigma_n(\boldsymbol{x})
\boldsymbol{n}(\boldsymbol{x})\,dA
$$

On the other hand,

$$
N_i^*=\int_{S_i}\sigma_n\,dA
$$

is a scalar that simply adds up the magnitudes at each point. The triangle inequality gives

$$
\|\boldsymbol{N}_i\|
\le
N_i^*
$$

Equality holds only in cases such as when the normal has the same direction wherever $\sigma_n>0$.

If a representative normal $\boldsymbol{n}_i$ is assumed constant over the whole base, then

$$
\boldsymbol{N}_i
=
-\boldsymbol{n}_i\int_{S_i}\sigma_n\,dA
=
-N_i\boldsymbol{n}_i
$$

This links the scalar $N_i$ used in LEM to the vector resultant.
:::

```{figure} ./figures/fig_c04_surface_integration.svg
:name: fig-c04-surface-integration
:alt: The traction distributed over a curved base, the normal forces at each point added as vectors, and the LEM model that represents the base as a single plane

Left: the traction distributed over a curved base. Center: the resultant $\boldsymbol{N}_i$ of the normal forces at each point added as vectors is shorter than $\int_{S_i}\sigma_n\,dA$, which adds only the magnitudes. Right: LEM represents the base by one plane and one direction, and takes the magnitude of the normal force as $N_i=\int_{S_i}\sigma_n\,dA$
```

---

(section-8)=

## 8. $N_i$, $U_i$ and $T_i$ in LEM

LEM does not assume that the base $S_i$ of a slice or column is small. Instead, it assumes the following.

> **Within $S_i$, the directions ($\boldsymbol{n},\boldsymbol{m}$) and the material parameters ($c',\phi'$) are held constant at representative values, and the stress and pore water pressure are represented by their surface integrals $N_i,U_i$.**

For example, the directions are modeled as

$$
\boldsymbol{n}(\boldsymbol{x})=\boldsymbol{n}_i,
\qquad
\boldsymbol{m}(\boldsymbol{x})=\boldsymbol{m}_i
\qquad (\boldsymbol{x}\in S_i)
$$ (eq-start-representative-direction)

The scalars obtained by integrating the normal stress and the pore water pressure over the surface are then defined as follows.

$$
\boxed{
N_i=\int_{S_i}\sigma_n\,dA,
\qquad
U_i=\int_{S_i}u\,dA
}
$$ (eq-start-ni-ui)

The resultant normal force on the sliding mass can then be written as a vector, as follows.

$$
\boxed{
\boldsymbol{N}_i=-N_i\boldsymbol{n}_i
}
$$ (eq-start-ni-vector)

If $\sigma_n$ and $u$ are also assumed constant at representative values, then

$$
N_i=\sigma_{n,i}A_i,
\qquad
U_i=u_iA_i
$$ (eq-start-ni-uniform)

```{note}
When a reference writes $\boldsymbol{N}_i=N_i\boldsymbol{n}_i$, it uses a different convention for the direction of the normal. For example, it takes $\boldsymbol{n}_i$ in the direction in which the normal force acts.
```

Now suppose $c_i'$ and $\phi_i'$ are constant within $S_i$. Integrating the Mohr–Coulomb failure criterion over the surface gives the magnitude of the resultant available shear strength as follows.

$$
\boxed{
T_{f,i}
=
c_i'A_i+(N_i-U_i)\tan\phi_i'
}
$$ (eq-start-base-strength)

If, in addition, $F_s$ is common to the whole slip surface, the magnitude of the mobilized shear force is

$$
\boxed{
T_i
=
\frac{c_i'A_i+(N_i-U_i)\tan\phi_i'}{F_s}
}
$$ (eq-start-base-shear)

If $\boldsymbol{m}_i$ is constant within the base, the vector, including the direction that resists sliding, is:

$$
\boxed{
\boldsymbol{T}_i=-T_i\boldsymbol{m}_i
}
$$ (eq-start-base-shear-vector)

Note that the scalar equation $T_{f,i}=c_i'A_i+(N_i-U_i)\tan\phi_i'$ does not require the distributions of $\sigma_n$ and $u$ to be constant. If $c_i'$ and $\phi_i'$ are constant and $N_i$ and $U_i$ are defined by the integrals of Eq. {eq}`eq-start-ni-ui`, Eq. {eq}`eq-start-base-strength` holds.

:::{dropdown} Supplement F: integrating the Mohr–Coulomb failure criterion over the base
Suppose $c_i'$ and $\phi_i'$ are constant on the base $S_i$. The magnitude of the resultant available shear strength is found as follows.

$$
\begin{aligned}
T_{f,i}
&=\int_{S_i}\tau_f\,dA\\
&=\int_{S_i}
\left[c_i'+(\sigma_n-u)\tan\phi_i'\right]dA\\
&=c_i'\int_{S_i}dA
+\tan\phi_i'\int_{S_i}(\sigma_n-u)dA\\
&=c_i'A_i
+\left(
\int_{S_i}\sigma_n\,dA
-\int_{S_i}u\,dA
\right)\tan\phi_i'\\
&=c_i'A_i+(N_i-U_i)\tan\phi_i'
\end{aligned}
$$

Since $\sigma_n$ and $u$ are never set constant along the way, this scalar equation holds even when $\sigma_n$ and $u$ vary over the base. If, in addition, $F_s$ is constant on the base (the assumption of a common factor of safety), then

$$
T_i
=
\int_{S_i}\frac{\tau_f}{F_s}\,dA
=
\frac{T_{f,i}}{F_s}
$$

To simplify all the way to the vector equation $\boldsymbol{T}_i=-T_i\boldsymbol{m}_i$, the direction $\boldsymbol{m}$ that resists sliding must also be assumed constant within $S_i$.
:::

```{note}
In LEM practice, $A_i$ is not necessarily small. For this reason, the explanation "each base holds its directions and material parameters constant at representative values, and represents the stress by integrated values" fits practice better than the numerical-integration explanation "$S_i$ is small enough to be treated as constant." This assumption also includes a geometric approximation: a curved base is represented by one plane and one direction.
```

:::{dropdown} Supplement G: "the base is small enough" versus "constant at representative values"
The following two statements mean different things.

1. **As a numerical-integration argument**: if $S_i$ is made small enough, continuous quantities vary little over it, and approximating the integral with representative values becomes more accurate
2. **As an assumption of the LEM model**: whether $S_i$ is large or small, the base is represented by a representative normal, a representative direction of sliding, representative material parameters and so on

In LEM practice, $A_i$ is not necessarily small. For this reason, the main text uses the second explanation. For example, if the model assumes within $S_i$ that

$$
\boldsymbol{n}(\boldsymbol{x})=\boldsymbol{n}_i,
\qquad
\sigma_n(\boldsymbol{x})=\sigma_{n,i}
$$

then

$$
\boldsymbol{N}_i
=
-\int_{S_i}\sigma_{n,i}\boldsymbol{n}_i\,dA
=
-\sigma_{n,i}A_i\boldsymbol{n}_i
$$

holds exactly within that model. With respect to the actual directions and stress distribution on the curved surface, however, it is an approximation.

Dividing into finer columns can improve the approximation of the geometry and the integrals. That alone, however, does not remove the mechanical assumptions specific to LEM, such as the assumptions about interslice forces.
:::

---

(section-9)=

## 9. Equilibrium equations, and how LEM determines its unknowns

Even with the following equation in hand, $N_i$, $T_i$, $F_s$ and the {term}`interslice forces <interslice force>` and intercolumn forces are still unknown.

$$
T_i
=
\frac{c_i'A_i+(N_i-U_i)\tan\phi_i'}{F_s}
$$ (eq-start-strength-law-recap)

Let $\boldsymbol{W}_i$ be the weight of column $i$, $\boldsymbol{P}_i$ the other known external forces on it, and $\boldsymbol{Q}_{ij}$ the force it receives from a neighboring column $j$. Force equilibrium can then be written schematically as follows.

$$
\boxed{
\boldsymbol{W}_i+\boldsymbol{P}_i
-N_i\boldsymbol{n}_i
-T_i\boldsymbol{m}_i
+\sum_j\boldsymbol{Q}_{ij}
=\boldsymbol{0}
}
$$ (eq-start-force-balance)

Moment equilibrium about an arbitrary reference point $O$ is:

$$
\boxed{
\sum_k
\boldsymbol{r}_k\times\boldsymbol{F}_k
=\boldsymbol{0}
}
$$ (eq-start-moment-balance)

LEM finds $F_s$ and each resultant force by combining these force and moment equilibrium equations, the equation for strength mobilization, and the assumptions each method adds. Examples of such assumptions are ignoring the shear force between slices, assuming the direction of or a relation among interslice forces, and satisfying only some of the equilibrium equations. Methods such as those of Bishop, Janbu and Spencer differ in how they determine these unknowns.

In other words, discretization in LEM does not create new unknowns. It replaces the continuous stress distribution, which was unknown from the start, with a finite number of unknown resultant forces. Representing the surface integrals over the bases by a finite number of quantities is also a separate issue from determining, by assumption, the unknowns that the equilibrium equations alone cannot fix.

:::{dropdown} Supplement H: discretization, and how the unknowns are determined
On the slip surface,

$$
\sigma_n(\boldsymbol{x}),
\qquad
\boldsymbol{\tau}(\boldsymbol{x})
$$

are unknown continuous distributions even before discretization. Discretization in LEM replaces them with a finite number of unknown resultant forces on each base:

$$
N_i,
\qquad
T_i
$$

Discretization alone, however, does not determine $N_i$ or the interslice forces. This is because, in general, there are more unknowns than independent equilibrium equations. For this reason, the following two steps must be kept apart.

- **Spatial discretization**: representing the continuous geometry, loads and stress distribution by a finite number of slices or columns and resultant forces
- **Closure**: adding method-specific assumptions about the direction or ratio of the interslice forces, the components to ignore and so on, so that the unknown resultants can be determined. Chapter 2 covers this in detail

```{note}
It is not that "the stresses are unknown, so dividing finely will find them automatically." The unknown continuous distribution is first replaced with a finite number of unknowns, and then the equilibrium equations, the equation for strength mobilization and the added assumptions are solved together for $F_s$ and the resultant forces.
```
:::

The steps so far can be summarized as follows.

$$
\boxed{
\begin{array}{c}
\text{continuum stress field and equilibrium at each point}\\[1mm]
\boldsymbol{\sigma},\quad
\nabla\!\cdot\!\boldsymbol{\sigma}+\rho\boldsymbol{b}=\boldsymbol{0}
\\[2mm]
\downarrow\\[2mm]
\text{traction on the slip surface}\\[1mm]
\boldsymbol{t}=\boldsymbol{\sigma}\boldsymbol{n}
\\[2mm]
\downarrow\\[2mm]
\text{split into normal and shear components}\\[1mm]
\sigma_n,\quad\boldsymbol{\tau}
\\[2mm]
\downarrow\quad\text{effective stress}\\[2mm]
\sigma_n'=\sigma_n-u
\\[2mm]
\downarrow\quad\text{Mohr--Coulomb failure criterion}\\[2mm]
\tau_f=c'+\sigma_n'\tan\phi'
\\[2mm]
\downarrow\quad\text{factor of safety}\\[2mm]
\tau_m=\tau_f/F_s
\\[2mm]
\downarrow\quad\text{surface integrals and per-base modeling}\\[2mm]
N_i,\quad U_i,\quad T_i
\\[2mm]
\downarrow\quad\text{equilibrium equations and LEM-specific assumptions}\\[2mm]
F_s\ \text{and each resultant force}
\end{array}
}
$$ (eq-start-summary)

---

## Review questions

Click a question to see its answer.

:::{dropdown} Q1. How does the stress tensor differ from the traction on a given surface?
:icon: question

The stress tensor $\boldsymbol{\sigma}$ is a second-order tensor that describes the state of stress at a point, and it is defined without choosing a surface. The traction $\boldsymbol{t}$, by contrast, is the force vector per unit area on a surface with normal $\boldsymbol{n}$; it is found only once the orientation of the surface is chosen, as $\boldsymbol{t}=\boldsymbol{\sigma}\boldsymbol{n}$. At the same point, a different surface orientation gives a different traction. (→[Section 2](#section-2))
:::

:::{dropdown} Q2. In 2D, take $x$ horizontal and $z$ vertically upward. At a point on the slip surface, the components of the stress tensor, with tension positive and in the notation of the figure in Section 2, are $\sigma_{xx}=-60$ kPa, $\sigma_{zz}=-100$ kPa and $\tau_{xz}=0$. The outward unit normal vector at the point is $\boldsymbol{n}=(0.6,\,-0.8)$. Find the traction $\boldsymbol{t}$, the normal stress $\sigma_n$ and the magnitude of the shear component $\|\boldsymbol{\tau}\|$.
:icon: question

With $\boldsymbol{\sigma}=\begin{bmatrix}-60&0\\0&-100\end{bmatrix}$ kPa, $\boldsymbol{t}=\boldsymbol{\sigma}\boldsymbol{n}=(-60\times0.6,\ -100\times(-0.8))=(-36,\ 80)$ kPa. The normal component is $t_n=\boldsymbol{n}^{\mathsf T}\boldsymbol{t}=0.6\times(-36)+(-0.8)\times80=-85.6$ kPa, so $\sigma_n=-t_n=85.6$ kPa. The shear component is $\boldsymbol{\tau}=\boldsymbol{t}+\sigma_n\boldsymbol{n}=(15.36,\ 11.52)$ kPa, and $\|\boldsymbol{\tau}\|=19.2$ kPa. The surface is inclined at 36.9° from the horizontal. Mohr's circle from mechanics of materials, drawn with the principal stresses of 100 kPa and 60 kPa (compression positive), gives the same values. (→[Section 2](#section-2), [Section 3](#section-3))
:::

:::{dropdown} Q3. How is the effective normal stress $\sigma_n'$ determined from the total normal stress and the pore water pressure?
:icon: question

It is the total normal stress minus the pore water pressure, $\sigma_n'=\sigma_n-u$. It follows from projecting the effective stress tensor $\boldsymbol{\sigma}'^{(c)}=\boldsymbol{\sigma}^{(c)}-u\boldsymbol{I}$ onto the normal direction of the surface. (→[Section 4](#section-4))
:::

:::{dropdown} Q4. Is the $\tau_f$ given by the Mohr–Coulomb failure criterion the shear stress acting now, or something else?
:icon: question

Something else. $\tau_f$ is the upper limit of the shear resistance that can be developed at failure under the current effective normal stress. The stress acting now is the mobilized shear stress $\tau_m$, which is smaller than $\tau_f$ in a stable slope. (→[Section 5](#section-5), [Section 6](#section-6))
:::

:::{dropdown} Q5. The factor of safety $F_s$ was introduced as the ratio of what to what?
:icon: question

The ratio of the available shear strength $\tau_f$ to the shear stress $\tau_m$ mobilized to maintain equilibrium, $F_s=\tau_f/\tau_m$. Textbooks sometimes describe it as the ratio of resisting force to driving force, but what the ratio is taken between differs from method to method. For example, the simplified Bishop method takes a ratio of moments about the center of the circle. (→["Overview of LEM"](#overview), [Section 6](#section-6))
:::

:::{dropdown} Q6. On the base of "Working through the numbers" in Section 6, suppose the pore water pressure drops to $u=20$ kPa. Find the shear strength $\tau_f$ and the factor of safety $F_s$.
:icon: question

$\sigma_n'=100-20=80$ kPa, so $\tau_f=10+80\tan 30^\circ=56.2$ kPa. If $\tau_m=30$ kPa stays the same, $F_s=56.2/30=1.87$. When the pore water pressure drops, the effective normal stress rises, and so does the factor of safety. (→[Section 6](#section-6))
:::

:::{dropdown} Q7. In "Working through the numbers" in Section 6, $\tau_m=30$ kPa is given and $F_s$ is found from it. Does an actual LEM analysis also find $\tau_m$ on each base first and then compute $F_s$ as a ratio?
:icon: question

Not in general. Once the mass is divided into slices or columns, the equilibrium equations alone do not determine the $\tau_m$ on each base. So LEM expresses the mobilized shear stress in terms of the unknown $F_s$, as $\tau_m=\tau_f/F_s$. Then it finds $F_s$ and the other unknown forces together so that the mass loaded by this traction satisfies force and moment equilibrium. In a simple model where equilibrium alone determines $\tau_m$, such as the infinite slope, the ratio can be taken with a $\tau_m$ found first. (→[Section 6](#section-6), [Section 9](#section-9), [Practice 1, Section 2](#infinite-section-2))
:::

:::{dropdown} Q8. What operation on the pointwise stress produced $N_i$, $U_i$ and $T_i$?
:icon: question

Integration over the base $S_i$. $N_i$ is the surface integral of the total normal stress $\sigma_n$, and $U_i$ is that of the pore water pressure $u$. $T_i$ was found by integrating the Mohr–Coulomb failure criterion with $c_i'$ and $\phi_i'$ constant over the base, then dividing by the common factor of safety $F_s$. (→[Section 7](#section-7), [Section 8](#section-8))
:::

:::{dropdown} Q9. On a curved base, which is larger: the magnitude $\|\boldsymbol{N}_i\|$ of the resultant of the normal forces at each point, added as vectors, or $\int_{S_i}\sigma_n\,dA$, which adds only their magnitudes? Which of the two is LEM's $N_i$?
:icon: question

$\int_{S_i}\sigma_n\,dA$, which adds only the magnitudes, is larger. On a curved surface, the direction of the normal varies from place to place, so adding the forces as vectors cancels part of them. The two are equal only in cases such as when the normal has the same direction over the whole base. LEM's $N_i$, on the other hand, is the sum of the magnitudes. LEM applies it along a representative normal $\boldsymbol{n}_i$ and so represents the curved base by one plane and one direction. (→[Section 7](#section-7), [Section 8](#section-8))
:::

:::{dropdown} Q10. Which quantities must be assumed constant over the base $S_i$, and which need not be?
:icon: question

The scalar equation $T_{f,i}=c_i'A_i+(N_i-U_i)\tan\phi_i'$ requires the material parameters $c_i'$ and $\phi_i'$ to be constant. On the other hand, $\sigma_n$ and $u$ may vary over the base. $T_i=T_{f,i}/F_s$ also requires the assumption that $F_s$ is common over the base. The vector equations $\boldsymbol{N}_i=-N_i\boldsymbol{n}_i$ and $\boldsymbol{T}_i=-T_i\boldsymbol{m}_i$ also require $\boldsymbol{n}$ and $\boldsymbol{m}$, respectively, to be constant. (→[Section 8](#section-8))
:::

:::{dropdown} Q11. What is still unknown after obtaining the equation for $T_i$ in Section 8?
:icon: question

The base normal force $N_i$, the factor of safety $F_s$, and the interslice and intercolumn forces. $T_i$ follows once $N_i$ and $F_s$ are known. Determining them takes the equilibrium equations plus method-specific assumptions. (→[Section 9](#section-9))
:::

:::{dropdown} Q12. If the slices or columns are made finer and finer, do the assumptions about the interslice forces go away?
:icon: question

No. Finer division can improve the approximation of the geometry and the integrals. Discretization, however, replaces the unknown continuous stress distribution with a finite number of unknown resultant forces. Dividing more finely does not change the fact that there are more unknowns than equilibrium equations. So the method-specific assumptions that determine the unknowns are needed separately from discretization. (→[Section 8](#section-8), [Section 9](#section-9))
:::

---

## What to read next

This chapter has gone from the stress in a continuum to the base resultants used in LEM and the equation for strength mobilization. $N_i$, $F_s$, and the interslice and intercolumn forces, however, are still undetermined. The assumptions each method uses to determine them are covered in [Chapter 2, "What is the limit equilibrium method?"](what-is-limit-equilibrium-method.md).
