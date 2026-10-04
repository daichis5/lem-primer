---
title: "極限平衡法とは何か：各手法は，残った未知量をどの仮定で決めるか"
lang: ja
series: "2 of 3"
---

# 極限平衡法とは何か

**各手法は，残った未知量をどの仮定で決めるか**

第1資料では，スライス底面の力の式を導いた．しかし，この式だけでは，底面の力の大きさも安全率も決まらない．この資料では，各手法が足りない条件をどの仮定で補うのかを，2次元と3次元の極限平衡法（limit equilibrium method，LEM）について比べる．手法ごとの式を覚えることが目的ではない．すべての力を考えた本来の静力学の問題と照らし合わせながら，各手法が何を満たし，何を簡略化し，何を解かないのかを整理する．

この資料は，[第1資料](continuum-mechanics-to-lem-start.md)を読んだ前提で進める．用語と記号は，[用語集](lem-glossary.md)にまとめた．

```{admonition} この資料の要点
LEMの手法どうしの違いは，計算式の形だけにあるのではない．連続体をスライスやカラムに分けると，つり合い式だけでは内力が決まらない状態が残る．この状態を，**静力学的不静定性**（static indeterminacy）という．手法の違いは，**この不静定性を，内力についてのどの仮定と，どのつり合い条件で解消するか**にある．
```

---

(what-section-0)=

## 0. この資料の範囲と用語

この資料では，「厳密」という語を，次の2つの意味に分けて使う．

1. **連続体力学としての厳密さ**：応力場，変位場，構成則，適合条件，境界条件をすべて満たす境界値問題として解くこと
2. **LEMの中での静力学的な厳密さ**：仮定した{term}`すべり面`，強度の動員の仕方，スライス間力やカラム間力のモデルのもとで，必要な力とモーメントのつり合いをすべて満たすこと

Spencer法やMorgenstern–Price法を「厳密法」（rigorous method）と呼ぶことがある．この「厳密」は，主に2つ目の意味である．これらの方法も，変位の適合条件や，土の応力とひずみの関係まで解く連続体の解析ではない．

この後は，断らない限り，有効応力で表した{term}`Mohr–Coulomb則`による強度を考える．記号は次のとおりとする．

| 記号 | 意味 |
|---|---|
| $F_s$ | 安全率（factor of safety） |
| $c_i',\phi_i'$ | 第 $i$ 要素の底面の有効粘着力と有効内部摩擦角 |
| $A_i$ | 第 $i$ 要素の底面積．2次元では，奥行きを単位長さとしたときの底面積 |
| $N_i$ | 底面に働く全垂直力 |
| $U_i$ | 底面に働く間隙水圧の合力 |
| $T_i$ | 底面に沿って動員されているせん断力の大きさ |
| $W_i$ | 自重．外力や地震時の慣性力は，必要に応じて別に加える |
| $E,X$ | 2次元のスライス間の垂直力とせん断力．$E$ は境界の面に垂直な成分，$X$ は境界の面に沿う成分 |
| $\boldsymbol{n}_i$ | 第 $i$ 要素の底面の単位法線ベクトル．すべり土塊の外向きにとる |
| $\boldsymbol{m}_i$ | 第 $i$ 要素の底面で仮定した，局所的なすべり方向の単位ベクトル |

---

## 第1部　2次元のLEMの出発点

(what-section-1)=

### 1. すでに分かっていることと，まだ分からないこと

第1資料でたどり着いた式は，次のとおりである．

$$
T_i
=
\frac{
c_i' A_i + (N_i-U_i)\tan\phi_i'
}{F_s}
$$ (eq-what-base-shear)

この式は，{term}`せん断強度`を

$$
c_{m,i}'=\frac{c_i'}{F_s},
\qquad
\tan\phi_{m,i}'=\frac{\tan\phi_i'}{F_s}
$$ (eq-what-mobilized-parameters)

まで低減した状態で，すべり面全体が極限状態にあると仮定している．

式 {eq}`eq-what-base-shear` から，$T_i$ は独立な未知量ではなく，$N_i$ と $F_s$ が決まれば求まる．しかし，それだけでは問題は解けない．

#### 分かっている量

- 斜面の形，地層の境界，仮定したすべり面
- 各スライスの重さ $W_i$
- $c_i',\phi_i'$ と底面積 $A_i$
- {term}`間隙水圧`の分布から求める $U_i$
- 与えた外力，地震時の慣性力，アンカー力など

#### まだ分からない量

- 各スライスの{term}`底面垂直力` $N_i$
- すべり面全体で共通の{term}`安全率` $F_s$
- スライス間力の大きさと向き
- 各スライスでモーメントのつり合いを考えるなら，スライス間力の合力が働く位置

このうち，スライス間力のように，隣り合うスライスどうしが境界で及ぼし合う力を，**内力**という．

つまり，LEMの本当の出発点は，式 {eq}`eq-what-base-shear` そのものではなく，次の問いである．

> **未知の内力を含む静力学の問題を，どんな仮定を加えて，一意に解ける形にするか．**

---

(what-section-2)=

### 2. 2次元で本来考えなければならない力

```{figure} ./figures/fig_01_2d_slice_forces.svg
:name: fig-01-2d-slice-forces
:alt: 側面が鉛直なスライスに働く自重，底面の垂直力とせん断力，左右のスライス間力の自由物体図

2次元のスライスの自由物体図．底面の $N_i$，$T_i$，左右の境界の $E$，$X$，自重 $W_i$，底面の傾き $\alpha_i$，スライス間力が働く高さ $h$ を示す．矢印の長さは，力のつり合いを満たすように描いた
```

第 $i$ スライスを土塊から切り出すと，少なくとも次の力を考えなければならない．

- 自重 $W_i$
- 底面垂直力 $N_i$
- {term}`底面せん断力` $T_i$
- 左の境界でのスライス間の垂直力 $E_{i-1}$ とせん断力 $X_{i-1}$
- 右の境界でのスライス間の垂直力 $E_i$ とせん断力 $X_i$
- 必要に応じて，水圧，外からの荷重，地震時の慣性力，補強材の力

剛体として取り出したスライスには，それぞれ，平面内で3つの独立なつり合い式がある．

$$
\sum F_x=0,
\qquad
\sum F_z=0,
\qquad
\sum M_y=0
$$ (eq-what-2d-equilibrium)

しかし，連続体力学から見ると，スライスどうしの境界（内部境界）には，1本の矢印ではなく，位置によって変わる{term}`表面力`（traction）の分布

$$
\boldsymbol{t}(\boldsymbol{x})
=
\boldsymbol{\sigma}(\boldsymbol{x})\boldsymbol{n}
$$ (eq-what-cauchy)

が働く．LEMは，この分布を，$E$ と $X$ という合力と，必要ならその合力が働く位置にまとめる．この時点で，連続な応力場を有限個の合力に置き換える**離散化**（discretization）が，すでに行われている．

