---
title: "Computing the factor of safety of a 3D slip surface with the method of columns: build a column table and check it against the infinite slope and the 2D values"
lang: en
series: "practice 3 of 3"
translated_from: "aa01203"
translated_on: 2026-10-05
---

# Computing the factor of safety of a 3D slip surface with the method of columns

**Build a column table and check it against the infinite slope and the 2D values**

In this practice, you extend the slope of Practice 2 in the depth direction and write code that computes the factor of safety of an ellipsoidal slip surface with the 3D method of columns. You build a column table and implement the Hovland method and the 3D simplified Bishop method. First, you check that a plane slip surface gives the infinite slope of Practice 1, and that a cylindrical slip surface gives the 2D values of Practice 2. Then, on spheres and ellipsoids, you look at the effect of the quantities that 3D newly requires you to choose, such as the local direction of sliding and the direction of sliding.

This practice assumes that you have read [Chapter 2](what-is-limit-equilibrium-method.md) and [Chapter 3](lem-in-practice-mechanical-perspective.md) and finished [Practice 1](practice-infinite-slope.md) and [Practice 2](practice-slices-2d.md). The terms and symbols are collected in the [Glossary](lem-glossary.md).

(columns-goal)=

## What you build

The slope is the slope of [Practice 2](practice-slices-2d.md), extended without end in the depth direction (the $y$ direction). The coordinates take $x$ horizontal to the right, $y$ horizontal into the page and $z$ vertically upward. The soil mass slides toward negative $x$. The soil constants are the same as in Practices 1 and 2: $\gamma=18$ kN/m³, $c'=10$ kPa, $\phi'=30^\circ$.

The {term}`slip surface` is the lower surface of an ellipsoid whose three axes are parallel to the coordinate axes. The center of the ellipsoid is $(6, 0, 18)$. Its radii in the $x$ and $z$ directions are the radius of the circle of Practice 2, $R=19.31$ m, and its radius in the $y$ direction is $B$. The section $y=0$ is therefore exactly the arc of Practice 2. With $B=R$ the ellipsoid is a sphere, and the larger $B$ is, the longer the ellipsoid is in the depth direction. For the checks, you also use a plane slip surface and a cylindrical slip surface that extends the arc of Practice 2 over a length of 10 m.

The {term}`direction of sliding` is $\boldsymbol{d}=(-1, 0, 0)$, down the slope. Moments are taken about the horizontal axis $\boldsymbol{a}=\boldsymbol{d}\times\boldsymbol{e}_z=(0, 1, 0)$, which passes through the center $O$ of the ellipsoid and is perpendicular to $\boldsymbol{d}$. Here $\boldsymbol{e}_z$ is the upward vertical unit vector.

```{figure} ./figures/fig_05_3d_column_forces.svg
:name: fig-columns-3d-forces
:alt: A 3D column with an inclined base, acted on by its weight, the normal and shear forces on the base, and the intercolumn forces on its sides

Forces on a 3D column

This is the same figure as {numref}`fig-05-3d-column-forces` of Chapter 2. The strength equation does not determine the direction of the shear force on the base. For the intercolumn forces on the sides, this practice either ignores their effect or takes them as horizontal.
```

You build the following.

| Functions and classes | What they compute | Section |
|---|---|---|
| `ground`, `Ellipsoid`, `centres`, `make_columns` | The ground surface, the ellipsoidal slip surface, the column table | Section 1 |
| `rotation_directions`, `section_directions`, `projected_directions` | The local direction of sliding on each base | Section 2 |
| `hovland` | The factor of safety of the Hovland method | Section 3 |
| `arms`, `hovland_moment` | The moment arms, and the factor of safety of the Hovland method written as a ratio of moments | Section 4 |
| `vertical_normal_force`, `bishop` | $N_i$ from vertical force equilibrium, and the factor of safety of the 3D simplified Bishop method | Section 4 |
| `Cylinder`, `Plane` | The cylindrical and plane slip surfaces used for the checks | Section 5 |
| `save_columns` | A file that stores the column table | Section 8 |

(columns-setup)=

## Setup

