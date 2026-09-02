---
title: "連続体力学から極限平衡法のスタート地点まで：応力，Mohr–Coulomb則，N_i・T_i，つり合い式"
lang: ja
series: "1 of 3"
---

# 連続体力学から極限平衡法のスタート地点まで

## 応力，Mohr–Coulomb 則，$N_i$・$T_i$，つり合い式

> **LEM理解シリーズ 1/3**  
> この資料では，連続体力学の応力テンソルから，すべり面上の表面力（traction），法線・せん断成分，有効応力，Mohr–Coulomb強度を経て，LEMで用いる底面合力$N_i$，$U_i$，$T_i$へ到達する流れを理解する．

## LEMの全体像（概要）

斜面が崩れるかどうかを判定するとき，LEMは次のように斜面安定問題を定義する．

```{figure} ./figures/fig_c00_slope_overview.svg
:name: fig-c00-slope-overview
:alt: 斜面に仮定したすべり面，すべり土塊，スライス分割と，1つのスライス底面に作用する自重・法線力・抵抗せん断力

LEMが対象とする場面．斜面の中にすべり面を仮定し，その上の土塊をスライスへ分割して，各底面に働く力を扱う．
```

1. 斜面の中に，崩れる可能性のある曲面（**すべり面**）を1つ仮定する．
2. すべり面より上の土塊（**すべり土塊**）を，鉛直な細片（2次元では**スライス**，3次元では**カラム**）へ分割する．
3. 各スライスの底面にはすべり面下の地盤から受ける**表面力**が作用する．これを面に垂直な**法線力** $N_i$ と，面に沿う**せん断力** $T_i$ に分解して扱う．

この設定のもとで，安全率 $F_s$ は，その底面が発揮できる最大のせん断力（**せん断強度**）と，現在の状態で実際に動員されているせん断力の比として定義する．

$$
F_s=\frac{\text{発揮できる最大せん断力}}{\text{動員されているせん断力}}
$$ (eq-start-fs-definition)

$F_s$ は，仮定したすべり面についての安定性の指標である．例えば $F_s=2$ は，発揮できるせん断強度が動員されているせん断力の2倍あることを，$F_s<1$ は，その面に沿ってはつり合いを保てないことを意味する．

LEMの説明資料では，式 {eq}`eq-start-fs-definition`の分子（せん断強度）を**抵抗力**，分母（動員せん断力）を**駆動力**とみなし，次のように表現することがある．

$$
F_s=\frac{\text{抵抗力}}{\text{駆動力}}
$$ (eq-start-fs-definition-mod)

厳密には，分母の動員せん断力は駆動力そのものではなく，**すべり面に沿う運動に抵抗する力**である．
ただし，静止しているすべり土塊の**力のつり合い**を考えると，すべり面が動員しているせん断力は，自重などによる滑動力とつり合う．
したがって，両者の大きさは等しく，分母を「駆動力」とみなしても安全率の値は変わらない．
そのため，直感的な表現として式 {eq}`eq-start-fs-definition-mod`がよく用いられる．


```{note}
式 {eq}`eq-start-fs-definition`および{eq}`eq-start-fs-definition-mod`
中の「力」という表現は，場合によっては比をとる対象が力ではないため，厳密ではない．
例えば Bishop 簡便法は，円弧中心まわりの**力のモーメント**の比として安全率を求める．
本資料でも §6 では，この定義を，発揮できるせん断強度と，つり合いを保つために必要なせん断応力の比として書き直す．
```

以降では，この図の $N_i$ と $T_i$ が，地盤内部の点ごとの応力からどのように作られるかを説明し，
土そのものの強さを表す Mohr–Coulomb 則が，どこで底面の $T_i$ に変わるのかを追う．

## この資料で理解すること

本資料の目的は，LEMの安全率式を最初から公式として受け入れるのではなく，

- 点の応力テンソルから，特定の面に作用する力をどう取り出すか
- 全応力，間隙水圧，有効法線応力がどう関係するか
- Mohr–Coulomb則が「作用せん断応力」ではなく「発揮可能な強度」を表すこと
- 点ごとの応力を有限なスライス／カラム底面の合力へどう置き換えるか
- なぜ$T_i$の式を得ても，$N_i$，$F_s$，内部力が未知として残るのか

を，一つの力学的な道筋としてつなぐことである．

読み終えた時点で，次式

$$
T_i
=
\frac{c_i'A_i+(N_i-U_i)\tan\phi_i'}{F_s}
$$ (eq-start-goal)

