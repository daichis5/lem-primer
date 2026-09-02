---
title: "極限平衡法とは何か：厳密な静力学問題から各手法の仮定を理解する"
lang: ja
series: "2 of 3"
---

# 極限平衡法とは何か

## 厳密な静力学問題から各手法の仮定を理解する

> **LEM理解シリーズ 2/3**  
> この資料は，第1資料で得た底面力の関係から出発し，残された未知量を各極限平衡法（limit equilibrium method; LEM）がどの仮定によって決定するのかを理解するための資料である．

## この資料で理解すること

本資料の目的は，手法ごとの式を暗記することではない．厳密な2次元・3次元の静力学問題と対比しながら，各手法が何を満たし，何を簡略化し，どの追加仮定によって問題を解ける形にしているのかを整理することである．

## シリーズ内での位置付け

| 資料 | 中心となる問い |
|---|---|
| 1. [連続体力学から極限平衡法のスタート地点まで](./continuum-mechanics-to-lem-start.md) | 応力と破壊規準は，底面の力へどう変換されるか |
| **2. 極限平衡法とは何か（本資料）** | 残った未知量を，各手法はどの仮定で決めるか |
| 3. [極限平衡法を実際に使うとき](./lem-in-practice-mechanical-perspective.md) | 任意形状，すべり方向，離散化をどう解釈するか |

用語と記号の定義は[用語集](./lem-glossary.md)にまとめている．

```{admonition} この資料の中心命題
極限平衡法（limit equilibrium method; LEM）の各手法の違いは，単なる計算式の違いではない．連続体をスライスまたはカラムに分割したときに残る**静力学的不静定性（static indeterminacy）を，どの内力仮定とつり合い条件によって解消するか**の違いである．
```

第1資料で得た底面せん断力と底面法線力の関係を出発点として，2次元および3次元の極限平衡法が何を考慮し，何を仮定し，何を解かないのかを整理する．

---

## 0. 本資料の範囲と用語

本資料でいう「厳密」は，二つの異なる意味に分ける必要がある．

1. **連続体力学としての厳密さ**  
   応力場，変位場，構成則，適合条件，境界条件を満足する境界値問題として解くこと．

2. **LEM内部での静力学的な厳密さ**  
   仮定したすべり面，強度動員則，スライス／カラム間力のモデルの下で，必要な力とモーメントのつり合いをすべて満足すること．

Spencer法やMorgenstern–Price法が「厳密法（rigorous method）」と呼ばれることがあるのは，主として2番目の意味である．これらも，変位の適合条件や土の応力―ひずみ関係まで解く連続体解析ではない．

以下では，断らない限り有効応力表示のMohr–Coulomb強度を考える．記号は次のとおりとする．

| 記号 | 意味 |
|---|---|
| $F_s$ | 安全率（factor of safety） |
| $c_i',\phi_i'$ | 第$i$要素底面の有効粘着力・有効内部摩擦角 |
| $A_i$ | 第$i$要素の底面積．2Dでは単位奥行きを仮定した底面積 |
| $N_i$ | 底面に作用する全法線力 |
| $U_i$ | 底面間隙水圧の合力 |
| $T_i$ | 底面に沿って動員されるせん断力の大きさ |
| $W_i$ | 自重．必要に応じて外力や地震慣性力を別に加える |
| $E,X$ | 2Dスライス間の法線力・せん断力 |
| $\boldsymbol{n}_i$ | 第$i$要素底面の，すべり土塊から外向きの単位法線 |
| $\boldsymbol{m}_i$ | 第$i$要素底面で仮定した局所的なすべり方向の単位ベクトル |

---

## Part I　2次元LEMの出発点

**この Part で分かること**

- 第1資料で得た底面せん断力の式から，何が既知で何が未知かを整理する．
- 1つのスライスに実際に働く力を，底面力・スライス間力・自重に分けて数え上げる．
- つり合い式だけでは内力分布が決まらないこと，すなわち静力学的不静定性を確認する．

### 1. すでに分かっていることと，まだ分からないこと

前資料の到達点を，次式で表す．

$$
T_i
=
\frac{
c_i' A_i + (N_i-U_i)\tan\phi_i'
}{F_s}.
\tag{1}
$$

これは，せん断強度を

$$
c_{m,i}'=\frac{c_i'}{F_s},
\qquad
\tan\phi_{m,i}'=\frac{\tan\phi_i'}{F_s}
\tag{2}
$$

まで低減した状態で，すべり面全体が極限状態にあると仮定した式である．

式(1)から，$T_i$は独立な未知量ではなく，$N_i$と$F_s$が決まれば求まる．しかし，これだけでは問題は解けない．

#### 既知量

- 斜面形状，地層境界，仮定したすべり面
- 各スライスの重量$W_i$
- $c_i',\phi_i'$および底面積$A_i$
- 間隙水圧分布から得る$U_i$
- 与えた外力，地震慣性力，アンカー力など

#### 残る未知量

- 各スライス底面の法線力$N_i$
- 共通の安全率$F_s$
- スライス間内力の大きさと方向
- モーメントつり合いを各スライスで課すなら，スライス間合力の作用位置

したがって，LEMの本当の出発点は式(1)そのものではなく，次の問いである．

> **未知の内部力を含む静力学問題を，どの追加仮定によって一意に解ける形にするか．**

---

### 2. 2次元で本来考えなければならない力

```{figure} ./figures/fig_01_2d_slice_forces.svg
:name: fig-01-2d-slice-forces
:alt: 2次元スライスに作用する底面力，スライス間力，自重の自由物体図

2次元スライスの自由物体図．底面の$N_i,T_i$，左右境界の$E,X$，自重$W_i$，底面角度$\alpha_i$，内力の作用位置を示す．
```

第$i$スライスを土塊から切り出すと，少なくとも次の力を考える必要がある．

- 自重$W_i$
- 底面法線力$N_i$
- 底面せん断力$T_i$
- 左境界のスライス間法線力$E_{i-1}$とせん断力$X_{i-1}$
- 右境界のスライス間法線力$E_i$とせん断力$X_i$
- 必要に応じて水圧，外荷重，地震慣性力，補強力

剛体として取り出した各スライスには，平面内で三つの独立なつり合い式がある．

