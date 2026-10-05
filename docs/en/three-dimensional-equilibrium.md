---
title: "Equilibrium equations satisfied by 3D LEM"
lang: en
translated_from: "0970d91"
translated_on: 2026-10-05
---

# Equilibrium equations satisfied by 3D LEM

A rigid body in 3D has six equilibrium equations. This page collects which of the six each method of LEM extended to 3D satisfies, as checked in the original papers. The check was made in October 2026. Where the full text of the original paper could not be read, the method was checked through its abstract or through other papers that describe it, and the tables say so.

This page assumes that you have read Sections 7 to 9 of [Chapter 2](what-is-limit-equilibrium-method.md). The terms and symbols are collected in the [Glossary](lem-glossary.md).

---

(equilibrium-section-1)=

## 1. How the methods were checked

Papers set up their axes in different ways. This page restates every paper in the following common axes.

- $x$: horizontal, parallel to the main {term}`direction of sliding`
- $y$: horizontal, normal to the direction of sliding (lateral)
- $z$: vertical, upward

The six equilibrium equations are written $\sum F_x$, $\sum F_y$, $\sum F_z$, $\sum M_x$, $\sum M_y$ and $\sum M_z$. $\sum M_y$ is the moment about a horizontal axis normal to the direction of sliding, which corresponds to the moment about the center of a circle in 2D. The moment about the {term}`axis of rotation <center of moments>` in [Chapter 2, Section 8](#what-section-8) is also this equation in most cases. $\sum M_z$, on the other hand, is the moment about a vertical axis.

For each method, three questions were kept apart.

1. Does it solve each equilibrium equation for the whole mass, or does the equation hold only by symmetry?
2. Which equilibrium equations does it satisfy for each {term}`column`?
3. How does the paper itself describe the method's rigor?

The sources are sorted into four kinds. DOIs were checked against the publisher's or Crossref's records.

- Full text: the full text of the original paper was read
- Predecessor's full text: the original paper could not be read, but the full text of an earlier report or paper in which the same authors present the same method was
- Abstract: only the abstract of the original paper was read
- Secondary sources: only other papers or documents that describe the method were read

---

(equilibrium-section-2)=

## 2. Summary tables

The symbols in the tables mean the following.

- ✓: holds for the whole mass without relying on symmetry. Most are solved as equations; those marked ※ or † follow from other equations
- S: the method handles only symmetric masses, and the equation holds by symmetry. It is not solved as an equation
- ✗: not treated as an equation. It may hold by symmetry for a symmetric mass, but not in general
- ?: could not be confirmed
- ( ): based not on the full text of the original paper but on a predecessor's full text, the abstract or secondary sources
- ＊: the paper does not mention this equation. It is inferred from the shape of the {term}`slip surface` and the assumptions

The column methods that extend 2D methods are summarized in the following table.

| Method and source | $\sum F_x$ | $\sum F_y$ | $\sum F_z$ | $\sum M_x$ | $\sum M_y$ | $\sum M_z$ | Equations satisfied for each column | Sources read |
|---|---|---|---|---|---|---|---|---|
| Hovland method: Hovland (1977) | ? | ? | ? | ? | ? | ? | Intercolumn forces ignored; base normal force taken as a component of the weight (secondary sources) | Abstract, secondary sources |
| 3D Spencer method: Chen and Chameau (1983) | (✓) | (S)＊ | (✓) | (S)＊ | (✓) | (S)＊ | $F_x$ and $F_z$ projected onto the central section, and $M_y$ about the center of the base | Abstract, predecessor's full text |
| 3D ordinary method of slices: Ugai et al. (1986) | ✗ | S＊ | ✗ | S＊ | ✓ | S＊ | Force normal to the base | Full text |
| 3D simplified Bishop method: Hungr (1987), Hungr et al. (1989) | (✗) | (✗) | (✓)※ | (✗) | (✓) | (✗) | Vertical force | Abstract, secondary sources |
| 3D simplified Janbu method: Ugai (1987) | ✓ | ✗ | ✓ | ✗ | ✗ | ✗ | Force in one direction | Full text |
| 3D simplified Bishop method: Ugai and Hosobori (1988) | ✗ | ✗ | ✓ | ✗ | ✓ | ✗ | Force in one direction | Full text |
| 3D simplified Janbu method: Ugai and Hosobori (1988) | ✓ | ✗ | ✓ | ✗ | ✗ | ✗ | Force in one direction | Full text |
| 3D Spencer method: Ugai and Hosobori (1988) | ✓ | ✗ | ✓ | ✗ | ✓ | ✗ | Force in one direction | Full text |
| 3D Spencer method: Ugai and Hosobori (1989) | ✓ | ✗ | ✓ | ✗ | ✓ | ✗ | Force in one direction | Full text |
| 3D GLE: Lam and Fredlund (1993) | ? | ? | ? | ? | ? | ? | ? | Abstract, secondary sources |
| Spencer type: Chen et al. (2003) | (✓) | (✓) | (✓) | (✗) | (✓) | (✗) | Force in one direction | Abstract, predecessor's full text |
| 3D Spencer method: Jiang and Yamagami (2004) | ✓ | ✗ | ✓† | ✗ | ✓ | ✗ | Force in one direction | Full text |
| 3D Morgenstern–Price method: Cheng and Yip (2007) | (✓) | (✓) | (✓)※ | (✓) | (✓) | (✗) | Vertical force | Abstract, secondary sources |

※ Holds by summing the vertical force equilibrium of every column.

† Not written as an equation in the paper. It follows from the column equations and $\sum F_x$ for the whole mass ([Section 3.7](#equilibrium-section-3-7)).

Methods that are not column extensions of 2D methods, and methods checked for comparison, are summarized in the following table.

| Method and source | $\sum F_x$ | $\sum F_y$ | $\sum F_z$ | $\sum M_x$ | $\sum M_y$ | $\sum M_z$ | Equations satisfied for each column | Sources read |
|---|---|---|---|---|---|---|---|---|
| Zhang (1988) | (✓) | ? | (✓) | (S) | (✓) | (S) | Force (secondary sources) | Abstract, secondary sources |
| Variational method: Leshchinsky and Huang (1992) | (✓) | ? | (✓) | (S) | (✓) | (S) | No division into columns | Abstract, secondary sources |
| Huang et al. (2002) | (✓) | (✓) | (✓) | (✓) | (✓) | (✗) | ? | Abstract, secondary sources. The symbols follow Jiang and Zhou (2018); Zhu and Qian (2007) say it roughly satisfies four |
| Zhu and Qian (2007), rigorous solution | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | May divide into columns, but sets up equilibrium only as the six whole-mass equations | Full text |
| Zhu and Qian (2007), quasi-rigorous solution | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | Same as the rigorous solution | Full text |
| Zheng (2007) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | No division into columns | Full text |
| Zheng (2009) | (✓) | (✓) | (✓) | (✓) | (✓) | (✓) | No division into columns | Abstract, secondary sources |
| 3D Morgenstern–Price method: Zheng (2012) | (✓) | (✓) | (✓) | (✓) | (✓) | (✓) | No division into columns | Abstract, secondary sources |
| Jiang and Zhou (2018) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Divides into columns, but sets up equilibrium only as the six whole-mass equations | Full text |

---

(equilibrium-section-3)=

## 3. Evidence for each method

Each section gives the scope, the assumption about the {term}`intercolumn forces <interslice force>`, the unknowns solved for, the equilibrium satisfied and the paper's own description, in that order. Quotes from the originals are in the collapsed blocks, with page and equation numbers.

(equilibrium-section-3-1)=

### 3.1 Hovland (1977): the Hovland method

The original paper could not be read. What follows comes from the descriptions in Chen (1981), Ugai et al. (1986), Ugai (1987) and Ugai and Hosobori (1989). In the original axes, $Y$ is the direction of sliding, $X$ is lateral and $Z$ is vertical.

- Ignores all intercolumn forces, and finds the normal and shear forces on the base from components of each column's weight
- Takes the {term}`factor of safety` as the ratio of the total resistance to the total driving action over the slip surface
- The descriptions disagree on equilibrium of the whole mass. Ugai et al. (1986) say that the method finds the factor of safety from moment equilibrium of the whole mass. Ugai (1987) and Ugai and Hosobori (1989), on the other hand, say that it satisfies no equilibrium of the whole mass at all. The table shows ?, because the original paper was not checked

:::{dropdown} Quotes from the originals
- Chen (1981), pp. 31–32: “defining the factor of safety as the ratio of the total available resistance along a failure surface to the total mobilized stress along it. In order to simplify the analysis, the ordinary method of slices was used. Thus the inter-column forces can be ignored and both normal and shear stresses on the base of each column are obtained simply as the component of the weight of the column.”
- Ugai et al. (1986), p. 268: 「各柱体の力のつり合いよりすべり面上の垂直力ΔNとせん断力ΔT（x軸に平行と仮定）を求め，土塊全体のモーメントのつり合いより安全率を決定するというものである．」「このような仮定のもとではy軸方向の力のつり合いが成り立たないからである．」
- Ugai (1987), p. 14: 「Hovlandの方法はすべり土塊全体のつり合い条件（力のつり合い，モーメントのつり合い）を何も満たしていないため，計算結果の信頼性に疑問が生じる．」
- Ugai and Hosobori (1989), p. 183: 「Hovland法は簡便であるが土塊全体のつり合いが全く満たされない」
:::

(equilibrium-section-3-2)=

### 3.2 Chen and Chameau (1983): the 3D Spencer method

The full text of the 1983 paper is not publicly available. Its abstract is almost word for word the summary of Chen's (1981) report, so the content was checked in the full text of that report. The report was written under the supervision of Chameau and others, and presents the same method as the program LEMIX. The equations may still have changed in the body of the 1983 paper. In the original axes, $X$ is the direction of sliding, $Y$ is vertical upward and $Z$ is lateral. The axis of rotation is parallel to $Z$, which corresponds to $y$ in the common axes.

- **Scope**: handles only symmetric {term}`sliding masses <sliding mass>`, and divides only half of the mass into columns. The slip surface is a surface of revolution; the 1983 paper centers on an ellipsoid of revolution
- **Intercolumn forces**: the forces on faces normal to the direction of sliding are assumed to have the same inclination $\theta$ throughout the mass. The shear forces on the lateral faces (faces normal to $y$) are also included, but not as unknowns: they are known values set from the $K_0$ state. The normal forces on the lateral faces do not appear in the equations
- **Unknowns**: two, the factor of safety $F$ and the inclination $\theta$. The direction of sliding is fixed along $x$
- **Whole mass**: uses equilibrium of $\sum F_x$ and $\sum F_z$. Because $\theta$ is constant, the two reduce to one equation. The method solves this together with the moment equation about the axis of rotation ($\sum M_y$). $\sum F_y$, $\sum M_x$ and $\sum M_z$ hold by symmetry for the whole mass, taken together with its mirror half
- **Each column**: satisfies two force equations projected onto the central section, and one moment equation about the center of the base. The moment equation is used to find the height at which the intercolumn force acts. In other words, the method satisfies each column's moment equilibrium by the position of the intercolumn force, but only about one axis parallel to $y$. It has no $F_y$, $M_x$ or $M_z$ for each column
- **Approximation in the force equations**: Ugai et al. (1986) point out that these column force equations ignore the $y$ component of the {term}`base normal force`
- **The paper's description**: the abstract says that force and moment equilibrium are satisfied for each column as well as for the whole mass. This means the three equations in the projected plane, not the six equations

:::{dropdown} Quotes from the originals
- Abstract of the 1983 paper: “The failure mass is assumed to be symmetrical and divided into many vertical columns. The inter-slice forces have the same inclination throughout the mass, and the inter-column shear forces are parallel to the base of the column and function of their positions. Force and moment equilibria are satisfied for each column as well as for the total mass.”
- Chen (1981), p. 57: “If the mass is divided into 600 vertical columns (m = 20, n = 30), and the geometry is assumed to be symmetrical, the number of the unknowns remaining are 0.5 · 6 · m · n = 0.5 · 6 · 20 · 30 = 1800”. Assumption (1): “The failure mass is symmetrical”
- Chen (1981), p. 69: “Fig. 3-15 shows the force system projected on the central plane (X-Y plane) of a column provided that dz is very small.”
- Chen (1981), p. 74, Eq. (3.34): “If the whole system is in equilibrium, then the sum of all forces in the system must be equal to zero: Σ Q = 0”. Eq. (3.34a): “The sum of all moment about any point (Fig. 3.11) must be equal to zero: Σ Q cos (θ − α) (r − h_Q cos α) = 0”
- Chen (1981), pp. 74–75, Eq. (3.35): “where the value of Q h_Q can be obtained by summing all moments in a column at the center of the base of that column”
- Chen (1981), p. 75: “In these equations the only two unknowns are, (1) the inclination of interslice force and (2) the factor of safety F.”
- Ugai et al. (1986), p. 268: 「分割柱に作用する力のつり合いを考えるにあたって，底面の垂直力ΔNがy方向成分を有することを無視している点である．したがって，彼らの論文中の式（9），（10）は誤りである．」
:::

(equilibrium-section-3-3)=

### 3.3 The series of studies by Ugai et al. (1986–1989)

The full text of every paper by Ugai et al. is available on J-STAGE. Their axes are the same as the common axes. Ugai et al. extended the 2D methods to 3D one by one. Every method takes force equilibrium of each column in one direction only, and finds the base normal force from it. For the whole mass, the ordinary method of slices then solves one equilibrium equation, the simplified Bishop and simplified Janbu methods two, and the Spencer method three.

| Source | Method | Slip surface | Unknowns | Equations solved for the whole mass |
|---|---|---|---|---|
| Ugai et al. (1986) | 3D ordinary method of slices | Surface of revolution symmetric about the $xz$ plane | $F$ | $\sum M_y$ |
| Ugai (1987) | 3D simplified Janbu method | Arbitrary | $F$, $\eta$ | $\sum F_x$, $\sum F_z$ |
| Ugai and Hosobori (1988) | 3D simplified Bishop method | Surface of revolution | $F$, $\eta$ | $\sum M_y$, $\sum F_z$ |
| Ugai and Hosobori (1988) | 3D simplified Janbu method | Arbitrary | $F$, $\eta$ | $\sum F_x$, $\sum F_z$ |
| Ugai and Hosobori (1988) | 3D Spencer method | Surface of revolution | $F$, $\eta$, $\delta$ | $\sum F_x$, $\sum F_z$, $\sum M_y$ |
| Ugai and Hosobori (1989) | 3D Spencer method | Arbitrary | $F$, $\eta$, $\delta$ | $\sum F_x$, $\sum F_z$, $\sum M_y$ |

- **Intercolumn forces**: every method places its assumption not on the force on each side of a column but on their resultant $\Delta Q$. It does not treat the shear forces on the lateral faces separately either. The ordinary method of slices takes $\Delta Q$ parallel to the slip surface, and adds a separate lateral restraining force $\Delta H$. In the other methods, the component of $\Delta Q$ in the $yz$ plane makes an angle $\tan^{-1}(\eta\tan\alpha_{yz})$ with the horizontal, where $\alpha_{yz}$ is the lateral inclination of the base and $\eta$ is an unknown constant. The Spencer method further assumes that the component in the $xz$ plane makes an unknown angle $\delta$ with the horizontal. Only the inclination in the $xz$ plane is common to all columns. So, unlike in the 2D Spencer method, the resultants of all columns do not line up in one direction
- **Each column**: takes force equilibrium in one direction, normal to the plane containing $\Delta Q$. As a result, even in the simplified Bishop method, the equation for each column is not vertical force equilibrium. In this it differs from Hungr's 3D simplified Bishop method in [Section 3.4](#equilibrium-section-3-4). Moment equilibrium of each column is not mentioned
- **Symmetry**: the 1988 paper mentions neither $\sum F_y$, $\sum M_x$ and $\sum M_z$ nor symmetry. Its worked example is a symmetric slope. The 1987 and 1989 papers, on the other hand, also apply their methods to an asymmetric real slope (the Ontake collapse). There, $\sum F_y$, $\sum M_x$ and $\sum M_z$ need not hold, even by symmetry
- **The papers' description**: the 3D Spencer method is described as a method that satisfies all the equilibrium conditions. This "all" means three: horizontal force, vertical force and moment

:::{dropdown} Quotes from the originals
- Ugai et al. (1986), p. 269: 「xz 面に関して対称なすべり面を仮定する」「すべりの方向は y 軸に垂直と仮定する」. p. 270: 「底面に垂直な方向（ΔN の方向）の力のつり合い式をたてると」
- Ugai (1987), p. 9: 「土塊全体に関して鉛直力と水平力のつり合いを考えると，次の2つの式が得られる．」
- Ugai and Hosobori (1988), p. 22: 「コラム間内力は全体のつり合いに関与しないことを考慮すると，すべり土塊のモーメントのつり合いは」 (Eq. (7))
- Ugai and Hosobori (1988), p. 23: 「これまでに提案してきた三次元簡便法，三次元簡易Bishop法および三次元簡易Janbu法はつり合い条件（水平力・鉛直力のつり合い，モーメントのつり合い）の一部しか満たさないため，得られる解の精度に多少の不安が残る．ここではつり合い条件をすべて満足する方法として，Spencer法の三次元化を試みる．コラム側面に作用する内力の合力 ΔQ_ij の分力のうち ΔQ_1（Fig.3）が水平面と δ（未知定数）の角度をなすと仮定する．」
- Ugai and Hosobori (1988), p. 23: 「S面に垂直な方向の力のつり合いから」 (Eq. (14)). 「式 (15)，(16) をすべり土塊のモーメントのつり合い式 (7)，鉛直力のつり合い式 (9) および水平力のつり合い式 (11) に代入すると3つの式が得られる」「3つの未知数 F, η, δ が計算され」
- Ugai and Hosobori (1989), English abstract, p. 183: “This method is applicable to the case of non-circular slip surface and satisfies moment equilibrium and vertical and horizontal force equilibrium for sliding mass.” p. 186: 「任意形状のすべり面に適用でき，すべり土塊の力とモーメントのつり合いがすべて満たされる三次元安定計算法（非円形Spencer法）を提案し」
:::

(equilibrium-section-3-4)=

### 3.4 Hungr (1987) and Hungr et al. (1989): the 3D simplified Bishop method

The full text of neither paper could be read. What follows comes from the abstracts and from the descriptions in Kalatehjari and Ali (2013), Read (2021) and Zheng (2007).

- **Scope**: Hungr (1987) handles symmetric problems, with a surface of revolution whose central section is a circle. Hungr et al. (1989) also apply the method to nonrotational and asymmetric surfaces
- **Intercolumn forces**: as in the 2D simplified Bishop method, ignores the vertical component of the intercolumn shear force. It does not ignore the intercolumn normal forces or the horizontal shear forces
- **Equilibrium**: finds the factor of safety from vertical force equilibrium of each column and moment equilibrium of the whole mass about the axis of rotation. It does not satisfy horizontal force equilibrium in the direction of sliding
- **Hungr et al. (1989)**: on rotational, symmetric slip surfaces the method agrees well with other methods. On nonrotational or asymmetric surfaces, on the other hand, it gives somewhat low factors of safety

:::{dropdown} Quotes from the originals
- Abstract of Hungr et al. (1989): “Very good correspondence is found in cases of rotational and symmetric sliding surfaces, such as ellipsoids. The Bishop method tends to be conservative when applied to nonrotational and asymmetric surfaces because it neglects internal strength.”
- Kalatehjari and Ali (2013), p. 125: “In this symmetrical problem, a rotational surface with circular central cross section was assumed as the failure surface. Following the assumption of Bishop, Hungr neglected the vertical Inter-column shear forces on the sides of columns. This method considered vertical force equilibriums of all columns as well as overall moment equilibrium of sliding mass about the axis of rotation to establish the equation of FOS.”
- Read (2021): “Hungr's analysis neglects vertical intercolumn shear but not the intercolumn normal forces and horizontal shear forces”
- Zheng (2007), p. 1530: 「有些方法，如 Hungr 法等，甚至连 3 个力平衡条件都未满足，其计算结果可能与坐标轴的选取有关。」
:::

(equilibrium-section-3-5)=

### 3.5 Lam and Fredlund (1993): the 3D GLE

No publicly available full text was found for the paper, for Hungr's (1994) discussion or for Lam and Fredlund's (1994) reply. What follows comes from the abstract and secondary sources.

- **Scope**: one version of the abstract says that the direction of sliding is assumed in advance. Kalatehjari and Ali (2013) say that the method handles symmetric problems, with a surface of revolution and a single direction of sliding
- **Intercolumn forces**: represents the direction of the resultant intercolumn forces by functions of the same form as in the Morgenstern–Price method. Kalatehjari and Ali (2013) say that there are five relations between the normal and shear forces, and that three of them were ignored as having little effect. Chen et al. (2001) say that coefficients $\lambda_3$ and $\lambda_4$ remain, and that $\lambda_3$ was chosen as the value that gives the smallest factor of safety. Which ratio of which components on which faces each relation sets could not be confirmed
- **Equilibrium**: as in the 2D {term}`GLE <general limit equilibrium>`, finds a factor of safety from force equilibrium and another from moment equilibrium, and makes them agree. The secondary sources that give a count, however, put the number of equilibrium equations satisfied at three or four. None says that the method satisfies $\sum M_z$

:::{dropdown} Quotes from the originals
- Abstract: “A generalized model for three-dimensional analysis, using the method of columns, is presented. The model is an extension of the two-dimensional general limit equilibrium formulation. Intercolumn force functions of arbitrary shape can be specified to simulate various directions for the intercolumn resultant forces.”
- Abstract as recorded in ETDE (OSTI): “A direction of movement must be assumed for the analysis.”
- Kalatehjari and Ali (2013), p. 126: “A rotational surface with single direction of movement was assumed as the slip surface. … The basic definition of these inter-column force functions was similar to Morgenstern and Price's (1965) function including five relationships between normal and shear inter-column forces. Lam and Fredlund decided to ignore three out of five inter-column forces due to their insignificance role in typical slopes based on their results of finite element analysis. They also established two different equations of FOS based on moment and force equilibriums”
- Chen et al. (2001), p. 525: 「Lam & Fredlund 在建立条柱法时发现，最终还多出两个系数 λ3，λ4，于是，便进一步假定 λ3 应该在若干个数值中选一个相应安全系数最小的」
- Zhu and Qian (2007), p. 1514: 「大多数条柱法只能满足 3 个平衡条件，严格来说这些方法只适合对称边坡」. The works this sentence cites include Lam and Fredlund (1993)
- Jiang and Yamagami (2004), p. 132: lists Lam and Fredlund (1993) as an example of the “one-directional force and moment equilibrium” methods, which satisfy equilibrium only in the direction of sliding (in the $xz$ plane)
- Jiang and Zhou (2018): “the 3-d methods by Zhang (1988), Hungr et al. (1989), Lam and Fredlund (1993) and Chen et al. (2003) belong to the simplified ones which can satisfy at most four equilibrium conditions”
:::

(equilibrium-section-3-6)=

### 3.6 Chen et al. (2003): a Spencer-type method

Only the abstract of the 2003 paper was read. The content was checked in the full text of Chen et al. (2001), in which the same authors present the same method in Chinese. Its assumptions and the equations it satisfies agree with the abstract, and so does the factor of safety of its worked example, 2.187. In the original axes, $x$ points against the direction of sliding, $y$ is vertical upward and $z$ is lateral.

- **Scope**: also handles asymmetric masses, and assumes no shape for the slip surface. The main direction of sliding is given
- **Intercolumn forces**: the forces on faces normal to the direction of sliding are parallel to the vertical $xz$ plane, with an inclination $\beta$ that is the same for all columns. This assumption corresponds to the 2D Spencer method. The forces on the lateral faces are normal forces in the $y$ direction only, with no shear. A distribution is assumed for the direction $\rho$ of the base shear force
- **Unknowns**: $F$, $\beta$ and $\rho$
- **Whole mass**: satisfies four equations: $\sum F_x$, $\sum F_y$, $\sum F_z$ and the moment about the lateral axis ($\sum M_y$). It has no equation for $\sum M_x$ or $\sum M_z$
- **Each column**: force equilibrium in one direction, normal to the intercolumn force
- **The paper's description**: “complete overall force equilibrium conditions” in the abstract refers to force in three directions for the whole mass. The 2001 paper calls the method an approximate calculation and says that it gives a lower-bound solution

:::{dropdown} Quotes from the originals
- Abstract of the 2003 paper: “The assumption involved in this method is of a parallel intercolumn force inclination, similar to Spencer's method in the two-dimensional (2D) area. It allows for the satisfaction of complete overall force equilibrium conditions and the moment equilibrium requirement about the main axis of rotation.”
- Chen et al. (2001), p. 526: 「a) 作用在行界面（平行于 yoz 平面的界面）的条间力 G 平行于 xoy 平面，其与 x 轴的倾角 β 为常量，这一假定相当于二维领域中的 Spencer 法；b) 作用在列界面（平行于 xoy 平面的界面）的作用力 Q 为水平方向，与 z 轴平行；」
- Chen et al. (2001), p. 527: 「建立与 S′ 垂直的 S 方向的整体平衡方程式 … 建立 z 方向的整体平衡方程式 … 同时建立绕 z 轴的整体力矩平衡方程式」
- Conclusions of Chen et al. (2001): 「由于忽略了条间力的一些剪切分量，同时又假定所有条块的 β 为同一数值，同一列的 ρ 值也为同一数值，故仍属近似算法。由于条间侧面剪力被假定为零，计算成果可能偏小，属下限解。」
:::

(equilibrium-section-3-7)=

### 3.7 Jiang and Yamagami (2004): the 3D Spencer method

The full text is available on J-STAGE. The paper's axes are the same as the common axes.

- **Scope**: searches for an {term}`arbitrary slip surface <general slip surface>` by dynamic programming. Assumes that the whole mass slides in one direction ($x$). The worked examples are symmetric conical embankments
- **Intercolumn forces**: as in Ugai and Hosobori (1989), places the assumption on the resultant $Q$ of the forces on all sides of a column. The component of $Q$ in the $xz$ plane makes an unknown angle $\delta$ with the $x$ axis, and this angle is common to all columns. The component in the $yz$ plane is taken parallel to the $y$ axis. Ugai and Hosobori (1989) inclined this component by $\tan^{-1}(\eta\tan\alpha_{yz})$; the paper does not explain the difference
- **Unknowns**: $F$ and $\delta$
- **Whole mass**: finds a factor of safety $F_f$ from $\sum F_x$ and another, $F_m$, from $\sum M_y$ about an axis of rotation parallel to $y$, and searches for the $\delta$ at which they agree. $\sum F_z$ is not written as an equation. The direction of each column's force equation, however, lies in the $xz$ plane and is the same for all columns. So when the column equations and $\sum F_x$ for the whole mass hold, $\sum F_z$ holds too
- **Symmetry**: does not solve $\sum F_y$, $\sum M_x$ or $\sum M_z$. The paper says that these hold by symmetry for a symmetric mass. It also says that the assumption of a single direction of sliding suits roughly symmetric masses
- **Each column**: takes force equilibrium in one direction, normal to the plane containing $Q$
- **The paper's description**: calls the method a {term}`statically rigorous <complete equilibrium method>` approach that satisfies force and moment equilibrium. On the other hand, it sets most earlier column methods apart as methods that satisfy equilibrium only in the direction of sliding

:::{dropdown} Quotes from the originals
- Abstract (p. 127): “a column method extended from the Spencer safety factor equation for 2D analysis”. “The comparative study presented in this paper strongly supports a recommendation of the use of a statically rigorous limit equilibrium approach satisfying both force and moment equilibrium for a realistic 3D analysis of the slope stability.”
- p. 128: “Q consists of two components, i.e. Q1 in the xz plane and Q2 in the yz plane. The former is inclined at an angle of δ (an unknown constant for all columns) to the x-axis (sliding direction) as in the Spencer method (1967), and the latter is assumed to be parallel to the y-axis.”
- p. 128: “a 3D method for slope stability analysis was presented by Ugai and Hosobori (1989) which could be considered partly as an extension of the Spencer method (Spencer, 1967) for 2D analyses.”
- p. 128: “The normal force N and shear force T acting on the column base can be derived by considering force equilibrium in the direction perpendicular to the Q1QQ2 plane and the Mohr-Coulomb failure criterion at the column base.”
- p. 128: “The summation of moments of all columns about an axis of rotation parallel to the y-axis was used to derive the factor of safety F_m with respect to moment equilibrium.”
- p. 132: “In these methods, force and/or moment equilibrium conditions are satisfied only in the sliding direction (i.e. in the xz plane) but are ignored in the transverse direction (i.e. in the yz plane). Hence, they are sometimes referred to as ‘one-directional force and moment equilibrium’ methods (Huang and Tsai, 2000).”
- p. 133: “When the limit equilibrium equations of the whole sliding mass are considered, therefore, their effects in the transverse direction will be cancelled out. In other words, transverse force and moment equilibrium conditions are automatically satisfied due to symmetry of the problem.”
:::

(equilibrium-section-3-8)=

### 3.8 Cheng and Yip (2007): extension to asymmetric slopes

The full text could not be read. What follows comes from the abstract, from the Slide3 theory document (Rocscience), which reproduces the equations of Cheng and Yip (2007), and from Read (2021), which quotes the paper word for word.

- **Scope**: solves an asymmetric mass as a whole. The direction of sliding is one for all columns, and is solved for as an unknown
- **Intercolumn forces**: places a normal force, a vertical shear force and a horizontal shear force on each face. So the shear forces on the lateral faces are included too. The vertical shear force is the normal force times a coefficient, $\lambda_x$ or $\lambda_y$. The horizontal shear forces in the two directions, on the other hand, are related to each other after the complementary shear stresses of an elastic body. This relation amounts to moment equilibrium of each column about a vertical axis, approximated for small columns
- **Unknowns**: $F$, $\lambda_x$, $\lambda_y$ and the direction of sliding
- **Equilibrium**: uses vertical force equilibrium of each column, and for the whole mass the forces in $x$ and $y$ and the moments about two horizontal axes. There is no equation for the moment of the whole mass about a vertical axis
- **The paper's description**: the abstract says that the direction of sliding is determined from 3D force and moment equilibrium. It does not use the word “rigorous”

:::{dropdown} Quotes from the originals
- Abstract: “Most existing three-dimensional (3D) slope stability analysis methods are based on simple extensions of corresponding two-dimensional (2D) methods of analysis and a plane of symmetry or direction of slide is implicitly assumed. … Under these new formulations, the direction of slide is unique and is determined from 3D force/moment equilibrium.”
- Slide3 theory document: “Let's first consider vertical force equilibrium (z-direction) of a single column.” “Overall force and moment equilibrium in the X and Y directions is given by the following equations.” “We then find the values of F, lamdax, lamday, aprime (sliding direction) that satisfy these 3 equations.”
- Read's (2021) summary: “by using the property of complementary shear (or moment equilibrium in the xy plane), Hy i+1 or Hx i+1 can be determined sequentially from the exterior columns”
- Cheng and Yip (2007) as quoted by Read (2021): “The important concept of complementary shear force which is similar to the complementary shear stress (τxy = τyx) in elasticity has not been used in any 3D slope stability analysis method in the past but is crucial in the present formulation.” “Although the concept of complementary shear stress is applicable only in the infinitesimal sense, if the size of the column is not great this assumption will greatly simplify the equations.”
:::

(equilibrium-section-3-9)=

### 3.9 Methods that solve the six whole-mass equations

Instead of assuming the direction of the intercolumn forces, Zhu and Qian (2007) and Zheng (2007) assume the distribution of {term}`normal stress` on the slip surface. They then solve the six equilibrium equations, treating the whole mass as one body. According to Jiang and Zhou (2018), Zheng (2009) takes the same approach. According to its abstract, Zheng (2012) places the Morgenstern–Price assumption on the {term}`internal forces <internal force>` of the mass. Its exact form could not be confirmed in the full text.

- **Zhu and Qian (2007)**: full text read. Divides the mass into columns to compute the integrals, but sets up equilibrium as whole-mass equations. Presents a rigorous solution that solves the six equations, and a quasi-rigorous solution that leaves out only $\sum M_z$. The paper says that it is the first to obtain a 3D solution that satisfies all six equations
- **Zheng (2007)**: full text read. Finds the factor of safety and five parameters of the normal-stress distribution from the six equations. The direction of sliding is given. Does not divide into columns
- **Zheng (2009)**: abstract read. Solves the same idea as a generalized eigenvalue problem. Does not divide into columns
- **Zheng (2012)**: abstract read. Places the Morgenstern–Price assumption on the internal forces of the sliding mass, and presents the result as the 3D version of a 2D rigorous method of slices. It turns volume integrals into boundary integrals, and so does not divide into columns. That it satisfies the six equations comes from Jiang and Zhou (2018)
- **Jiang and Zhou (2018)**: full text of the authors' manuscript read. Divides into columns, but sets up equilibrium as the six whole-mass equations, and also solves for the direction of sliding as an unknown

:::{dropdown} Quotes from the originals
- Zhu and Qian (2007), p. 1514: 「严格的三维极限平衡法需满足 6 个平衡方程，即 3个方向力平衡条件与绕 3个方向轴的力矩平衡。但大多数条柱法只能满足 3 个平衡条件，严格来说这些方法只适合对称边坡」
- Zhu and Qian (2007), p. 1520: 「由于只忽略了一个最次要的平衡条件，满足其余 5 个平衡条件，这样的解答可称为三维边坡准严格极限平衡解答。」
- Zhu and Qian (2007), p. 1527: 「本文应用滑面正应力修正方法，首次得到满足所有 6 个平衡条件的三维边坡严格极限平衡解答与满足 3 个力平衡和 2 个力矩平衡条件的三维边坡准严格极限平衡解答。」
- Zheng (2007), English abstract, p. 1529: “Up to now, there is no three-dimensional limit equilibrium method that is able to satisfy all six equilibrium conditions. … a rigorous limit equilibrium method for the three-dimensional stability analysis of slope is realized, which satisfies all the six equilibrium conditions and accommodates to slip surfaces of any shape.”
- Zheng (2007), p. 1530: 「迄今为止几乎所有已公开发表的三维方法最多只能满足 4 个平衡条件。除非滑体沿其滑动方向有一对称面且采用对称剖分，否则就没有充足的理由说明计算结果的可靠性。」
- Abstract of Zheng (2009): “Of the existing methods for the three-dimensional (3D) limit equilibrium analysis of slopes, none can simultaneously satisfy all six equilibrium equations. … the proposed method does not need to partition the sliding body into columns.”
- Abstract of Zheng (2012): “the attempts to realize their three-dimensional rigorous counterparts have not yet been realized. Introducing the Morgenstern–Price (M-P) assumption on the internal forces of the slip body, this study presents the three-dimensional version of the M-P method, which is rigorous and applicable to failure surfaces of complex shape. In the formulation, meanwhile, the volume integrals over the slip body are transformed into the boundary integrals, rendering column-partitioning unnecessary.”
- Jiang and Zhou (2018): “the method by Zheng (2012) belongs to the rigorous one which meets all six equilibrium conditions”. “All six equilibrium conditions (three force-equilibrium and three moment-equilibrium conditions) are strictly satisfied in the proposed method.”
:::

(equilibrium-section-3-10)=

### 3.10 Other methods

- **Zhang (1988)**: the abstract says that force and moment equilibrium are satisfied. According to Kalatehjari and Ali (2013), the method handles only symmetric slopes. According to Zheng (2007), it satisfies the three force equations and $\sum M_y$, and $\sum M_x$ and $\sum M_z$ hold automatically by symmetry. Whether it solves $\sum F_y$ as an equation or satisfies it by symmetry could not be confirmed
- **Leshchinsky and Huang (1992)**: finds the distribution of normal stress on the slip surface by a variational method. The abstract says that all the limit equilibrium equations are satisfied. The method, however, handles only symmetric problems. According to Zheng (2007), it satisfies the three force equations and one moment equation about the axis of rotation. Whether it solves $\sum F_y$ as an equation or satisfies it by symmetry could not be confirmed
- **Huang et al. (2002)**: the abstract says that the method uses force and moment equilibrium in two directions. Jiang and Zhou (2018) call it a quasi-rigorous method that satisfies force in three directions and moment in two. Zhu and Qian (2007), on the other hand, say that it roughly satisfies four equations

---

(equilibrium-section-4)=

## 4. Findings

(equilibrium-section-4-1)=

### 4.1 3D Spencer-type methods do not solve all six equations

The 3D Spencer-type methods examined satisfy three or four equations for the whole mass without relying on symmetry. Each uses only one moment equation, $\sum M_y$.

- The symmetric formulation of Chen and Chameau (1983) satisfies $\sum F_x$, $\sum F_z$ and $\sum M_y$. So three hold without relying on symmetry, and the other three hold by symmetry. For each column, it satisfies the three equations in the projected plane
- The formulations of Ugai and Hosobori (1988, 1989) and Jiang and Yamagami (2004) do not presume symmetry. On an asymmetric slope, therefore, $\sum F_y$, $\sum M_x$ and $\sum M_z$ need not hold
- Chen et al. (2003) satisfy four: force in three directions and $\sum M_y$

Zheng (2007) cites Zhang et al. (2005) as a 3D Spencer method that satisfies five equations, leaving out only $\sum M_z$. That paper was not read.

(equilibrium-section-4-2)=

### 4.2 Cheng and Yip's (2007) Morgenstern–Price method does not solve $\sum M_z$

According to the Slide3 theory document and Read (2021), Cheng and Yip (2007) use the five equations other than $\sum M_z$. They do, however, use moment equilibrium of each column about a vertical axis approximately, in the form of complementary shear. Lam and Fredlund (1993) could not be checked in the original paper. The secondary sources that give a count put the number of equations satisfied at three or four, and none says that the method satisfies $\sum M_z$.

(equilibrium-section-4-3)=

### 4.3 Methods that solve all six equations can be confirmed from 2007

3D {term}`LEM <limit equilibrium method>` methods that solve all six equations for the whole mass can be confirmed in the full texts of Zhu and Qian (2007) and Zheng (2007). Later, Zheng (2012) presented a 3D version of the Morgenstern–Price method that satisfies the six equations. That it satisfies them comes from the abstract and from Jiang and Zhou (2018). All of them set up the six equations treating the whole mass as one body. So none is a column method that extends a 2D method by assuming the direction of the intercolumn forces.

The abstract of the variational method of Leshchinsky and Huang (1992) says that all equilibrium is satisfied. The method, however, handles only symmetric problems. According to Zheng (2007), it satisfies the three force equations and one moment equation about the axis of rotation.

---

(equilibrium-section-5)=

## 5. How "rigorous" and "all" are used

In 3D papers, "rigorous" and "satisfies all" are used in two senses.

The first is that the method satisfies all of the equations it treats, which are only some of the six. This sense is common in earlier papers.

- Ugai and Hosobori (1988) call a method that solves three equations, $\sum F_x$, $\sum F_z$ and $\sum M_y$, a method that satisfies all the equilibrium conditions
- Ugai and Hosobori (1989) apply a method that solves the same three equations to an asymmetric slope, and say that force and moment equilibrium are all satisfied
- Jiang and Yamagami (2004) call a method that solves $\sum F_x$ and $\sum M_y$ statically rigorous
- Chen and Chameau (1983) say that the three equations in the projected plane are satisfied for each column as well as for the whole mass
- In Chen et al. (2003), “complete overall force equilibrium” refers only to force in three directions for the whole mass
- The abstracts of Zhang (1988) and of Leshchinsky and Huang (1992) also say that force and moment equilibrium, or all the limit equilibrium equations, are satisfied. According to Zheng (2007), the only moment equation they actually solve is $\sum M_y$

The second sense is that the method satisfies all six equations for the whole mass. This sense is common in papers from 2007 on. Zhu and Qian (2007) and Jiang and Zhou (2018) define a rigorous 3D method as one that satisfies the six equations. They call a method that satisfies the five other than $\sum M_z$ quasi-rigorous. The abstract of Zheng (2012), too, defines rigorous methods as those that satisfy complete equilibrium conditions.

In the papers that take the six equations as the standard, "all" refers to equilibrium of the whole mass. No paper was found that calls the six equations for each column "complete." Some papers also count equations that hold by symmetry and call a solution "rigorous." Zheng (2007) writes that the solution of Zhang (1988), for a symmetric mass divided symmetrically, can be regarded as rigorous.

:::{dropdown} Quotes from the originals
- Jiang and Zhou (2018): “In rigorous 3-d methods for slope stability analysis, all six equilibrium conditions (three directional force and three moment equilibrium equations) should be satisfied for the potential failure mass.”
- Abstract of Zheng (2012): “the “rigorous” methods that satisfy complete equilibrium conditions are more reliable and are preferred.”
- Zheng (2007), p. 1535: 「因滑体均质、对称，如果对称地对滑体进行条分，则关于 z 轴和 x 轴的力矩平衡能被自动满足，此时 X. Zhang 所建议的能满足 3个力平衡和 1个绕 y 轴的力矩平衡的解也可被视为严格解」
- Abstract of Zhang (1988): “The force equilibrium and the moment equilibrium conditions over failure mass are satisfied in the analysis.”
- Abstract of Leshchinsky and Huang (1992): “A 3-D slope-stability-analysis method, explicitly satisfying all limiting-equilibrium equations, is presented.”
:::

---

(equilibrium-section-6)=

## 6. Papers that could not be checked in full

| Source | What could be read | Reason |
|---|---|---|
| Hovland (1977) | Abstract, secondary sources | Paywalled, with no publicly available version |
| Chen and Chameau (1983) | Abstract; full text of the predecessor, Chen (1981) | Paywalled, with no publicly available version |
| Hungr (1987) | Secondary sources | Paywalled; not even the abstract is shown |
| Hungr et al. (1989) | Abstract, secondary sources | Paywalled, with no publicly available version |
| Lam and Fredlund (1993), with its discussion and reply | Abstract, secondary sources | Paywalled, with no publicly available version |
| Chen et al. (2003) | Abstract; full text of the predecessor, Chen et al. (2001) | Paywalled, with no publicly available version |
| Cheng and Yip (2007) | Abstract, secondary sources | Paywalled; the version in the institutional repository has been withdrawn |
| Zheng (2012) | Abstract, secondary sources | Paywalled, with no publicly available version |
| Zhang (1988), Zheng (2009) | Abstract, secondary sources | Paywalled, with no publicly available version |
| Leshchinsky and Huang (1992), Huang et al. (2002) | Abstract, secondary sources | Paywalled, with no publicly available version |
| Zhang et al. (2005) | The description in Zheng (2007) | Outside the scope of this check |
| Duncan (1996) | Abstract | Paywalled; its table of 3D methods could not be checked |

---

## References

DOIs are given only where they were checked against the publisher's or Crossref's records.

### 3D LEM methods

1. Hovland, H. J. (1977). “Three-Dimensional Slope Stability Analysis Method.” *Journal of the Geotechnical Engineering Division*, 103(9), 971–986. [https://doi.org/10.1061/AJGEB6.0000493](https://doi.org/10.1061/AJGEB6.0000493)
2. Chen, R. H. (1981). *Three-Dimensional Slope Stability Analysis*. Joint Highway Research Project, Report JHRP-81-17, Purdue University. [Bibliographic record](https://docs.lib.purdue.edu/jtrp/897/)
3. Chen, R.-H., and Chameau, J.-L. (1983). “Three-dimensional limit equilibrium analysis of slopes.” *Géotechnique*, 33(1), 31–40. [https://doi.org/10.1680/geot.1983.33.1.31](https://doi.org/10.1680/geot.1983.33.1.31)
4. 鵜飼恵三・細堀建司・永瀬英生・榎戸源則（Ugai et al.）(1986)．簡便分割法による斜面の三次元安定解析．*土木学会論文集*，No. 376/III-6，267–276．[https://doi.org/10.2208/jscej.1986.376_267](https://doi.org/10.2208/jscej.1986.376_267)
5. 鵜飼恵三（Ugai）(1987)．簡易Janbu法による斜面の3次元安定解析．*地すべり*，24(3)，8–14．[https://doi.org/10.3313/jls1964.24.3_8](https://doi.org/10.3313/jls1964.24.3_8)
6. Hungr, O. (1987). “An extension of Bishop's simplified method of slope stability analysis to three dimensions.” *Géotechnique*, 37(1), 113–117. [https://doi.org/10.1680/geot.1987.37.1.113](https://doi.org/10.1680/geot.1987.37.1.113)
7. Zhang, X. (1988). “Three-dimensional stability analysis of concave slopes in plan view.” *Journal of Geotechnical Engineering*, 114(6), 658–671. [https://doi.org/10.1061/(ASCE)0733-9410(1988)114:6(658)](https://doi.org/10.1061/%28ASCE%290733-9410%281988%29114%3A6%28658%29)
8. 鵜飼恵三・細堀建司（Ugai and Hosobori）(1988)．簡易Bishop法，簡易Janbu法およびSpencer法の三次元への拡張．*土木学会論文集*，No. 394/III-9，21–26．[https://doi.org/10.2208/jscej.1988.394_21](https://doi.org/10.2208/jscej.1988.394_21)
9. Hungr, O., Salgado, F. M., and Byrne, P. M. (1989). “Evaluation of a three-dimensional method of slope stability analysis.” *Canadian Geotechnical Journal*, 26(4), 679–686. [https://doi.org/10.1139/t89-079](https://doi.org/10.1139/t89-079)
10. 鵜飼恵三・細堀建司（Ugai and Hosobori）(1989)．任意形状の地形とすべり面を有する斜面の安定解析．*土木学会論文集*，No. 412/III-12，183–186．[https://doi.org/10.2208/jscej.1989.412_183](https://doi.org/10.2208/jscej.1989.412_183)
11. Leshchinsky, D., and Huang, C.-C. (1992). “Generalized three-dimensional slope-stability analysis.” *Journal of Geotechnical Engineering*, 118(11), 1748–1764. [https://doi.org/10.1061/(ASCE)0733-9410(1992)118:11(1748)](https://doi.org/10.1061/%28ASCE%290733-9410%281992%29118%3A11%281748%29)
12. Lam, L., and Fredlund, D. G. (1993). “A general limit equilibrium model for three-dimensional slope stability analysis.” *Canadian Geotechnical Journal*, 30(6), 905–919. [https://doi.org/10.1139/t93-089](https://doi.org/10.1139/t93-089)
13. Hungr, O. (1994). “A general limit equilibrium model for three-dimensional slope stability analysis: Discussion.” *Canadian Geotechnical Journal*, 31(5), 793–795. [https://doi.org/10.1139/t94-093](https://doi.org/10.1139/t94-093)
14. Lam, L., and Fredlund, D. G. (1994). “A general limit equilibrium model for three-dimensional slope stability analysis: Reply.” *Canadian Geotechnical Journal*, 31(5), 795–796. [https://doi.org/10.1139/t94-094](https://doi.org/10.1139/t94-094)
15. Huang, C.-C., and Tsai, C.-C. (2000). “New method for 3D and asymmetrical slope stability analysis.” *Journal of Geotechnical and Geoenvironmental Engineering*, 126(10), 917–927. [https://doi.org/10.1061/(ASCE)1090-0241(2000)126:10(917)](https://doi.org/10.1061/%28ASCE%291090-0241%282000%29126%3A10%28917%29)
16. 陈祖煜・弥宏亮・汪小刚（Chen et al.）(2001)．边坡稳定三维分析的极限平衡方法．*岩土工程学报*，23(5)，525–529．[Bibliographic record](https://www.cgejournal.com/cn/article/id/10783)
17. Huang, C.-C., Tsai, C.-C., and Chen, Y.-H. (2002). “Generalized method for three-dimensional slope stability analysis.” *Journal of Geotechnical and Geoenvironmental Engineering*, 128(10), 836–848. [https://doi.org/10.1061/(ASCE)1090-0241(2002)128:10(836)](https://doi.org/10.1061/%28ASCE%291090-0241%282002%29128%3A10%28836%29)
18. Chen, Z., Mi, H., Zhang, F., and Wang, X. (2003). “A simplified method for 3D slope stability analysis.” *Canadian Geotechnical Journal*, 40(3), 675–683. [https://doi.org/10.1139/t03-002](https://doi.org/10.1139/t03-002)
19. Jiang, J.-C., and Yamagami, T. (2004). “Three-Dimensional Slope Stability Analysis Using an Extended Spencer Method.” *Soils and Foundations*, 44(4), 127–135. [https://doi.org/10.3208/sandf.44.4_127](https://doi.org/10.3208/sandf.44.4_127)
20. 张均锋・王思莹・祈涛（Zhang et al.）(2005)．边坡稳定分析的三维 Spencer 法．*岩石力学与工程学报*，24(19)，3434–3439．Pages as given in the reference list of Zheng (2007). [Bibliographic record](https://rockmech.whrsm.ac.cn/CN/abstract/abstract21749.shtml)
21. Cheng, Y. M., and Yip, C. J. (2007). “Three-Dimensional Asymmetrical Slope Stability Analysis—Extension of Bishop's, Janbu's, and Morgenstern–Price's Techniques.” *Journal of Geotechnical and Geoenvironmental Engineering*, 133(12), 1544–1555. [https://doi.org/10.1061/(ASCE)1090-0241(2007)133:12(1544)](https://doi.org/10.1061/%28ASCE%291090-0241%282007%29133%3A12%281544%29)
22. 朱大勇・钱七虎（Zhu and Qian）(2007)．三维边坡严格与准严格极限平衡解答及工程应用．*岩石力学与工程学报*，26(8)，1513–1528．[Bibliographic record](https://rockmech.whrsm.ac.cn/CN/abstract/abstract22094.shtml)
23. 郑宏（Zheng）(2007)．严格三维极限平衡法．*岩石力学与工程学报*，26(8)，1529–1537．[Bibliographic record](https://rockmech.whrsm.ac.cn/CN/abstract/abstract22095.shtml)
24. Zheng, H. (2009). “Eigenvalue problem from the stability analysis of slopes.” *Journal of Geotechnical and Geoenvironmental Engineering*, 135(5), 647–656. [https://doi.org/10.1061/(ASCE)GT.1943-5606.0000071](https://doi.org/10.1061/%28ASCE%29GT.1943-5606.0000071)
25. Zheng, H. (2012). “A three-dimensional rigorous method for stability analysis of landslides.” *Engineering Geology*, 145–146, 30–40. [https://doi.org/10.1016/j.enggeo.2012.06.010](https://doi.org/10.1016/j.enggeo.2012.06.010)
26. Jiang, Q., and Zhou, C. (2018). “A rigorous method for three-dimensional asymmetrical slope stability analysis.” *Canadian Geotechnical Journal*, 55(4), 495–513. [https://doi.org/10.1139/cgj-2017-0317](https://doi.org/10.1139/cgj-2017-0317)

### Reviews and documents describing the methods

27. Duncan, J. M. (1996). “State of the Art: Limit Equilibrium and Finite-Element Analysis of Slopes.” *Journal of Geotechnical Engineering*, 122(7), 577–596. [https://doi.org/10.1061/(ASCE)0733-9410(1996)122:7(577)](https://doi.org/10.1061/%28ASCE%290733-9410%281996%29122%3A7%28577%29)
28. Kalatehjari, R., and Ali, N. (2013). “A Review of Three-Dimensional Slope Stability Analyses based on Limit Equilibrium Method.” *Electronic Journal of Geotechnical Engineering*, 18, Bund. A, 119–134. [Bibliographic record](https://web.archive.org/web/20131228112355/http://www.ejge.com/2013/Ppr2013.011alr.pdf)
29. Read, J. (2021). “Three-dimensional limit equilibrium slope stability analyses, method, and design acceptance criteria uncertainties.” *SSIM 2021: Second International Slope Stability in Mining*, 3–10. [https://doi.org/10.36487/ACG_repo/2135_0.01](https://doi.org/10.36487/ACG_repo/2135_0.01)
30. Rocscience. “Slide3 – 3D Limit Equilibrium Slope Stability Overview.” Accessed October 2026. [Bibliographic record](https://static.rocscience.cloud/assets/verification-and-theory/Slide3/3D-Limit-Equilibrium-Slope-Stability.pdf)