がどこから来たのか，またこの式が**LEMのスタート地点**である理由を説明できることを目標とする．

## シリーズ内での位置付け

| 資料 | 中心となる問い |
|---|---|
| **1. 連続体力学から極限平衡法のスタート地点まで（本資料）** | 応力と破壊規準は，底面の力へどう変換されるか |
| 2. [極限平衡法とは何か](./what-is-limit-equilibrium-method.md) | 残った未知量を，各手法はどの仮定で決めるか |
| 3. [極限平衡法を実際に使うとき](./lem-in-practice-mechanical-perspective.md) | 任意形状，すべり方向，離散化をどう解釈するか |

用語と記号の定義は[用語集](./lem-glossary.md)にまとめている．

---


(notation)=

## 記号と符号規約

以降では，連続体力学の式と地盤工学の強度式を混同しないよう，次の規約を用いる．

- $\boldsymbol{\sigma}$：引張を正とする Cauchy 応力テンソル
- $\boldsymbol{n}$：すべり土塊から外向きの単位法線ベクトル
- $\boldsymbol{t}(\boldsymbol{n})=\boldsymbol{\sigma}\boldsymbol{n}$：その法線をもつ面上で，周囲からすべり土塊に作用する表面力ベクトル
- $\sigma_n$：地盤工学の慣例に従い，圧縮を正とした法線応力（圧縮状態では $\sigma_n\ge 0$）
- $u\ge 0$：間隙水圧
- $\boldsymbol{m}$：すべり面の接平面内で仮定した，局所的なすべり方向の単位ベクトル
- $c'$，$\phi'$：有効応力表示の粘着力と内部摩擦角
- $F_s$：安全率

この規約では，すべり土塊に作用する圧縮側の法線表面力は $-\sigma_n\boldsymbol{n}$，すべりに抵抗するせん断表面力は $-\tau_m\boldsymbol{m}$ となる．符号規約を変えた場合の対応は次のとおりである．

:::{dropdown} 補足 A：引張正と圧縮正の符号規約
標準的な連続体力学で引張を正とすれば，Cauchy の公式は

$$
\boldsymbol{t}=\boldsymbol{\sigma}\boldsymbol{n}
$$

であり，符号付き法線成分は

$$
t_n=\boldsymbol{n}^{\mathsf T}\boldsymbol{\sigma}\boldsymbol{n}
$$

である．圧縮状態では $t_n<0$ となる．

地盤工学で圧縮を正とするスカラー量は

$$
\sigma_n=-t_n
$$

である．また，圧縮正の応力テンソルを

$$
\boldsymbol{\sigma}^{(c)}=-\boldsymbol{\sigma}
$$

と定義すれば

$$
\sigma_n
=
\boldsymbol{n}^{\mathsf T}\boldsymbol{\sigma}^{(c)}\boldsymbol{n}
$$

となる．ただしこのとき，実際の表面力は

$$
\boldsymbol{t}=-\boldsymbol{\sigma}^{(c)}\boldsymbol{n}
$$

である．

```{note}
文献によっては，圧縮正の $\sigma_n$ を使いながら力の向きを別途定義し，符号を式の外で処理する．本稿では，強度式には圧縮正の大きさ $\sigma_n$ を使い，ベクトル式では作用方向を $-\boldsymbol{n}$ と明記した．
```
:::

---

(section-1)=

## 1. 連続体力学における厳密な出発点

地盤内部の応力状態は，点 $\boldsymbol{x}$ ごとの Cauchy 応力テンソル

$$
\boldsymbol{\sigma}=\boldsymbol{\sigma}(\boldsymbol{x})
$$ (eq-start-stress-field)

で表される．すべり面上の応力分布は，離散化する前から未知の関数である．これを連続体解析として決定するには，つり合い式だけでなく，構成則，変位の適合条件，境界条件などが必要になる．LEM（limit equilibrium method，極限平衡法）は，一般にこの完全な境界値問題を解く代わりに，すべり土塊を有限個のスライスまたはカラムへ分割し，各部分の合力とつり合いを扱う．

```{note}
**連続体力学とのつながり**

静的な連続体では，局所的な力のつり合いは

$$
\nabla\!\cdot\!\boldsymbol{\sigma}+\rho\boldsymbol{b}=\boldsymbol{0}
$$

であり，偶力を考えない通常の連続体では角運動量のつり合いから $\boldsymbol{\sigma}=\boldsymbol{\sigma}^{\mathsf T}$ となる．ここで $\rho\boldsymbol{b}$ は単位体積当たりの物体力であり，重力だけなら $\boldsymbol{b}=\boldsymbol{g}$ である．

ただし本資料が以降で直接使うのは，次節の Cauchy の公式 $\boldsymbol{t}=\boldsymbol{\sigma}\boldsymbol{n}$ だけである．上の2式は，出発点が連続体力学のどこに接続しているかを示すためのものである．
```