$$
\sum F_x=0,
\qquad
\sum F_z=0,
\qquad
\sum M_y=0.
\tag{3}
$$

しかし，連続体力学の観点では，内部境界に実際に作用するのは単一の矢印ではなく，位置とともに変化する表面力（traction）分布

$$
\boldsymbol{t}(\boldsymbol{x})
=
\boldsymbol{\sigma}(\boldsymbol{x})\boldsymbol{n}
\tag{4}
$$

である．LEMは，この分布を$E$と$X$という合力，および必要ならその作用位置にまとめる．この時点ですでに，連続な応力場から有限個の合力への**離散化（discretization）**が行われている．

---

### 3. なぜつり合い式だけでは解けないのか

```{figure} ./figures/fig_02_indeterminacy.svg
:name: fig-02-indeterminacy
:alt: スライス法における未知数とつり合い式の不足を示す概念図

連続体からスライス系へ移ったときに生じる未知量と，不静定性を解消するために必要な追加仮定．
```

#### 3.1 未知数を数える

$n$個のスライスについて，式(1)を用いて底面せん断力$T_i$を$N_i$と$F_s$で表した後も，代表的な定式化では次が残る．

| 未知量 | 個数 |
|---|---:|
| 底面法線力$N_i$ | $n$ |
| スライス間法線力$E_i$ | $n-1$ |
| スライス間せん断力$X_i$ | $n-1$ |
| スライス間合力の作用位置$h_i$ | $n-1$ |
| 安全率$F_s$ | $1$ |
| **合計** | **$4n-2$** |

一方，各スライスに式(3)を課して得る式は$3n$本である．未知量の数え方は，合力と作用位置の表現方法や，全体つり合いを独立に数えるかによって変わる．しかし，どの表現でも本質は同じである．

$$
\boxed{
\text{つり合い条件と底面強度式だけでは，内部力分布は一意に決まらない}
}
\tag{5}
$$

これが静力学的不静定性である．

```{note}
なお，この表では底面法線力$N_i$の作用位置を未知に数えていない．これは，$N_i$が底面の中央に作用するという慣用的な仮定を先に置いたことに相当する．作用位置を未知に含める教科書的な数え方では，Mohr–Coulomb式を含めて未知量$6n-2$・式$4n$本となるが，いずれの数え方でも不足する仮定の数は$n-2$個で一致する．
```

#### 3.2 連続体解析なら何が追加されるか

連続体の境界値問題では，つり合いだけでなく，少なくとも次が結び付けられる．

- ひずみ―変位関係
- 構成則，すなわち応力―ひずみ関係
- 変位の適合条件
- 応力境界条件と変位境界条件
- 弾塑性履歴や局所的な降伏条件

LEMは通常，これらを解かない．その代わり，スライス間力の方向，比率，作用位置，あるいは無視できる成分を仮定する．

#### 3.3 不静定性を「解消する」とは何をすることか

不静定問題を解けるようにする操作を，ここでは**不静定性の解消（closure）**と呼ぶ．典型的な解消の仕方は次の三種類である．

1. 内力の一部を無視する．
2. 内力の方向または成分比を仮定する．
3. 一部のつり合い条件だけを使い，残りを要求しない．

各LEMは，この組合せによって分類できる．2D各手法の統一的な比較については，[Fredlund and Krahn (1977)](https://doi.org/10.1139/t77-045)も参照されたい．

---

## Part II　2次元LEMは何を簡略化しているのか

**この Part で分かること**

- Fellenius法，Bishop簡便法，Janbu簡便法が，どの内力を無視しどのつり合いを使うかを比較する．
- Spencer法とMorgenstern–Price法が，内力の方向を仮定して力とモーメントを同時に満たす仕組みを見る．
- 「簡便法」と「静力学的に完全な方法」の差が，精度そのものではなく仮定の置き方の差であることを確認する．

### 4. 2D手法を比較するための共通視点

```{figure} ./figures/fig_03_2d_methods.svg
:name: fig-03-2d-methods
:alt: Fellenius法，Bishop簡便法，Janbu簡便法の内力仮定の比較

Fellenius法，Bishop簡便法，Janbu簡便法の比較．基準となる自由物体図から，無視する内力成分と採用するつり合い条件を対比する．
```

以下では各手法を，次の四つの観点から整理する．

1. スライス間力をどう扱うか．
2. どのつり合い条件を満足するか．
3. すべり面形状にどの制約があるか．
4. その結果，何が計算しやすくなり，何が保証されなくなるか．

#### 4.1 Fellenius法／通常分割法

Fellenius法（Ordinary Method of Slices; Swedish Circle Method）は，隣接スライスから受ける法線力とせん断力の効果を底面法線力の評価で無視し，円弧すべりに対する全体モーメントつり合いから安全率を求める．

単位奥行き，円弧すべり，水平スライス幅$b_i$，底面長$l_i$，底面傾斜角$\alpha_i$を用いる代表式は，概念的に

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
}.
\tag{6}
$$

と書ける．

```{note}
記号規約によって水圧項の表現は変わる．
```

##### 不静定性の解消方法

- スライス間力の効果を無視する．
- 円弧中心まわりの全体モーメントつり合いを用いる．
- 各スライスの水平・鉛直力つり合いを同時には満足しない．

##### 力学的な意味

スライス間力の合力効果を安全率計算に含めない近似であり，局所的な底面法線力や内部力を評価する用途には向かない．

```{note}
これは「スライス間力が物理的に存在しない」という主張ではない．存在はするが，その効果を安全率の計算に含めていない．
```

**原典**：Felleniusの方法は1920年代の著作に遡る．書誌が確認できる資料として，W. Fellenius, *Erdstatische Berechnungen mit Reibung und Kohäsion (Adhäsion) und unter Annahme kreiszylindrischer Gleitflächen*, Ernst & Sohn, Berlin, 1927（[書誌情報](https://books.google.com/books?id=yHhHAAAAIAAJ)），および “Calculation of the Stability of Earth Dams,” *Proceedings of the Second Congress on Large Dams*, Vol. 4, pp. 445–462, 1936（[書誌情報](https://cir.nii.ac.jp/crid/1573950399306830336)）がある．いずれも確認できる現代的DOIはない．

---

#### 4.2 Bishop簡便法

Bishop簡便法（Simplified Bishop Method）は，スライス間法線力$E_i$の存在を許しながら，スライス間せん断力の合力を簡略化する．典型的には$X_i-X_{i-1}=0$，実装上は各境界の$X_i=0$として扱い，各スライスの鉛直力つり合いと，円弧中心まわりの全体モーメントつり合いを組み合わせる．

代表的な形は

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
}.
\tag{7}
$$