---

### 3. なぜつり合い式だけでは解けないのか

```{figure} ./figures/fig_02_indeterminacy.svg
:name: fig-02-indeterminacy
:alt: 5つのスライスで，各底面の垂直力，各境界のスライス間力とその作用位置，全体で1つの安全率が働く場所を示した図

$n=5$ のスライスに残る未知量．各底面に $N$，スライスの間の各境界に $E$，$X$，$h$，全体で1つの $F_s$ があり，合わせて18個になる
```

(what-section-3-1)=

#### 3.1 未知数を数える

$n$ 個のスライスについて，式 {eq}`eq-what-base-shear` を使って底面せん断力 $T_i$ を $N_i$ と $F_s$ で表しても，代表的な定式化では次の未知量が残る．

| 未知量 | 個数 |
|---|---:|
| 底面垂直力 $N_i$ | $n$ |
| スライス間の垂直力 $E_i$ | $n-1$ |
| スライス間のせん断力 $X_i$ | $n-1$ |
| スライス間力の合力が働く位置 $h_i$ | $n-1$ |
| 安全率 $F_s$ | $1$ |
| **合計** | **$4n-2$** |

一方，各スライスに式 {eq}`eq-what-2d-equilibrium` を当てはめて得られる式は，$3n$ 本である．未知量の数え方は，合力とその位置をどう表すかや，全体のつり合いを別に数えるかによって変わる．しかし，どの数え方でも，次の点は変わらない．

$$
\boxed{
\text{つり合い条件と底面の強度の式だけでは，内力の分布は一意に決まらない}
}
$$ (eq-what-indeterminacy)

これが，冒頭で述べた静力学的不静定性である．

```{note}
この表では，底面垂直力 $N_i$ が働く位置を，未知量に数えていない．$N_i$ が底面の中央に働くという，慣例の仮定を先に置いたことにあたる．作用位置も未知量に数える教科書の数え方では，Mohr–Coulomb則の式も含めて，未知量が $6n-2$ 個，式が $4n$ 本になる．足りない $2n-2$ 個のうち $n$ 個を，$N_i$ が底面の中央に働くという仮定で補えば，残りは $n-2$ 個で，この表の数え方と一致する．
```

#### 3.2 連続体の解析なら，何が加わるか

連続体の境界値問題では，つり合いに加えて，少なくとも次の条件を連立させる．

- ひずみと変位の関係
- 構成則（応力とひずみの関係）
- 変位の適合条件
- 応力の境界条件と変位の境界条件
- 弾塑性の履歴や，各点の降伏条件

LEMは，ふつう，これらを解かない．その代わりに，スライス間力の向き，比，働く位置，または無視できる成分を仮定する．

(what-section-3-3)=

#### 3.3 不静定性を「解消する」とは，何をすることか

不静定の問題を解けるようにする操作を，ここでは**不静定性の解消**（closure）と呼ぶ．よく使われる解消の仕方は，次の3種類である．

1. 内力の一部を無視する
2. 内力の向きや，成分の比を仮定する
3. つり合い条件の一部だけを使い，残りは満たさなくてよいとする