---

(section-2)=

## 2. 応力テンソルから表面力を取り出す

すべり面上の点 $\boldsymbol{x}$ における外向き単位法線を $\boldsymbol{n}(\boldsymbol{x})$ とする．この面に作用する単位面積当たりの力，すなわち表面力は Cauchy の公式により

$$
\boxed{
\boldsymbol{t}(\boldsymbol{x},\boldsymbol{n})
=
\boldsymbol{\sigma}(\boldsymbol{x})\boldsymbol{n}(\boldsymbol{x})
}
$$ (eq-start-cauchy)

で与えられる．

ここで，応力テンソル $\boldsymbol{\sigma}$ は二階テンソル，特定の面に作用する $\boldsymbol{t}$ はベクトルである．「応力」という語が，文脈によりテンソル，表面力，またはその成分を指すことがあるため，これらは区別する必要がある．

```{figure} ./figures/fig_c01_stress_to_traction.svg
:name: fig-c01-stress-to-traction
:alt: 応力テンソルから任意面の表面力を取り出すCauchy公式の模式図

点の応力テンソルと，法線$\boldsymbol{n}$をもつ面に作用する表面力 $\boldsymbol{t}=\boldsymbol{\sigma}\boldsymbol{n}$の関係．
```

---

(section-3)=

## 3. 表面力の法線成分とせん断成分

表面力の符号付き法線成分を

$$
t_n
=
\boldsymbol{n}^{\mathsf T}\boldsymbol{t}
=
\boldsymbol{n}^{\mathsf T}\boldsymbol{\sigma}\boldsymbol{n}
$$ (eq-start-normal-component)

とする．引張正の規約では圧縮時に $t_n<0$ となるため，地盤工学で用いる圧縮正の法線応力の大きさを

$$
\boxed{
\sigma_n=-t_n
=
-\boldsymbol{n}^{\mathsf T}\boldsymbol{\sigma}\boldsymbol{n}
}
$$ (eq-start-sigma-n)

と定義する．圧縮状態では $\sigma_n\ge 0$ となる．土が引張を受ける場合や，有効法線応力が負になる場合の扱いは，第3資料で述べる数値上の注意点に関わる．

表面力は法線成分と接平面内のせん断成分に一意に分解できる．

$$
\boxed{
\boldsymbol{t}
=
-\sigma_n\boldsymbol{n}+\boldsymbol{\tau}
}
$$ (eq-start-traction-split)

ここで

$$
\boldsymbol{\tau}\cdot\boldsymbol{n}=0
$$ (eq-start-tau-tangential)

である．

:::{dropdown} 補足 B：法線・せん断分解と射影行列
$\|\boldsymbol{n}\|=1$ とする．法線方向への射影行列と接平面への射影行列は

$$
\boldsymbol{P}_n=\boldsymbol{n}\boldsymbol{n}^{\mathsf T},
\qquad
\boldsymbol{P}_t=\boldsymbol{I}-\boldsymbol{n}\boldsymbol{n}^{\mathsf T}
$$

である．表面力の法線ベクトル成分は

$$
\begin{aligned}
\boldsymbol{t}_n
&=(\boldsymbol{n}^{\mathsf T}\boldsymbol{t})\boldsymbol{n}\\
&=\boldsymbol{n}\boldsymbol{n}^{\mathsf T}\boldsymbol{t}\\
&=\boldsymbol{P}_n\boldsymbol{t},
\end{aligned}
$$

せん断表面力は

$$
\begin{aligned}
\boldsymbol{\tau}
&=\boldsymbol{t}-\boldsymbol{t}_n\\
&=(\boldsymbol{I}-\boldsymbol{n}\boldsymbol{n}^{\mathsf T})\boldsymbol{t}\\
&=(\boldsymbol{I}-\boldsymbol{n}\boldsymbol{n}^{\mathsf T})
\boldsymbol{\sigma}\boldsymbol{n}.
\end{aligned}
$$

ここで

$$
\boldsymbol{n}^{\mathsf T}\boldsymbol{\tau}=0
$$

