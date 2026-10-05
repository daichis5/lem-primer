---
title: "3次元のLEMが満たすつり合い式"
lang: ja
---

# 3次元のLEMが満たすつり合い式

3次元の剛体には，6つのつり合い式がある．このページは，3次元に拡張したLEMの各手法が，その6つのうちどれを満たすかを，原論文で確かめた結果をまとめている．調べたのは2026年10月である．原論文の全文を読めなかった手法は，要旨や，その手法を紹介した別の論文で確かめ，そのことを表に示している．

このページは，[第2章](what-is-limit-equilibrium-method.md)の7節から9節を読んだ前提で進める．用語と記号は，[用語集](lem-glossary.md)にまとめている．

---

(equilibrium-section-1)=

## 1. 調べ方

座標の取り方は，論文ごとに違う．このページでは，次の共通の取り方に読み替えて書く．

- $x$：水平で，主な{term}`すべり方向 <全体すべり方向>`に平行
- $y$：水平で，すべり方向に直交する（横方向）
- $z$：鉛直上向き

6つのつり合い式は，$\sum F_x$，$\sum F_y$，$\sum F_z$，$\sum M_x$，$\sum M_y$，$\sum M_z$ と書く．$\sum M_y$ は，すべり方向に直交する水平な軸まわりのモーメントで，2次元の円弧の中心まわりのモーメントにあたる．[第2章 8節](#what-section-8)の{term}`回転軸 <モーメントの中心>`まわりのモーメントも，多くはこの式である．一方，$\sum M_z$ は，鉛直な軸まわりのモーメントを表す．

手法ごとに，次の3つを分けて調べた．

1. 土塊全体で，つり合いを式として解いているか．それとも，対称性によってだけ成り立つか
2. 各{term}`カラム`で，どのつり合いを満たしているか
3. 論文自身が，その手法の厳密さをどう述べているか

確かめた資料は，次の4種類に分けている．DOIは，出版社かCrossrefの書誌情報で照合した．

- 全文：原論文の全文を読んだ
- 前身の全文：原論文は読めなかったが，同じ著者が同じ手法を書いた，それより前の報告書や論文の全文を読んだ
- 要旨：原論文の要旨だけを読んだ
- 二次文献：その手法を紹介した別の論文や資料だけを読んだ

---

(equilibrium-section-2)=

## 2. 一覧表

表の記号の意味は，次のとおりである．

- ✓：土塊全体で，対称性に頼らずに成り立つ．多くは式として解く．※と†は，ほかの式から導けるもの
- S：対称な土塊だけを扱う手法で，対称性によって成り立つ．式としては解かない
- ✗：式として扱わない．対称な土塊では対称性で成り立つこともあるが，一般には成り立たない
- ?：確かめられなかった
- （　）：原論文の全文ではなく，前身の全文，要旨，または二次文献による
- ＊：論文はこの式に触れていない．{term}`すべり面`の形と仮定から読み取った

カラム法で，2次元の手法を拡張したものを，次の表にまとめる．

| 手法・文献 | $\sum F_x$ | $\sum F_y$ | $\sum F_z$ | $\sum M_x$ | $\sum M_y$ | $\sum M_z$ | カラムごとに満たす式 | 確かめた資料 |
|---|---|---|---|---|---|---|---|---|
| Hovland法：Hovland (1977) | ? | ? | ? | ? | ? | ? | カラム間力を無視し，底面垂直力を重さの成分とする（二次文献） | 要旨，二次文献 |
| 3次元のSpencer法：Chen and Chameau (1983) | (✓) | (S)＊ | (✓) | (S)＊ | (✓) | (S)＊ | 中央断面に射影した $F_x$ と $F_z$，底面の中央まわりの $M_y$ | 要旨，前身の全文 |
| 3次元の簡便分割法：Ugai et al. (1986) | ✗ | S＊ | ✗ | S＊ | ✓ | S＊ | 底面に垂直な方向の力 | 全文 |
| 3次元の簡易Bishop法：Hungr (1987)，Hungr et al. (1989) | (✗) | (✗) | (✓)※ | (✗) | (✓) | (✗) | 鉛直方向の力 | 要旨，二次文献 |
| 3次元の簡易Janbu法：Ugai (1987) | ✓ | ✗ | ✓ | ✗ | ✗ | ✗ | 1方向の力 | 全文 |
| 3次元の簡易Bishop法：Ugai and Hosobori (1988) | ✗ | ✗ | ✓ | ✗ | ✓ | ✗ | 1方向の力 | 全文 |
| 3次元の簡易Janbu法：Ugai and Hosobori (1988) | ✓ | ✗ | ✓ | ✗ | ✗ | ✗ | 1方向の力 | 全文 |
| 3次元のSpencer法：Ugai and Hosobori (1988) | ✓ | ✗ | ✓ | ✗ | ✓ | ✗ | 1方向の力 | 全文 |
| 3次元のSpencer法：Ugai and Hosobori (1989) | ✓ | ✗ | ✓ | ✗ | ✓ | ✗ | 1方向の力 | 全文 |
| 3次元のGLE：Lam and Fredlund (1993) | ? | ? | ? | ? | ? | ? | ? | 要旨，二次文献 |
| Spencer型：Chen et al. (2003) | (✓) | (✓) | (✓) | (✗) | (✓) | (✗) | 1方向の力 | 要旨，前身の全文 |
| 3次元のSpencer法：Jiang and Yamagami (2004) | ✓ | ✗ | ✓† | ✗ | ✓ | ✗ | 1方向の力 | 全文 |
| 3次元のMorgenstern–Price法：Cheng and Yip (2007) | (✓) | (✓) | (✓)※ | (✓) | (✓) | (✗) | 鉛直方向の力 | 要旨，二次文献 |

※ 各カラムの鉛直方向の力のつり合いを足し合わせると，成り立つ．

† 論文は式として書いていない．各カラムの式と，土塊全体の $\sum F_x$ から導ける（[3.7節](#equilibrium-section-3-7)）．

カラム法で2次元の手法を拡張したものではない手法や，比べるために調べた手法を，次の表にまとめる．

| 手法・文献 | $\sum F_x$ | $\sum F_y$ | $\sum F_z$ | $\sum M_x$ | $\sum M_y$ | $\sum M_z$ | カラムごとに満たす式 | 確かめた資料 |
|---|---|---|---|---|---|---|---|---|
| Zhang (1988) | (✓) | ? | (✓) | (S) | (✓) | (S) | 力（二次文献） | 要旨，二次文献 |
| 変分法：Leshchinsky and Huang (1992) | (✓) | ? | (✓) | (S) | (✓) | (S) | カラムに分けない | 要旨，二次文献 |
| Huang et al. (2002) | (✓) | (✓) | (✓) | (✓) | (✓) | (✗) | ? | 要旨，二次文献．記号はJiang and Zhou (2018)の紹介による．Zhu and Qian (2007)は，大まかに4つを満たすとする |
| Zhu and Qian (2007)の厳密解 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | カラムに分けることもあるが，つり合いは土塊全体の6つの式だけで立てる | 全文 |
| Zhu and Qian (2007)の準厳密解 | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | 厳密解と同じ | 全文 |
| Zheng (2007) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | カラムに分けない | 全文 |
| Zheng (2009) | (✓) | (✓) | (✓) | (✓) | (✓) | (✓) | カラムに分けない | 要旨，二次文献 |
| 3次元のMorgenstern–Price法：Zheng (2012) | (✓) | (✓) | (✓) | (✓) | (✓) | (✓) | カラムに分けない | 要旨，二次文献 |
| Jiang and Zhou (2018) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | カラムに分けるが，つり合いは土塊全体の6つの式だけで立てる | 全文 |

---

(equilibrium-section-3)=

## 3. 手法ごとの根拠

各節では，対象，{term}`カラム間力 <スライス間力>`の仮定，解く未知量，満たすつり合い，論文自身の言い方の順に書く．原文の引用は，折りたたみの中に，ページと式番号を付けて載せている．

(equilibrium-section-3-1)=

### 3.1 Hovland (1977)：Hovland法

原論文は読めなかった．次のことは，Chen (1981)，Ugai et al. (1986)，Ugai (1987)，Ugai and Hosobori (1989)の紹介による．元の座標は，$Y$ がすべり方向，$X$ が横方向，$Z$ が鉛直である．

- カラム間力をすべて無視し，各カラムの重さの成分から，底面に働く垂直力とせん断力を求める
- {term}`安全率`は，すべり面全体の抵抗の和と，滑動の和の比とする
- 土塊全体のつり合いについては，紹介が食い違う．Ugai et al. (1986)は，土塊全体のモーメントのつり合いから安全率を決めるとする．一方，Ugai (1987)とUgai and Hosobori (1989)は，土塊全体のつり合いを何も満たさないとする．表では ? としている．原論文で確かめていないからである

:::{dropdown} 原文の引用
- Chen (1981), pp. 31–32：“defining the factor of safety as the ratio of the total available resistance along a failure surface to the total mobilized stress along it. In order to simplify the analysis, the ordinary method of slices was used. Thus the inter-column forces can be ignored and both normal and shear stresses on the base of each column are obtained simply as the component of the weight of the column.”
- Ugai et al. (1986), p. 268：「各柱体の力のつり合いよりすべり面上の垂直力ΔNとせん断力ΔT（x軸に平行と仮定）を求め，土塊全体のモーメントのつり合いより安全率を決定するというものである．」「このような仮定のもとではy軸方向の力のつり合いが成り立たないからである．」
- Ugai (1987), p. 14：「Hovlandの方法はすべり土塊全体のつり合い条件（力のつり合い，モーメントのつり合い）を何も満たしていないため，計算結果の信頼性に疑問が生じる．」
- Ugai and Hosobori (1989), p. 183：「Hovland法は簡便であるが土塊全体のつり合いが全く満たされない」
:::

(equilibrium-section-3-2)=

### 3.2 Chen and Chameau (1983)：3次元のSpencer法

1983年の論文は，全文が公開されていない．要旨は，Chen (1981)の報告書の要約とほぼ同じ文である．そのため，この報告書の全文で中身を確かめた．報告書は，Chameauらの指導のもとで書かれ，同じ手法をプログラムLEMIXとして示している．ただし，1983年の本文で式が変わった可能性は残る．元の座標は，$X$ がすべり方向，$Y$ が鉛直上向き，$Z$ が横方向である．回転軸は $Z$ に平行で，共通の取り方の $y$ にあたる．

- **対象**：対称な{term}`すべり土塊`だけを扱い，その半分だけをカラムに分けて解く．すべり面は回転体の面で，1983年の論文の中心は回転楕円体である
- **カラム間力**：すべり方向に垂直な面の力は，土塊全体で同じ傾き $\theta$ をもつと仮定する．横方向の面（$y$ に垂直な面）のせん断力も考えるが，未知量ではない．$K_0$ の状態から決めた既知の値とする．横方向の面の垂直力は，式に現れない
- **未知量**：安全率 $F$ と傾き $\theta$ の2つ．すべり方向は $x$ に固定する
- **土塊全体**：$\sum F_x$ と $\sum F_z$ のつり合いを使う．$\theta$ が一定なので，この2つは1つの式にまとまる．これと，回転軸まわりのモーメントの式（$\sum M_y$）を解く．$\sum F_y$，$\sum M_x$，$\sum M_z$ は，鏡像の半分と合わせた土塊全体で，対称性によって成り立つ
- **カラムごと**：中央断面に射影した2つの力の式と，底面の中央まわりの1つのモーメントの式を満たす．モーメントの式は，カラム間力の作用高さを決めるのに使う．つまり，カラムごとのモーメントを，カラム間力の作用位置で満たしている．ただし，$y$ に平行な1つの軸についてだけである．カラムごとの $F_y$，$M_x$，$M_z$ はない
- **力の式の近似**：Ugai et al. (1986)は，このカラムの力の式が，{term}`底面垂直力`の $y$ 方向の成分を無視していると指摘している
- **論文の言い方**：要旨は，力とモーメントのつり合いを，各カラムでも土塊全体でも満たすと書く．これは，射影した面の中の3つの式の意味で，6つの式の意味ではない

:::{dropdown} 原文の引用
- 1983年の論文の要旨：“The failure mass is assumed to be symmetrical and divided into many vertical columns. The inter-slice forces have the same inclination throughout the mass, and the inter-column shear forces are parallel to the base of the column and function of their positions. Force and moment equilibria are satisfied for each column as well as for the total mass.”
- Chen (1981), p. 57：“If the mass is divided into 600 vertical columns (m = 20, n = 30), and the geometry is assumed to be symmetrical, the number of the unknowns remaining are 0.5 · 6 · m · n = 0.5 · 6 · 20 · 30 = 1800”．仮定 (1)：“The failure mass is symmetrical”
- Chen (1981), p. 69：“Fig. 3-15 shows the force system projected on the central plane (X-Y plane) of a column provided that dz is very small.”
- Chen (1981), p. 74，式 (3.34)：“If the whole system is in equilibrium, then the sum of all forces in the system must be equal to zero: Σ Q = 0”．式 (3.34a)：“The sum of all moment about any point (Fig. 3.11) must be equal to zero: Σ Q cos (θ − α) (r − h_Q cos α) = 0”
- Chen (1981), pp. 74–75，式 (3.35)：“where the value of Q h_Q can be obtained by summing all moments in a column at the center of the base of that column”
- Chen (1981), p. 75：“In these equations the only two unknowns are, (1) the inclination of interslice force and (2) the factor of safety F.”
- Ugai et al. (1986), p. 268：「分割柱に作用する力のつり合いを考えるにあたって，底面の垂直力ΔNがy方向成分を有することを無視している点である．したがって，彼らの論文中の式（9），（10）は誤りである．」
:::

(equilibrium-section-3-3)=

### 3.3 Ugaiらの一連の研究（1986〜1989）

Ugaiらの論文は，どれもJ-STAGEで全文を読める．座標は，共通の取り方と同じである．Ugaiらは，2次元の手法を1つずつ3次元に拡張した．どの手法も，各カラムでは1つの方向の力のつり合いだけをとり，底面垂直力を求める．そのうえで，土塊全体では，簡便分割法は1つ，簡易Bishop法と簡易Janbu法は2つ，Spencer法は3つのつり合い式を解く．

| 文献 | 手法 | すべり面 | 未知量 | 土塊全体で解く式 |
|---|---|---|---|---|
| Ugai et al. (1986) | 3次元の簡便分割法 | $xz$ 面に対称な回転体の面 | $F$ | $\sum M_y$ |
| Ugai (1987) | 3次元の簡易Janbu法 | 任意形状 | $F$，$\eta$ | $\sum F_x$，$\sum F_z$ |
| Ugai and Hosobori (1988) | 3次元の簡易Bishop法 | 回転体の面 | $F$，$\eta$ | $\sum M_y$，$\sum F_z$ |
| Ugai and Hosobori (1988) | 3次元の簡易Janbu法 | 任意形状 | $F$，$\eta$ | $\sum F_x$，$\sum F_z$ |
| Ugai and Hosobori (1988) | 3次元のSpencer法 | 回転体の面 | $F$，$\eta$，$\delta$ | $\sum F_x$，$\sum F_z$，$\sum M_y$ |
| Ugai and Hosobori (1989) | 3次元のSpencer法 | 任意形状 | $F$，$\eta$，$\delta$ | $\sum F_x$，$\sum F_z$，$\sum M_y$ |

- **カラム間力**：どの手法も，カラムの各側面の力ではなく，その合力 $\Delta Q$ に仮定を置く．横方向の面のせん断力も，個別には扱わない．簡便分割法では，$\Delta Q$ をすべり面に平行とし，これとは別に横方向の拘束力 $\Delta H$ を入れる．ほかの手法では，$\Delta Q$ の $yz$ 面内の成分は，水平面と $\tan^{-1}(\eta\tan\alpha_{yz})$ の角をなすとする．$\alpha_{yz}$ は底面の横の傾き，$\eta$ は未知の定数である．Spencer法では，さらに $xz$ 面内の成分が，水平面と未知の角 $\delta$ をなすとする．全カラムで共通なのは，$xz$ 面内の傾きだけである．つまり，2次元のSpencer法のように，全カラムの合力が1つの向きにそろうわけではない
- **カラムごと**：$\Delta Q$ を含む面に垂直な方向の力のつり合いを1つとる．そのため，簡易Bishop法でも，カラムごとの式は鉛直方向の力ではない．この点が，[3.4節](#equilibrium-section-3-4)のHungrの3次元の簡易Bishop法と違う．カラムごとのモーメントには触れない
- **対称性**：1988年の論文は，$\sum F_y$，$\sum M_x$，$\sum M_z$ にも，対称性にも触れない．計算例は対称な斜面である．一方，1987年と1989年の論文は，非対称な実際の斜面（御岳崩壊）にも当てはめている．このとき，$\sum F_y$，$\sum M_x$，$\sum M_z$ は，対称性によっても成り立つとは限らない
- **論文の言い方**：3次元のSpencer法を，つり合い条件をすべて満たす方法と書く．この「すべて」は，水平力，鉛直力，モーメントの3つを指す

:::{dropdown} 原文の引用
- Ugai et al. (1986), p. 269：「xz 面に関して対称なすべり面を仮定する」「すべりの方向は y 軸に垂直と仮定する」．p. 270：「底面に垂直な方向（ΔN の方向）の力のつり合い式をたてると」
- Ugai (1987), p. 9：「土塊全体に関して鉛直力と水平力のつり合いを考えると，次の2つの式が得られる．」
- Ugai and Hosobori (1988), p. 22：「コラム間内力は全体のつり合いに関与しないことを考慮すると，すべり土塊のモーメントのつり合いは」（式 (7)）
- Ugai and Hosobori (1988), p. 23：「これまでに提案してきた三次元簡便法，三次元簡易Bishop法および三次元簡易Janbu法はつり合い条件（水平力・鉛直力のつり合い，モーメントのつり合い）の一部しか満たさないため，得られる解の精度に多少の不安が残る．ここではつり合い条件をすべて満足する方法として，Spencer法の三次元化を試みる．コラム側面に作用する内力の合力 ΔQ_ij の分力のうち ΔQ_1（Fig.3）が水平面と δ（未知定数）の角度をなすと仮定する．」
- Ugai and Hosobori (1988), p. 23：「S面に垂直な方向の力のつり合いから」（式 (14)）．「式 (15)，(16) をすべり土塊のモーメントのつり合い式 (7)，鉛直力のつり合い式 (9) および水平力のつり合い式 (11) に代入すると3つの式が得られる」「3つの未知数 F, η, δ が計算され」
- Ugai and Hosobori (1989), p. 183の英文要旨：“This method is applicable to the case of non-circular slip surface and satisfies moment equilibrium and vertical and horizontal force equilibrium for sliding mass.”．p. 186：「任意形状のすべり面に適用でき，すべり土塊の力とモーメントのつり合いがすべて満たされる三次元安定計算法（非円形Spencer法）を提案し」
:::

(equilibrium-section-3-4)=

### 3.4 Hungr (1987)，Hungr et al. (1989)：3次元の簡易Bishop法

どちらの論文も，全文は読めなかった．次のことは，要旨と，Kalatehjari and Ali (2013)，Read (2021)，Zheng (2007)の紹介による．

- **対象**：Hungr (1987)は，対称な問題で，中央断面が円の回転体の面を扱う．Hungr et al. (1989)は，回転しない面や非対称な面にも当てはめている
- **カラム間力**：2次元の簡易Bishop法と同じく，カラム間のせん断力の鉛直成分を無視する．カラム間の垂直力と水平なせん断力は無視しない
- **つり合い**：各カラムの鉛直方向の力のつり合いと，回転軸まわりの土塊全体のモーメントのつり合いから，安全率を求める．すべり方向の水平な力のつり合いは満たさない
- **Hungr et al. (1989)**：回転体で対称なすべり面では，ほかの方法とよく合う．一方，回転しない面や非対称な面では，安全率が小さめに出る

:::{dropdown} 原文の引用
- Hungr et al. (1989)の要旨：“Very good correspondence is found in cases of rotational and symmetric sliding surfaces, such as ellipsoids. The Bishop method tends to be conservative when applied to nonrotational and asymmetric surfaces because it neglects internal strength.”
- Kalatehjari and Ali (2013), p. 125：“In this symmetrical problem, a rotational surface with circular central cross section was assumed as the failure surface. Following the assumption of Bishop, Hungr neglected the vertical Inter-column shear forces on the sides of columns. This method considered vertical force equilibriums of all columns as well as overall moment equilibrium of sliding mass about the axis of rotation to establish the equation of FOS.”
- Read (2021)：“Hungr's analysis neglects vertical intercolumn shear but not the intercolumn normal forces and horizontal shear forces”
- Zheng (2007), p. 1530：「有些方法，如 Hungr 法等，甚至连 3 个力平衡条件都未满足，其计算结果可能与坐标轴的选取有关。」
:::

(equilibrium-section-3-5)=

### 3.5 Lam and Fredlund (1993)：3次元のGLE

本文も，Hungr (1994)の討議とLam and Fredlund (1994)の回答も，公開されている全文が見つからなかった．次のことは，要旨と二次文献による．

- **対象**：要旨の1つの版は，すべり方向を前もって仮定すると書く．Kalatehjari and Ali (2013)は，すべり方向が1つの回転体の面で，対称な問題を扱うとする
- **カラム間力**：Morgenstern–Price法と同じ形の関数で，カラム間力の合力の向きを表す．Kalatehjari and Ali (2013)は，垂直力とせん断力の関係が5つあり，そのうち3つを影響が小さいとして無視したとする．Chen et al. (2001)は，係数 $\lambda_3$，$\lambda_4$ が残り，$\lambda_3$ は安全率が最小になる値を選んだとする．各関係が，どの面のどの成分の比かは，確かめられなかった
- **つり合い**：2次元の{term}`GLE`と同じく，力のつり合いとモーメントのつり合いから，それぞれ安全率を求めて一致させる．ただし，数を挙げる二次文献は，満たすつり合いを3つか4つとしている．$\sum M_z$ を満たすとする文献はない

:::{dropdown} 原文の引用
- 要旨：“A generalized model for three-dimensional analysis, using the method of columns, is presented. The model is an extension of the two-dimensional general limit equilibrium formulation. Intercolumn force functions of arbitrary shape can be specified to simulate various directions for the intercolumn resultant forces.”
- ETDE（OSTI）に収録された要旨：“A direction of movement must be assumed for the analysis.”
- Kalatehjari and Ali (2013), p. 126：“A rotational surface with single direction of movement was assumed as the slip surface. … The basic definition of these inter-column force functions was similar to Morgenstern and Price's (1965) function including five relationships between normal and shear inter-column forces. Lam and Fredlund decided to ignore three out of five inter-column forces due to their insignificance role in typical slopes based on their results of finite element analysis. They also established two different equations of FOS based on moment and force equilibriums”
- Chen et al. (2001), p. 525：「Lam & Fredlund 在建立条柱法时发现，最终还多出两个系数 λ3，λ4，于是，便进一步假定 λ3 应该在若干个数值中选一个相应安全系数最小的」
- Zhu and Qian (2007), p. 1514：「大多数条柱法只能满足 3 个平衡条件，严格来说这些方法只适合对称边坡」．この文が引く文献に，Lam and Fredlund (1993)が含まれる
- Jiang and Yamagami (2004), p. 132：Lam and Fredlund (1993)を，すべり方向（$xz$ 面内）のつり合いだけを満たす “one-directional force and moment equilibrium” の方法の例に挙げる
- Jiang and Zhou (2018)：“the 3-d methods by Zhang (1988), Hungr et al. (1989), Lam and Fredlund (1993) and Chen et al. (2003) belong to the simplified ones which can satisfy at most four equilibrium conditions”
:::

(equilibrium-section-3-6)=

### 3.6 Chen et al. (2003)：Spencer型の方法

2003年の論文は，要旨だけを読んだ．同じ著者が同じ手法を中国語で書いたChen et al. (2001)の全文で，中身を確かめた．仮定と満たす式が要旨と一致し，例題の安全率2.187も一致する．元の座標は，$x$ がすべり方向と逆向き，$y$ が鉛直上向き，$z$ が横方向である．

- **対象**：非対称な土塊も扱い，すべり面の形を仮定しない．主なすべり方向は与える
- **カラム間力**：すべり方向に垂直な面の力は，鉛直な $xz$ 面に平行で，その傾き $\beta$ が全カラムで一定とする．2次元のSpencer法にあたる仮定である．横方向の面の力は，$y$ 方向の垂直力だけで，せん断力はない．底面のせん断力の向き $\rho$ には，分布の形を仮定する
- **未知量**：$F$，$\beta$，$\rho$
- **土塊全体**：$\sum F_x$，$\sum F_y$，$\sum F_z$ と，横方向の軸まわりのモーメント（$\sum M_y$）の4つを満たす．$\sum M_x$ と $\sum M_z$ の式はない
- **カラムごと**：カラム間力に垂直な1つの方向の力のつり合い
- **論文の言い方**：要旨の “complete overall force equilibrium conditions” は，土塊全体の3方向の力を指す．2001年の論文は，この方法を近似的な計算法とし，下界の解になるとしている

:::{dropdown} 原文の引用
- 2003年の論文の要旨：“The assumption involved in this method is of a parallel intercolumn force inclination, similar to Spencer's method in the two-dimensional (2D) area. It allows for the satisfaction of complete overall force equilibrium conditions and the moment equilibrium requirement about the main axis of rotation.”
- Chen et al. (2001), p. 526：「a) 作用在行界面（平行于 yoz 平面的界面）的条间力 G 平行于 xoy 平面，其与 x 轴的倾角 β 为常量，这一假定相当于二维领域中的 Spencer 法；b) 作用在列界面（平行于 xoy 平面的界面）的作用力 Q 为水平方向，与 z 轴平行；」
- Chen et al. (2001), p. 527：「建立与 S′ 垂直的 S 方向的整体平衡方程式 … 建立 z 方向的整体平衡方程式 … 同时建立绕 z 轴的整体力矩平衡方程式」
- Chen et al. (2001)の結論：「由于忽略了条间力的一些剪切分量，同时又假定所有条块的 β 为同一数值，同一列的 ρ 值也为同一数值，故仍属近似算法。由于条间侧面剪力被假定为零，计算成果可能偏小，属下限解。」
:::

(equilibrium-section-3-7)=

### 3.7 Jiang and Yamagami (2004)：3次元のSpencer法

J-STAGEで全文を読める．座標は，共通の取り方と同じである．

- **対象**：{term}`任意形状のすべり面 <一般形状のすべり面>`を，動的計画法で探す．土塊全体が1つの方向（$x$）にすべると仮定する．計算例は対称な円錐状の盛土である
- **カラム間力**：Ugai and Hosobori (1989)と同じく，カラムの全側面の合力 $Q$ に仮定を置く．$Q$ の $xz$ 面内の成分は，$x$ 軸と未知の角 $\delta$ をなし，この角は全カラムで共通である．$yz$ 面内の成分は，$y$ 軸に平行とする．Ugai and Hosobori (1989)は，この成分を $\tan^{-1}(\eta\tan\alpha_{yz})$ だけ傾けていた．論文は，この違いを説明していない
- **未知量**：$F$ と $\delta$
- **土塊全体**：$\sum F_x$ から安全率 $F_f$ を，$y$ に平行な回転軸まわりの $\sum M_y$ から安全率 $F_m$ を求め，両者が一致する $\delta$ を探す．$\sum F_z$ は，式としては書いていない．ただし，各カラムの力の式の方向は $xz$ 面内にあり，全カラムで同じである．そのため，カラムごとの式と土塊全体の $\sum F_x$ が成り立てば，$\sum F_z$ も成り立つ
- **対称性**：$\sum F_y$，$\sum M_x$，$\sum M_z$ は解かない．対称な土塊では，これらは対称性によって成り立つと，論文が書いている．また，すべり方向を1つとする仮定は，ほぼ対称な土塊に向くとしている
- **カラムごと**：$Q$ を含む面に垂直な方向の力のつり合いを1つとる
- **論文の言い方**：この手法を，力とモーメントのつり合いを満たす，{term}`静力学的に厳密な方法 <静力学的に完全な方法>`と呼ぶ．一方，既往のカラム法の多くを，すべり方向のつり合いだけを満たす方法として区別している

:::{dropdown} 原文の引用
- 要旨（p. 127）：“a column method extended from the Spencer safety factor equation for 2D analysis”．“The comparative study presented in this paper strongly supports a recommendation of the use of a statically rigorous limit equilibrium approach satisfying both force and moment equilibrium for a realistic 3D analysis of the slope stability.”
- p. 128：“Q consists of two components, i.e. Q1 in the xz plane and Q2 in the yz plane. The former is inclined at an angle of δ (an unknown constant for all columns) to the x-axis (sliding direction) as in the Spencer method (1967), and the latter is assumed to be parallel to the y-axis.”
- p. 128：“a 3D method for slope stability analysis was presented by Ugai and Hosobori (1989) which could be considered partly as an extension of the Spencer method (Spencer, 1967) for 2D analyses.”
- p. 128：“The normal force N and shear force T acting on the column base can be derived by considering force equilibrium in the direction perpendicular to the Q1QQ2 plane and the Mohr-Coulomb failure criterion at the column base.”
- p. 128：“The summation of moments of all columns about an axis of rotation parallel to the y-axis was used to derive the factor of safety F_m with respect to moment equilibrium.”
- p. 132：“In these methods, force and/or moment equilibrium conditions are satisfied only in the sliding direction (i.e. in the xz plane) but are ignored in the transverse direction (i.e. in the yz plane). Hence, they are sometimes referred to as ‘one-directional force and moment equilibrium’ methods (Huang and Tsai, 2000).”
- p. 133：“When the limit equilibrium equations of the whole sliding mass are considered, therefore, their effects in the transverse direction will be cancelled out. In other words, transverse force and moment equilibrium conditions are automatically satisfied due to symmetry of the problem.”
:::

(equilibrium-section-3-8)=

### 3.8 Cheng and Yip (2007)：非対称な斜面への拡張

本文は読めなかった．次のことは，要旨と，Cheng and Yip (2007)の式を転載したSlide3の理論資料（Rocscience），本文を逐語で引用したRead (2021)による．

- **対象**：非対称な土塊を，全体のまま解く．すべり方向は全カラムで1つで，未知量として解く
- **カラム間力**：各面に，垂直力，鉛直なせん断力，水平なせん断力を置く．つまり，横方向の面のせん断力も考える．鉛直なせん断力は，垂直力に係数 $\lambda_x$，$\lambda_y$ を掛けた形である．一方，2方向の水平なせん断力は，弾性体の共役せん断応力にならって関係づける．この関係は，カラムごとの鉛直な軸まわりのモーメントのつり合いを，小さなカラムで近似したものにあたる
- **未知量**：$F$，$\lambda_x$，$\lambda_y$，すべり方向
- **つり合い**：各カラムの鉛直方向の力のつり合いと，土塊全体の $x$ と $y$ の力，2つの水平な軸まわりのモーメントを使う．土塊全体の鉛直な軸まわりのモーメントの式はない
- **論文の言い方**：要旨は，すべり方向を3次元の力とモーメントのつり合いから決めると書く．“rigorous” とは書いていない

:::{dropdown} 原文の引用
- 要旨：“Most existing three-dimensional (3D) slope stability analysis methods are based on simple extensions of corresponding two-dimensional (2D) methods of analysis and a plane of symmetry or direction of slide is implicitly assumed. … Under these new formulations, the direction of slide is unique and is determined from 3D force/moment equilibrium.”
- Slide3の理論資料：“Let's first consider vertical force equilibrium (z-direction) of a single column.”．“Overall force and moment equilibrium in the X and Y directions is given by the following equations.”．“We then find the values of F, lamdax, lamday, aprime (sliding direction) that satisfy these 3 equations.”
- Read (2021)の要約：“by using the property of complementary shear (or moment equilibrium in the xy plane), Hy i+1 or Hx i+1 can be determined sequentially from the exterior columns”
- Read (2021)が引くCheng and Yip (2007)の文：“The important concept of complementary shear force which is similar to the complementary shear stress (τxy = τyx) in elasticity has not been used in any 3D slope stability analysis method in the past but is crucial in the present formulation.”．“Although the concept of complementary shear stress is applicable only in the infinitesimal sense, if the size of the column is not great this assumption will greatly simplify the equations.”
:::

(equilibrium-section-3-9)=

### 3.9 土塊全体の6つの式を解く方法

Zhu and Qian (2007)とZheng (2007)は，カラム間力の向きを仮定する代わりに，すべり面の{term}`垂直応力`の分布を仮定する．そのうえで，土塊全体を1つの物体として，6つのつり合い式を解く．Zheng (2009)も，Jiang and Zhou (2018)によれば同じ考え方である．Zheng (2012)は，要旨によれば，土塊の{term}`内力`にMorgenstern–Price法の仮定を置く．その詳しい形は，本文で確かめられなかった．

- **Zhu and Qian (2007)**：全文を読んだ．積分を計算するときは土塊をカラムに分けるが，つり合いは土塊全体の式で立てる．6つの式を解く厳密解と，$\sum M_z$ だけを省いた準厳密解を示す．論文は，6つの式を満たす3次元の解を初めて得たと書く
- **Zheng (2007)**：全文を読んだ．安全率と，垂直応力の分布の5つのパラメータを，6つの式から求める．全体すべり方向は与える．カラムには分けない
- **Zheng (2009)**：要旨を読んだ．同じ考え方を，一般化固有値問題として解く．カラムには分けない
- **Zheng (2012)**：要旨を読んだ．すべり土塊の内力にMorgenstern–Price法の仮定を置き，2次元の厳密な分割法の3次元版として示す．体積積分を境界積分に変えるので，カラムに分けない．6つの式を満たすことは，Jiang and Zhou (2018)の紹介による
- **Jiang and Zhou (2018)**：著者稿の全文を読んだ．カラムに分けるが，つり合いは土塊全体の6つの式で立て，全体すべり方向も未知量として解く

:::{dropdown} 原文の引用
- Zhu and Qian (2007), p. 1514：「严格的三维极限平衡法需满足 6 个平衡方程，即 3个方向力平衡条件与绕 3个方向轴的力矩平衡。但大多数条柱法只能满足 3 个平衡条件，严格来说这些方法只适合对称边坡」
- Zhu and Qian (2007), p. 1520：「由于只忽略了一个最次要的平衡条件，满足其余 5 个平衡条件，这样的解答可称为三维边坡准严格极限平衡解答。」
- Zhu and Qian (2007), p. 1527：「本文应用滑面正应力修正方法，首次得到满足所有 6 个平衡条件的三维边坡严格极限平衡解答与满足 3 个力平衡和 2 个力矩平衡条件的三维边坡准严格极限平衡解答。」
- Zheng (2007), p. 1529の英文要旨：“Up to now, there is no three-dimensional limit equilibrium method that is able to satisfy all six equilibrium conditions. … a rigorous limit equilibrium method for the three-dimensional stability analysis of slope is realized, which satisfies all the six equilibrium conditions and accommodates to slip surfaces of any shape.”
- Zheng (2007), p. 1530：「迄今为止几乎所有已公开发表的三维方法最多只能满足 4 个平衡条件。除非滑体沿其滑动方向有一对称面且采用对称剖分，否则就没有充足的理由说明计算结果的可靠性。」
- Zheng (2009)の要旨：“Of the existing methods for the three-dimensional (3D) limit equilibrium analysis of slopes, none can simultaneously satisfy all six equilibrium equations. … the proposed method does not need to partition the sliding body into columns.”
- Zheng (2012)の要旨：“the attempts to realize their three-dimensional rigorous counterparts have not yet been realized. Introducing the Morgenstern–Price (M-P) assumption on the internal forces of the slip body, this study presents the three-dimensional version of the M-P method, which is rigorous and applicable to failure surfaces of complex shape. In the formulation, meanwhile, the volume integrals over the slip body are transformed into the boundary integrals, rendering column-partitioning unnecessary.”
- Jiang and Zhou (2018)：“the method by Zheng (2012) belongs to the rigorous one which meets all six equilibrium conditions”．“All six equilibrium conditions (three force-equilibrium and three moment-equilibrium conditions) are strictly satisfied in the proposed method.”
:::

(equilibrium-section-3-10)=

### 3.10 その他の手法

- **Zhang (1988)**：要旨は，力とモーメントのつり合いを満たすと書く．Kalatehjari and Ali (2013)によれば，対称な斜面だけを扱う．Zheng (2007)によれば，満たすのは3つの力の式と $\sum M_y$ で，対称なので $\sum M_x$ と $\sum M_z$ は自動的に成り立つ．$\sum F_y$ を式として解くか，対称性によって満たすかは，確かめられなかった
- **Leshchinsky and Huang (1992)**：変分法で，すべり面の垂直応力の分布を求める．要旨は，極限平衡の式をすべて満たすと書く．ただし，扱うのは対称な問題に限られる．Zheng (2007)によれば，満たすのは3つの力の式と回転軸まわりの1つのモーメントの式である．$\sum F_y$ を式として解くか，対称性によって満たすかは，確かめられなかった
- **Huang et al. (2002)**：要旨は，2方向の力とモーメントのつり合いを使うと書く．Jiang and Zhou (2018)は，3方向の力と2方向のモーメントを満たす準厳密な方法とする．一方，Zhu and Qian (2007)は，4つの式を大まかに満たすとする

---

(equilibrium-section-4)=

## 4. 分かったこと

(equilibrium-section-4-1)=

### 4.1 3次元のSpencer型の手法は，6つの式をすべては解かない

調べた3次元のSpencer型の手法が，土塊全体で対称性に頼らずに満たすのは，3つか4つの式である．モーメントの式は，どれも $\sum M_y$ の1つだけを使う．

- Chen and Chameau (1983)の対称な定式化は，$\sum F_x$，$\sum F_z$，$\sum M_y$ を満たす．つまり，対称性に頼らずに満たすのが3つで，残りの3つは対称性によって成り立つ．カラムごとには，射影した面の中の3つの式を満たす
- Ugai and Hosobori (1988, 1989)とJiang and Yamagami (2004)の定式化は，対称性を前提にしない．そのため，非対称な斜面では，$\sum F_y$，$\sum M_x$，$\sum M_z$ が成り立つとは限らない
- Chen et al. (2003)は，3方向の力と $\sum M_y$ の4つを満たす

Zheng (2007)は，$\sum M_z$ だけを省いた5つの式を満たす3次元のSpencer法として，Zhang et al. (2005)を挙げている．この論文は読んでいない．

(equilibrium-section-4-2)=

### 4.2 Cheng and Yip (2007)のMorgenstern–Price法は，$\sum M_z$ を解かない

Slide3の理論資料とRead (2021)によれば，Cheng and Yip (2007)は，$\sum M_z$ を除く5つの式を使う．ただし，カラムごとの鉛直な軸まわりのモーメントを，共役せん断として近似的に使う．Lam and Fredlund (1993)は，原論文で確かめられなかった．数を挙げる二次文献は，満たす式を3つか4つとし，$\sum M_z$ を満たすとする文献はない．

(equilibrium-section-4-3)=

### 4.3 6つの式をすべて解く方法は，2007年の論文から確かめられる

土塊全体の6つの式をすべて解く3次元の{term}`LEM <極限平衡法>`は，Zhu and Qian (2007)とZheng (2007)から全文で確かめられる．その後，Zheng (2012)は，6つの式を満たすMorgenstern–Price法の3次元版を示した．6つの式を満たすことは，要旨とJiang and Zhou (2018)による．どれも，土塊全体を1つの物体として6つの式を立てる．つまり，カラム間力の向きを仮定して2次元の手法を拡張したカラム法ではない．

変分法のLeshchinsky and Huang (1992)は，すべてのつり合いを満たすと要旨で書く．しかし，扱うのは対称な問題だけである．Zheng (2007)によれば，この方法は，3つの力の式と，回転軸まわりの1つのモーメントの式を満たす．

---

(equilibrium-section-5)=

## 5. 「厳密」と「すべて」の使われ方

3次元の論文では，「厳密」（rigorous）や「すべて満たす」が，2つの意味で使われている．

1つ目は，論文が扱う一部の式を，すべて満たすという意味である．古い論文に多い．

- Ugai and Hosobori (1988)は，$\sum F_x$，$\sum F_z$，$\sum M_y$ の3つを解く方法を，つり合い条件をすべて満たす方法と呼ぶ
- Ugai and Hosobori (1989)は，同じ3つの式を解く方法を，非対称な斜面に当てはめ，力とモーメントのつり合いがすべて満たされると書く
- Jiang and Yamagami (2004)は，$\sum F_x$ と $\sum M_y$ を解く方法を，静力学的に厳密な方法と呼ぶ
- Chen and Chameau (1983)は，射影した面の中の3つの式を，各カラムでも土塊全体でも満たすと書く
- Chen et al. (2003)の “complete overall force equilibrium” は，土塊全体の3方向の力だけを指す
- Zhang (1988)とLeshchinsky and Huang (1992)の要旨も，力とモーメントのつり合い，または極限平衡の式をすべて満たすと書く．Zheng (2007)によれば，実際に解くモーメントの式は，$\sum M_y$ の1つである

2つ目は，土塊全体の6つの式をすべて満たすという意味である．2007年以降の論文に多い．Zhu and Qian (2007)とJiang and Zhou (2018)は，3次元の厳密な方法を，6つの式を満たす方法と定義する．$\sum M_z$ を除く5つを満たす方法は，準厳密（quasi-rigorous）と呼ぶ．また，Zheng (2012)の要旨も，厳密な方法を，つり合いの条件をすべて満たす方法とする．

6つの式を基準にする論文では，「すべて」は土塊全体のつり合いを指す．カラムごとの6つの式を「完全」とする論文は，見つからなかった．なお，対称性で成り立つ式を数えて「厳密」とする例もある．Zheng (2007)は，対称な土塊を対称に分けたZhang (1988)の解を，厳密な解とみなせると書いている．

:::{dropdown} 原文の引用
- Jiang and Zhou (2018)：“In rigorous 3-d methods for slope stability analysis, all six equilibrium conditions (three directional force and three moment equilibrium equations) should be satisfied for the potential failure mass.”
- Zheng (2012)の要旨：“the “rigorous” methods that satisfy complete equilibrium conditions are more reliable and are preferred.”
- Zheng (2007), p. 1535：「因滑体均质、对称，如果对称地对滑体进行条分，则关于 z 轴和 x 轴的力矩平衡能被自动满足，此时 X. Zhang 所建议的能满足 3个力平衡和 1个绕 y 轴的力矩平衡的解也可被视为严格解」
- Zhang (1988)の要旨：“The force equilibrium and the moment equilibrium conditions over failure mass are satisfied in the analysis.”
- Leshchinsky and Huang (1992)の要旨：“A 3-D slope-stability-analysis method, explicitly satisfying all limiting-equilibrium equations, is presented.”
:::

---

(equilibrium-section-6)=

## 6. 確かめられなかった文献

| 文献 | 読めたもの | 理由 |
|---|---|---|
| Hovland (1977) | 要旨，二次文献 | 有料で，公開されている版がない |
| Chen and Chameau (1983) | 要旨．前身のChen (1981)は全文 | 有料で，公開されている版がない |
| Hungr (1987) | 二次文献 | 有料で，要旨も表示されない |
| Hungr et al. (1989) | 要旨，二次文献 | 有料で，公開されている版がない |
| Lam and Fredlund (1993)と，その討議と回答 | 要旨，二次文献 | 有料で，公開されている版がない |
| Chen et al. (2003) | 要旨．前身のChen et al. (2001)は全文 | 有料で，公開されている版がない |
| Cheng and Yip (2007) | 要旨，二次文献 | 有料．機関リポジトリの版は取り下げられている |
| Zheng (2012) | 要旨，二次文献 | 有料で，公開されている版がない |
| Zhang (1988)，Zheng (2009) | 要旨，二次文献 | 有料で，公開されている版がない |
| Leshchinsky and Huang (1992)，Huang et al. (2002) | 要旨，二次文献 | 有料で，公開されている版がない |
| Zhang et al. (2005) | Zheng (2007)の紹介 | 調べる範囲に入れなかった |
| Duncan (1996) | 要旨 | 有料．3次元の手法をまとめた表を確かめられなかった |

---

## 参考文献

DOIは，出版社かCrossrefの書誌情報で照合したものだけを載せている．

### 3次元のLEMの手法

1. Hovland, H. J. (1977). “Three-Dimensional Slope Stability Analysis Method.” *Journal of the Geotechnical Engineering Division*, 103(9), 971–986. [https://doi.org/10.1061/AJGEB6.0000493](https://doi.org/10.1061/AJGEB6.0000493)
2. Chen, R. H. (1981). *Three-Dimensional Slope Stability Analysis*. Joint Highway Research Project, Report JHRP-81-17, Purdue University. [書誌情報](https://docs.lib.purdue.edu/jtrp/897/)
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
16. 陈祖煜・弥宏亮・汪小刚（Chen et al.）(2001)．边坡稳定三维分析的极限平衡方法．*岩土工程学报*，23(5)，525–529．[書誌情報](https://www.cgejournal.com/cn/article/id/10783)
17. Huang, C.-C., Tsai, C.-C., and Chen, Y.-H. (2002). “Generalized method for three-dimensional slope stability analysis.” *Journal of Geotechnical and Geoenvironmental Engineering*, 128(10), 836–848. [https://doi.org/10.1061/(ASCE)1090-0241(2002)128:10(836)](https://doi.org/10.1061/%28ASCE%291090-0241%282002%29128%3A10%28836%29)
18. Chen, Z., Mi, H., Zhang, F., and Wang, X. (2003). “A simplified method for 3D slope stability analysis.” *Canadian Geotechnical Journal*, 40(3), 675–683. [https://doi.org/10.1139/t03-002](https://doi.org/10.1139/t03-002)
19. Jiang, J.-C., and Yamagami, T. (2004). “Three-Dimensional Slope Stability Analysis Using an Extended Spencer Method.” *Soils and Foundations*, 44(4), 127–135. [https://doi.org/10.3208/sandf.44.4_127](https://doi.org/10.3208/sandf.44.4_127)
20. 张均锋・王思莹・祈涛（Zhang et al.）(2005)．边坡稳定分析的三维 Spencer 法．*岩石力学与工程学报*，24(19)，3434–3439．ページは，Zheng (2007)の文献表による．[書誌情報](https://rockmech.whrsm.ac.cn/CN/abstract/abstract21749.shtml)
21. Cheng, Y. M., and Yip, C. J. (2007). “Three-Dimensional Asymmetrical Slope Stability Analysis—Extension of Bishop's, Janbu's, and Morgenstern–Price's Techniques.” *Journal of Geotechnical and Geoenvironmental Engineering*, 133(12), 1544–1555. [https://doi.org/10.1061/(ASCE)1090-0241(2007)133:12(1544)](https://doi.org/10.1061/%28ASCE%291090-0241%282007%29133%3A12%281544%29)
22. 朱大勇・钱七虎（Zhu and Qian）(2007)．三维边坡严格与准严格极限平衡解答及工程应用．*岩石力学与工程学报*，26(8)，1513–1528．[書誌情報](https://rockmech.whrsm.ac.cn/CN/abstract/abstract22094.shtml)
23. 郑宏（Zheng）(2007)．严格三维极限平衡法．*岩石力学与工程学报*，26(8)，1529–1537．[書誌情報](https://rockmech.whrsm.ac.cn/CN/abstract/abstract22095.shtml)
24. Zheng, H. (2009). “Eigenvalue problem from the stability analysis of slopes.” *Journal of Geotechnical and Geoenvironmental Engineering*, 135(5), 647–656. [https://doi.org/10.1061/(ASCE)GT.1943-5606.0000071](https://doi.org/10.1061/%28ASCE%29GT.1943-5606.0000071)
25. Zheng, H. (2012). “A three-dimensional rigorous method for stability analysis of landslides.” *Engineering Geology*, 145–146, 30–40. [https://doi.org/10.1016/j.enggeo.2012.06.010](https://doi.org/10.1016/j.enggeo.2012.06.010)
26. Jiang, Q., and Zhou, C. (2018). “A rigorous method for three-dimensional asymmetrical slope stability analysis.” *Canadian Geotechnical Journal*, 55(4), 495–513. [https://doi.org/10.1139/cgj-2017-0317](https://doi.org/10.1139/cgj-2017-0317)

### 総説と，手法を紹介した資料

27. Duncan, J. M. (1996). “State of the Art: Limit Equilibrium and Finite-Element Analysis of Slopes.” *Journal of Geotechnical Engineering*, 122(7), 577–596. [https://doi.org/10.1061/(ASCE)0733-9410(1996)122:7(577)](https://doi.org/10.1061/%28ASCE%290733-9410%281996%29122%3A7%28577%29)
28. Kalatehjari, R., and Ali, N. (2013). “A Review of Three-Dimensional Slope Stability Analyses based on Limit Equilibrium Method.” *Electronic Journal of Geotechnical Engineering*, 18, Bund. A, 119–134. [書誌情報](https://web.archive.org/web/20131228112355/http://www.ejge.com/2013/Ppr2013.011alr.pdf)
29. Read, J. (2021). “Three-dimensional limit equilibrium slope stability analyses, method, and design acceptance criteria uncertainties.” *SSIM 2021: Second International Slope Stability in Mining*, 3–10. [https://doi.org/10.36487/ACG_repo/2135_0.01](https://doi.org/10.36487/ACG_repo/2135_0.01)
30. Rocscience. “Slide3 – 3D Limit Equilibrium Slope Stability Overview.” 2026年10月閲覧．[書誌情報](https://static.rocscience.cloud/assets/verification-and-theory/Slide3/3D-Limit-Equilibrium-Slope-Stability.pdf)
