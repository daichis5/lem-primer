---
title: "Computing the factor of safety of an infinite slope: from splitting the traction to the factor of safety, in code"
lang: en
series: "practice 1 of 3"
translated_from: "aa01203"
translated_on: 2026-10-05
---

# Computing the factor of safety of an infinite slope

**From splitting the traction to the factor of safety, in code**

In this practice, you write Python code that computes the factor of safety of an infinite slope. An infinite slope is the simplest model of a slope: it treats a slope of one inclination as continuing without end. The equation for its factor of safety is well known. Here, though, it is built along the path of Chapter 1, starting from splitting the traction on the slip surface into a normal component and a shear component. The functions you write are used again to check the answers in Practice 2 and Practice 3.

This practice assumes that you have read [Chapter 1](continuum-mechanics-to-lem-start.md). The terms and symbols are collected in the [Glossary](lem-glossary.md).

(infinite-goal)=

## What you build

Assume a {term}`slip surface` parallel to the ground surface, at a vertical depth $z$ below a ground surface of inclination $\beta$, and find its {term}`factor of safety` $F_s$. The soil constants are the same as in [Chapter 1, Section 6](#section-6): $c'=10$ kPa and $\phi'=30^\circ$. The unit weight is $\gamma=18$ kN/m³, and $\gamma_{sat}=20$ kN/m³ for soil below the water table. Practice 2 and Practice 3 use the same $c'$, $\phi'$ and $\gamma$.

```{figure} ./figures/fig_e1_infinite_slope.svg
:name: fig-e1-infinite-slope
:alt: The weight of a column taken from an infinite slope, the normal and shear forces on the slip surface, the forces on its two sides, and two ways to set the pore water pressure on the slip surface when there is a water table

Forces on a column of the infinite slope, and the pore water pressure on the slip surface

Left: the forces on the column's two sides cancel, so the normal force $N$ and the shear force $T$ on the slip surface carry the weight $W$. Right: the figure shows the pore water pressure at point P on the slip surface when the water table is a vertical height $h_w$ above the slip surface. With seepage parallel to the slope, the equipotential line through P is perpendicular to the slope.
```

The $x$ axis points horizontally to the right, and the $z$ axis points vertically up. The depth $z$ of the slip surface is not this coordinate: it is a length measured vertically down from the ground surface. In these coordinates, the ground surface rises to the right, and the soil slides down to the left. As in Chapter 1, the unit normal vector $\boldsymbol{n}$ of the slip surface points outward from the {term}`sliding mass`, toward the ground below the slip surface. The unit vector in the direction of sliding is $\boldsymbol{m}$.

You write the following six functions.

| Function | What it computes | Section |
|---|---|---|
| `plane_vectors` | $\boldsymbol{n}$ and $\boldsymbol{m}$ of the slip surface | Section 1 |
| `split_traction` | The normal and shear components of a traction | Section 2 |
| `base_stresses` | $\sigma_n$ and $\tau$ on the slip surface from the column's weight | Section 2 |
| `factor_of_safety` | The factor of safety $F_s$ | Section 3 |
| `column_weight` | The column's weight when there is a water table | Section 4 |
| `pore_pressure` | Two ways to set the pore water pressure on the slip surface | Section 4 |

(infinite-setup)=

## Setup

You need Python 3.11 or later, with NumPy and pytest. Here, uv, a tool that sets up Python environments, is used, and the code of Practice 1 to Practice 3 goes in one folder, `lem-practice`.

```bash
uv init --bare --python 3.12 lem-practice
cd lem-practice
uv python pin 3.12
uv add numpy
uv add --dev pytest
```

1. Create the folder `lem-practice`, with only the project's settings file `pyproject.toml` in it
2. Move into the folder. Put the files from here on in it, and run the commands in it too
3. Set the Python for this project to 3.12
4. Add NumPy, used for the calculations
5. Add pytest, used for the tests. `--dev` records it separately as a tool used only during development

Without uv, create the folder `lem-practice` and move into it, then create and activate a virtual environment with Python 3.11 or later (`python3 -m venv .venv`). Then run `pip install numpy pytest`, and drop `uv run` from the commands that follow. The code of this practice is in {download}`infinite_slope.py <examples/infinite_slope.py>` and {download}`test_infinite_slope.py <examples/test_infinite_slope.py>`. If the code you write does not work, compare it with them.

---

(infinite-section-1)=

## 1. Set the direction of the slip surface

On a slip surface of inclination $\beta$, the outward unit normal vector and the unit vector in the direction of sliding are as follows.

$$
\boldsymbol{n}=
\begin{bmatrix}
\sin\beta\\
-\cos\beta
\end{bmatrix},
\qquad
\boldsymbol{m}=
\begin{bmatrix}
-\cos\beta\\
-\sin\beta
\end{bmatrix}
$$ (eq-infinite-vectors)

$\boldsymbol{n}$ points down to the right, toward the ground below the slip surface. $\boldsymbol{m}$ points down to the left along the slip surface. The two are perpendicular, so $\boldsymbol{n}\cdot\boldsymbol{m}=0$. Create `infinite_slope.py`, and write the following first.

```{literalinclude} examples/infinite_slope.py
:language: python
:end-at: GAMMA_W =
```

Next, turn Eq. {eq}`eq-infinite-vectors` into a function. It takes the angle in degrees and converts it to radians with `math.radians`.

```{literalinclude} examples/infinite_slope.py
:language: python
:pyobject: plane_vectors
```

---

(infinite-section-2)=

## 2. Split the traction on the slip surface

As shown in [Chapter 1, Section 3](#section-3), the {term}`traction` $\boldsymbol{t}$ on a surface with outward unit normal vector $\boldsymbol{n}$ splits into the {term}`normal stress` $\sigma_n=-\boldsymbol{n}\cdot\boldsymbol{t}$, positive in compression, and the shear component $(\boldsymbol{I}-\boldsymbol{n}\boldsymbol{n}^{\mathsf T})\boldsymbol{t}$ in the tangent plane. Turn this into a function.

```{literalinclude} examples/infinite_slope.py
:language: python
:pyobject: split_traction
```

Next, find the traction on the slip surface. Take one column, 1 m wide and 1 m deep, out of the infinite slope. The neighboring columns push on its two sides. However, the slope is the same everywhere, so the forces on the left and right sides are equal in size and opposite in direction. The two forces therefore cancel, and the ground below the slip surface carries the whole weight of the column (left of the figure). In other words, in an infinite slope, equilibrium alone determines the force on the base, without any assumption on the {term}`interslice forces <interslice force>`. The {term}`static indeterminacy` treated in [Chapter 2, Section 3.1](#what-section-3-1) does not arise here.

Let $w$ be the column's weight per unit horizontal area. For dry soil, $w=\gamma z$. A column 1 m wide and 1 m deep weighs $w$ [kN]. The slip surface below it has an area of $1/\cos\beta$ [m²], so the traction with which the ground supports the column is as follows.

$$
\boldsymbol{t}
=
-\frac{1}{1/\cos\beta}
\begin{bmatrix}
0\\
-w
\end{bmatrix}
=
\begin{bmatrix}
0\\
w\cos\beta
\end{bmatrix}
$$ (eq-infinite-traction)

Splitting this with `split_traction` gives the following normal stress and shear stress.

$$
\sigma_n=w\cos^2\beta,
\qquad
\tau=w\sin\beta\cos\beta
$$ (eq-infinite-stresses)

The code follows Eq. {eq}`eq-infinite-traction`: it writes the column's weight as a vector, then divides by the area.

```{literalinclude} examples/infinite_slope.py
:language: python
:pyobject: base_stresses
```

Check what you have so far with tests. Create `test_infinite_slope.py`, and write the following first.

```{literalinclude} examples/test_infinite_slope.py
:language: python
:end-at: import infinite_slope
```

Then write two tests. The first checks that a traction built from a pushing component and a resisting component splits back into those two components. The second compares the code with Eq. {eq}`eq-infinite-stresses`.

```{literalinclude} examples/test_infinite_slope.py
:language: python
:pyobject: test_traction_splits_into_normal_and_shear
```

```{literalinclude} examples/test_infinite_slope.py
:language: python
:pyobject: test_stresses_on_the_slip_plane_by_hand
```

```bash
uv run pytest
```

If it shows `2 passed`, both tests pass. `pytest.approx` compares values while allowing for rounding errors.

---

(infinite-section-3)=

## 3. Find the factor of safety

From the {term}`Mohr–Coulomb failure criterion` of [Chapter 1, Section 5](#section-5), the {term}`shear strength` is $\tau_f=c'+(\sigma_n-u)\tan\phi'$. As in [Chapter 1, Section 6](#section-6), the factor of safety is the ratio of $\tau_f$ to the {term}`mobilized shear stress` $\tau_m$. In an infinite slope, the $\tau$ of Section 2 is $\tau_m$.

$$
F_s=\frac{c'+(\sigma_n-u)\tan\phi'}{\tau}
$$ (eq-infinite-fs)

```{literalinclude} examples/infinite_slope.py
:language: python
:pyobject: factor_of_safety
```

Compute a dry slope ($u=0$) with $\beta=30^\circ$ and $z=5$ m. Since $w=\gamma z=90$ kPa, Eq. {eq}`eq-infinite-stresses` gives $\sigma_n=67.50$ kPa and $\tau=38.97$ kPa. When $\beta=\phi'$, the frictional resistance $\sigma_n\tan\phi'$ exactly equals $\tau$. So $F_s$ is 1 plus the share of cohesion: $1+10/38.97=1.257$.

The base in "Working through the numbers" in [Chapter 1, Section 6](#section-6) can also be read as the base of an infinite slope. There, $\sigma_n=100$ kPa and $\tau_m=30$ kPa, so the ratio $\tau/\sigma_n=\tan\beta$ from Eq. {eq}`eq-infinite-stresses` gives an inclination of $\beta=16.70^\circ$. With $w=\sigma_n/\cos^2\beta=109.0$ kPa, the values $F_s=1.49$ ($u=40$ kPa) and 1.10 ($u=60$ kPa) found there come out directly. Add these two values to the tests, together with the fact that dry sand without cohesion has exactly $F_s=1$ at $\beta=\phi'$.

```{literalinclude} examples/test_infinite_slope.py
:language: python
:pyobject: test_dry_sand_at_its_friction_angle_is_just_stable
```

```{literalinclude} examples/test_infinite_slope.py
:language: python
:pyobject: test_the_base_of_section_6_of_chapter_1
```

---

(infinite-section-4)=

## 4. Add a water table

Suppose the water table is at a height $h_w$ above the slip surface, measured vertically (right of the figure). The soil below the water table has unit weight $\gamma_{sat}$, so the column's weight per unit horizontal area is $w=\gamma(z-h_w)+\gamma_{sat}h_w$.

```{literalinclude} examples/infinite_slope.py
:language: python
:pyobject: column_weight
```

How the {term}`pore water pressure` $u$ on the slip surface is set depends on what is assumed about the groundwater flow.

- **Seepage parallel to the slope**: when groundwater flows parallel to the slope, the equipotential lines, which cross the flow at right angles, are perpendicular to the slope. Along an equipotential line, the total head is the same. Where the equipotential line through point P on the slip surface meets the water table, the water pressure is zero, so the total head is the elevation of that point. The distance from P to that point, perpendicular to the slope, is $h_w\cos\beta$, and its vertical component is $h_w\cos^2\beta$. This is the pressure head at P, so $u=\gamma_w h_w\cos^2\beta$
- **Vertical hydrostatic pressure**: the pressure is hydrostatic in the depth measured vertically from the water table, so $u=\gamma_w h_w$. This amounts to treating the equipotential lines as vertical. Some {term}`LEM <limit equilibrium method>` programs that take the water table as a line use this rule. If the water table is inclined, water actually flows, so this rule gives a $u$ that is $1/\cos^2\beta$ times that of seepage parallel to the slope

```{literalinclude} examples/infinite_slope.py
:language: python
:pyobject: pore_pressure
```

Compare the two with the water table at the ground surface ($h_w=z=5$ m, $\beta=30^\circ$). Since $w=\gamma_{sat}z=100$ kPa, $\sigma_n=75.00$ kPa and $\tau=43.30$ kPa. With seepage parallel to the slope, $u=36.79$ kPa and $F_s=0.740$. With vertical hydrostatic pressure, on the other hand, $u=49.05$ kPa and $F_s$ drops to 0.577. So even for the same water table, the way the pore water pressure is set changes the factor of safety by more than 20 percent. Check with a test that the ratio of the two rules is $\cos^2\beta$.

```{literalinclude} examples/test_infinite_slope.py
:language: python
:pyobject: test_the_two_water_rules_differ_by_cos_squared
```

---

(infinite-section-5)=

## 5. When the effective normal stress is negative

With the water table at the ground surface, Eq. {eq}`eq-infinite-stresses` gives the following {term}`effective normal stress` $\sigma_n-u$ for the two rules.

$$
\text{parallel seepage: }
(\gamma_{sat}-\gamma_w)z\cos^2\beta,
\qquad
\text{vertical hydrostatic: }
(\gamma_{sat}\cos^2\beta-\gamma_w)z
$$ (eq-infinite-effective)

The first is positive at any inclination. The second is negative when $\cos^2\beta<\gamma_w/\gamma_{sat}$. With $\gamma_{sat}=20$ kN/m³, this happens for $\beta>45.5^\circ$.

A negative effective normal stress means the soil skeleton on the slip surface is in tension. Soil carries almost no tension, so calculating on as if nothing happened has no mechanical meaning. `factor_of_safety` follows Eq. {eq}`eq-infinite-fs` as written, so the friction term turns negative and works against the resistance from cohesion. On a steep slope, the factor of safety itself can become negative. As [Chapter 3, Section 12.1](#practice-section-12-1) notes, how to treat this, for example by taking negative values as zero or by placing a tension crack, has to be decided separately. Add a test that the value is negative only for vertical hydrostatic pressure.

```{literalinclude} examples/test_infinite_slope.py
:language: python
:pyobject: test_only_the_vertical_rule_makes_the_effective_stress_negative
```

---

(infinite-section-6)=

## 6. Print the results for different conditions

Use the functions so far to print values for a range of conditions. Download {download}`run_infinite_slope.py <examples/run_infinite_slope.py>`, put it in `lem-practice`, and run it.

```bash
uv run python run_infinite_slope.py
```

```{literalinclude} examples/output/run_infinite_slope.txt
:language: text
```

Items 1. to 4. are the values from Sections 3 to 5. Item 5. puts the water table 2 m below the ground surface and varies the depth $z$ of the slip surface. In every column of the table, the deeper the slip surface, the smaller the factor of safety. This is because $\sigma_n$ and $\tau$ both grow with $z$, while the resistance from cohesion $c'$ does not depend on depth. Below the water table, the pore water pressure adds to this, so the factor of safety drops further.

In other words, in the infinite slope model, the factor of safety keeps falling as the slip surface goes deeper. An upper limit on the depth of the slip surface, such as the thickness of soil above bedrock, therefore has to be given separately. Searching over depth for the smallest factor of safety is the simplest search for the {term}`critical slip surface`. As [Chapter 3, Section 12.4](#practice-section-12-4) notes, computing the factor of safety and searching for the critical slip surface are separate problems. Finally, add a test that a deeper slip surface has a smaller factor of safety.

```{literalinclude} examples/test_infinite_slope.py
:language: python
:pyobject: test_a_deeper_plane_is_less_stable
```

If `uv run pytest` shows `7 passed`, all the tests of this practice pass.

---

(infinite-trouble)=

## Troubleshooting

| What you see | Cause and fix |
|---|---|
| `ModuleNotFoundError: No module named 'infinite_slope'` | You are running outside `lem-practice`, or the file has a different name. Move into `lem-practice` and check that `infinite_slope.py` is there. (→[Setup](#infinite-setup)) |
| `ModuleNotFoundError: No module named 'numpy'` | You are running without `uv run`, with a Python whose environment has no NumPy. Run `uv run python …` or `uv run pytest`. (→[Setup](#infinite-setup)) |
| `AttributeError: module 'infinite_slope' has no attribute …` | A function the tests use is not yet in `infinite_slope.py`. Also check the spelling of the function's name. (→[Section 1](#infinite-section-1) to [Section 4](#infinite-section-4)) |
| `ValueError: h_w must be between 0 and z` | `column_weight` received a water table below the slip surface or above the ground surface. (→[Section 4](#infinite-section-4)) |
| The factor of safety is negative, or far from the values in the table | Check that angles in degrees are not passed straight to `math.sin`, `math.cos` or `math.tan`. Convert them to radians with `math.radians`. (→[Section 1](#infinite-section-1)) |
| The factor of safety differs slightly from the values in the table | Check that the unit weight of water `GAMMA_W` is 9.81 kN/m³. (→[Section 1](#infinite-section-1), [Section 4](#infinite-section-4)) |

## Summary

- The traction on the slip surface splits, using the outward unit normal vector, into a normal stress, positive in compression, and a shear component (→[Section 2](#infinite-section-2))
- In an infinite slope, the forces on the two sides of a column cancel. So equilibrium alone determines the force on the base, without any assumption on the interslice forces (→[Section 2](#infinite-section-2))
- The factor of safety is the ratio of the shear strength to the mobilized shear stress. The $\sigma_n$ and $\tau_m$ of the base in Chapter 1, Section 6 are those of the base of an infinite slope inclined at 16.70° (→[Section 3](#infinite-section-3))
- How the pore water pressure is set depends on the assumed groundwater flow. The ratio of $u$ for seepage parallel to the slope to $u$ for vertical hydrostatic pressure is $\cos^2\beta$ (→[Section 4](#infinite-section-4))
- With vertical hydrostatic pressure, the effective normal stress becomes negative on steep slopes. How to treat this has to be decided separately (→[Section 5](#infinite-section-5))
- With cohesion, the deeper the slip surface, the smaller the factor of safety. An upper limit on the depth of the slip surface has to be given separately (→[Section 6](#infinite-section-6))

---

## Review questions

Click a question to see its answer. Do the (Try it) questions in `lem-practice`.

:::{dropdown} Q1. Why does an infinite slope determine the force on the base without any assumption on the interslice forces?
:icon: question

Because the forces on the two sides of a column are equal in size and opposite in direction, and cancel. The slope is the same everywhere, so the left and right sides are in the same state. The slip surface therefore carries the whole weight of the column, and equilibrium alone determines $\sigma_n$ and $\tau$. (→[Section 2](#infinite-section-2))
:::

:::{dropdown} Q2. For a dry slope with $\beta=25^\circ$ and $z=3$ m, find $\sigma_n$, $\tau$ and $F_s$. The other conditions are as in Section 3.
:icon: question

Since $w=18\times3=54$ kPa, $\sigma_n=54\cos^2 25^\circ=44.36$ kPa and $\tau=54\sin 25^\circ\cos 25^\circ=20.68$ kPa. Then $F_s=(10+44.36\tan 30^\circ)/20.68=1.722$. Passing `base_stresses(25.0, 54.0)` to `factor_of_safety` gives the same value. (→[Section 2](#infinite-section-2), [Section 3](#infinite-section-3))
:::

:::{dropdown} Q3. (Try it) As a seismic inertia force, apply a horizontal force $kw$ to the column in the direction of sliding. Write a `base_stresses` that includes it, and find $F_s$ for the dry slope of Section 3 with $k=0.2$.
:icon: question

Add a component $-kw$ in the direction of sliding (the negative $x$ direction) to the vector of the column's weight. Write the following function at the end of `test_infinite_slope.py`.

```{literalinclude} examples/test_answers.py
:language: python
:pyobject: base_stresses_seismic
```

Then start Python with `uv run python`, and call it after `from test_infinite_slope import base_stresses_seismic`. `base_stresses_seismic(30.0, 90.0, 0.2)` returns $\sigma_n=59.71$ kPa and $\tau=52.47$ kPa, which gives $F_s=0.848$. With $k=0.1$, $F_s=1.022$. The horizontal force reduces the component that presses on the slip surface and increases the component that drives sliding. So in the factor of safety, $\sigma_n$ in the numerator falls and $\tau$ in the denominator rises. (→[Section 2](#infinite-section-2))
:::

:::{dropdown} Q4. For the same water table, why do seepage parallel to the slope and vertical hydrostatic pressure give different pore water pressures?
:icon: question

Because they assume different directions for the equipotential lines. With seepage parallel to the slope, the equipotential lines are perpendicular to the slope. The pressure head at a point on the slip surface is therefore $h_w\cos^2\beta$, the difference in elevation between that point and the point where the equipotential line through it meets the water table. Vertical hydrostatic pressure amounts to treating the equipotential lines as vertical. In other words, the vertical distance $h_w$ to the water table is itself the pressure head. (→[Section 4](#infinite-section-4))
:::

:::{dropdown} Q5. (Try it) If a negative effective normal stress is taken as zero, how does $F_s$ change for vertical hydrostatic pressure on a slope with $\beta=50^\circ$ and $z=5$ m, with the water table at the ground surface?
:icon: question

Pass `min(u, sigma_n)` to `factor_of_safety` in place of $u$. This sets $\sigma_n-u$ to zero only when it is negative. Here $\sigma_n-u=-7.73$ kPa, so $F_s=0.112$ as it stands, and 0.203 when it is taken as zero. Once it is taken as zero, only cohesion resists. (→[Section 5](#infinite-section-5))
:::

:::{dropdown} Q6. On a dry slope without cohesion ($c'=0$), does the factor of safety change with the depth of the slip surface?
:icon: question

It does not. With $c'=0$, $F_s=\tan\phi'/\tan\beta$, and $z$ drops out of the equation. For example, with $\phi'=35^\circ$ and $\beta=30^\circ$, $F_s=1.213$ at every depth. (→[Section 6](#infinite-section-6))
:::

---

## What to read next

This practice dealt with a model in which the equilibrium of one column alone determines the forces on the slip surface. On a circular slip surface, the base of each {term}`slice` has a different direction, and the interslice forces do not cancel. [Practice 2, "Computing the factor of safety of a circular slip with the method of slices"](practice-slices-2d.md) puts into code how each method achieves {term}`closure`. It also checks that a plane slip surface returns the values of this practice.