であるため，$\boldsymbol{\tau}$ は接平面内にある．引張正では $\boldsymbol{t}_n=t_n\boldsymbol{n}=-\sigma_n\boldsymbol{n}$ である．
:::

2D では接線方向は符号を除いて一意である．一方，3D の接平面内には無数の方向があるため，接線基底と実際に仮定する局所すべり方向を区別する必要がある．本稿では

$$
\|\boldsymbol{m}\|=1,
\qquad
\boldsymbol{m}\cdot\boldsymbol{n}=0
$$ (eq-start-slip-direction)

を満たす $\boldsymbol{m}$ を局所的な想定すべり方向とし，抵抗せん断表面力を

$$
\boxed{
\boldsymbol{\tau}_m=-\tau_m\boldsymbol{m}
}
$$ (eq-start-shear-traction)

と表す．

:::{dropdown} 補足 C：3D における接線基底と想定した局所すべり方向
3D の接平面は

$$
\left\{
\boldsymbol{v}\mid \boldsymbol{v}\cdot\boldsymbol{n}=0
\right\}
$$

であり，直交接線基底 $\boldsymbol{t}_1,\boldsymbol{t}_2$ を使えば，任意の接線ベクトルは

$$
\boldsymbol{v}=a\boldsymbol{t}_1+b\boldsymbol{t}_2
$$

と表される．したがって $\boldsymbol{n}$ だけから $\boldsymbol{m}$ は決まらない．

例えば，全体的な移動方向 $\boldsymbol{d}$ を仮定し，それを局所接平面へ射影するなら

$$
\boldsymbol{d}_{\mathrm{tan}}
=
(\boldsymbol{I}-\boldsymbol{n}\boldsymbol{n}^{\mathsf T})\boldsymbol{d}
$$

とし，$\boldsymbol{d}_{\mathrm{tan}}\ne\boldsymbol{0}$ のとき

$$
\boxed{
\boldsymbol{m}
=
\frac{\boldsymbol{d}_{\mathrm{tan}}}
{\|\boldsymbol{d}_{\mathrm{tan}}\|}
}
$$

と定義できる．ただし，これは一つの選択方法にすぎない．3D LEM では，局所すべり方向の仮定やせん断抵抗の投影方法が手法ごとに異なり得る．
:::

---

(section-4)=

## 4. 全応力から有効応力へ

飽和土に Terzaghi の有効応力原理を適用する．圧縮正で表した全応力テンソルを $\boldsymbol{\sigma}^{(c)}=-\boldsymbol{\sigma}$ とすれば，有効応力テンソルは

$$
\boxed{
\boldsymbol{\sigma}'^{(c)}
=
\boldsymbol{\sigma}^{(c)}-u\boldsymbol{I}
}
$$ (eq-start-effective-tensor)

である．

これをすべり面の法線方向へ射影すると，有効法線応力は

$$
\boxed{
\sigma_n'
=
\sigma_n-u
}
$$ (eq-start-effective-normal)

となる．したがって「有効応力」は本来テンソル全体を指し，$\sigma_n'$ はその特定の面に対する有効法線成分である．間隙水圧は等方的に作用するため，表面力のせん断成分を直接は変化させない．

:::{dropdown} 補足 D：有効応力テンソルから有効法線応力を得る
圧縮正の全応力テンソルについて

$$
\boldsymbol{\sigma}'^{(c)}
=
\boldsymbol{\sigma}^{(c)}-u\boldsymbol{I}
$$

とする．単位法線 $\boldsymbol{n}$ への射影は

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
&=\sigma_n-u.
\end{aligned}
$$

また，$u\boldsymbol{I}$ による表面力は

$$
u\boldsymbol{I}\boldsymbol{n}=u\boldsymbol{n}
$$

で常に法線方向を向く．このため，等方的な間隙水圧は接平面内のせん断成分を持たない．
:::

```{figure} ./figures/fig_c02_normal_shear_effective.svg
:name: fig-c02-normal-shear-effective
:alt: 表面力の法線・せん断分解と間隙水圧による有効法線応力低下の模式図

表面力の法線・せん断分解と，$\sigma_n'=\sigma_n-u$による有効法線応力の関係．
```

---

(section-5)=

## 5. Mohr–Coulomb 則によるせん断強度

有効応力表示の Mohr–Coulomb 則では，現在の有効法線応力 $\sigma_n'$ の下で発揮可能なせん断強度を

$$
\boxed{
\tau_f
=
c'+\sigma_n'\tan\phi'
=
c'+(\sigma_n-u)\tan\phi'
}
$$ (eq-start-mohr-coulomb)