LEMの各手法は，この3つの組み合わせで分類できる．2次元の各手法を1つの枠組みで比べた論文に，[Fredlund and Krahn (1977)](https://doi.org/10.1139/t77-045)がある．

---

## 第2部　2次元のLEMは何を簡略化しているのか

(what-section-4)=

### 4. 2次元の手法を比べる観点

```{figure} ./figures/fig_03_2d_methods.svg
:name: fig-03-2d-methods
:alt: 同じスライスで，Fellenius法，簡易Bishop法，簡易Janbu法が無視する内力と，使うつり合いを比べた図

Fellenius法，簡易Bishop法，簡易Janbu法の比較．同じスライスで，無視する内力（薄い破線）と，使うつり合いを比べる
```

この後は，各手法を次の4つの観点から比べる．

1. スライス間力をどう扱うか
2. どのつり合い条件を満たすか
3. すべり面の形にどんな制約があるか
4. その結果，何が計算しやすくなり，何が保証されなくなるか

4.1節から4.3節の3つの手法は，どれも内力の一部またはすべてを無視し，つり合い条件の一部だけを満たす．このシリーズでは，こうした手法をまとめて**つり合いの一部だけを満たす方法**と呼び，5節の静力学的に完全な方法と区別する．

#### 4.1 Fellenius法（簡便分割法）

Fellenius法（簡便分割法）は，底面垂直力を求めるときに，隣のスライスから受ける垂直力とせん断力の効果を無視する．そのうえで，円弧すべりについての全体のモーメントのつり合いから，安全率を求める．英語では，Ordinary Method of SlicesやSwedish Circle Methodとも呼ばれる．日本の基準や実務の資料では，単に簡便法と呼ぶことが多い．

奥行きを単位長さとし，円弧すべりで，スライスの水平の幅 $b_i$，底面の長さ $l_i$，底面の傾き $\alpha_i$ を使うと，代表的な式は次の形になる．

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
水圧の項の書き方は，記号の決め方によって変わる．
```

##### 不静定性の解消の仕方

- スライス間力の効果を無視する
- 円弧の中心まわりの，全体のモーメントのつり合いを使う
- 各スライスの水平方向と鉛直方向の力のつり合いは，同時には満たさない

##### 力学的な意味

スライス間力の合力の効果を，安全率の計算に含めない近似である．そのため，各スライスの底面垂直力や内力を求める用途には向かない．

```{note}
この近似は，スライス間力が物理的に存在しないとみなすものではない．スライス間力は存在するが，その効果を安全率の計算に含めていないだけである．
```

**原典**：Felleniusの方法は，1920年代の著作までさかのぼる．書誌を確かめられた資料には，W. Fellenius, *Erdstatische Berechnungen mit Reibung und Kohäsion (Adhäsion) und unter Annahme kreiszylindrischer Gleitflächen*, Ernst & Sohn, Berlin, 1927がある（[書誌情報](https://books.google.com/books?id=yHhHAAAAIAAJ)）．もう1つは，“Calculation of the Stability of Earth Dams,” *Proceedings of the Second Congress on Large Dams*, Vol. 4, pp. 445–462, 1936である（[書誌情報](https://cir.nii.ac.jp/crid/1573950399306830336)）．どちらにも，確かめられる現代のDOIはない．

---

#### 4.2 簡易Bishop法

簡易Bishop法（Simplified Bishop Method）は，スライス間の垂直力 $E_i$ は残し，スライス間のせん断力の合力を簡略化する．ふつうは $X_i-X_{i-1}=0$ とし，実装では各境界で $X_i=0$ として扱う．そのうえで，各スライスの鉛直方向の力のつり合いと，円弧の中心まわりの全体のモーメントのつり合いを組み合わせる．

代表的な形は，次のとおりである．

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

右辺にも $F_s$ が現れるので，反復計算で求める．

##### 不静定性の解消の仕方

- スライス間の垂直力は残す
- スライス間のせん断力を簡略化する
- 各スライスの鉛直方向の力のつり合いから，$N_i$ を求める
- 全体のモーメントのつり合いから，$F_s$ を求める
- 全体の水平方向の力のつり合いは，一般に厳密には満たさない

##### 力学的な意味

Fellenius法より底面垂直力の求め方はよくなるが，内力の向きまでは解いていない．古典的な定式化は，円弧すべりを対象とする．円弧では，共通の中心まわりのモーメントの式が，特に簡単になるからである．

**原著論文**：[A. W. Bishop (1955), “The use of the slip circle in the stability analysis of slopes,” *Géotechnique*, 5(1), 7–17. DOI: 10.1680/geot.1955.5.1.7](https://doi.org/10.1680/geot.1955.5.1.7)

---

#### 4.3 簡易Janbu法

Janbu法の系統は，{term}`任意形状のすべり面 <一般形状のすべり面>`を扱いやすくし，主に力のつり合いから安全率を求める方向に発展した．簡易Janbu法（Simplified Janbu Method）は，スライス間のせん断力を簡略化し，全体の水平方向の力のつり合いを中心に安全率を求める．

##### 不静定性の解消の仕方

- ふつうは，スライス間のせん断力を無視するか，簡略化する
- 力のつり合いを使う
- 全体のモーメントのつり合いは，完全には満たさない
- モーメントのつり合いが崩れる影響を補うために，経験的な補正係数 $f_0$ を使う簡便な形がある

##### 簡易Bishop法との対比

$$
\begin{array}{c|c}
\text{簡易Bishop法} & \text{簡易Janbu法} \\
\hline
\text{円弧すべりと相性がよい} & \text{任意形状のすべり面を扱いやすい} \\
\text{全体のモーメントのつり合いを重視} & \text{全体の力のつり合いを重視} \\
\text{水平方向の力のつり合いを満たさない} & \text{モーメントのつり合いを満たさない}
\end{array}
$$ (eq-what-bishop-janbu)

```{note}
補正係数を掛けても，満たしていないモーメントのつり合いが厳密に満たされるわけではない．補正係数は，特定の仮定と経験的な整理のもとで，安全率の偏りを減らすための補正である．
```

**初期の文献**：N. Janbu (1954), “Application of composite slip surfaces for stability analysis,” *Proceedings of the European Conference on Stability of Earth Slopes*, Stockholm, Vol. 3, pp. 43–49（[書誌情報](https://cir.nii.ac.jp/crid/1570009750148611712)）．確かめられるDOIはない．一般化して整理した文献として，N. Janbu (1973), “Slope Stability Computations,” in *Embankment-Dam Engineering: Casagrande Volume*, pp. 47–86もよく参照される．

---

### 5. 内力の向きを仮定し，力とモーメントを同時に満たす方法

```{figure} ./figures/fig_04_spencer_mp.svg
:name: fig-04-spencer-mp
:alt: Spencer法とMorgenstern–Price法で，スライス境界の合力の傾きと，関数 f(x) を比べた図

Spencer法では，合力の傾きがすべての境界で同じである．Morgenstern–Price法では，傾きが $\lambda f(x)$ に従って変わる．下のグラフは，それぞれの $f(x)$ を同じ横軸で示す
```

(what-section-5-1)=

#### 5.1 Spencer法

Spencer法は，各スライスの境界に働く合力の向きが互いに平行，つまり一定の角度 $\theta$ をもつと仮定する．

$$
\frac{X_i}{E_i}=\tan\theta
=\text{一定}
$$ (eq-what-spencer)

$F_s$ と $\theta$ を未知量として，全体の力のつり合いとモーメントのつり合いを，両方とも満たす．

##### 不静定性の解消の仕方

- スライス間力を無視しない
- スライス間力の合力の**向きが，すべての境界で同じ**だと仮定する
- 力とモーメントのつり合いを同時に満たすように，$F_s$ と $\theta$ を求める

##### 「厳密」の意味

Spencer法は，仮定した内力の向きのもとで，力とモーメントのつり合いをすべて満たす．このように，つり合いをすべて満たす方法を，**静力学的に完全な方法**という．ただし，角度 $\theta$ が一定だというのは仮定で，連続体の実際の応力場から導いたものではない．そのため，静力学的に完全であっても，求まる内力の分布が物理的に唯一の解だとは限らない．

**原著論文**：[E. Spencer (1967), “A method of analysis of the stability of embankments assuming parallel inter-slice forces,” *Géotechnique*, 17(1), 11–26. DOI: 10.1680/geot.1967.17.1.11](https://doi.org/10.1680/geot.1967.17.1.11)

---

(what-section-5-2)=

#### 5.2 Morgenstern–Price法

Morgenstern–Price法は，スライス間のせん断力と垂直力の比を，位置 $x$ の既知の形の関数 $f(x)$ と，未知の倍率 $\lambda$ で表す．

$$
X(x)=\lambda f(x)E(x),
\qquad
\frac{X(x)}{E(x)}=\lambda f(x)
$$ (eq-what-morgenstern-price)

$f(x)$ は，正弦の半波（half-sine），台形（trapezoidal），一定（constant）などから選び，$\lambda$ は解析の中で決める．$F_s$ と $\lambda$ を調整して，力とモーメントのつり合いと，両端での条件を満たす．

##### 不静定性の解消の仕方

- スライス間力を無視しない
- 内力の向きが**場所によってどう変わるか**を，$f(x)$ として仮定する
- その大きさを決める $\lambda$ と，安全率 $F_s$ を解く
- 力とモーメントのつり合いを，同時に満たす

##### Spencer法との関係

$f(x)=1$ とすれば，$X/E=\lambda$ は一定になる．つまり，Spencer法は，Morgenstern–Price法の内力の関数を一定にした，特別な場合とみなせる．

##### 何が残るか

妥当な $f(x)$ を何通りか試して，安全率が近い値になったとしても，スライス間力や底面垂直力の分布は違うことがある．安全率が一致しても，内部の応力場が1つに決まったことにはならない．

**原著論文**：[N. R. Morgenstern and V. E. Price (1965), “The analysis of the stability of general slip surfaces,” *Géotechnique*, 15(1), 79–93. DOI: 10.1680/geot.1965.15.1.79](https://doi.org/10.1680/geot.1965.15.1.79)

**数値解法**：[N. R. Morgenstern and V. E. Price (1967), “A numerical method for solving the equations of stability of general slip surfaces,” *The Computer Journal*, 9(4), 388–393. DOI: 10.1093/comjnl/9.4.388](https://doi.org/10.1093/comjnl/9.4.388)

---

(what-section-6)=

### 6. 2次元のLEMを一覧表で比べる

| 手法 | 主なすべり面 | スライス間力の扱い | 主に満たすつり合い | 満たさないつり合い・主な仮定 | 位置付け |
|---|---|---|---|---|---|
| Fellenius法 | 円弧 | 効果を無視 | 全体のモーメント | 力のつり合い，内力 | 最も単純 |
| 簡易Bishop法 | 主に円弧 | 垂直力は考え，せん断力を簡略化 | 各スライスの鉛直方向の力＋全体のモーメント | 全体の水平方向の力 | モーメントのつり合いを重視 |
| 簡易Janbu法 | 任意形状 | せん断力を簡略化 | 全体の力 | 全体のモーメント | 力のつり合いを重視 |
| Spencer法 | 円弧．一般形状にも拡張できる | 合力の向きを一定と仮定 | 力＋モーメント | 内力の向きが一定 | 静力学的に完全なLEM |
| Morgenstern–Price法 | 任意形状 | $X/E=\lambda f(x)$ | 力＋モーメント | 内力の関数 $f(x)$ | 一般化したLEM |

```{note}
「主に満たすつり合い」は，標準的な定式化についてのまとめである．ソフトウェアの実装は，同じ名前の手法でも，拡張した式や，地震荷重・補強材・非円弧面の扱いによって，細部が違う．使う前に，マニュアルに書かれた式と収束の判定を確かめておく．
```

---

## 第3部　3次元では何が増えるのか

(what-section-7)=

### 7. スライスからカラムへ

```{figure} ./figures/fig_05_3d_column_forces.svg
:name: fig-05-3d-column-forces
:alt: 傾いた底面をもつ3次元のカラムに働く自重，底面の垂直力とせん断力，側面のカラム間力

3次元のカラムに働く力．底面のせん断力 $\boldsymbol{T}_i$ は接平面の中のベクトルで，向きは強度の式からは決まらない（点線の円）．側面には，垂直成分と2つのせん断成分が働く
```

2次元では，{term}`すべり土塊`を1方向にだけ分け，各要素を「スライス」と呼ぶ．3次元では，平面上の2方向に分けるため，各要素は柱の形の「カラム」になる．

#### 7.1 底面の力がベクトルになる

第 $i$ カラムの底面に，すべり土塊の外向きの単位法線ベクトル $\boldsymbol{n}_i$ をとる．また，仮定した{term}`局所的なすべり方向 <局所すべり方向>`の単位ベクトルを $\boldsymbol{m}_i$ とし，すべりに抵抗する底面のせん断力のベクトルを，次のように定める．

$$
\boldsymbol{T}_i=-T_i\boldsymbol{m}_i
$$

このとき，すべり土塊が底面から受ける合力は，次のように分けられる．

$$
\boldsymbol{R}_{b,i}
=
-N_i\boldsymbol{n}_i+\boldsymbol{T}_i,
\qquad
\boldsymbol{T}_i\cdot\boldsymbol{n}_i=0
$$ (eq-what-column-base-force)

$\boldsymbol{T}_i$ は，底面の接平面内のベクトルで，一般に独立な成分を2つもつ．

Mohr–Coulomb則から直接分かるのは，その**大きさ**だけである．

$$
\|\boldsymbol{T}_i\|
=
\frac{
c_i'A_i+(N_i-U_i)\tan\phi_i'
}{F_s}
$$ (eq-what-column-shear)

しかし，式 {eq}`eq-what-column-shear` だけでは，接平面内の**向き**は決まらない．そのため，3次元のLEMでは，少なくとも次のどれかが要る．

- すべてのカラムで共通の，または規則的なすべり方向を仮定する
- 各点で最も急に傾く方向を使う
- 全体のつり合いと合う向きを，未知量として解く
- 速度場や，運動学的な機構から向きを与える

2次元では，せん断力の向きが断面内で事実上決まっているので，この問題は目立たない．3次元では，安全率だけでなく，**どちら向きにすべると仮定したか**も，定式化の一部になる．

(what-section-7-2)=

#### 7.2 内部境界が2組になる

直交する $x$ 方向と $y$ 方向にカラムを並べると，内部境界は2つの組に分かれる．各カラムの鉛直な側面では，一般に次の量を考えなければならない．

- 面に垂直な成分の合力（垂直力）
- 面内のせん断力の鉛直成分
- 面内のせん断力の水平成分
- それぞれの合力が働く位置

つまり，2次元の $E$ と $X$ を，本数だけ増やせばよいのではない．内力の合力の向きの自由度と，モーメントへの寄与が増える．

#### 7.3 つり合い式も6つになるが，未知量はさらに増える

3次元の剛体には，次の6つのつり合い条件がある．

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

しかし，カラムごとに，底面のせん断力の向きと，2組のカラム間力が未知量に加わる．そのため，つり合い式が3つから6つに増えただけでは，問題は解ける形にならない．

$$
\boxed{
\text{2次元から3次元への拡張}
\neq
\text{同じ式に奥行きの幅を掛けること}
}
$$ (eq-what-3d-not-extrusion)

3次元に拡張するには，内部境界が増えること，底面のせん断力の向きに自由度があること，{term}`回転軸 <モーメントの中心>`や{term}`全体すべり方向`を選ぶことを，同時に扱わなければならない．

---

### 8. 3次元のLEMは，どのような考え方で拡張されたか

3次元のLEMの多くは，一から別に作られたのではない．代表的な考え方は，次のとおりである．

1. スライスをカラムに置き換える
2. 2次元で置いた内力の仮定を，2方向のカラムの境界に広げる
3. 円弧の中心まわりのモーメントを，3次元の回転軸まわりのモーメントに置き換える
4. 2次元では暗黙だったすべり方向を，対称面，主なすべり方向，または未知のパラメータとして加える

この後は，代表的な手法の発展を，この観点から見ていく．

---

#### 8.1 Hovland法：Fellenius型の直接の拡張

Hovland法は，初期の一般的な3次元のLEMである．すべり土塊を鉛直なカラムに分け，3次元の底面の形と，側方の端部の効果を扱えるようにした．力学的な骨組みは，カラム間力を無視する，Fellenius型の拡張とみなせる．

##### 拡張の考え方

- 2次元のスライスを，3次元のカラムに置き換える
- 各カラムの底面の傾きと面積を使う
- カラム間力を無視し，重さから底面垂直力を求める
- 仮定した全体すべり方向について，{term}`抵抗力`と{term}`滑動力`を足し合わせる

##### 得られるものと失うもの

幅が有限なすべり土塊や，一様でない3次元の形，端部を含む形の効果を表せる．一方，内力を無視するので，3方向の力のつり合いとモーメントのつり合いを，一般に完全には満たさない．つまり，3次元にしただけで，静力学的により厳密になるわけではない．

**原著論文**：[H. J. Hovland (1977), “Three-Dimensional Slope Stability Analysis Method,” *Journal of the Geotechnical Engineering Division*, 103(9), 971–986. DOI: 10.1061/AJGEB6.0000493](https://doi.org/10.1061/AJGEB6.0000493)

---

#### 8.2 HungrとUgai：簡易Bishop法などをカラム法に拡張する

Hungrは，簡易Bishop法を3次元に直接拡張した．Ugaiらも，簡便分割法，簡易Bishop法，簡易Janbu法，Spencer法を3次元に拡張する一連の研究を行った．

##### 3次元の簡易Bishop法の考え方

- 2次元と同じく，カラム間のせん断力の鉛直成分を無視する
- 各カラムの鉛直方向の力のつり合いから，底面垂直力を求める
- 仮定した回転軸まわりの，全体のモーメントのつり合いから，$F_s$ を求める
- 水平な2方向の力のつり合いは，一般に満たさない

この拡張は，簡易Bishop法の計算のしやすさを保ちながら，有限の幅，端部，平面の形の効果を取り込む．しかし，回転しない機構の問題や，非対称性が強い問題，底面のせん断力の向きが複雑な問題では，元の仮定が適切かを別に確かめなければならない．

##### Ugaiらの位置付け

Ugaiらは，まず3次元の簡便分割法を示し，その後，簡易Bishop法，簡易Janbu法，Spencer法を3次元に拡張した．このことから，3次元のLEMの発展は，1つの3次元の公式にまとまるものではないことが分かる．実際には，**2次元での不静定性の解消の仕方を，カラムの集まりに移した，いくつもの系譜**からなる．

**主な一次論文**：

- [O. Hungr (1987), “An extension of Bishop's simplified method of slope stability analysis to three dimensions,” *Géotechnique*, 37(1), 113–117. DOI: 10.1680/geot.1987.37.1.113](https://doi.org/10.1680/geot.1987.37.1.113)
- [O. Hungr, F. M. Salgado and P. M. Byrne (1989), “Evaluation of a three-dimensional method of slope stability analysis,” *Canadian Geotechnical Journal*, 26(4), 679–686. DOI: 10.1139/t89-079](https://doi.org/10.1139/t89-079)
- [K. Ugai, K. Hosobori, H. Nagase and M. Enokido (1986), “Three-dimensional stability analysis of slopes by simple slice method,” *土木学会論文集*, No. 376/III-6, 267–276. DOI: 10.2208/jscej.1986.376_267](https://doi.org/10.2208/jscej.1986.376_267)
- [K. Ugai and K. Hosobori (1988), “Extension of simplified Bishop method, simplified Janbu method and Spencer's method to three dimensions,” *土木学会論文集*, No. 394/III-9, 21–26. DOI: 10.2208/jscej.1988.394_21](https://doi.org/10.2208/jscej.1988.394_21)

---

#### 8.3 3次元のSpencer法：一定の向きの仮定を，平面と空間に拡張する

2次元のSpencer法では，スライス間力の合力が，共通の傾きの角をもつ．3次元への拡張では，この「平行な内力」という考えを，2方向のカラムの境界での合力の向きや，共通の方向の面として表す．

##### 拡張で新しく要るもの

- 主なすべり方向，または回転軸
- 2組のカラム間力の向きの関係
- 底面の接平面内でのせん断力の向き
- 3方向の力のつり合いと，使うモーメントのつり合い条件

3次元のSpencer型の手法は，カラム間力の向きの仮定のもとで，Hovland法や3次元の簡易Bishop法より多くのつり合い条件を満たすことを目指す．ただし，2次元で「すべての内力が平行」とした1つの角度を，3次元にどう拡張するかは，1通りには決まらない．論文やソフトウェアによって，どの成分を平行とするか，どの軸まわりのモーメントのつり合いを使うかが違う．

Jiang and Yamagamiは，2次元のSpencer法の安全率の式をカラム法に拡張し，動的計画法で3次元の{term}`臨界すべり面`を探す方法と組み合わせた．

**代表的な一次論文**：[J.-C. Jiang and T. Yamagami (2004), “Three-Dimensional Slope Stability Analysis Using an Extended Spencer Method,” *Soils and Foundations*, 44(4), 127–135. DOI: 10.3208/sandf.44.4_127](https://doi.org/10.3208/sandf.44.4_127)

---

(what-section-8-4)=

#### 8.4 Lam–Fredlundの3次元のGLE：Morgenstern–Price型の一般化

Lam and Fredlundは，2次元の一般極限平衡法（general limit equilibrium，GLE）を，カラム法に拡張した．3次元では内部境界が2方向にあるので，それぞれのカラム間力の合力の向きを表す関数が要る．

考え方としては，2方向の内部境界について，次のような関係を仮定する．

$$
x\text{方向の境界でのせん断力と垂直力の比}
=\lambda_x f_x(x,y)
$$ (eq-what-3d-lambda-x)

$$
y\text{方向の境界でのせん断力と垂直力の比}
=\lambda_y f_y(x,y)
$$ (eq-what-3d-lambda-y)

実際の成分の記号や関数の置き方は，定式化によって違う．しかし，中心となる考えは同じである．

##### 拡張の考え方

- 2次元の $X/E=\lambda f(x)$ を，2方向のカラム間力の関数に一般化する
- カラム間力の合力の向きの変化を，任意の形の関数で表す
- 力とモーメントのつり合いを同時に満たす，安全率と倍率を探す
- 斜面，地層，すべり面，間隙水圧を，3次元の空間でモデル化する

この方法で，3次元のLEMはより一般的になる．一方で，仮定しなければならない内力の関数や，未知の倍率，収束計算が増える．自由度が増えた分だけ，入力した仮定が結果に与える影響を，よく確かめなければならない．

**原著論文**：[L. Lam and D. G. Fredlund (1993), “A general limit equilibrium model for three-dimensional slope stability analysis,” *Canadian Geotechnical Journal*, 30(6), 905–919. DOI: 10.1139/t93-089](https://doi.org/10.1139/t93-089)

---

#### 8.5 Cheng–Yip：非対称な3次元の斜面への一般化

初期の3次元のLEMの多くは，対称面や，既知の主なすべり方向を，暗黙に仮定していた．Cheng and Yipは，簡易Bishop法，簡易Janbu法，Morgenstern–Price法の考えを，非対称な3次元の斜面に拡張した．

##### 考え方の要点

- 平面の形とすべり面が対称であることを，前提にしない
- 2つの水平な軸の方向について，底面の力とカラム間力をはっきり書く
- 2次元の各手法の「何を無視し，何をつり合わせるか」を，3次元に対応させる
- Morgenstern–Price型では，2方向の内力の関数と係数を加える

この研究から，3次元への拡張の要点は，形を立体にすることだけではないことが分かる．**2次元では1方向だった内力の仮定と全体すべり方向を，空間の中で定め直すこと**にある．

**原著論文**：[Y. M. Cheng and C. J. Yip (2007), “Three-Dimensional Asymmetrical Slope Stability Analysis—Extension of Bishop's, Janbu's, and Morgenstern–Price's Techniques,” *Journal of Geotechnical and Geoenvironmental Engineering*, 133(12), 1544–1555. DOI: 10.1061/(ASCE)1090-0241(2007)133:12(1544)](https://doi.org/10.1061/%28ASCE%291090-0241%282007%29133%3A12%281544%29)

---

(what-section-9)=

### 9. 3次元のLEMを一覧表で比べる

| 手法・系統 | 対応する2次元の考え方 | カラム間力 | 主なつり合い | 特徴・制約 | 一次文献 |
|---|---|---|---|---|---|
| Hovland法 | Fellenius型 | 無視 | 主に全体の抵抗力と滑動力を足し合わせる | 単純だが，静力学的に完全ではない | Hovland (1977) |
| Hungrの3次元の簡易Bishop法 | 簡易Bishop法 | せん断力の鉛直成分を簡略化 | カラムの鉛直方向の力＋全体のモーメント | 回転する，比較的対称な問題と相性がよい | Hungr (1987) |
| Ugaiらの系統 | 簡易Bishop法・簡易Janbu法・Spencer法 | 元の2次元の手法に合わせて仮定 | 手法ごとに違う | 2次元の各系統を，それぞれ3次元に拡張した | Ugai et al. (1986); Ugai & Hosobori (1988) |
| 3次元に拡張したSpencer法 | Spencer法 | 空間の中で平行と仮定 | 力＋使うモーメントの条件 | 3次元での「平行」の定め方が，実装によって違う | Jiang & Yamagami (2004) |
| Lam–Fredlundの3次元のGLE | Morgenstern–Price法・GLE | 2方向の関数で表す | 力＋モーメント | 一般性は高いが，仮定と未知量も多い | Lam & Fredlund (1993) |
| Cheng–Yip | 簡易Bishop法・簡易Janbu法・Morgenstern–Price法 | 2方向で，2次元の各仮定を拡張 | 手法ごとに違う | 非対称な3次元の形を，直接扱う | Cheng & Yip (2007) |

#### 3次元の安全率を読むときの注意

3次元の解析では，側方の端部の抵抗が加わるので，同じ中央の断面での2次元の解析より，安全率が高くなる例が多い．しかし，次の条件が違えば，単純には比べられない．

- 2次元と3次元で探したすべり面が，同じ破壊の機構を表しているか
- 3次元で仮定した全体すべり方向が適切か
- カラム間力をどこまで考えたか
- 側面に働く強度を，二重計上していないか
- 2次元の単位長さの奥行きと，3次元の有限の幅を，どう対応させたか
- 地層，間隙水圧，外力の3次元の分布が，2次元の解析と一致しているか

```{warning}
そのため，この傾向を，「3次元の安全率は，必ず2次元より大きい」という決まりとして使ってはならない．差が出た理由は，形，強度，内力の仮定，探した破壊の機構に分けて説明しなければならない．
```

---

## 第4部　LEMに含まれる近似の階層

(what-section-10)=

### 10. 近似は内力の仮定だけではない

LEMの近似は，下から上へ積み重なる層として整理すると，分かりやすい．

#### 第1層：幾何学的な離散化

連続な土塊を，有限個のスライスやカラムに置き換える．

- 曲面を，平面の小片や単純な底面で近似する
- 分布する荷重や応力を，合力に置き換える
- 分割の数と向きによって，離散化の誤差が生じる

#### 第2層：破壊機構の仮定

すべり面，または探すことのできるすべり面の族を，あらかじめ決める．

- 円弧，複合面，非円弧面，楕円体，NURBS面など
- 実際の進行性破壊や，複数の面がつながる破壊が，探す範囲に入っていないことがある
- 求まる最小安全率は，探した面の族の中での最小値である

#### 第3層：強度の動員の仮定

すべり面全体で1つの安全率 $F_s$ を共有し，強度が，どこでも同時に同じ割合で動員されるとする．

$$
\tau_{m,i}
=
\frac{
c_i'+(\sigma_{n,i}-u_i)\tan\phi_i'
}{F_s}
$$ (eq-what-mobilized-stress)

この仮定は，場所によるひずみの違いや，ピーク強度から残留強度への軟化，進行性破壊を，直接は表さない．

#### 第4層：内力の決め方

- 内力の成分を無視する
- 内力の向きを一定とする
- 内力の比が場所によってどう変わるかを，関数で仮定する
- 内力が働く位置を，仮定するか，計算する

LEMの各手法の名前は，主にこの層を表している．

#### 第5層：3次元の全体すべり方向と回転軸

3次元では，さらに，底面のせん断力のベクトルの向き，全体すべり方向，モーメントをとる軸を決めなければならない．対称な問題では，形から候補が決まる．非対称な問題では，これらは未知量か，探す変数になる．

#### 第6層：数値解法と探索

- $F_s$，内力の倍率，内力の角度を反復して解く方法
- 臨界すべり面の探索
- 収束の判定と局所解
- 適切でない底面垂直力，負の有効垂直力，内力線（スライス間力の作用点を結んだ線）がスライスの外にはみ出すことへの対処

理論の式が同じでも，数値計算の実装や探し方が違えば，結果が違うことがある．

---

### 11. LEMと連続体の解析の役割分担

| 問い | LEM | FEMやFDMなどの連続体の解析 |
|---|---|---|
| 全体の安全率 | 得意 | 強度低減法などで求められる |
| 仮定したすべり面での抵抗力と滑動力 | 直接求める | 応力場から後処理で求める |
| 変位の大きさ | 原則として求めない | 求める |
| 応力の再配分 | 内力の仮定で間接的に表す | 構成則を通して求める |
| 進行性破壊 | 原則として直接は表さない | 軟化則や非局所化などが要る |
| 3次元の端部の効果 | 3次元のLEMで求められる | 3次元のモデルで求められる |
| 入力と計算の手間 | 比較的小さい | 一般に大きい |
| 主に読み取るもの | 安全率とすべりの機構 | 応力，変位，塑性域，破壊の過程 |

両者は，どちらが優れているという関係ではない．LEMは，仮定した破壊の機構について，全体の安定性を見通しのよい力学で評価する．一方，連続体の解析は，変形と応力の再配分を扱える．ただし，その結果は，構成則，メッシュ，境界条件，強度低減の手順に左右される．

実務では，両者を補い合う形で使うとよい．まずLEMで複数の手法と複数のすべり面を比べ，必要に応じて，連続体の解析で変形，局所的な応力，施工の過程，進行性破壊を確かめる．

---

## 第5部　系譜とまとめ

### 12. LEMの系譜

2次元の手法から3次元の手法への系譜は，次のようになる．

```text
連続体力学
    ↓ 離散化＋すべり面の仮定
2次元のスライス法
    ├─ Fellenius法 ─────────────→ Hovland型の3次元の方法
    ├─ 簡易Bishop法 ────────────→ Hungr・Ugaiの3次元の簡易Bishop法
    ├─ 簡易Janbu法 ─────────────→ Ugai・Cheng–Yipの3次元の簡易Janbu法
    ├─ Spencer法 ───────────────→ Ugai・Jiang–Yamagamiの3次元のSpencer法
    └─ Morgenstern–Price法・GLE → Lam–Fredlund・Cheng–Yipの3次元のGLE
```

この系譜は，年代順に並べた発明の歴史ではない．**力学的な仮定がどう受け継がれたか**を示す概念図である．

---

### 13. 最後にもう一度まとめる

#### 13.1 LEMの出発点

LEMでは，次の式が分かっても，$N_i$，$F_s$，スライス間力やカラム間力は，まだ分からない．

$$
T_i
=
\frac{c_i'A_i+(N_i-U_i)\tan\phi_i'}{F_s}
$$ (eq-what-summary-shear)

#### 13.2 2次元での要点

- 各スライスには，底面の力と，左右のスライス間力が働く
- 力とモーメントのつり合いだけでは，内力の分布は一意に決まらない
- Fellenius法，簡易Bishop法，簡易Janbu法，Spencer法，Morgenstern–Price法の違いは，不静定性の解消の仕方にある
- 「つり合いの一部だけを満たす方法」（Fellenius法，簡易Bishop法，簡易Janbu法）は，内力の一部またはすべてを無視する
- 「静力学的に完全な方法」は，内力の向きを仮定したうえで，力とモーメントのつり合いをすべて満たす

#### 13.3 3次元で増えるもの

- スライスがカラムになる
- 内部境界が，1方向から2方向に増える
- 底面せん断力が，接平面内のベクトルになる
- 全体すべり方向，回転軸，2方向のカラム間力についての仮定が要る
- 剛体のつり合い式が6つあっても，内力の自由度がさらに増えるので，それだけでは解ける形にならない

#### 13.4 3次元への拡張の考え方

- Hovlandは，Fellenius型の簡略化をカラム法に拡張した
- HungrとUgaiらは，簡易Bishop法などの2次元の仮定を，3次元に移した
- 3次元のSpencer型の手法は，内力の向きが平行という考えを，空間に拡張した
- Lam–Fredlundは，Morgenstern–Price法やGLEの内力の関数を，2方向のカラムの境界に一般化した
- Cheng–Yipは，非対称な3次元の斜面について，簡易Bishop法，簡易Janbu法，Morgenstern–Price法の考えを拡張した

(what-section-13-5)=

#### 13.5 解析結果の読み方

解析結果を見るときは，手法の名前だけでなく，次の点を確かめる．

1. すべり面を，どのように仮定し，どう探したか
2. 強度と安全率を，どう定めたか
3. 内力のどの成分を無視し，どの成分を関数で表したか
4. 力とモーメントの，どのつり合いを満たしたか
5. 3次元では，全体すべり方向と回転軸をどう決めたか
6. 収束した解の垂直力と内力の分布が，物理的に妥当か

つまり，LEMは，単に「抵抗力を滑動力で割る方法」ではない．

$$
\boxed{
\begin{aligned}
&\text{LEMとは，仮定した破壊の機構を離散化し，}\\
&\text{強度の動員の仕方と内力の決め方を定めて，}\\
&\text{極限状態での静力学的なつり合いから，安全率を求める方法である．}
\end{aligned}
}
$$ (eq-what-summary)

---

## 確認問題

答えは問題をクリックすると開く．

:::{dropdown} 問1　つり合い式と底面の強度の式だけでは，なぜ内力の分布が決まらないのか
:icon: question

未知量の数が，独立なつり合い式の数より多いため．$n$ 個のスライスでは，未知量が $4n-2$ 個あるのに対し，つり合い式は各スライス3本の $3n$ 本しかない．（→[3.1節](#what-section-3-1)）
:::

:::{dropdown} 問2　「不静定性を解消する」とは，具体的にどの3種類の操作か
:icon: question

内力の一部を無視する，内力の向きや成分の比を仮定する，つり合い条件の一部だけを使う，の3つ．LEMの各手法は，この組み合わせで分類できる．（→[3.3節](#what-section-3-3)）
:::

:::{dropdown} 問3　Fellenius法・簡易Bishop法・簡易Janbu法は，それぞれ何を無視し，どのつり合いを使うか
:icon: question

- Fellenius法：スライス間力の効果を無視し，円弧の中心まわりの全体のモーメントのつり合いを使う
- 簡易Bishop法：スライス間の垂直力は残し，せん断力を簡略化する（実装では $X_i=0$）．各スライスの鉛直方向の力のつり合いと，全体のモーメントのつり合いを使う
- 簡易Janbu法：スライス間のせん断力を無視するか簡略化し，力のつり合いを使う

（→[6節](#what-section-6)）
:::

:::{dropdown} 問4　Spencer法が「静力学的に完全」と呼ばれるのは，どの意味での完全さか
:icon: question

仮定した内力の向き（すべての境界で同じ角度 $\theta$）のもとで，力とモーメントのつり合いをすべて満たす，という意味である．ただし，Spencer法の解は，連続体としての厳密解ではない．求まる内力の分布が，物理的に唯一の解だとも限らない．（→[5.1節](#what-section-5-1)）
:::

:::{dropdown} 問5　3次元で新しく決めなければならない量は何か．つり合い式が6本になっても足りないのはなぜか
:icon: question

底面のせん断力の接平面内での向き，全体すべり方向，回転軸を，新しく決めなければならない．つり合い式は6本に増えるが，未知量がそれ以上に増えるため．内部境界が2方向になるので，カラム間力の成分と作用位置が増える．底面のせん断力の向きも，未知量に加わる．（→[7節](#what-section-7)）
:::

:::{dropdown} 問6　「3次元の安全率は2次元より大きい」と言い切れないのはなぜか
:icon: question

2次元と3次元で，比べている条件が同じとは限らないため．探したすべり面が同じ破壊の機構か，全体すべり方向は適切か，カラム間力をどこまで考えたか，側面の強度を二重計上していないか，といった点が違えば，単純には比べられない．（→[9節](#what-section-9)）
:::

:::{dropdown} 問7　手法の名前だけでは分からないことは何か
:icon: question

すべり面の仮定と探し方，強度と安全率の定め方，無視した内力の成分や関数で表した成分，満たしたつり合い，3次元での全体すべり方向と回転軸の決め方，収束した解が物理的に妥当かどうか．手法の名前は，10節で見た近似の層のうち，主に内力の決め方の層を表す．その層でも，同じ名前の手法の細部は，実装によって違う．（→[10節](#what-section-10)，[13.5節](#what-section-13-5)）
:::

:::{dropdown} 問8（計算してみよう）　すべり土塊を $n=10$ 個のスライスに分けると，3.1節の表の数え方で，未知量と式はそれぞれいくつになるか．足りない条件はいくつか
:icon: question

未知量は $4n-2=38$ 個である．つり合い式は $3n=30$ 本なので，足りない条件は $n-2=8$ 個になる．スライスを細かく分けるほど，足りない条件も増える．（→[3.1節](#what-section-3-1)）
:::

---

## 次に読む

この資料では，LEMの各手法が静力学的不静定性をどう解消するかを整理した．ただし，実際の解析では，すべり面の形，すべり方向，離散化の仕方，探す範囲なども，結果の意味を左右する．これらを力学的にどう読み解くかは，[第3資料「極限平衡法を実際に使うとき」](lem-in-practice-mechanical-perspective.md)で扱う．

## 参考文献

### 手法ごとの原著論文

本文で扱った原著論文と，代表的な一次文献を，手法ごとにまとめる．DOIは，出版社やCrossrefの書誌情報で照合できたものだけを載せた．DOIを確かめられなかったFellenius (1927, 1936)とJanbu (1954, 1973)には，DOIを付けていない．書誌ページが見つかったものには，そのリンクを付けた．

#### 2次元の手法

##### Fellenius法（簡便分割法）

1. Fellenius, W. (1927). *Erdstatische Berechnungen mit Reibung und Kohäsion (Adhäsion) und unter Annahme kreiszylindrischer Gleitflächen*. Berlin: Ernst & Sohn. [書誌情報](https://books.google.com/books?id=yHhHAAAAIAAJ).
2. Fellenius, W. (1936). “Calculation of the Stability of Earth Dams.” *Proceedings of the Second Congress on Large Dams*, Vol. 4, pp. 445–462. [書誌情報](https://cir.nii.ac.jp/crid/1573950399306830336).

##### 簡易Bishop法

3. Bishop, A. W. (1955). “The use of the slip circle in the stability analysis of slopes.” *Géotechnique*, 5(1), 7–17. [https://doi.org/10.1680/geot.1955.5.1.7](https://doi.org/10.1680/geot.1955.5.1.7)

##### Janbu法

4. Janbu, N. (1954). “Application of composite slip surfaces for stability analysis.” *Proceedings of the European Conference on Stability of Earth Slopes*, Stockholm, Vol. 3, pp. 43–49. [書誌情報](https://cir.nii.ac.jp/crid/1570009750148611712).
5. Janbu, N. (1973). “Slope Stability Computations.” In R. C. Hirschfeld and S. J. Poulos (eds.), *Embankment-Dam Engineering: Casagrande Volume*, pp. 47–86. New York: Wiley.

##### Spencer法

6. Spencer, E. (1967). “A method of analysis of the stability of embankments assuming parallel inter-slice forces.” *Géotechnique*, 17(1), 11–26. [https://doi.org/10.1680/geot.1967.17.1.11](https://doi.org/10.1680/geot.1967.17.1.11)

##### Morgenstern–Price法・GLE

7. Morgenstern, N. R., and Price, V. E. (1965). “The analysis of the stability of general slip surfaces.” *Géotechnique*, 15(1), 79–93. [https://doi.org/10.1680/geot.1965.15.1.79](https://doi.org/10.1680/geot.1965.15.1.79)
8. Morgenstern, N. R., and Price, V. E. (1967). “A numerical method for solving the equations of stability of general slip surfaces.” *The Computer Journal*, 9(4), 388–393. [https://doi.org/10.1093/comjnl/9.4.388](https://doi.org/10.1093/comjnl/9.4.388)

##### 手法の比較

9. Fredlund, D. G., and Krahn, J. (1977). “Comparison of slope stability methods of analysis.” *Canadian Geotechnical Journal*, 14(3), 429–439. [https://doi.org/10.1139/t77-045](https://doi.org/10.1139/t77-045)

#### 3次元の手法

##### Hovland法

10. Hovland, H. J. (1977). “Three-Dimensional Slope Stability Analysis Method.” *Journal of the Geotechnical Engineering Division*, 103(9), 971–986. [https://doi.org/10.1061/AJGEB6.0000493](https://doi.org/10.1061/AJGEB6.0000493)

##### Hungr（3次元の簡易Bishop法）

11. Hungr, O. (1987). “An extension of Bishop's simplified method of slope stability analysis to three dimensions.” *Géotechnique*, 37(1), 113–117. [https://doi.org/10.1680/geot.1987.37.1.113](https://doi.org/10.1680/geot.1987.37.1.113)
12. Hungr, O., Salgado, F. M., and Byrne, P. M. (1989). “Evaluation of a three-dimensional method of slope stability analysis.” *Canadian Geotechnical Journal*, 26(4), 679–686. [https://doi.org/10.1139/t89-079](https://doi.org/10.1139/t89-079)

##### Ugaiら

13. Ugai, K., Hosobori, K., Nagase, H., and Enokido, M. (1986). “Three-dimensional stability analysis of slopes by simple slice method.” *土木学会論文集*, No. 376/III-6, 267–276. [https://doi.org/10.2208/jscej.1986.376_267](https://doi.org/10.2208/jscej.1986.376_267)
14. Ugai, K. (1987). “Three-dimensional slope stability analysis by simplified Janbu method.” *地すべり*, 24(3), 8–14. [https://doi.org/10.3313/jls1964.24.3_8](https://doi.org/10.3313/jls1964.24.3_8)
15. Ugai, K., and Hosobori, K. (1988). “Extension of simplified Bishop method, simplified Janbu method and Spencer's method to three dimensions.” *土木学会論文集*, No. 394/III-9, 21–26. [https://doi.org/10.2208/jscej.1988.394_21](https://doi.org/10.2208/jscej.1988.394_21)

##### 3次元のGLE（Morgenstern–Price型）

16. Lam, L., and Fredlund, D. G. (1993). “A general limit equilibrium model for three-dimensional slope stability analysis.” *Canadian Geotechnical Journal*, 30(6), 905–919. [https://doi.org/10.1139/t93-089](https://doi.org/10.1139/t93-089)

##### 3次元に拡張したSpencer法

17. Jiang, J.-C., and Yamagami, T. (2004). “Three-Dimensional Slope Stability Analysis Using an Extended Spencer Method.” *Soils and Foundations*, 44(4), 127–135. [https://doi.org/10.3208/sandf.44.4_127](https://doi.org/10.3208/sandf.44.4_127)

##### 非対称な斜面への3次元の拡張

18. Cheng, Y. M., and Yip, C. J. (2007). “Three-Dimensional Asymmetrical Slope Stability Analysis—Extension of Bishop's, Janbu's, and Morgenstern–Price's Techniques.” *Journal of Geotechnical and Geoenvironmental Engineering*, 133(12), 1544–1555. [https://doi.org/10.1061/(ASCE)1090-0241(2007)133:12(1544)](https://doi.org/10.1061/%28ASCE%291090-0241%282007%29133%3A12%281544%29)