Use the folder `lem-practice` from [Practice 1](practice-infinite-slope.md) and [Practice 2](practice-slices-2d.md). The code for this practice is in {download}`columns.py <examples/columns.py>` and {download}`test_columns.py <examples/test_columns.py>`. This code reads the shape of the slope from `slices.py` of Practice 2. The tests and `run_columns.py` also use `infinite_slope.py` of Practice 1. So if you start here, put {download}`infinite_slope.py <examples/infinite_slope.py>` and {download}`slices.py <examples/slices.py>` in the same folder too.

---

(columns-section-1)=

## 1. Build the column table

Divide the plan into squares with side $h$. If the slip surface lies below the ground surface at the center of a square, that square becomes a {term}`column`. Each column's base is represented by the point where the vertical line through its center meets the slip surface, and by the tangent plane there. This is the 3D version of what Practice 2 did, when it represented the base of each {term}`slice` by the point at the middle of its width.

Let the center of the ellipsoid be $(c_x, c_y, c_z)$ and its radii along the three axes $(R_x, R_y, R_z)$. The height of the lower intersection with the vertical line $(x, y)$ and the outward unit normal vector are then as follows.

$$
z_s=c_z-R_z\sqrt{1-\left(\frac{x-c_x}{R_x}\right)^2-\left(\frac{y-c_y}{R_y}\right)^2},
\qquad
\boldsymbol{n}\propto
\begin{bmatrix}
(x-c_x)/R_x^2\\
(y-c_y)/R_y^2\\
(z_s-c_z)/R_z^2
\end{bmatrix}
$$ (eq-columns-ellipsoid)

$\boldsymbol{n}$ points out of the ellipsoid. On the base it points downward, which is also outward from the {term}`sliding mass`. Create `columns.py` and begin with the following.

```{literalinclude} examples/columns.py
:language: python
:end-at: return slices.ground
```

```{literalinclude} examples/columns.py
:language: python
:pyobject: Ellipsoid
```

The column table consists of the following quantities. The base area $A_i$ is the area of the tangent plane above the square with side $h$, which is $h^2/|n_{z,i}|$. It corresponds to $l_i=b_i/\cos\alpha_i$ in Practice 2. The weight uses the height of the prism measured at the center: $W_i=\gamma h^2(z_g-z_s)$. Here $z_g$ is the height of the ground surface at the center of the column.

```{literalinclude} examples/columns.py
:language: python
:pyobject: Columns
```

```{literalinclude} examples/columns.py
:language: python
:pyobject: centres
```

```{literalinclude} examples/columns.py
:language: python
:pyobject: make_columns
```