と表す．

ここで $\tau_f$ は「現在作用しているせん断応力」ではない．これは，現在の法線拘束条件の下で破壊時に発揮できるせん断抵抗の上限である．同じ土でも，$\sigma_n'$ が増えれば粒子間の摩擦抵抗が増し，$\tau_f$ は大きくなる．反対に，全法線応力 $\sigma_n$ が同じでも間隙水圧 $u$ が増えれば

$$
u\uparrow
\quad\Longrightarrow\quad
\sigma_n'\downarrow
\quad\Longrightarrow\quad
\tau_f\downarrow
$$ (eq-start-pore-pressure-effect)

となる．

---

(section-6)=

## 6. 安全率と動員せん断応力

LEM では，発揮可能なせん断強度 $\tau_f$ と，つり合いを保つために実際に動員されるせん断応力 $\tau_m$ の比として安全率を定義する．

$$
\boxed{
F_s=\frac{\tau_f}{\tau_m}
}
$$ (eq-start-fs-stress)

したがって

$$
\boxed{
\tau_m
=
\frac{c'+(\sigma_n-u)\tan\phi'}{F_s}
}
$$ (eq-start-mobilized-stress)

である．ベクトルとしての抵抗せん断表面力は

$$
\boxed{
\boldsymbol{\tau}_m
=
-\frac{c'+(\sigma_n-u)\tan\phi'}{F_s}\boldsymbol{m}
}
$$ (eq-start-mobilized-vector)

となる．

```{note}
式 {eq}`eq-start-mobilized-stress` と {eq}`eq-start-mobilized-vector` は，現在の $\tau_m$ を事前に測定してから比を取るという意味ではない．未知の $F_s$ を導入してせん断強度の動員割合を表し，この表面力を作用させた土塊が力とモーメントのつり合いを満たすように，$F_s$ と他の未知力を同時に求める．
```

```{figure} ./figures/fig_c03_strength_mobilization.svg
:name: fig-c03-strength-mobilization
:alt: Mohr-Coulombせん断強度と安全率によって低減された動員せん断応力の関係

発揮可能な強度$\tau_f$と，つり合いに必要な動員せん断応力$\tau_m=\tau_f/F_s$の違い．
```

```{admonition} 数値でたどる
ある底面で，全法線応力 $\sigma_n=100$ kPa，間隙水圧 $u=40$ kPa，$c'=10$ kPa，$\phi'=30^\circ$ とする．このとき

$$
\sigma_n'=100-40=60\ \text{kPa},
\qquad
\tau_f=10+60\tan 30^\circ=44.6\ \text{kPa}
$$

である．つり合いを保つために必要なせん断応力が $\tau_m=30$ kPa なら

$$
F_s=\frac{44.6}{30}=1.49
$$

となる．ここで水位が上がって $u=60$ kPa になり，駆動側の $\tau_m$ は変わらないとすると

$$
\sigma_n'=40\ \text{kPa},
\qquad
\tau_f=10+40\tan 30^\circ=33.1\ \text{kPa},
\qquad
F_s=\frac{33.1}{30}=1.10
$$

である．土の強度定数 $c'$ と $\phi'$ は何も変わっていないのに，安全率は 1.49 から 1.10 へ下がる．これが前節の $u\uparrow\Rightarrow\tau_f\downarrow$ の中身である．
```

---

(section-7)=

## 7. 点の応力から有限面積上の合力へ

カラム $i$ の底面を $S_i$，その面積を

$$
A_i=\int_{S_i}dA
$$ (eq-start-base-area)

とする．底面に作用する表面力全体の合力は厳密に

$$
\boxed{
\boldsymbol{R}_i
=
\int_{S_i}\boldsymbol{t}\,dA
}
$$ (eq-start-resultant)

である．

圧縮側の法線表面力の合力ベクトルと，抵抗せん断表面力の合力ベクトルは，それぞれ

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

である．なお，$\boldsymbol{R}_i=\int_{S_i}\boldsymbol{t}\,dA$ は厳密であるが，$\boldsymbol{T}_i$ を式 {eq}`eq-start-shear-resultant` の形で書けるのは，各点の実際のせん断表面力が $-\boldsymbol{m}(\boldsymbol{x})$ 方向に一致する，すなわち 6 節の動員状態にあると仮定した場合である．この仮定の下で

$$
\boldsymbol{R}_i=\boldsymbol{N}_i+\boldsymbol{T}_i
$$ (eq-start-resultant-split)