右辺にも$F_s$が現れるため，反復計算が必要である．

##### 不静定性の解消方法

- スライス間法線力は残す．
- スライス間せん断力を簡略化する．
- 各スライスの鉛直力つり合いを使って$N_i$を求める．
- 全体モーメントつり合いから$F_s$を求める．
- 一般には全体水平力つり合いを厳密には満足しない．

##### 力学的な意味

Fellenius法よりも底面法線力の評価が改善される一方，内力方向を完全には解いていない．古典的定式化は円弧すべりを対象とする．円弧では共通中心まわりのモーメント式が特に簡潔になるためである．

**原著論文**：[A. W. Bishop (1955), “The use of the slip circle in the stability analysis of slopes,” *Géotechnique*, 5(1), 7–17. DOI: 10.1680/geot.1955.5.1.7](https://doi.org/10.1680/geot.1955.5.1.7)

---

#### 4.3 Janbu簡便法

Janbu法の系統は，任意形状のすべり面を扱いやすくし，主として力のつり合いから安全率を求める方向に発展した．Janbu簡便法（Simplified Janbu Method）では，スライス間せん断力を簡略化し，全体の水平力つり合いを中心に安全率を求める．

##### 不静定性の解消方法

- 典型的にはスライス間せん断力を無視または簡略化する．
- 力のつり合いを用いる．
- 全体モーメントつり合いを完全には満足しない．
- モーメント不釣合いの影響を補うため，経験的な補正係数$f_0$を用いる簡便形がある．

##### Bishop簡便法との対比

$$
\begin{array}{c|c}
\text{Bishop簡便法} & \text{Janbu簡便法} \\
\hline
\text{円弧すべりと相性がよい} & \text{任意形状のすべり面を扱いやすい} \\
\text{全体モーメントつり合いを重視} & \text{全体力つり合いを重視} \\
\text{水平力つり合いが残る} & \text{モーメントつり合いが残る}
\end{array}
\tag{8}
$$

```{note}
補正係数は，欠けているモーメントつり合いを厳密に回復するものではない．特定の仮定と経験的整理の下で，安全率の偏りを減らすための補正である．
```

**初期文献**：N. Janbu (1954), “Application of composite slip surfaces for stability analysis,” *Proceedings of the European Conference on Stability of Earth Slopes*, Stockholm, Vol. 3, pp. 43–49（[書誌情報](https://cir.nii.ac.jp/crid/1570009750148611712)）．確認できるDOIはない．一般化された整理として，N. Janbu (1973), “Slope Stability Computations,” in *Embankment-Dam Engineering: Casagrande Volume*, pp. 47–86も広く参照される．

---

### 5. 内力方向を仮定し，力とモーメントを同時に満足させる方法

```{figure} ./figures/fig_04_spencer_mp.svg
:name: fig-04-spencer-mp
:alt: Spencer法とMorgenstern–Price法におけるスライス間力方向の仮定

Spencer法の一定内力傾斜と，Morgenstern–Price法の関数で変化する内力傾斜．$E$と$X$の比をどう仮定するかを対比する．
```

#### 5.1 Spencer法

Spencer法は，各スライス境界に作用する合力の方向が互いに平行，すなわち一定角$\theta$をもつと仮定する．

$$
\frac{X_i}{E_i}=\tan\theta
=\text{一定}.
\tag{9}
$$

$F_s$と$\theta$を未知量として，全体の力つり合いとモーメントつり合いの双方を満足させる．

##### 不静定性の解消方法

- スライス間力を無視しない．
- スライス間合力の**方向が全境界で同一**と仮定する．
- 力とモーメントのつり合いを同時に満足するように$F_s$と$\theta$を求める．

##### 「厳密」の意味

Spencer法は，採用した内力方向仮定の範囲内で静力学的つり合いを満足する．ただし，一定角$\theta$が連続体の実際の内部応力場から導かれたわけではない．したがって，**静力学的に完全であること**と，**内力分布が唯一の物理解であること**は同じではない．

**原著論文**：[E. Spencer (1967), “A method of analysis of the stability of embankments assuming parallel inter-slice forces,” *Géotechnique*, 17(1), 11–26. DOI: 10.1680/geot.1967.17.1.11](https://doi.org/10.1680/geot.1967.17.1.11)

---

#### 5.2 Morgenstern–Price法

Morgenstern–Price法は，スライス間せん断力と法線力の比を，位置$x$の既知形状関数$f(x)$と未知倍率$\lambda$で表す．

$$
X(x)=\lambda f(x)E(x),
\qquad
\frac{X(x)}{E(x)}=\lambda f(x).
\tag{10}
$$

ここで，$f(x)$は正弦半波（half-sine），台形（trapezoidal），一定（constant）などから選ばれ，$\lambda$が解析中に決定される．$F_s$と$\lambda$を調整し，力とモーメントのつり合い，および端部条件を満足させる．

##### 不静定性の解消方法

- スライス間力を無視しない．
- 内力方向の**空間変化の形**を$f(x)$として仮定する．
- その大きさを支配する$\lambda$と安全率$F_s$を解く．
- 力とモーメントのつり合いを同時に満足する．

##### Spencer法との関係

$f(x)=1$とすれば，$X/E=\lambda$は一定となる．この意味で，Spencer法はMorgenstern–Price型の内力関数を一定とした特殊形として理解できる．

##### 何が残るか

異なる妥当な$f(x)$が近い安全率になる場合でも，局所的なスライス間力や底面法線力の分布は異なり得る．安全率の一致は，内部応力場の一意性を保証しない．

**原著論文**：[N. R. Morgenstern and V. E. Price (1965), “The analysis of the stability of general slip surfaces,” *Géotechnique*, 15(1), 79–93. DOI: 10.1680/geot.1965.15.1.79](https://doi.org/10.1680/geot.1965.15.1.79)

**数値解法**：[N. R. Morgenstern and V. E. Price (1967), “A numerical method for solving the equations of stability of general slip surfaces,” *The Computer Journal*, 9(4), 388–393. DOI: 10.1093/comjnl/9.4.388](https://doi.org/10.1093/comjnl/9.4.388)

---

### 6. 2D LEMを一覧表で比較する

| 手法 | 主なすべり面 | スライス間力の扱い | 主に満足するつり合い | 主な未充足・仮定 | 位置付け |
|---|---|---|---|---|---|
| Fellenius | 円弧 | 効果を無視 | 全体モーメント | 力つり合い，内力 | 最も単純 |
| Bishop簡便 | 主に円弧 | 法線力は考慮，せん断力を簡略化 | 各スライス鉛直力＋全体モーメント | 全体水平力 | モーメント系簡便法 |
| Janbu簡便 | 任意形状 | せん断力を簡略化 | 全体力 | 全体モーメント | 力系簡便法 |
| Spencer | 円弧から一般面へ拡張可能 | 合力方向を一定と仮定 | 力＋モーメント | 内力方向一定 | 静力学的に完全なLEM |
| Morgenstern–Price | 任意形状 | $X/E=\lambda f(x)$ | 力＋モーメント | 内力関数$f(x)$ | 一般化されたLEM |

```{note}
「満足するつり合い」は，標準的な定式化についての要約である．ソフトウェア実装では，拡張式，地震荷重，補強材，非円弧面への適用方法などによって名称が同じでも細部が異なる．使用時には実装マニュアルの式と収束判定を確認する必要がある．
```

---

## Part III　3次元では何が増えるのか

**この Part で分かること**

- スライスがカラムになると，底面せん断力が向きの自由度をもつベクトルになることを見る．
- 内部境界が2方向に増え，つり合い式が6本になっても問題が閉じない理由を確認する．
- Hovland，Hungr／Ugai，3D Spencer，Lam–Fredlund，Cheng–Yip が，2Dのどの仮定を引き継いだかを整理する．

### 7. スライスからカラムへ

```{figure} ./figures/fig_05_3d_column_forces.svg
:name: fig-05-3d-column-forces
:alt: 三次元カラムの底面法線力，底面せん断力，四側面のカラム間力

一般的な3Dカラムに作用する力．曲面底面の法線力，接平面内の二成分をもつ底面せん断力，二方向の内部境界に作用するカラム間力を示す．
```

2Dでは，すべり土塊を一方向にだけ分割し，各要素は「スライス」となる．3Dでは，平面上の二方向に分割するため，各要素は「カラム」となる．

#### 7.1 底面力がベクトルになる

第$i$カラムの底面に，すべり土塊から外向きの単位法線$\boldsymbol{n}_i$をとる．また，局所的な想定すべり方向の単位ベクトルを$\boldsymbol{m}_i$とし，底面の抵抗せん断力ベクトルを

$$
\boldsymbol{T}_i=-T_i\boldsymbol{m}_i
$$

と定義する．このとき，すべり土塊が底面から受ける合力は

$$
\boldsymbol{R}_{b,i}
=
-N_i\boldsymbol{n}_i+\boldsymbol{T}_i,
\qquad
\boldsymbol{T}_i\cdot\boldsymbol{n}_i=0
\tag{11}
$$

と分解できる．$\boldsymbol{T}_i$は底面接平面内のベクトルであり，一般に二つの独立成分をもつ．

Mohr–Coulomb式が直接与えるのは，その限界**大きさ**である．

$$
\|\boldsymbol{T}_i\|
=
\frac{
c_i'A_i+(N_i-U_i)\tan\phi_i'
}{F_s}.
\tag{12}
$$

しかし，式(12)だけでは接平面内の**方向**は決まらない．よって3D LEMでは，少なくとも次のいずれかが必要になる．

- 全カラムで共通または規則的なすべり方向を仮定する．
- 局所的な最大傾斜方向を使う．
- 全体つり合いと整合する方向を未知量として解く．
- 速度場または運動学的機構から方向を与える．

2Dではせん断方向が断面内で事実上固定されるため，この問題は目立たない．3Dでは安全率だけでなく，**どちら向きに滑ると仮定したか**が定式化の一部になる．

#### 7.2 内部境界が二組になる

直交する$x$方向と$y$方向にカラムを並べると，内部境界は二つの族をもつ．各鉛直側面には，一般には

- 面に垂直な法線合力
- 面内の鉛直せん断成分
- 面内の水平せん断成分
- 各合力の作用位置

が存在する．

つまり，2Dの$E$と$X$をそのまま本数だけ増やせばよいのではない．内力合力の方向自由度とモーメントへの寄与が増える．

#### 7.3 つり合い式も六つになるが，未知量はさらに増える

3D剛体には

$$
\sum F_x=0,
\quad
\sum F_y=0,
\quad
\sum F_z=0,
\tag{13}
$$

$$
\sum M_x=0,
\quad
\sum M_y=0,
\quad
\sum M_z=0
\tag{14}
$$

の六つのつり合い条件がある．しかし，カラムごとに底面せん断方向と二組のカラム間力が増えるため，つり合い式が三つから六つに増えただけでは問題は解ける形にならない．

$$
\boxed{
\text{2Dから3Dへの拡張}
\neq
\text{同じ式に奥行き幅を掛けること}
}
\tag{15}
$$

本質的には，内部境界の増加，底面せん断方向の自由度，回転軸または全体すべり方向の選択を同時に扱う必要がある．

---

### 8. 3D LEMはどのような考え方で拡張されたか

```{figure} ./figures/fig_06_3d_extensions.svg
:name: fig-06-3d-extensions
:alt: 2DのFellenius，Bishop，Spencer，Morgenstern–Priceから3Dカラム法への拡張

2D LEMから3D LEMへの代表的な拡張．スライスをカラムへ置き換え，元の手法の内力仮定とつり合い条件を3Dへ移し，一般化する流れを示す．
```

3D LEMの多くは，ゼロから独立に作られたのではない．代表的な考え方は次のとおりである．

1. スライスをカラムへ置き換える．
2. 2Dで採用した内力仮定を，二方向のカラム境界へ拡張する．
3. 円弧中心まわりのモーメントを，3Dの回転軸まわりのモーメントへ置き換える．
4. 2Dで暗黙だったすべり方向を，対称面，主すべり方向，または未知パラメータとして導入する．

以下では，代表的な発展をこの観点から読む．

---

#### 8.1 Hovland法：Fellenius型の直接拡張

Hovland法は，すべり土塊を鉛直カラムに分割し，3Dの底面形状と側方端部の効果を扱えるようにした初期の一般的3D LEMである．力学的な骨格は，カラム間力を無視するFellenius型の拡張として理解できる．

##### 拡張の考え方

- 2Dスライスを3Dカラムへ置き換える．
- 各カラム底面の局所傾斜と面積を使う．
- カラム間力を無視し，重量から底面法線力を評価する．
- 仮定した全体すべり方向に対する抵抗と駆動を集計する．

##### 得られるものと失うもの

有限幅のすべり土塊，非一様な3D形状，端部を含む幾何学効果を表現できる一方，内部力を無視するため，3方向の力つり合いとモーメントつり合いを一般に完全には満足しない．したがって，3D化したこと自体が静力学的厳密性の向上を意味するわけではない．

**原著論文**：[H. J. Hovland (1977), “Three-Dimensional Slope Stability Analysis Method,” *Journal of the Geotechnical Engineering Division*, 103(9), 971–986. DOI: 10.1061/AJGEB6.0000493](https://doi.org/10.1061/AJGEB6.0000493)

---

#### 8.2 Hungr／Ugai：Bishop簡便法などをカラム法へ拡張する

HungrはBishop簡便法を3Dへ直接拡張した．Ugaiらも，簡易分割法，Bishop簡便法，Janbu簡便法，Spencer法を3Dへ拡張する一連の研究を行った．

##### 3D Bishop簡便法の考え方

- 2Dと同様に，鉛直方向のカラム間せん断力を無視する．
- 各カラムの鉛直力つり合いから底面法線力を評価する．
- 仮定した回転軸まわりの全体モーメントつり合いから$F_s$を求める．
- 水平二方向の力つり合いは一般に満足させない．

この拡張は，Bishop簡便法の計算上の長所を維持しながら，有限幅，端部，平面形状の効果を取り込む．しかし，非回転的な機構，強い非対称性，複雑な底面せん断方向をもつ問題では，元の仮定が適切かを別途検討する必要がある．

##### Ugaiらの位置付け

Ugaiらは，まず3D簡便分割法を提示し，その後，Bishop簡便法，Janbu簡便法，Spencer法を3Dへ拡張した．これは，3D LEMの発展が「単一の3D公式」ではなく，**2Dでの不静定性の解消方法をカラム系へ移した複数の系譜**であることを示している．

**主要一次論文**：

- [O. Hungr (1987), “An extension of Bishop's simplified method of slope stability analysis to three dimensions,” *Géotechnique*, 37(1), 113–117. DOI: 10.1680/geot.1987.37.1.113](https://doi.org/10.1680/geot.1987.37.1.113)
- [O. Hungr, F. M. Salgado and P. M. Byrne (1989), “Evaluation of a three-dimensional method of slope stability analysis,” *Canadian Geotechnical Journal*, 26(4), 679–686. DOI: 10.1139/t89-079](https://doi.org/10.1139/t89-079)
- [K. Ugai, K. Hosobori, H. Nagase and M. Enokido (1986), “Three-dimensional stability analysis of slopes by simple slice method,” *土木学会論文集*, No. 376/III-6, 267–276. DOI: 10.2208/jscej.1986.376_267](https://doi.org/10.2208/jscej.1986.376_267)
- [K. Ugai and K. Hosobori (1988), “Extension of simplified Bishop method, simplified Janbu method and Spencer's method to three dimensions,” *土木学会論文集*, No. 394/III-9, 21–26. DOI: 10.2208/jscej.1988.394_21](https://doi.org/10.2208/jscej.1988.394_21)

---

#### 8.3 3D Spencer法：一定方向仮定を平面・空間へ拡張する

2D Spencer法では，スライス間合力が共通の傾斜角をもつ．3Dへの拡張では，この「平行な内力」という考えを，二方向のカラム境界上の合力方向，または共通の方向面として表現する．

##### 拡張で新たに必要なもの

- 主すべり方向または回転軸
- 二組のカラム間力の方向関係
- 底面接平面内のせん断方向
- 3方向の力つり合いと，採用するモーメントつり合い条件

3D Spencer型手法は，採用したカラム間力方向仮定の下で，簡便3D法より多くのつり合い条件を満足させることを目指す．ただし「全内力が平行」という2Dの単一角度は，3Dでは一意の拡張をもたない．論文やソフトウェアによって，どの成分を平行とするか，どのモーメント軸を課すかが異なる．

Jiang and Yamagamiは，2D Spencer安全率式をカラム法へ拡張し，動的計画法による3D臨界すべり面探索と組み合わせた．

**代表的一次論文**：[J.-C. Jiang and T. Yamagami (2004), “Three-Dimensional Slope Stability Analysis Using an Extended Spencer Method,” *Soils and Foundations*, 44(4), 127–135. DOI: 10.3208/sandf.44.4_127](https://doi.org/10.3208/sandf.44.4_127)

---

#### 8.4 Lam–Fredlund 3D GLE：Morgenstern–Price型の一般化

Lam and Fredlundは，2Dの一般極限平衡法（general limit equilibrium; GLE）をカラム法へ拡張した．3Dでは内部境界が二方向に存在するため，それぞれのカラム間合力方向を表す関数が必要になる．

概念的には，二方向の内部境界について

$$
x\text{方向境界群のせん断力／法線力比}
=\lambda_x f_x(x,y),
\tag{16}
$$

$$
y\text{方向境界群のせん断力／法線力比}
=\lambda_y f_y(x,y)
\tag{17}
$$

のような関係を仮定する．実際の成分記号と関数の置き方は定式化によって異なるが，中心となる考えは同じである．

##### 拡張の考え方

- 2Dの$X/E=\lambda f(x)$を，二方向のカラム間力関数へ一般化する．
- カラム間合力の方向変化を，任意形状の関数で表す．
- 力とモーメントのつり合いを同時に満たす安全率と倍率を探索する．
- 斜面，地層，すべり面，間隙水圧を3D空間内でモデル化する．

これは3D LEMの一般性を高める一方，仮定すべき内力関数，未知倍率，収束計算が増える．自由度が増えた分だけ，入力仮定が結果へ与える影響の確認が重要になる．

**原著論文**：[L. Lam and D. G. Fredlund (1993), “A general limit equilibrium model for three-dimensional slope stability analysis,” *Canadian Geotechnical Journal*, 30(6), 905–919. DOI: 10.1139/t93-089](https://doi.org/10.1139/t93-089)

---

#### 8.5 Cheng–Yip：非対称3D斜面への一般化

初期の3D LEMの多くは，対称面または既知の主すべり方向を暗黙に仮定していた．Cheng and Yipは，Bishop簡便法，Janbu簡便法，Morgenstern–Price法の考えを，非対称な3D斜面へ拡張した．

##### 重要な考え方

- 平面形状とすべり面が対称であることを前提にしない．
- 二つの水平軸方向に対する底面力とカラム間力を明示する．
- 2D各手法の「何を無視し，何をつり合わせるか」を3Dで対応付ける．
- Morgenstern–Price型では，二方向の内力関数と係数を導入する．

この研究は，3D拡張の本質が幾何学の立体化だけでなく，**2Dでは一方向だった内力仮定と全体すべり方向を空間内で再定義すること**にあると明確に示す．

**原著論文**：[Y. M. Cheng and C. J. Yip (2007), “Three-Dimensional Asymmetrical Slope Stability Analysis—Extension of Bishop's, Janbu's, and Morgenstern–Price's Techniques,” *Journal of Geotechnical and Geoenvironmental Engineering*, 133(12), 1544–1555. DOI: 10.1061/(ASCE)1090-0241(2007)133:12(1544)](https://doi.org/10.1061/%28ASCE%291090-0241%282007%29133%3A12%281544%29)

---

### 9. 3D LEMを一覧表で比較する

| 手法・系統 | 2Dで対応する考え方 | カラム間力 | 主なつり合い | 特徴・制約 | 一次文献 |
|---|---|---|---|---|---|
| Hovland | Fellenius型 | 無視 | 主として全体抵抗・駆動の集計 | 単純だが静力学的に完全ではない | Hovland (1977) |
| Hungr 3D Bishop | Bishop簡便 | 鉛直せん断成分を簡略化 | カラム鉛直力＋全体モーメント | 回転的・比較的対称な問題と相性 | Hungr (1987) |
| Ugai系 | Bishop／Janbu／Spencer | 元の2D法に対応して仮定 | 手法ごとに異なる | 2D各系統を明示的に3D化 | Ugai et al. (1986); Ugai & Hosobori (1988) |
| Extended 3D Spencer | Spencer | 空間内で平行性を仮定 | 力＋採用したモーメント条件 | 3Dでの「平行」の定義が実装依存 | Jiang & Yamagami (2004) |
| Lam–Fredlund 3D GLE | Morgenstern–Price／GLE | 二方向の関数で表現 | 力＋モーメント | 一般性が高いが仮定・未知量も多い | Lam & Fredlund (1993) |
| Cheng–Yip | Bishop／Janbu／MP | 二方向で各2D仮定を拡張 | 手法ごとに異なる | 非対称3D形状を明示的に扱う | Cheng & Yip (2007) |

#### 3D安全率を解釈するときの注意

3D解析では側方端部の抵抗が加わるため，同じ中央断面の2D解析より安全率が高くなる例が多い．しかし，次の条件が異なれば単純比較できない．

- 2Dと3Dで探索されたすべり面が同じ破壊機構を表しているか．
- 3Dで仮定した全体すべり方向が適切か．
- カラム間力をどこまで考慮したか．
- 側面に働く強度を二重計上していないか．
- 2Dの単位奥行きと3Dの有限幅をどう対応させたか．
- 地層，間隙水圧，外力の3D分布が一致しているか．

```{warning}
したがって，「3D安全率は必ず2Dより大きい」という規則として用いてはならない．差の理由を，幾何学，強度，内力仮定，探索された破壊機構に分けて説明する必要がある．
```

---

## Part IV　LEMに含まれる近似の階層

**この Part で分かること**

- LEMの近似が，幾何学的離散化から数値解法まで6つの層に分かれることを見る．
- 手法名が主に表しているのは，そのうち「内部力の決め方」の層だけであることを確認する．
- LEMと連続体解析（FEM/FDMなど）が何を得意とし，どう補い合うかを整理する．

### 10. 近似は内力仮定だけではない

LEMの近似を，下から上へ積み重なる層として整理すると理解しやすい．

#### 第1層：幾何学的離散化

連続な土塊を，有限個のスライスまたはカラムに置き換える．

- 曲面を平面片または単純な底面で近似する．
- 分布荷重と分布応力を合力へ置き換える．
- 分割数と分割方向による離散化誤差が生じる．

#### 第2層：破壊機構の仮定

すべり面または探索可能なすべり面族をあらかじめ定める．

- 円弧，複合面，非円弧面，楕円体，NURBS面など．
- 実際の進行性破壊や複数面の連結が探索空間に含まれない可能性がある．
- 得られる最小安全率は，探索した面族の中での最小値である．

#### 第3層：強度動員の仮定

すべり面全体で一つの安全率$F_s$を共有し，強度が同時に同じ比率で動員されるとする．

$$
\tau_{m,i}
=
\frac{
c_i'+(\sigma_{n,i}-u_i)\tan\phi_i'
}{F_s}.
\tag{18}
$$

これは，局所ひずみの違い，ピークから残留強度への軟化，進行性破壊を直接は表さない．

#### 第4層：内部力の決め方

- 内力成分を無視する．
- 内力方向を一定とする．
- 内力比の空間関数を仮定する．
- 内力作用位置を仮定または計算する．

各LEMの名称が主に表しているのはこの層である．

#### 第5層：3Dの全体すべり方向と回転軸

3Dではさらに，底面せん断ベクトルの方向，全体すべり方向，モーメント軸を決める必要がある．対称問題では幾何学から候補が決まるが，非対称問題では未知量または探索変数になる．

#### 第6層：数値解法と探索

- $F_s$，内力倍率，内力角度の反復解法
- 臨界すべり面探索
- 収束判定と局所解
- 不適切な底面法線力，負の有効法線力，内力線の逸脱の処理

理論式が同じでも，数値実装と探索方法が異なれば結果が異なることがある．

---

### 11. LEMと連続体解析の役割分担

| 問い | LEM | FEM/FDMなどの連続体解析 |
|---|---|---|
| 全体安全率 | 得意 | 強度低減法などで評価可能 |
| 仮定すべり面上の抵抗と駆動 | 直接評価 | 応力場から後処理 |
| 変位量 | 原則として求めない | 求める |
| 応力再配分 | 内力仮定で間接表現 | 構成則を通じて求める |
| 進行性破壊 | 原則として直接表現しない | 軟化則・非局所化等が必要 |
| 3D端部効果 | 3D LEMで評価可能 | 3Dモデルで評価可能 |
| 入力・計算負荷 | 比較的小さい | 一般に大きい |
| 解釈の主対象 | 安全率とすべり機構 | 応力，変位，塑性域，破壊過程 |

両者は単純な優劣関係ではない．LEMは，仮定した破壊機構に対する全体安定性を見通しのよい力学で評価する．一方，連続体解析は，変形と応力再配分を扱えるが，構成則，メッシュ，境界条件，強度低減手順への依存をもつ．

実務では，LEMで複数手法・複数すべり面を比較し，必要に応じて連続体解析で変形，局所応力，施工過程，進行性破壊を確認するという相補的な使い方が有効である．

---

## Part V　系譜とまとめ

**この Part で分かること**

- 2Dの各手法から3Dカラム法への，力学的な仮定の受け継がれ方を1枚の図で見る．
- 資料全体を，出発点・2Dの本質・3Dで増えるもの・拡張の考え方の順に振り返る．
- 解析結果を読むときに確認すべき項目を整理する．

### 12. LEM系譜の概念図

```{figure} ./figures/fig_07_lem_overview.svg
:name: fig-07-lem-overview
:alt: 2Dおよび3D極限平衡法の系譜と近似階層

LEMの概念的系譜．2Dでの内力の無視，成分の簡略化，方向関数の導入が，3Dのカラム法へどのように移され，一般化されたかを示す．
```

この系譜を文字で表すと，次の関係になる．

```text
連続体力学
        ↓ 離散化＋すべり面の仮定
2D スライス法
        ├─ Fellenius ─────────────→ Hovland 型 3D
        ├─ Simplified Bishop ─────→ Hungr / Ugai 3D Bishop
        ├─ Simplified Janbu ──────→ Ugai / Cheng–Yip 3D Janbu
        ├─ Spencer ───────────────→ Ugai / extended 3D Spencer
        └─ Morgenstern–Price / GLE → Lam–Fredlund / Cheng–Yip 3D GLE
```

この系譜は，年代順の完全な発明史ではなく，**力学的な仮定がどう受け継がれたか**を示す概念図である．

---

### 13. 最後にもう一度まとめる

#### 13.1 LEMの出発点

$$
T_i
=
\frac{c_i'A_i+(N_i-U_i)\tan\phi_i'}{F_s}
\tag{19}
$$

まで分かっても，$N_i$，$F_s$，スライス／カラム間内力は残る．

#### 13.2 2Dでの本質

- 各スライスには底面力と左右のスライス間力が作用する．
- 力とモーメントのつり合いだけでは内部力分布が一意に決まらない．
- Fellenius，Bishop，Janbu，Spencer，Morgenstern–Priceの違いは，不静定性の解消の仕方にある．
- 「簡便法」は，一部の内力またはつり合い条件を簡略化する．
- 「静力学的に完全な方法」は，内力方向を仮定したうえで力とモーメントを満足する．

#### 13.3 3Dで増えるもの

- スライスがカラムになる．
- 内部境界が一方向から二方向へ増える．
- 底面せん断力が接平面内のベクトルになる．
- 全体すべり方向，回転軸，二方向のカラム間力仮定が必要になる．
- 六つの剛体つり合い式があっても，内部力自由度がさらに増えるため自動的には解ける形にならない．

#### 13.4 3D拡張の考え方

- HovlandはFellenius型の単純化をカラム法へ拡張した．
- HungrとUgaiらはBishop簡便法などの2D仮定を3Dへ移した．
- 3D Spencer型手法は，平行な内力方向の考えを空間へ拡張した．
- Lam–FredlundはMorgenstern–Price／GLEの内力関数を二方向のカラム境界へ一般化した．
- Cheng–Yipは，非対称な3D斜面に対してBishop，Janbu，Morgenstern–Priceの考えを拡張した．

#### 13.5 最も重要な読み方

解析結果を見るときは，手法名だけでなく，次を確認する．

1. すべり面はどのように仮定・探索されたか．
2. 強度と安全率はどう定義されたか．
3. どの内力成分を無視または関数化したか．
4. どの力・モーメントつり合いを満足したか．
5. 3Dでは全体すべり方向と回転軸をどう決めたか．
6. 収束解が物理的に妥当な法線力・内力分布をもつか．

したがって，LEMとは単に「抵抗力を駆動力で割る方法」ではない．

$$
\boxed{
\begin{aligned}
&\text{LEMとは，仮定した破壊機構を離散化し，}\\
&\text{強度動員則と内部力の決め方を与えて，}\\
&\text{極限状態の静力学的つり合いから安全率を求める方法である．}
\end{aligned}
}
\tag{20}
$$

---

## 読み終えたら答えられること

- なぜ，つり合い式と底面強度式だけでは内力分布が決まらないのか．
- 「不静定性を解消する」とは，具体的にどの三種類の操作か．
- Fellenius法・Bishop簡便法・Janbu簡便法は，それぞれ何を無視し，どのつり合いを使うか．
- Spencer法が「静力学的に完全」と呼ばれるのは，どの意味での完全さか．
- 3次元で新たに決めなければならない量は何か．なぜつり合い式が6本になっても足りないのか．
- 「3D安全率は2Dより大きい」と言い切れないのはなぜか．
- 手法名だけからは分からないことは何か．

---

## 次の資料へ

本資料では，各LEMが静力学的不静定性をどのように処理するかを整理した．ただし，実際の解析では，すべり面の形状，すべり方向，離散化の仕方，探索範囲なども結果の意味を左右する．これらを力学的に解釈するには，[第3資料「極限平衡法を実際に使うとき」](./lem-in-practice-mechanical-perspective.md)へ進む．

## References

### Primary references by method

本文で扱った原著・代表的一次文献を手法別にまとめる．DOIは出版社またはCrossref系書誌情報で照合できたものだけを記載し，確認できない文献には書誌ページへのリンクのみを付した．

```{note}
Fellenius (1927, 1936) と Janbu (1954, 1973) は DOI を確認できなかったため，書誌ページへのリンクのみを付している．
```

#### 2D methods

##### Fellenius / Ordinary Method of Slices

1. Fellenius, W. (1927). *Erdstatische Berechnungen mit Reibung und Kohäsion (Adhäsion) und unter Annahme kreiszylindrischer Gleitflächen*. Berlin: Ernst & Sohn. [Bibliographic record](https://books.google.com/books?id=yHhHAAAAIAAJ).
2. Fellenius, W. (1936). “Calculation of the Stability of Earth Dams.” *Proceedings of the Second Congress on Large Dams*, Vol. 4, pp. 445–462. [Bibliographic record](https://cir.nii.ac.jp/crid/1573950399306830336).

##### Simplified Bishop

3. Bishop, A. W. (1955). “The use of the slip circle in the stability analysis of slopes.” *Géotechnique*, 5(1), 7–17. [https://doi.org/10.1680/geot.1955.5.1.7](https://doi.org/10.1680/geot.1955.5.1.7)

##### Janbu

4. Janbu, N. (1954). “Application of composite slip surfaces for stability analysis.” *Proceedings of the European Conference on Stability of Earth Slopes*, Stockholm, Vol. 3, pp. 43–49. [Bibliographic record](https://cir.nii.ac.jp/crid/1570009750148611712).
5. Janbu, N. (1973). “Slope Stability Computations.” In R. C. Hirschfeld and S. J. Poulos (eds.), *Embankment-Dam Engineering: Casagrande Volume*, pp. 47–86. New York: Wiley.

##### Spencer

6. Spencer, E. (1967). “A method of analysis of the stability of embankments assuming parallel inter-slice forces.” *Géotechnique*, 17(1), 11–26. [https://doi.org/10.1680/geot.1967.17.1.11](https://doi.org/10.1680/geot.1967.17.1.11)

##### Morgenstern–Price / GLE

7. Morgenstern, N. R., and Price, V. E. (1965). “The analysis of the stability of general slip surfaces.” *Géotechnique*, 15(1), 79–93. [https://doi.org/10.1680/geot.1965.15.1.79](https://doi.org/10.1680/geot.1965.15.1.79)
8. Morgenstern, N. R., and Price, V. E. (1967). “A numerical method for solving the equations of stability of general slip surfaces.” *The Computer Journal*, 9(4), 388–393. [https://doi.org/10.1093/comjnl/9.4.388](https://doi.org/10.1093/comjnl/9.4.388)

##### Comparative formulation

9. Fredlund, D. G., and Krahn, J. (1977). “Comparison of slope stability methods of analysis.” *Canadian Geotechnical Journal*, 14(3), 429–439. [https://doi.org/10.1139/t77-045](https://doi.org/10.1139/t77-045)

#### 3D methods

##### Hovland

10. Hovland, H. J. (1977). “Three-Dimensional Slope Stability Analysis Method.” *Journal of the Geotechnical Engineering Division*, 103(9), 971–986. [https://doi.org/10.1061/AJGEB6.0000493](https://doi.org/10.1061/AJGEB6.0000493)

##### Hungr / 3D Simplified Bishop

11. Hungr, O. (1987). “An extension of Bishop's simplified method of slope stability analysis to three dimensions.” *Géotechnique*, 37(1), 113–117. [https://doi.org/10.1680/geot.1987.37.1.113](https://doi.org/10.1680/geot.1987.37.1.113)
12. Hungr, O., Salgado, F. M., and Byrne, P. M. (1989). “Evaluation of a three-dimensional method of slope stability analysis.” *Canadian Geotechnical Journal*, 26(4), 679–686. [https://doi.org/10.1139/t89-079](https://doi.org/10.1139/t89-079)

##### Ugai and coauthors

13. Ugai, K., Hosobori, K., Nagase, H., and Enokido, M. (1986). “Three-dimensional stability analysis of slopes by simple slice method.” *土木学会論文集*, No. 376/III-6, 267–276. [https://doi.org/10.2208/jscej.1986.376_267](https://doi.org/10.2208/jscej.1986.376_267)
14. Ugai, K. (1987). “Three-dimensional slope stability analysis by simplified Janbu method.” *地すべり*, 24(3), 8–14. [https://doi.org/10.3313/jls1964.24.3_8](https://doi.org/10.3313/jls1964.24.3_8)
15. Ugai, K., and Hosobori, K. (1988). “Extension of simplified Bishop method, simplified Janbu method and Spencer's method to three dimensions.” *土木学会論文集*, No. 394/III-9, 21–26. [https://doi.org/10.2208/jscej.1988.394_21](https://doi.org/10.2208/jscej.1988.394_21)

##### 3D GLE / Morgenstern–Price

16. Lam, L., and Fredlund, D. G. (1993). “A general limit equilibrium model for three-dimensional slope stability analysis.” *Canadian Geotechnical Journal*, 30(6), 905–919. [https://doi.org/10.1139/t93-089](https://doi.org/10.1139/t93-089)

##### Extended 3D Spencer

17. Jiang, J.-C., and Yamagami, T. (2004). “Three-Dimensional Slope Stability Analysis Using an Extended Spencer Method.” *Soils and Foundations*, 44(4), 127–135. [https://doi.org/10.3208/sandf.44.4_127](https://doi.org/10.3208/sandf.44.4_127)

##### Asymmetrical 3D extensions

18. Cheng, Y. M., and Yip, C. J. (2007). “Three-Dimensional Asymmetrical Slope Stability Analysis—Extension of Bishop's, Janbu's, and Morgenstern–Price's Techniques.” *Journal of Geotechnical and Geoenvironmental Engineering*, 133(12), 1544–1555. [https://doi.org/10.1061/(ASCE)1090-0241(2007)133:12(1544)](https://doi.org/10.1061/%28ASCE%291090-0241%282007%29133%3A12%281544%29)