`centres` makes the grid of squares symmetric about the midpoint of the range where the slip surface can lie. With this, a slip surface symmetric about $y=0$ also gives a symmetric table. The water table `water_level` is handled as in [Practice 2, Section 1](#slices-section-1). Finally, write a test that checks the table by hand. Create `test_columns.py` and write the following.

```{literalinclude} examples/test_columns.py
:language: python
:end-at: R = slices
```

```{literalinclude} examples/test_columns.py
:language: python
:pyobject: test_the_column_table_by_hand
```

---

(columns-section-2)=

## 2. Choose the local direction of sliding

As [Chapter 2, Section 7.1](#what-section-7-1) showed, in 3D the strength equation determines only the size of the {term}`base shear force`, not its direction. So the {term}`local direction of sliding` $\boldsymbol{m}_i$ on each base has to be assumed separately. This practice builds two ways to choose it.

- **The direction in the vertical plane**: take the direction along the line where the base meets the vertical plane containing the direction of sliding $\boldsymbol{d}$, heading toward $\boldsymbol{d}$. This is the choice of Hovland (1977). It is the same as the direction in which the soil mass moves when it rotates about the horizontal axis $\boldsymbol{a}$ perpendicular to $\boldsymbol{d}$, so $\boldsymbol{m}_i\propto\boldsymbol{a}\times\boldsymbol{n}_i$. On bases near the toe, it points uphill
- **Projection onto the tangent plane**: project $\boldsymbol{d}$ onto the tangent plane of each base, so $\boldsymbol{m}_i\propto(\boldsymbol{I}-\boldsymbol{n}_i\boldsymbol{n}_i^{\mathsf T})\boldsymbol{d}$. This is the choice of [Chapter 3, Section 8.2](#practice-section-8-2)

```{literalinclude} examples/columns.py
:language: python
:pyobject: rotation_directions
```

```{literalinclude} examples/columns.py
:language: python
:pyobject: section_directions
```

```{literalinclude} examples/columns.py
:language: python
:pyobject: projected_directions
```

Both directions lie in the tangent plane of the base and head toward $\boldsymbol{d}$. On a column whose base is not tilted sideways ($n_{y,i}=0$), the two coincide. On a column tilted sideways they differ, and Section 7 shows how the difference appears in the {term}`factor of safety`. First, check that both lie in the tangent plane.

```{literalinclude} examples/test_columns.py
:language: python
:pyobject: test_both_local_directions_lie_in_the_base
```

---

(columns-section-3)=

## 3. The Hovland method

The Hovland method of [Chapter 2, Section 8.1](#what-section-8-1) extends the Fellenius method (ordinary method of slices) to 3D. It ignores the effect of the {term}`intercolumn forces <interslice force>` and takes the {term}`base normal force` as the component of the weight along the normal, $N_i=W_i\,(\boldsymbol{g}\cdot\boldsymbol{n}_i)$. Here $\boldsymbol{g}=(0, 0, -1)$ is the direction of gravity. It then sums the {term}`resisting force` of each column and the component of its weight along $\boldsymbol{m}_i$ (the {term}`driving force`), and takes their ratio.

$$
F_s=
\frac{
\displaystyle\sum_i\left[c_i'A_i+(N_i-U_i)\tan\phi_i'\right]
}{
\displaystyle\sum_i W_i\,(\boldsymbol{g}\cdot\boldsymbol{m}_i)
},
\qquad
N_i=W_i\,(\boldsymbol{g}\cdot\boldsymbol{n}_i)
$$ (eq-columns-hovland)

Here $U_i=u_iA_i$ is the {term}`pore water force on the base`. On a column whose base is not tilted sideways, $\boldsymbol{g}\cdot\boldsymbol{n}_i=\cos\alpha_i$ and $\boldsymbol{g}\cdot\boldsymbol{m}_i=\sin\alpha_i$, and the equation takes the same form as the Fellenius method of [Practice 2, Section 2](#slices-section-2). Write `hovland(col, m)`. `m` is one of the two local directions of sliding of Section 2.

:::{dropdown} Example implementation
```{literalinclude} examples/columns.py
:language: python
:pyobject: hovland
```
:::

You write its tests in Section 5, with the others.

---

(columns-section-4)=

## 4. Moments about the axis of rotation, and the 3D simplified Bishop method

As [Chapter 2, Section 8.2](#what-section-8-2) showed, the 3D simplified Bishop method finds $F_s$ from moment equilibrium about the {term}`axis of rotation <center of moments>`. So first build the moment arms. Let the axis $\boldsymbol{a}$ pass through the point $O$. Let $\boldsymbol{r}_{b,i}$ be the position vector from $O$ to the point on the base, and $\boldsymbol{r}_{g,i}$ the position vector to the point at mid-height of the column. The moments about $\boldsymbol{a}$ of the base shear force, the weight and the base normal force, per unit magnitude, are the following three.

$$
\ell_{t,i}=(\boldsymbol{r}_{b,i}\times\boldsymbol{m}_i)\cdot\boldsymbol{a},
\qquad
\ell_{w,i}=(\boldsymbol{r}_{g,i}\times\boldsymbol{g})\cdot\boldsymbol{a},
\qquad
\ell_{n,i}=(\boldsymbol{r}_{b,i}\times\boldsymbol{n}_i)\cdot\boldsymbol{a}
$$ (eq-columns-arms)

Here $\boldsymbol{m}_i$ is the direction of rotation about the axis $\boldsymbol{a}$ (the first choice of Section 2). The intercolumn forces are {term}`internal forces <internal force>`, so they cancel in the moment of the whole soil mass. Moment equilibrium about $\boldsymbol{a}$ is therefore $\sum_i(W_i\ell_{w,i}-N_i\ell_{n,i}-T_i\ell_{t,i})=0$. Substituting $T_i=[c_i'A_i+(N_i-U_i)\tan\phi_i']/F_s$ and solving for $F_s$ gives the following.

$$
F_s=
\frac{
\displaystyle\sum_i\left[c_i'A_i+(N_i-U_i)\tan\phi_i'\right]\ell_{t,i}
}{
\displaystyle\sum_i\left(W_i\ell_{w,i}-N_i\ell_{n,i}\right)
}
$$ (eq-columns-moment)

```{literalinclude} examples/columns.py
:language: python
:pyobject: arms
```

Using the Hovland value of $N_i$ from Eq. {eq}`eq-columns-hovland` gives the Hovland method written as a ratio of moments. This is the 3D version of `fellenius_about` in Practice 2.

```{literalinclude} examples/columns.py
:language: python
:pyobject: hovland_moment
```

The 3D simplified Bishop method finds $N_i$ from the vertical force equilibrium of each column. The intercolumn forces are then taken as horizontal. The vertical components of the base normal force $-N_i\boldsymbol{n}_i$ and the shear force $-T_i\boldsymbol{m}_i$ balance the weight, so $N_i$ is as follows.

$$
N_i=
\frac{
W_i+m_{z,i}\left(c_i'A_i-U_i\tan\phi_i'\right)/F_s
}{
m_{\alpha,i}
},
\qquad
m_{\alpha,i}=-n_{z,i}-\frac{m_{z,i}\tan\phi_i'}{F_s}
$$ (eq-columns-bishop-normal)

On a base not tilted sideways, $-n_{z,i}=\cos\alpha_i$ and $m_{z,i}=-\sin\alpha_i$, so $m_{\alpha,i}$ becomes the same as $m_{\alpha,i}=\cos\alpha_i+\sin\alpha_i\tan\phi_i'/F_s$ of the simplified Bishop method in [Practice 2, Section 2](#slices-section-2).

```{literalinclude} examples/columns.py
:language: python
:pyobject: vertical_normal_force
```

Substituting this $N_i$ into Eq. {eq}`eq-columns-moment` puts $F_s$ on the right-hand side as well. So, as with the simplified Bishop method in Practice 2, the value is found by iteration. Write `bishop(col, center, axis)`.

:::{dropdown} Example implementation
```{literalinclude} examples/columns.py
:language: python
:pyobject: bishop
```
:::

---

(columns-section-5)=

## 5. Check with a plane and a cylinder

Build the plane and cylindrical slip surfaces. `Plane` is the `Line` of Practice 2, extended in the depth direction into a plane. `Cylinder` extends the arc of Practice 2 over the length `length` and cuts both ends with vertical planes.

```{literalinclude} examples/columns.py
:language: python
:pyobject: Cylinder
```

```{literalinclude} examples/columns.py
:language: python
:pyobject: Plane
```

Download {download}`run_columns.py <examples/run_columns.py>`, put it in `lem-practice` and run it.

```bash
uv run python run_columns.py
```

Items 1. and 2. of the output are the checks of this section.

```{literalinclude} examples/output/run_columns.txt
:language: text
:start-at: 1. a plane
:end-before: 3. ellipsoids
```

For the plane, all three values match the {term}`infinite slope` value of Practice 1, 1.2566. This is because every column has the same shape, and each column is in equilibrium on its own, like the column of Practice 1. Every base faces the same way, so the sum of the moments of the weight and the base normal force is $W_i\sin\beta\,\ell_{t,i}$. The arm of the shear force $\ell_{t,i}$ is also the same for every column (the distance from $O$ to the plane). So the ratio of moments equals the ratio of forces.

For the cylinder, the bases are not tilted sideways, so every strip in the depth direction is the 2D problem of Practice 2. The Hovland method therefore matches the Fellenius method of Practice 2, and the 3D simplified Bishop method matches the simplified Bishop method of Practice 2, to within about 0.1%. A difference remains because the square columns do not fit exactly at the exit and entry of the arc. Add these two to the tests.

```{literalinclude} examples/test_columns.py
:language: python
:pyobject: test_a_plane_under_a_planar_slope_gives_the_infinite_slope
```

```{literalinclude} examples/test_columns.py
:language: python
:pyobject: test_a_cylinder_gives_the_2d_values
```

---

(columns-section-6)=

## 6. See the 3D effects on spheres and ellipsoids

Vary the radius $B$ in the $y$ direction of an ellipsoid whose middle section ($y=0$) is the arc of Practice 2.

```{literalinclude} examples/output/run_columns.txt
:language: text
:start-at: 3. ellipsoids
:end-before: 4. Hovland on the sphere
```

In Practice 2, the values for the middle section were 1.888 by the Fellenius method and 2.063 by the simplified Bishop method. For the sphere ($B=R$), the Hovland method gives 1.816, smaller than the middle section, and the 3D simplified Bishop method gives 2.142, larger. On the same slip surface, which of the 3D and 2D values is larger depends on the method.

The reason the Hovland value is smaller splits into two parts. One is the shape of the sections. A section away from $y=0$ is a shallower arc with the same center height and a smaller radius. The other is the sideways tilt of the bases. Let $\alpha_i$ be the inclination of a base seen in a section of constant $y$. On a base tilted sideways, $|n_{z,i}|$ is smaller than $\cos\alpha_i$. So the base area $A_i=h^2/|n_{z,i}|$ grows and $N_i=W_i|n_{z,i}|$ shrinks. The driving force $W_i\,(\boldsymbol{g}\cdot\boldsymbol{m}_i)$, with the direction in the vertical plane, equals $W_i\sin\alpha_i$ regardless of the sideways tilt. Separate the two effects and find the Hovland value for the sphere.

```{literalinclude} examples/output/run_columns.txt
:language: text
:start-at: 4. Hovland on the sphere
:end-before: 5. base normal force
```

The first line treats each column as a slice of its section, not tilted sideways. The shape of the sections alone lowers the value from 1.888 for the middle section to 1.858. Adding the sideways tilt raises the cohesive resistance as the base area grows, and lowers the frictional resistance as $N_i$ shrinks. In this example the latter wins, and the value drops to 1.816.

In the 3D simplified Bishop method, on the other hand, the more a base is tilted sideways, the larger the $N_i$ that vertical equilibrium gives. Compared with the $N_i$ of the Hovland method, it is as follows.

```{literalinclude} examples/output/run_columns.txt
:language: text
:start-at: 5. base normal force
:end-before: 6. local direction
```

On columns tilted sideways by more than 30°, $N_i$ is 1.6 times the Hovland value, and the frictional resistance grows. As [Chapter 2, Section 9](#what-section-9) showed, there is no rule that "the 3D factor of safety is always larger than the 2D one." As in this example, which is larger can reverse with the shape of the slip surface and the method.

The last line gives the number of columns where $N_i-U_i$ is negative. In the 3D simplified Bishop method, it is negative on 168 of the 9198 columns. All of them are columns at the edge of the slip surface, with a prism height of at most 0.51 m. There, as at the rightmost slice of [Practice 2, Section 5](#slices-section-5), the vertical component of the shear force from cohesion exceeds the weight. The Hovland value $N_i=W_i|n_{z,i}|$, on the other hand, does not become negative on a dry slope.

As $B$ grows, the sideways tilt of the bases shrinks. So the Hovland value approaches the value that treats each column as a slice of its section, not tilted sideways. Stretching the ellipsoid in the depth direction only lines up sections of the same shapes over a length proportional to $B$, so this value is about 1.86 regardless of $B$. In other words, the Hovland value does not approach 1.888 of the middle section. To compare with the 2D value of the middle section, use the cylinder of Section 5. Add the values for the sphere to the tests.

```{literalinclude} examples/test_columns.py
:language: python
:pyobject: test_the_sphere
```

---

(columns-section-7)=

## 7. Vary the local direction of sliding and the direction of sliding

On the sphere, compare the two local directions of sliding of Section 2.

```{literalinclude} examples/output/run_columns.txt
:language: text
:start-at: 6. local direction
:end-before: 7. azimuth
```

With the same column table and the same direction of sliding, changing only how the local direction of sliding is chosen changes the factor of safety by 17%, from 1.816 to 2.122. On a base tilted sideways, the projection of $\boldsymbol{d}$ onto the tangent plane has a sideways component, and its downhill component is smaller. For example, on a base with $\boldsymbol{n}=(0.3, 0.6, -0.742)$, $\boldsymbol{g}\cdot\boldsymbol{m}$ is 0.375 with the direction in the vertical plane and 0.233 with the projection. So the projection gives a smaller driving force and a larger factor of safety. As [Chapter 3, Section 9](#practice-section-9) showed, the direction of sliding determines the factor of safety through the local directions of sliding $\boldsymbol{m}_i$. How $\boldsymbol{m}_i$ is derived from $\boldsymbol{d}$ is part of the formulation too.

Next, rotate the direction of sliding $\boldsymbol{d}$ in the horizontal plane.

```{literalinclude} examples/output/run_columns.txt
:language: text
:start-at: 7. azimuth
:end-before: 8. column size
```

With either choice, among the azimuths tried, the factor of safety is smallest straight down the slope (0°). Rotating left and right by the same angle gives equal values. This is because the slip surface is symmetric about $y=0$. Symmetry alone, however, does not guarantee a minimum at 0°. As in [Chapter 3, Section 8.1](#practice-section-8-1), on a symmetric slope the plane of symmetry gives the candidate direction of sliding. On an asymmetric slope, you have to try several azimuths and look for the minimum, or solve for the direction from equilibrium. Add to the tests that the minimum is at 0° and that the left and right values are equal.

```{literalinclude} examples/test_columns.py
:language: python
:pyobject: test_straight_down_is_least_stable_of_three_azimuths
```

Finally, vary the column size $h$.

```{literalinclude} examples/output/run_columns.txt
:language: text
:start-at: 8. column size
```

Going from $h=1$ m to 0.25 m changes the values by 0.2% or less. In other words, the values compared in Sections 6 and 7 have settled at $h=0.25$ m. As [Chapter 3, Section 11.5](#practice-section-11-5) says, before comparing the effects of other conditions, check in this way that the values settle as the division changes.

---

(columns-section-8)=

## 8. Save the column table and compare with other implementations

Save the column table, together with the reference point for moments and the axis of rotation, in NumPy's `.npz` format.

```{literalinclude} examples/columns.py
:language: python
:pyobject: save_columns
```

{download}`save_table.py <examples/save_table.py>` builds a table of columns with side 0.5 m for the ellipsoid $B=2R$ of Section 6, and saves it to `columns.npz`.

```{literalinclude} examples/save_table.py
:language: python
```

Put it in `lem-practice` and run it. It prints the number of columns saved (4596).

```bash
uv run python save_table.py
```

You can pass the saved table to the solver of another implementation and compare the factors of safety for the same slip surface. This works because, as [Chapter 3, Section 1](#practice-section-1) showed, the base area, normal, weight, {term}`pore water pressure`, strength and position vectors are enough to sum forces and moments. [LEM Lab](https://github.com/ibaraki-kozo-lab/lem-lab), one example of an implementation, is also built with the column table separate from the solver. Before comparing values, however, check the following conventions.

1. What the quantities in the table mean: is the base area the area of the inclined base or the area in plan? Is the pore water pressure a pressure or a resultant force?
2. The direction of the normal: outward from the sliding mass (as in this practice), or upward?
3. The local direction of sliding: derived from the axis of rotation, or the projection of the direction of sliding? Does it point the way the mass slides, or against it?
4. The pore water pressure term: is the resultant $U_i=u_iA_i$ subtracted (as in this practice), or is the effective normal force found from the effective weight, as in $(W_i-u_ib_i)\cos\alpha_i$ of [Practice 2, Section 5](#slices-section-5)?
5. The reference point for moments and the axis of rotation: where are they, and which sense of rotation is positive? Do they move with the size of the slip surface?
6. What is returned when there is no solution: some implementations return a special value, such as infinity, when the iteration does not converge. That does not mean "very safe" ([Chapter 3, Section 11.4](#practice-section-11-4))

Item 6. needs particular care. For example, if a table with no sideways tilt, such as the cylinder's, is passed to a 3D formulation with a sideways unknown, that unknown has no effect on the equations, and the iteration may fail to solve.

Check with a test that the saved table reproduces the original columns.

```{literalinclude} examples/test_columns.py
:language: python
:pyobject: test_the_saved_table
```

Run `uv run pytest` and check that all the tests of Practices 1 to 3 pass.

---

(columns-trouble)=

## Troubleshooting

| What you see | Cause and fix |
|---|---|
| `ModuleNotFoundError: No module named 'slices'` | `slices.py` of Practice 2 is not in the same folder. (→[Setup](#columns-setup)) |
| `ModuleNotFoundError: No module named 'infinite_slope'` | `infinite_slope.py` of Practice 1 is not in the same folder. The tests and `run_columns.py` read it. (→[Setup](#columns-setup)) |
| `RuntimeWarning: invalid value encountered in sqrt` | `Ellipsoid.z` computes the square root even for vertical lines that do not meet the ellipsoid. `np.where` computes both values first, so use `np.sqrt(np.abs(q))`. (→[Section 1](#columns-section-1)) |
| `ValueError: m_alpha is zero or negative for some column` | In the iteration of the 3D simplified Bishop method, $F_s$ became too small, or some columns have bases that rise steeply or are tilted steeply sideways. Raise the initial value `fs`, or review the slip surface. (→[Section 4](#columns-section-4)) |
| The computation takes a long time | The number of columns grows in inverse proportion to $h^2$. The sphere with $h=0.25$ m has about 9200 columns. While checking, try $h=0.5$ m or 1 m. (→[Section 7](#columns-section-7)) |
| The values differ slightly from the table | Check $h$ and the grid of columns (`centres`). If the grid is not symmetric, the values for directions of sliding rotated left and right also drift apart. (→[Section 1](#columns-section-1)) |

## Summary

- The column table consists of each base's representative point, normal, base area, weight, pore water pressure and strength. The base area is $h^2/|n_z|$, which corresponds to $b/\cos\alpha$ in 2D (→[Section 1](#columns-section-1))
- In 3D, the local direction of sliding is assumed separately. The direction in the vertical plane and the projection onto the tangent plane differ on bases tilted sideways (→[Section 2](#columns-section-2))
- The Hovland method ignores the intercolumn forces and sums the resisting and driving forces of the columns. The 3D simplified Bishop method finds $N_i$ from the vertical equilibrium of each column and takes the ratio of moments about the axis of rotation (→[Section 3](#columns-section-3), [Section 4](#columns-section-4))
- A plane slip surface gives the infinite slope value, and a cylindrical slip surface gives the 2D values. A new method is checked by reducing it to the model before it (→[Section 5](#columns-section-5))
- On the sphere, the Hovland value is smaller than that of the 2D middle section, and the 3D simplified Bishop value is larger. Which of 3D and 2D is larger can reverse with the shape of the slip surface and the method. In the simplified Bishop method, the effective normal force becomes negative on the thin columns at the edge of the slip surface (→[Section 6](#columns-section-6))
- Even with the same table, the way the local direction of sliding is chosen changes the factor of safety by 17%. On the sphere, among the directions of sliding tried, the factor of safety was smallest straight down the slope (→[Section 7](#columns-section-7))
- Before comparing with another implementation, check what the quantities in the table mean, the direction of the normal, the local direction of sliding, the pore water pressure term, the axis of rotation and what is returned when there is no solution (→[Section 8](#columns-section-8))

---

## Review questions

Click a question to see its answer. Do the (Try it) questions in `lem-practice`.

:::{dropdown} Q1. Why does the 3D method of columns need the local direction of sliding to be chosen separately?
:icon: question

Because the strength equation from the Mohr–Coulomb failure criterion determines only the size of the base shear force, not its direction in the tangent plane. In 2D, the direction is limited to the two along the tangent in the section, and it is set to the side that opposes sliding. The tangent plane in 3D has infinitely many directions, so one has to be assumed. (→[Section 2](#columns-section-2))
:::

:::{dropdown} Q2. The base of a column with side $h=0.25$ m is inclined at 30° from the horizontal. What is its base area?
:icon: question

$|n_z|=\cos 30^\circ$, so $A=0.25^2/\cos 30^\circ=0.0722$ m². It is larger than the area of the horizontal square, 0.0625 m², by the effect of the inclination. (→[Section 1](#columns-section-1))
:::

:::{dropdown} Q3. Why, on a plane slip surface, do the Hovland method, its moment form and the 3D simplified Bishop method all match the infinite slope value?
:icon: question

Because every column has the same shape, and each column is in equilibrium on its own, like the column of the infinite slope. In each column, the weight and the base forces cancel on the same vertical line, so their moment about any axis is zero. So differences in the intercolumn forces or in the choice of the axis of rotation do not appear in the values. (→[Section 5](#columns-section-5))
:::

:::{dropdown} Q4. Why was the Hovland value on the spherical slip surface smaller than the value for the 2D middle section? Can you say that "the 3D factor of safety is larger than the 2D one"?
:icon: question

Because the shape of the sections and the sideways tilt of the bases both lower the value. Sections away from $y=0$ are shallower arcs, and just treating each column as a slice of its section lowers the value from 1.888 to 1.858. On bases tilted sideways, the base area grows, which raises the cohesive resistance. But $N_i=W_i|n_{z,i}|$ shrinks, and the loss of frictional resistance is larger, so the value becomes 1.816. On the same sphere, on the other hand, the 3D simplified Bishop value is larger than the middle section's. So which of 3D and 2D is larger can reverse with the shape of the slip surface and the method, and you cannot say it is "always larger." (→[Section 6](#columns-section-6))
:::

:::{dropdown} Q5. Why did changing how the local direction of sliding is chosen change the factor of safety on the sphere by as much as 17%?
:icon: question

Because on bases tilted sideways, the projection of the direction of sliding onto the tangent plane has a sideways component, and its downhill component is smaller than that of the direction in the vertical plane. The driving force from the weight shrinks by that amount, and the factor of safety grows. On bases not tilted sideways, the two directions coincide. (→[Section 2](#columns-section-2), [Section 7](#columns-section-7))
:::

:::{dropdown} Q6. (Try it) Put the water table at the horizontal line $z=4$ m, and find the values of the Hovland method and the 3D simplified Bishop method on the sphere. How do they compare with the values of Practice 2 with a water table?
:icon: question

Build the table with `columns.make_columns(columns.Ellipsoid(centre, (R, R, R)), 0.25, water_level=4.0)`. As in Practice 2, Section 5, the soil below the water table keeps $\gamma=18$ kN/m³. The Hovland method gives 1.418, and the 3D simplified Bishop method gives 1.699. The values of Practice 2 with the same water table were 1.402 by the Fellenius method and 1.540 by the simplified Bishop method. With the Hovland method, unlike the dry case, the 3D value is larger than the 2D one. With the simplified Bishop method, the difference widens from 0.079 in the dry case to 0.159. This is because sections away from $y=0$ are shallow, less of their base lies below the water table, and they are less affected by the pore water pressure. The sum of the pore water forces divided by the sum of the weights is 0.25 for the sphere, smaller than 0.28 for the arc of Practice 2. (→[Section 6](#columns-section-6), [Practice 2, Section 5](#slices-section-5))
:::

:::{dropdown} Q7. (Try it) On the sphere, how do the values of the Hovland method, its moment form and the 3D simplified Bishop method change when the reference point $O$ of the axis of rotation is moved 2 m up?
:icon: question

Compute with the reference point `centre + np.array([0.0, 0.0, 2.0])`. The Hovland method, which takes the ratio of sums of forces, does not use the reference point, so it stays at 1.816. The moment form changes from 1.816 to 1.849, and the 3D simplified Bishop method from 2.142 to 2.122. This is because neither satisfies horizontal force equilibrium. As in Practice 2, Section 7, moving the reference point by $\boldsymbol{s}$ changes the moment about the axis $\boldsymbol{a}$ by $-(\boldsymbol{s}\times\sum\boldsymbol{F})\cdot\boldsymbol{a}$. Since $\boldsymbol{s}$ is vertical, only the horizontal component of $\sum\boldsymbol{F}$ matters. In an implementation whose reference point moves with the size of the slip surface, this effect can appear in the values. (→[Section 4](#columns-section-4), [Practice 2, Section 7](#slices-section-7))
:::

:::{dropdown} Q8. When you pass a saved column table to the solver of another implementation, what do you check before comparing factors of safety?
:icon: question

- What the quantities in the table mean (is the base area that of the inclined base or of the plan, is the pore water pressure a pressure or a resultant force)
- The direction of the normal (outward from the sliding mass, or upward)
- How the local direction of sliding is chosen, and which way it points (the way the mass slides, or the way that resists it)
- How the pore water pressure term is taken (subtract the resultant force, or derive it from the effective weight)
- How the reference point for moments and the axis of rotation are chosen, and which sense of rotation is positive
- The value returned when the iteration does not converge

(→[Section 8](#columns-section-8))
:::

---

## References

1. Hovland, H. J. (1977). “Three-Dimensional Slope Stability Analysis Method.” *Journal of the Geotechnical Engineering Division*, 103(9), 971–986. [https://doi.org/10.1061/AJGEB6.0000493](https://doi.org/10.1061/AJGEB6.0000493)
2. Hungr, O. (1987). “An extension of Bishop's simplified method of slope stability analysis to three dimensions.” *Géotechnique*, 37(1), 113–117. [https://doi.org/10.1680/geot.1987.37.1.113](https://doi.org/10.1680/geot.1987.37.1.113)