となる．

曲面上では $\boldsymbol{n}$ が場所によって変化するため，一般には

$$
\left\|\boldsymbol{N}_i\right\|
\le
\int_{S_i}\sigma_n\,dA
$$ (eq-start-resultant-bound)

となる．等号が成り立つのは法線方向が底面全体で共通である場合などに限られる．すなわち，局所的な法線力の大きさを足したスカラーと，向きを考慮して足したベクトル合力の大きさは区別しなければならない．

:::{dropdown} 補足 E：曲面上のベクトル合力とスカラー積分
曲面 $S_i$ では，一般に $\boldsymbol{n}=\boldsymbol{n}(\boldsymbol{x})$ である．圧縮側の法線表面力のベクトル合力は

$$
\boldsymbol{N}_i
=
-\int_{S_i}\sigma_n(\boldsymbol{x})
\boldsymbol{n}(\boldsymbol{x})\,dA
$$

である．一方，

$$
N_i^*=\int_{S_i}\sigma_n\,dA
$$

は局所的な大きさを足したスカラーである．三角不等式から

$$
\|\boldsymbol{N}_i\|
\le
N_i^*
$$

であり，等号が成り立つのは，$\sigma_n>0$ の領域で法線方向が共通である場合などに限られる．

代表法線 $\boldsymbol{n}_i$ を底面全体で一定と仮定すれば

$$
\boldsymbol{N}_i
=
-\boldsymbol{n}_i\int_{S_i}\sigma_n\,dA
=
-N_i\boldsymbol{n}_i
$$

となり，LEM で用いるスカラー $N_i$ とベクトル合力の関係が得られる．
:::

```{figure} ./figures/fig_c04_surface_integration.svg
:name: fig-c04-surface-integration
:alt: 曲面上の応力分布を底面の法線合力とせん断合力へ面積分する模式図

点ごとの表面力分布から，有限底面のベクトル合力$\boldsymbol{N}_i$，$\boldsymbol{T}_i$へ移る面積分．
```

---

(section-8)=

## 8. LEM における $N_i$，$U_i$，$T_i$

LEM の各スライスまたはカラムでは，底面 $S_i$ が必ずしも小さいとは仮定しない．代わりに，

> **$S_i$ 内で，方向（$\boldsymbol{n},\boldsymbol{m}$）と材料定数（$c',\phi'$）を代表値で一定と仮定し，応力と間隙水圧は面積分値 $N_i,U_i$ として代表させる．**

例えば

$$
\boldsymbol{n}(\boldsymbol{x})=\boldsymbol{n}_i,
\qquad
\boldsymbol{m}(\boldsymbol{x})=\boldsymbol{m}_i
\qquad (\boldsymbol{x}\in S_i)
$$ (eq-start-representative-direction)

とモデル化し，法線応力と間隙水圧のスカラー積分値を

$$
\boxed{
N_i=\int_{S_i}\sigma_n\,dA,
\qquad
U_i=\int_{S_i}u\,dA
}
$$ (eq-start-ni-ui)

と定義する．このとき，すべり土塊に作用する法線合力ベクトルは

$$
\boxed{
\boldsymbol{N}_i=-N_i\boldsymbol{n}_i
}
$$ (eq-start-ni-vector)

となる．さらに $\sigma_n$ と $u$ まで代表値で一定とする追加の仮定を置けば

$$
N_i=\sigma_{n,i}A_i,
\qquad
U_i=u_iA_i
$$ (eq-start-ni-uniform)

である．

```{note}
文献で $\boldsymbol{N}_i=N_i\boldsymbol{n}_i$ と書く場合は，$\boldsymbol{n}_i$ を法線力の作用方向に取るなど，法線の向きに別の規約を用いている．
```

一方，$S_i$ 内で $c_i'$，$\phi_i'$ を一定とし，$F_s$ をすべり面全体で共通とすると，Mohr–Coulomb 則を面積分して，発揮可能なせん断強度の合力の大きさは

$$
\boxed{
T_{f,i}
=
c_i'A_i+(N_i-U_i)\tan\phi_i'
}
$$ (eq-start-base-strength)

となる．動員されるせん断力の大きさは

$$
\boxed{
T_i
=
\frac{c_i'A_i+(N_i-U_i)\tan\phi_i'}{F_s}
}
$$ (eq-start-base-shear)

であり，$\boldsymbol{m}_i$ が底面内で一定なら，その抵抗方向を含むベクトルは

