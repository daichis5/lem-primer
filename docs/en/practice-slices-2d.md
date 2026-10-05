---
title: "Computing the factor of safety of a circular slip with the method of slices: implement four methods and check equilibrium in one framework"
lang: en
series: "practice 2 of 3"
translated_from: "4396db4"
translated_on: 2026-10-05
---

# Computing the factor of safety of a circular slip with the method of slices

**Implement four methods and check equilibrium in one framework**

In this practice, you write code that computes the factor of safety of the slope and circle of Figure 1 of Chapter 1 with the 2D method of slices. First, you build a slice table and implement the Fellenius method, the simplified Bishop method and the simplified Janbu method exactly as the textbook formulas state them. Next, you build one framework in which the inclination of the interslice forces is a variable. With this framework, you check by residuals that the simplified Bishop and simplified Janbu methods are special cases of it, and that the Spencer method satisfies both force and moment equilibrium. Finally, on a slip surface that is not a circle, you see that the choice of the center of moments changes the factor of safety.

This practice assumes that you have read [Chapter 2](what-is-limit-equilibrium-method.md) and [Chapter 3](lem-in-practice-mechanical-perspective.md) and finished [Practice 1](practice-infinite-slope.md). The terms and symbols are collected in the [Glossary](lem-glossary.md).

(slices-goal)=

## What you build

The slope is the same as in Figure 1 of Chapter 1. The toe is at $x=0$ and the crest at $x=15$ m. The slope is 10 m high (a gradient of 1:1.5), and the ground stays flat to the right of the crest. The {term}`slip surface` is a circular arc with center $(6, 18)$ and radius 19.31 m. The arc leaves the ground at $x=-1$ m, left of the toe, and enters it at $x=23.58$ m, right of the crest. The soil is the same as in [Practice 1](practice-infinite-slope.md): $\gamma=18$ kN/m³, $c'=10$ kPa and $\phi'=30^\circ$. The slope is dry, except in the second half of Section 5, where a water table is added. On this basis, you compute the {term}`factor of safety` of this circle with four methods.

```{figure} ./figures/fig_c00_slope_overview.svg
:name: fig-slices-slope-overview
:alt: The circular slip surface assumed in the slope, the sliding mass, six slices, and the weight, normal force and shear force on one slice

The slope and circle computed in this practice. They are the same as in Figure 1 of Chapter 1, and the mass slides to the left. The six slices of the figure give the table of Section 1
```

The coordinates and directions are the same as in Practice 1. The $x$ axis points horizontally to the right and the $z$ axis vertically upward. The unit normal vector $\boldsymbol{n}_i$ of a base points out of the {term}`sliding mass`. The unit vector in the direction of sliding is $\boldsymbol{m}_i$. Lengths are in m, and forces are in kN per meter of depth (kN/m). You build the following.

| Functions and classes | What they compute | Section |
|---|---|---|
| `ground`, `Circle`, `Slices`, `make_slices` | The ground surface, the circular slip surface and the slice table | Section 1 |
| `cross` | The cross product of 2D vectors | Section 1 |
| `fellenius`, `bishop`, `janbu` | The factor of safety of the three methods, from the textbook formulas | Section 2 |
| `base_forces`, `residuals` | The base forces under interslice forces inclined at $\theta$, and the residuals of equilibrium | Section 3 |
| `secant`, `fs_moment`, `fs_force` | The secant method, and the factor of safety that makes the moment or force residual zero | Section 3 |
| `spencer` | The factor of safety and $\theta$ that make both the force and moment residuals zero | Section 4 |
| `Line` | A planar slip surface | Section 6 |
| `Ellipse`, `fellenius_about` | An elliptical slip surface, and the Fellenius factor of safety from moments about any point | Section 7 |

(slices-setup)=

## Setup

Use the folder `lem-practice` that you made in [Practice 1](practice-infinite-slope.md). The code of this practice is in {download}`slices.py <examples/slices.py>` and {download}`test_slices.py <examples/test_slices.py>`. The tests and Section 6 import `infinite_slope.py` from Practice 1. If you did not start with Practice 1, put {download}`infinite_slope.py <examples/infinite_slope.py>` in the same folder as well.

---

(slices-section-1)=

## 1. Build the slice table