$$
\boxed{
\boldsymbol{T}_i=-T_i\boldsymbol{m}_i
}
$$ (eq-start-base-shear-vector)

となる．

重要なのは，スカラー式 $T_{f,i}=c_i'A_i+(N_i-U_i)\tan\phi_i'$ を得るために，$\sigma_n$ と $u$ の点ごとの分布まで一定である必要はないことである．$c_i'$ と $\phi_i'$ が一定で，$N_i$ と $U_i$ を式 {eq}`eq-start-ni-ui` の積分値として定義すれば，式 {eq}`eq-start-base-strength` は成立する．

:::{dropdown} 補足 F：Mohr–Coulomb 則の面積分
底面 $S_i$ で $c_i'$ と $\phi_i'$ が一定であるとする．発揮可能なせん断強度の合力の大きさは

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
&=c_i'A_i+(N_i-U_i)\tan\phi_i'.
\end{aligned}
$$

したがって，このスカラー式については $\sigma_n$ と $u$ が底面内で分布していてもよい．さらに $F_s$ を底面で一定とする共通安全率の仮定を用いれば

$$
T_i
=
\int_{S_i}\frac{\tau_f}{F_s}\,dA
=
\frac{T_{f,i}}{F_s}
$$

となる．

ベクトル式 $\boldsymbol{T}_i=-T_i\boldsymbol{m}_i$ まで単純化するには，抵抗方向 $\boldsymbol{m}$ も $S_i$ 内で一定と仮定する必要がある．
:::

```{note}
したがって「$S_i$ が十分小さいから一定とみなせる」という数値積分的な説明よりも，「底面ごとに方向と材料定数を代表値で一定と仮定し，応力は積分値で代表させる」という表現の方が，$A_i$ が必ずしも小さくない実務上の LEM と整合する．この仮定には，曲面状の底面を一つの代表平面と代表方向で表す幾何学的近似も含まれる．
```

:::{dropdown} 補足 G：「底面が十分小さい」と「代表値で一定」の違い
次の二つは同じ主張ではない．

1. **数値積分としての説明**：$S_i$ を十分小さくすれば，連続な量の変化が小さくなり，代表値による積分近似が良くなる．
2. **LEM のモデル仮定**：$S_i$ の大小にかかわらず，その底面を一つの代表法線，代表すべり方向，代表材料定数などで表す．

実務上の LEM では $A_i$ が必ずしも微小ではないため，本文では後者を基本表現とした．例えば

$$
\boldsymbol{n}(\boldsymbol{x})=\boldsymbol{n}_i,
\qquad
\sigma_n(\boldsymbol{x})=\sigma_{n,i}
$$

を $S_i$ 内のモデル仮定として置けば

$$
\boldsymbol{N}_i
=
-\int_{S_i}\sigma_{n,i}\boldsymbol{n}_i\,dA
=
-\sigma_{n,i}A_i\boldsymbol{n}_i
$$

は，そのモデルの内部では厳密に成立する．ただし，実際の曲面上の方向や応力分布に対しては近似である．

カラムを細分化すれば幾何学や積分の近似が改善する場合はあるが，それだけでスライス間力に関する仮定など，LEM 固有の力学的仮定が消えるわけではない．
:::

---

(section-9)=

## 9. つり合い式と LEM 固有の未知量の決め方

式

$$
T_i
=
\frac{c_i'A_i+(N_i-U_i)\tan\phi_i'}{F_s}
$$ (eq-start-strength-law-recap)

を得ても，$N_i$，$T_i$，$F_s$ およびスライス間力・カラム間力はまだ未知である．

カラム $i$ に作用する自重を $\boldsymbol{W}_i$，その他の既知外力を $\boldsymbol{P}_i$，隣接カラム $j$ から受ける力を $\boldsymbol{Q}_{ij}$ とすれば，力のつり合いは概念的に

$$
\boxed{
\boldsymbol{W}_i+\boldsymbol{P}_i
-N_i\boldsymbol{n}_i
-T_i\boldsymbol{m}_i
+\sum_j\boldsymbol{Q}_{ij}
=\boldsymbol{0}
}
$$ (eq-start-force-balance)

と書ける．また，任意の基準点 $O$ に関するモーメントのつり合いは

$$
\boxed{
\sum_k
\boldsymbol{r}_k\times\boldsymbol{F}_k
=\boldsymbol{0}
}
$$ (eq-start-moment-balance)

である．