Divide the slip surface into $n$ {term}`slices <slice>` of equal width, and represent the base of each slice by the point at the middle of its width and the tangent there. In the words of [Chapter 1, Section 8](#section-8), this assumes that the orientation of each base is constant at a representative value. The base inclination $\alpha_i$ is positive when the base rises to the right, and a base with positive $\alpha_i$ makes the mass slide to the left. The normal and the direction of sliding then take the same form as the equation of Practice 1.

$$
\boldsymbol{n}_i=
\begin{bmatrix}
\sin\alpha_i\\
-\cos\alpha_i
\end{bmatrix},
\qquad
\boldsymbol{m}_i=
\begin{bmatrix}
-\cos\alpha_i\\
-\sin\alpha_i
\end{bmatrix}
$$ (eq-slices-vectors)

With width $b_i$, the length of the base is $l_i=b_i/\cos\alpha_i$. The weight $W_i$ is the height of the slice at the middle of its width, times $\gamma b_i$. Create `slices.py`, and first write the ground surface of the slope and the circular slip surface.

```{literalinclude} examples/slices.py
:language: python
:end-at: return np.clip
```

```{literalinclude} examples/slices.py
:language: python
:pyobject: Circle
```

Next, write the slice table. Every quantity is a NumPy array ordered from the leftmost slice. `@dataclass` is a short way to write a container with named fields.

```{literalinclude} examples/slices.py
:language: python
:pyobject: Slices
```

```{literalinclude} examples/slices.py
:language: python
:pyobject: make_slices
```

When a water table `water_level` is given, the {term}`pore water pressure` on a base is the hydrostatic pressure at the depth measured vertically from the water table. This is the same rule as `"vertical"` in `pore_pressure` of Practice 1. Where the water table is above the ground surface, the water table is set to the ground surface, and water above the ground is ignored. The unit weight of the soil stays $\gamma$ below the water table too. This is so that Section 5 isolates the effect of the pore water pressure alone.

With the six slices of Figure 1, the table is as follows. The output shown in this practice comes from `run_slices.py`, which you run at the end of Section 7.

```{literalinclude} examples/output/run_slices.txt
:language: text
:start-at: 1. slice table
:end-before: 2. factor of safety
```

Check the third slice by hand. With one more digit than the table, the width is $b=4.0964$ m and the middle of the width is at $x=9.241$ m. The ground is at height $9.241\times10/15=6.161$ m and the circle at $-1.039$ m, so $W=18\times4.0964\times(6.161+1.039)=530.9$ kN/m. The inclination follows from $\tan\alpha=(9.241-6)/(18+1.039)=0.170$ as $9.66^\circ$.

The last line shows that, on every base, the magnitude of the cross product of the position vector $\boldsymbol{r}_i$ from the center of the circle to the base point and the normal $\boldsymbol{n}_i$ is below $10^{-12}$ m. This is only the size of rounding error, so the line of action of every {term}`base normal force` passes through the center. This is the property peculiar to a circle that [Chapter 3, Section 2](#practice-section-2) described. Write these two checks as tests. Create `test_slices.py` and write the following.

```{literalinclude} examples/test_slices.py
:language: python
:end-at: import slices
```

```{literalinclude} examples/test_slices.py
:language: python
:pyobject: test_the_slice_table_by_hand
```

```{literalinclude} examples/test_slices.py
:language: python
:pyobject: test_on_a_circle_every_normal_passes_through_the_centre
```

`cross` computes the cross product of 2D vectors. Sections 3 and 7 also use it. Add it to `slices.py`.

```{literalinclude} examples/slices.py
:language: python
:pyobject: cross
```

---

(slices-section-2)=

## 2. Implement the three formulas

Implement the three {term}`simplified methods <simplified method>` of [Chapter 2, Section 4](#what-section-4) exactly as the textbook formulas state them. Each of them ignores or simplifies the shear forces between slices. The Fellenius method (ordinary method of slices) ignores every effect of the {term}`interslice forces <interslice force>` and takes the ratio of moments about the center of the circle.

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
$$ (eq-slices-fellenius)

Here $U_i=u_il_i$ is the {term}`pore water force on the base`. The simplified Bishop method (Bishop, 1955) finds $N_i$ from the vertical force equilibrium of each slice, and takes the ratio of moments about the center of the circle. Since $F_s$ also appears on the right-hand side, the value is found by iteration.

$$
F_s
=
\frac{
\displaystyle\sum_i
\frac{
c_i'b_i+(W_i-u_i b_i)\tan\phi_i'
}{
m_{\alpha,i}
}
}{
\displaystyle\sum_i W_i\sin\alpha_i
},
\qquad
m_{\alpha,i}=\cos\alpha_i+\frac{\sin\alpha_i\tan\phi_i'}{F_s}
$$ (eq-slices-bishop)

The simplified Janbu method (Janbu, 1973), without its correction factor, uses the same $N_i$ and finds $F_s$ from the overall horizontal force equilibrium.

$$
F_s
=
\frac{
\displaystyle\sum_i
\frac{
c_i'b_i+(W_i-u_i b_i)\tan\phi_i'
}{
\cos\alpha_i\,m_{\alpha,i}
}
}{
\displaystyle\sum_i W_i\tan\alpha_i
}
$$ (eq-slices-janbu)

Write the three as functions `fellenius(s)`, `bishop(s)` and `janbu(s)`, where `s` is the slice table of Section 1. Give `fellenius` the keyword argument `effective_weight`, which Section 5 uses. When it is `True`, the effective normal force is $(W_i-u_ib_i)\cos\alpha_i$ instead of $W_i\cos\alpha_i-u_il_i$. In the iteration, compute the right-hand side with the previous $F_s$, and stop when the change in value is small enough. On a slice where $m_{\alpha,i}$ is zero or negative, $N_i$ becomes infinite or changes sign and has no meaning. In that case, stop the computation and report it. When the functions are written, check them with the following test.

```{literalinclude} examples/test_slices.py
:language: python
:pyobject: test_the_three_formulas_on_the_circle_of_figure_1
```

:::{dropdown} Example implementation
```{literalinclude} examples/slices.py
:language: python
:pyobject: fellenius
```

```{literalinclude} examples/slices.py
:language: python
:pyobject: bishop
```

```{literalinclude} examples/slices.py
:language: python
:pyobject: janbu
```
:::

The table of Section 5 collects the values for other numbers of slices. With $n=50$, the Fellenius method gives 1.888, the simplified Bishop method 2.063 and the simplified Janbu method 1.868.

---

(slices-section-3)=

## 3. Put the methods in one framework, with the inclination of the interslice forces as a variable

The three formulas of Section 2 look as if each method were derived on its own. As [Chapter 2, Section 3.3](#what-section-3-3) showed, however, the methods differ in how they achieve {term}`closure`. Fredlund and Krahn (1977) used this view to put the 2D methods in one framework and compare them. This practice, too, takes the assumption of the Spencer method from [Chapter 2, Section 5.1](#what-section-5-1) and keeps it as a variable. The resultant $Q_i$ of the interslice forces on each slice is assumed to have the same direction on every slice:

$$
\boldsymbol{d}=
\begin{bmatrix}
\cos\theta\\
\sin\theta
\end{bmatrix}
$$ (eq-slices-direction)

Here $\theta$ is the inclination of the resultant, measured from the horizontal.

The forces on slice $i$ are the weight $W_i$, the base normal force $-N_i\boldsymbol{n}_i$, the {term}`base shear force` $T_i\boldsymbol{e}_i$ and the resultant interslice force $Q_i\boldsymbol{d}$. Here $\boldsymbol{e}_i=-\boldsymbol{m}_i$ is the direction that resists sliding. $T_i$ is tied to $N_i$ by the equation for the mobilization of strength in [Chapter 1, Section 8](#section-8).

$$
T_i=\frac{c_i'l_i+(N_i-U_i)\tan\phi_i'}{F_s}
$$ (eq-slices-shear)

Force equilibrium in the direction $\boldsymbol{p}=(-\sin\theta,\ \cos\theta)$, perpendicular to $\boldsymbol{d}$, removes $Q_i$ from the equation. Solving it for $N_i$ gives the following.

$$
N_i=
\frac{
W_i\cos\theta
-\left(c_i'l_i-U_i\tan\phi_i'\right)(\boldsymbol{e}_i\cdot\boldsymbol{p})/F_s
}{
D_i
},
\qquad
D_i=-\boldsymbol{n}_i\cdot\boldsymbol{p}
+\frac{\tan\phi_i'}{F_s}\,\boldsymbol{e}_i\cdot\boldsymbol{p}
$$ (eq-slices-normal)

When $\theta=0$, $\boldsymbol{p}$ points vertically upward, and $D_i$ equals $m_{\alpha,i}$ of Eq. {eq}`eq-slices-bishop`. In other words, Eq. {eq}`eq-slices-normal` extends the $N_i$ of the simplified Bishop method to inclined interslice forces. On the other hand, if $\boldsymbol{d}$ of each slice is taken parallel to its base ($\theta$ set to $\alpha_i$ slice by slice), then $D_i=1$ and $N_i=W_i\cos\alpha_i$. This is the $N_i$ of the Fellenius method. Since its $\theta$ differs from slice to slice, the Fellenius method does not fit this framework, which fixes a single $\theta$.

```{literalinclude} examples/slices.py
:language: python
:pyobject: base_forces
```

Equilibrium in the other direction, $\boldsymbol{d}$, gives $Q_i$. The interslice forces are {term}`internal forces <internal force>`, so they cancel over the whole mass. Force equilibrium of the whole mass is therefore the same as $\sum_i Q_i=0$. In this table, the weight also acts on the vertical line through the base point. The moment of the weight and the base forces of slice $i$ about a point $O$ then sums to $-\boldsymbol{r}_i\times Q_i\boldsymbol{d}$, where $\boldsymbol{r}_i$ is the position vector from $O$ to the base point. In other words, moment equilibrium about $O$ is the same as $\sum_i \boldsymbol{r}_i\times Q_i\boldsymbol{d}=\boldsymbol{0}$. These two sums are called the force residual and the moment residual.

```{literalinclude} examples/slices.py
:language: python
:pyobject: residuals
```

Once $\theta$ is fixed, the residuals are functions of $F_s$ alone. Write $F_m(\theta)$ for the $F_s$ that makes the moment residual zero, and $F_f(\theta)$ for the $F_s$ that makes the force residual zero. Find both with the secant method. The secant method is an iteration that takes, as the next point, the zero of the straight line through two points. It amounts to Newton's method with the derivative replaced by a difference.

```{literalinclude} examples/slices.py
:language: python
:pyobject: secant
```

```{literalinclude} examples/slices.py
:language: python
:pyobject: fs_moment
```

```{literalinclude} examples/slices.py
:language: python
:pyobject: fs_force
```

Compare them with the formulas of Section 2 at $\theta=0$.

```{literalinclude} examples/output/run_slices.txt
:language: text
:start-at: 3. one framework
:end-before: 4. F_m and F_f
```

$F_m(0)$ agrees with the simplified Bishop method, and $F_f(0)$ with the simplified Janbu method without its correction factor, to six digits. The framework at $\theta=0$ takes the interslice forces as horizontal and finds $N_i$ from the vertical equilibrium of each slice. On that basis, the simplified Bishop method satisfies overall moment equilibrium, and the simplified Janbu method overall horizontal force equilibrium. The two methods differ only in which overall equilibrium they satisfy. Add this to the tests.

```{literalinclude} examples/test_slices.py
:language: python
:pyobject: test_theta_zero_gives_simplified_bishop_and_janbu
```

---

(slices-section-4)=

## 4. The Spencer method: satisfy both force and moment equilibrium

Find $F_m(\theta)$ and $F_f(\theta)$ while varying $\theta$.

```{literalinclude} examples/output/run_slices.txt
:language: text
:start-at: 4. F_m and F_f
:end-before: 5. water table
```

```{figure} ./figures/fig_e2_theta_curves.svg
:name: fig-e2-theta-curves
:alt: Two curves of the factor of safety from moment equilibrium and from force equilibrium, plotted against the inclination of the resultant interslice force, with the points of the simplified Bishop, simplified Janbu and Spencer methods

The inclination $\theta$ of the resultant interslice force, and the factors of safety from the two equilibrium conditions. $F_m$ at $\theta=0$ is the simplified Bishop method and $F_f$ the simplified Janbu method; the point where the two curves cross is the solution of the Spencer method
```

Where the two curves cross, the same $F_s$ and $\theta$ make both the force and moment residuals zero. This is the solution of the Spencer method (Spencer, 1967) of [Chapter 2, Section 5.1](#what-section-5-1). The crossing is found by solving $F_m(\theta)-F_f(\theta)=0$ for $\theta$ with the secant method. Write `spencer(s, center)` and check it with a test.

```{literalinclude} examples/test_slices.py
:language: python
:pyobject: test_spencer_satisfies_both_force_and_moment_equilibrium
```

:::{dropdown} Example implementation
```{literalinclude} examples/slices.py
:language: python
:pyobject: spencer
```
:::

The crossing is at $\theta=18.27^\circ$ and $F_s=2.059$. The figure shows that $F_m$ barely changes with $\theta$, while $F_f$ changes a lot. This is because, on a circle, moment equilibrium is little affected by the assumption on the interslice forces, as [Chapter 3, Section 2](#practice-section-2) showed. About the center of the circle, the base normal forces have zero moment and every shear force has the radius as its lever arm, so $\theta$ enters $F_m$ only through $N_i\tan\phi_i'$. For this reason, the simplified Bishop method (2.063) and the Spencer method (2.059) are close. The simplified Janbu method (1.868), which uses force equilibrium alone, is farther from the Spencer method. The Fellenius method (1.888), which ignores every effect of the interslice forces, also gives a lower value.

---

(slices-section-5)=

## 5. Change the number of slices and the water table

As the number of slices $n$ changes, the four methods give the following values.

```{literalinclude} examples/output/run_slices.txt
:language: text
:start-at: 2. factor of safety
:end-before: 3. one framework
```

Beyond $n=50$, no method changes much in the first three digits. Even with the six slices of Figure 1, the values differ by only about 2%. As [Chapter 3, Section 11.5](#practice-section-11-5) showed, check that the values settle as the number of slices changes before comparing methods.

Next, put the water table on the horizontal line $z=4$ m. As decided in Section 1, the soil below the water table also keeps $\gamma=18$ kN/m³.

```{literalinclude} examples/output/run_slices.txt
:language: text
:start-at: 5. water table
:end-before: 6. slices with
```

Every method's value drops by about 25% from the dry case. The two values of the Fellenius method differ in how they approximate the effective normal force $N_i'$ on the base. The first is $W_i\cos\alpha_i-u_il_i$, the normal component of the weight minus the pore water force $U_i=u_il_i$. The second uses $(W_i-u_ib_i)\cos\alpha_i$, the effective weight (the weight minus $u_ib_i$) resolved in the direction normal to the base. The latter equals $W_i\cos\alpha_i-u_il_i\cos^2\alpha_i$, so it subtracts $U_i\cos^2\alpha_i$ instead of the resultant $U_i$. As a result, the steeper the base, the more it underestimates the effect of the pore water pressure, and the larger the value. The two are not two ways of writing the same quantity but different approximations. When you compare with another implementation, you must check which approximation it uses.

Finally, as in [Chapter 3, Section 5.2](#practice-section-5-2), check the effective normal force $N_i-U_i$ on the bases as well as the factor of safety. The output shows the $x$ of the slices where it is negative, for the dry slope and the slope with the water table.

```{literalinclude} examples/output/run_slices.txt
:language: text
:start-at: 6. slices with
:end-before: 7. a plane
```

Every negative value is on the rightmost slice. This slice has a steep base and little soil above it. For this reason, in the numerator of Eq. {eq}`eq-slices-normal`, the term of the shear force due to cohesion outweighs the term of the weight. In the simplified Bishop method at $\theta=0$, its vertical component $c_i'l_i\sin\alpha_i/F_s$ is larger than the weight $W_i$, as the last line of the output shows. The $N_i=W_i\cos\alpha_i$ of the Fellenius method has no such term. This code uses the negative values as they are. However, as [Practice 1, Section 5](#infinite-section-5) showed, a negative effective normal force means that the soil is in tension. Its treatment, such as adding a tension crack or cutting the contact, must therefore be decided separately ([Chapter 3, Section 12.1](#practice-section-12-1)).

---

(slices-section-6)=

## 6. Compare a planar slip surface with the infinite slope

Under a planar ground surface inclined at $30^\circ$, put a parallel slip surface at a vertical depth of 5 m, and divide it into eight slices. `Line` is the planar slip surface for this.

```{literalinclude} examples/slices.py
:language: python
:pyobject: Line
```

```{literalinclude} examples/output/run_slices.txt
:language: text
:start-at: 7. a plane
:end-before: 8. an ellipse
```

All three methods agree with the value 1.2566 of the {term}`infinite slope` of Practice 1. Every slice has the same shape, so each slice is in equilibrium on its own, like the columns of Practice 1. In other words, $Q_i=0$ on every slice, and the value does not change whatever is assumed about the interslice forces. For the same reason, the $\theta$ of the Spencer method is not determined on this surface. This is because, at any $\theta$, $F_s=1.2566$ makes both residuals zero. Add this agreement to the tests.

```{literalinclude} examples/test_slices.py
:language: python
:pyobject: test_a_plane_under_a_planar_slope_gives_the_infinite_slope
```

---

(slices-section-7)=

## 7. Slip surfaces other than circles, and the center of moments

Consider an elliptical slip surface through the same exit, $x=-1$. Its center is $(6, 18)$, the same as the circle's, and its vertical semi-axis is 20 m.

```{literalinclude} examples/slices.py
:language: python
:pyobject: Ellipse
```

```{literalinclude} examples/output/run_slices.txt
:language: text
:start-at: 8. an ellipse
:end-before: 9. moving
```

The first line is Eq. {eq}`eq-slices-bishop` with the base angles of the ellipse put in. The second line, by contrast, makes the moment residual about the center $(6, 18)$ zero in the framework of Eq. {eq}`eq-slices-normal`. The two correspond to the two readings of "computed a non-circular surface with Bishop" in [Chapter 3, Section 5.1](#practice-section-5-1), and they differ by 4%, 1.994 against 1.922. The circle formula is derived from three facts: the line of action of each base normal force passes through the center, every shear force has the radius $R$ as its lever arm, and the lever arm of the weight is $R\sin\alpha_i$. On an ellipse, none of the three holds. The first two are as [Chapter 3, Section 3](#practice-section-3) showed. For the Fellenius method, too, Eq. {eq}`eq-slices-fellenius` gives 1.733, and going back to moments about the center gives 1.803. The latter, `fellenius_about`, also includes the moment of the base normal force $N_i=W_i\cos\alpha_i$.

```{literalinclude} examples/slices.py
:language: python
:pyobject: fellenius_about
```

Add a test that `fellenius_about`, taken about the center of a circle, reduces to Eq. {eq}`eq-slices-fellenius`.

```{literalinclude} examples/test_slices.py
:language: python
:pyobject: test_fellenius_about_the_centre_of_a_circle_is_the_formula
```

Next, move the {term}`center of moments` from $(6, 18)$ up by 7 m and to the right by 4 m.

```{literalinclude} examples/output/run_slices.txt
:language: text
:start-at: 9. moving
```

The Fellenius method changes value whichever way the center moves. The simplified Bishop method changes when the center moves up, but not when it moves to the right. The Spencer method does not change either way. The equation of [Chapter 3, Section 6](#practice-section-6) explains this difference. Moving the center by $\boldsymbol{a}$ changes the moment by $-\boldsymbol{a}\times\sum\boldsymbol{F}$, where $\sum\boldsymbol{F}$ is the force left over on the whole mass.

- The Spencer method satisfies force equilibrium, so $\sum\boldsymbol{F}=\boldsymbol{0}$, and the value does not change wherever the center moves
- The simplified Bishop method satisfies the vertical equilibrium of each slice and takes the interslice forces as horizontal. The leftover force $\sum\boldsymbol{F}$ is therefore horizontal, and $\boldsymbol{a}\times\sum\boldsymbol{F}=\boldsymbol{0}$ only when the center moves horizontally
- The Fellenius method satisfies, on each slice, only equilibrium in the direction normal to the base. That direction differs from slice to slice, so $\sum\boldsymbol{F}$ keeps both a vertical and a horizontal component, and the value changes whether the center moves up or to the right

On a circle, choosing the center of the circle keeps this question of choice mostly out of sight. On other surfaces, however, the less a method satisfies force equilibrium, the more the choice of the center of moments shows in its value. In 3D, the same happens with methods that fix an axis of rotation and a reference point. Add this to the tests.

```{literalinclude} examples/test_slices.py
:language: python
:pyobject: test_the_moment_centre_matters_only_where_force_equilibrium_is_missing
```

You now have every function that `run_slices.py` uses. Download {download}`run_slices.py <examples/run_slices.py>`, put it in `lem-practice` and run it.

```bash
uv run python run_slices.py
```

If it prints the same values as the output shown in this practice, your functions so far are correct. Finally, run `uv run pytest` and check that the tests of this practice and of Practice 1 all pass.

---

(slices-trouble)=

## Troubleshooting

| What you see | Cause and fix |
|---|---|
| `ValueError: m_alpha is zero or negative for some slice` | $F_s$ became too small during the iteration, or a slice near the exit has a base that rises steeply. Make the initial value `fs` larger, or revise the shape of the slip surface. (→[Section 2](#slices-section-2)) |
| `ValueError: D is zero or negative for some slice; check F_s and theta` | The secant method tried an $F_s$ that is too small or a $\theta$ that is too large. Set the initial value of `fs` near the value of the simplified Bishop method. (→[Section 3](#slices-section-3)) |
| `RuntimeError: secant method: the two points have the same value` | At the two points of the secant method, the equation being solved has the same value. This happens when you use `spencer` on a planar slip surface, where $F_m(\theta)-F_f(\theta)$ is zero at every $\theta$. (→[Section 6](#slices-section-6)) |
| `TypeError: fellenius() got an unexpected keyword argument 'effective_weight'` | `fellenius` lacks the argument `effective_weight`, which Section 5 uses. (→[Section 2](#slices-section-2)) |
| `ModuleNotFoundError: No module named 'infinite_slope'` | `infinite_slope.py` from Practice 1 is not in the same folder. (→[Setup](#slices-setup)) |
| The values differ slightly from the table | Check the number of slices $n$, and that the base point is at the middle of the width. Compute the weight from the height at the middle of the width, too. (→[Section 1](#slices-section-1)) |

## Summary

- The slice table consists of the base point, inclination, normal and direction of sliding, length, weight and pore water pressure of each base. On a circle, the normal of every base passes through the center (→[Section 1](#slices-section-1))
- The Fellenius, simplified Bishop and simplified Janbu methods can be implemented exactly as the textbook formulas state them. In the last two, $F_s$ also appears on the right-hand side, so the value is found by iteration (→[Section 2](#slices-section-2))
- With the inclination $\theta$ of the resultant interslice force as a variable, one equation gives the $N_i$ of each slice. At $\theta=0$, making the moment residual zero gives the simplified Bishop method, and making the force residual zero gives the simplified Janbu method (→[Section 3](#slices-section-3))
- The crossing of $F_m(\theta)$ and $F_f(\theta)$ is the solution of the Spencer method, where both the force and moment residuals are zero. On a circle, $F_m$ hardly depends on $\theta$, so the simplified Bishop and Spencer methods are close (→[Section 4](#slices-section-4))
- Check that the values settle as the number of slices grows before comparing methods. Besides the factor of safety, check that no base has a negative effective normal force. With a water table, the Fellenius value also depends on how the effective normal force is approximated (→[Section 5](#slices-section-5))
- On a planar slip surface, every method agrees with the infinite slope value. This is because each slice is in equilibrium on its own (→[Section 6](#slices-section-6))
- On surfaces other than circles, the less a method satisfies force equilibrium, the more the choice of the center of moments shows in its value (→[Section 7](#slices-section-7))

---

## Review questions

Click a question to see its answer. Do the (Try it) questions in `lem-practice`.

:::{dropdown} Q1. How did the code check that the base normal forces do not appear in the equation of moments about the center of a circle?
:icon: question

It checked that, on every slice, the cross product of the position vector $\boldsymbol{r}_i$ from the center of the circle to the base point and the base normal $\boldsymbol{n}_i$ is only the size of rounding error. Since the cross product is zero, the line of action of each base normal force passes through the center and has no moment about it. (→[Section 1](#slices-section-1))
:::

:::{dropdown} Q2. (Try it) For the six slices of Figure 1, find $m_{\alpha,i}$ of each slice at the solution of the simplified Bishop method. Which slice has the smallest?
:icon: question

Compute `s = make_slices(Circle(), 6)` and `fs = bishop(s)`. Then compute `np.cos(s.alpha) + np.sin(s.alpha) * s.tan_phi / fs`. From left to right, the values are 0.894, 0.987, 1.033, 1.032, 0.973 and 0.822. The smallest is the sixth slice, whose base is steepest ($\alpha=53.5^\circ$). The first slice, on the exit side, has a gentle base ($\alpha=-14.9^\circ$), so its value stays at 0.894. $m_{\alpha,i}$ approaches zero when a base near the exit rises steeply ($\alpha_i$ a large negative value). (→[Section 2](#slices-section-2))
:::

:::{dropdown} Q3. In the framework at $\theta=0$, why does making the moment residual zero give the same value as the simplified Bishop method?
:icon: question

Because at $\theta=0$, $\boldsymbol{p}$ is vertical, and the vertical equilibrium of each slice gives the same $N_i$ as the simplified Bishop method. On that basis, making the moment residual zero means satisfying moment equilibrium of the whole mass about the center of the circle. This is the same equilibrium that the simplified Bishop method uses. (→[Section 3](#slices-section-3))
:::

:::{dropdown} Q4. (Try it) Find the force residual at the solution of the simplified Bishop method with $n=50$. What does it represent?
:icon: question

The first value of `residuals(s, bishop(s), 0.0, (6.0, 18.0))` is the force residual, 86.7 kN/m. This is 3.6% of the total weight of the mass, 2415.6 kN/m. It shows that the simplified Bishop method does not satisfy overall horizontal force equilibrium. The $Q_i$ of each slice is the difference between the interslice normal forces on its two sides. Summed from the left, they do not return to zero at the right end. (→[Section 3](#slices-section-3))
:::

:::{dropdown} Q5. (Try it) With $\phi'=25^\circ$, what are the values of the four methods, and in what order?
:icon: question

Build the table with `make_slices(Circle(), 50, phi_deg=25.0)`. The values are Fellenius method 1.594, simplified Bishop method 1.734, simplified Janbu method 1.575 and Spencer method 1.731 ($\theta=17.9^\circ$). From smallest to largest, the order is the simplified Janbu, Fellenius, Spencer and simplified Bishop methods, the same as with $\phi'=30^\circ$. Every value is about 0.84 times its value at $\phi'=30^\circ$. The drop is smaller than the ratio of $\tan\phi'$, 0.81, because the resistance due to cohesion does not change. (→[Section 2](#slices-section-2), [Section 4](#slices-section-4))
:::

:::{dropdown} Q6. Why is the $\theta$ of the Spencer method not determined on a planar slip surface?
:icon: question

Because every slice has the same shape, and each slice is in equilibrium on its own. $Q_i=0$ on every slice, and at any $\theta$, $F_s=1.2566$ makes both the force and moment residuals zero. (→[Section 6](#slices-section-6))
:::

:::{dropdown} Q7. On the elliptical slip surface, why does the simplified Bishop value not change when the center of moments moves to the right?
:icon: question

Because the simplified Bishop method satisfies the vertical equilibrium of each slice and takes the interslice forces as horizontal. The force $\sum\boldsymbol{F}$ left over on the whole mass is then horizontal. When the center moves horizontally, the shift $\boldsymbol{a}$ is parallel to $\sum\boldsymbol{F}$, and the change in moment $-\boldsymbol{a}\times\sum\boldsymbol{F}$ is zero. When the center moves up, $\boldsymbol{a}$ is not parallel to $\sum\boldsymbol{F}$, so the value changes. (→[Section 7](#slices-section-7))
:::

:::{dropdown} Q8. (Try it) Move the center of the circle to $(4, 16)$ and find the simplified Bishop $F_s$ of the circle through the same exit, $x=-1$. Is the circle of this practice the critical slip surface?
:icon: question

`bishop(make_slices(Circle((4.0, 16.0)), 50))` is 1.790, smaller than the circle of this practice (2.063). So the circle of this practice is not the {term}`critical slip surface`. The critical slip surface is known only after computing the factor of safety of many circles, with different centers and exits, and searching for the smallest. Computing the factor of safety and searching for the critical slip surface are separate problems. (→[Chapter 3, Section 12.4](#practice-section-12-4))
:::

---

## What to read next

In this practice, you checked by residuals, on 2D slices, that the methods differ in how they achieve closure. In 3D, the sliding mass is divided into {term}`columns <column>`, and the direction of the base shear force and the axis of rotation must be decided anew. In [Practice 3, "Computing the factor of safety of a 3D slip surface with the method of columns"](practice-columns-3d.md), you extend the circle of this practice in depth and build a column table. You also check that a cylindrical slip surface gives back the values of this practice.

## References

1. Bishop, A. W. (1955). “The use of the slip circle in the stability analysis of slopes.” *Géotechnique*, 5(1), 7–17. [https://doi.org/10.1680/geot.1955.5.1.7](https://doi.org/10.1680/geot.1955.5.1.7)
2. Janbu, N. (1973). “Slope Stability Computations.” In R. C. Hirschfeld and S. J. Poulos (eds.), *Embankment-Dam Engineering: Casagrande Volume*, pp. 47–86. New York: Wiley.
3. Spencer, E. (1967). “A method of analysis of the stability of embankments assuming parallel inter-slice forces.” *Géotechnique*, 17(1), 11–26. [https://doi.org/10.1680/geot.1967.17.1.11](https://doi.org/10.1680/geot.1967.17.1.11)
4. Fredlund, D. G., and Krahn, J. (1977). “Comparison of slope stability methods of analysis.” *Canadian Geotechnical Journal*, 14(3), 429–439. [https://doi.org/10.1139/t77-045](https://doi.org/10.1139/t77-045)