LEM では，これらの力・モーメントのつり合い式，強度動員式，および手法ごとの追加仮定を組み合わせて，$F_s$ と各合力を求める．追加仮定の例には，スライス間せん断力を無視する，スライス間力の方向または関係を仮定する，満たすつり合い式を限定する，といったものがある．Bishop，Janbu，Spencer などの違いは，この問題の未知量の決め方に関係する．

したがって，LEM の離散化は未知量を新たに生み出す操作というより，もともと未知だった連続的な応力分布を有限個の未知合力へ置き換える操作である．また，底面の面積分を有限個の量で表すことと，つり合い式だけでは不足する未知量を追加仮定で決めることは，別の問題である．

:::{dropdown} 補足 H：離散化と未知量の決め方
すべり面上の

$$
\sigma_n(\boldsymbol{x}),
\qquad
\boldsymbol{\tau}(\boldsymbol{x})
$$

は，離散化前から未知の連続分布である．LEM の離散化は，これらを各底面の

$$
N_i,
\qquad
T_i
$$

という有限個の未知合力へ置き換える．

しかし，離散化しただけでは $N_i$ やスライス間力は決まらない．一般に未知数の数が独立なつり合い式の数を上回るため，次の二段階を区別する必要がある．

- **空間離散化**：連続的な形状，荷重および応力分布を，有限個のスライス・カラムと合力で表現する．
- **力学的な未知量の決定**（closure）：未知合力を決定できるよう，スライス間力の方向・比率・無視する成分などについて手法固有の仮定を導入する．

```{note}
したがって，「応力が未知だから細かく分割すれば自動的に求まる」のではない．正確には，未知の連続分布を有限個の未知量へ変換した後，つり合い式，強度動員式および追加仮定を連立して $F_s$ と合力を求める．
```
:::

```{figure} ./figures/fig_c05_discrete_forces_closure.svg
:name: fig-c05-discrete-forces-closure
:alt: 連続応力分布をスライスまたはカラム底面合力へ離散化し追加仮定で未知量を決める流れ

連続な未知応力分布の離散化と，LEM固有の未知量の決め方は別の操作である．
```

以上の流れは，次のようにまとめられる．

$$
\boxed{
\begin{array}{c}
\text{連続体の応力場と局所つり合い}\\[1mm]
\boldsymbol{\sigma},\quad
\nabla\!\cdot\!\boldsymbol{\sigma}+\rho\boldsymbol{b}=\boldsymbol{0}
\\[2mm]
\downarrow\\[2mm]
\text{すべり面上の表面力}\\[1mm]
\boldsymbol{t}=\boldsymbol{\sigma}\boldsymbol{n}
\\[2mm]
\downarrow\\[2mm]
\text{法線・せん断分解}\\[1mm]
\sigma_n,\quad\boldsymbol{\tau}
\\[2mm]
\downarrow\quad\text{有効応力}\\[2mm]
\sigma_n'=\sigma_n-u
\\[2mm]
\downarrow\quad\text{Mohr--Coulomb}\\[2mm]
\tau_f=c'+\sigma_n'\tan\phi'
\\[2mm]
\downarrow\quad\text{安全率}\\[2mm]
\tau_m=\tau_f/F_s
\\[2mm]
\downarrow\quad\text{面積分・底面ごとのモデル化}\\[2mm]
N_i,\quad U_i,\quad T_i
\\[2mm]
\downarrow\quad\text{つり合い式・LEM 固有の仮定}\\[2mm]
F_s\ \text{と各未知合力}
\end{array}
}
$$ (eq-start-summary)

---

## 読み終えたら答えられること

- 応力テンソルと，特定の面に作用する表面力は何が違うか．
- 有効法線応力 $\sigma_n'$ は，全法線応力と間隙水圧からどう決まるか．
- Mohr–Coulomb 則が与える $\tau_f$ は「いま働いているせん断応力」か，それとも別のものか．
- 安全率 $F_s$ は，何と何の比として導入されたか．
- $N_i$，$U_i$，$T_i$ は，点ごとの応力にどのような操作を加えて作られたか．
- 底面 $S_i$ で一定と仮定する必要があるのはどの量で，一定でなくてよいのはどの量か．
- 式 {eq}`eq-start-base-shear` を得てもなお未知として残るのは何か．

---

## 次の資料へ

ここまでで，連続体の応力からLEMで用いる底面合力と強度動員式へ到達した．しかし，$N_i$，$F_s$，スライス／カラム間内力はまだ決まっていない．これらを各手法がどの仮定によって決定するかは，[第2資料「極限平衡法とは何か」](./what-is-limit-equilibrium-method.md)で扱う．
