---
title: "連続体力学から極限平衡法の出発点まで：応力からスライス底面の力を導く"
lang: ja
series: "1 of 3"
---

# 連続体力学から極限平衡法の出発点まで

**応力からスライス底面の力を導く**

この章では，連続体力学の応力テンソルから出発して，極限平衡法（limit equilibrium method，LEM）がスライスの底面で扱う力 $N_i$，$U_i$，$T_i$ を導く．途中で，すべり面に働く力を法線成分とせん断成分に分け，有効応力とMohr–Coulomb則によるせん断強度を順に組み込む．

用語と記号は，[用語集](lem-glossary.md)にまとめている．

(overview)=

## LEMの全体像

斜面が崩れるかどうかを調べるとき，LEMは問題を次のように設定する．

```{figure} ./figures/fig_c00_slope_overview.svg
:name: fig-c00-slope-overview
:alt: 斜面に仮定した円弧のすべり面，すべり土塊，6つのスライスと，1つのスライスに働く自重・垂直力・せん断力

LEMが対象とする場面．斜面の中にすべり面を仮定し，その上の土塊をスライスに分けて，各底面に働く力を扱う．スライス間力は省いている
```

1. 斜面の中に，崩れるかもしれない曲面（**すべり面**）を1つ仮定する
2. すべり面より上の土塊（**すべり土塊**）を，鉛直な細片に分ける．細片は，2次元では**スライス**，3次元では**カラム**と呼ぶ
3. 各スライスの底面には，すべり面より下の地盤から力が働く．この力を，底面に垂直な成分 $N_i$（**垂直力**）と，底面に沿う成分 $T_i$（**せん断力**）に分けて扱う

このとき，**安全率** $F_s$ は，底面が発揮できる最大のせん断力（**せん断強度**）と，今の状態で底面に実際に働いているせん断力の比で定める．実際に働いているせん断力は，強度のうち使われている分なので，**動員されている**せん断力ともいう．

$$
F_s=\frac{\text{発揮できる最大せん断力}}{\text{動員されているせん断力}}
$$ (eq-start-fs-definition)

$F_s$ は，仮定したすべり面についての安定性の指標である．例えば $F_s=2$ なら，発揮できるせん断強度は，動員されているせん断力の2倍ある．$F_s<1$ なら，その面に沿ってつり合いを保てない．

LEMの教科書や解説では，式 {eq}`eq-start-fs-definition` の分子（せん断強度）を**抵抗力**，分母（動員されているせん断力）を**滑動力**（土塊をすべらせようとする力）とみなして，次のように書くことがある．

$$
F_s=\frac{\text{抵抗力}}{\text{滑動力}}
$$ (eq-start-fs-definition-mod)

厳密には，分母の動員されているせん断力は，滑動力そのものではない．すべり面に沿う動きに**抵抗する**力である．ただし，静止しているすべり土塊の**力のつり合い**を考えると，すべり面が動員しているせん断力は，自重などによる滑動力とつり合っている．つまり，両者の大きさは等しく，分母を滑動力とみなしても安全率の値は変わらない．そのため，直感に合う書き方として，式 {eq}`eq-start-fs-definition-mod` がよく使われる．

```{note}
式 {eq}`eq-start-fs-definition` と式 {eq}`eq-start-fs-definition-mod` の「力」は，厳密な言い方ではない．手法によっては，力ではないものの比をとるからである．例えば簡易Bishop法は，円弧の中心まわりの**力のモーメント**の比として安全率を求める．この章でも，6節で，この定義を，発揮できるせん断強度と，つり合いを保つのに必要なせん断応力の比に書き直す．
```

この後は，図の $N_i$ と $T_i$ が，地盤の中の点ごとの応力からどう作られるかを説明する．あわせて，土そのものの強さを表すMohr–Coulomb則が，どこで底面の $T_i$ に変わるのかを追う．最終的には，次の式にたどり着く．

$$
T_i
=
\frac{c_i'A_i+(N_i-U_i)\tan\phi_i'}{F_s}
$$ (eq-start-goal)

この式をどう導くのか，なぜこの式が**LEMの出発点**になるのかを，1節から9節で順に説明する．

---


(notation)=

## 記号と符号規約

この後は，連続体力学の式と，地盤工学の強度の式を取り違えないように，次の記号と符号規約を使う．

- $\boldsymbol{\sigma}$：Cauchyの応力テンソル．引張を正とする
- $\boldsymbol{n}$：単位法線ベクトル．すべり土塊の外向きにとる
- $\boldsymbol{t}(\boldsymbol{n})=\boldsymbol{\sigma}\boldsymbol{n}$：法線が $\boldsymbol{n}$ の面で，周りの地盤からすべり土塊に働く表面力のベクトル
- $\sigma_n$：垂直応力．地盤工学の慣例に従い，圧縮を正とする（圧縮を受けていれば $\sigma_n\ge 0$）
- $u\ge 0$：間隙水圧
- $\boldsymbol{m}$：局所的なすべり方向の単位ベクトル．すべり面の接平面内で仮定する
- $\tau_m$：動員されているせん断応力の大きさ（6節で定める）
- $c'$，$\phi'$：有効応力で表した粘着力と内部摩擦角
- $F_s$：安全率

この符号規約では，すべり土塊に働く表面力のうち，圧縮の法線成分は $-\sigma_n\boldsymbol{n}$，すべりに抵抗するせん断成分は $-\tau_m\boldsymbol{m}$ になる．符号規約を変えたときの対応は，次の補足にまとめている．

:::{dropdown} 補足A：引張を正とする符号と，圧縮を正とする符号
連続体力学で標準的な，引張を正とする符号では，Cauchyの公式は

$$
\boldsymbol{t}=\boldsymbol{\sigma}\boldsymbol{n}
$$

である．表面力の法線成分は，符号を含めて

$$
t_n=\boldsymbol{n}^{\mathsf T}\boldsymbol{\sigma}\boldsymbol{n}
$$

になる．圧縮を受けていれば，$t_n<0$ である．

地盤工学では，圧縮を正とする．このときの垂直応力は

$$
\sigma_n=-t_n
$$

である．また，圧縮を正とする応力テンソルを

$$
\boldsymbol{\sigma}^{(c)}=-\boldsymbol{\sigma}
$$

と定めれば，

$$
\sigma_n
=
\boldsymbol{n}^{\mathsf T}\boldsymbol{\sigma}^{(c)}\boldsymbol{n}
$$

と書ける．ただし，このとき実際の表面力は

$$
\boldsymbol{t}=-\boldsymbol{\sigma}^{(c)}\boldsymbol{n}
$$

になる．

```{note}
文献によっては，圧縮を正とする $\sigma_n$ を使いながら，力の向きを別に定め，符号を式の外で扱う．この章では，強度の式には圧縮を正とする大きさ $\sigma_n$ を使い，ベクトルの式では力の向きを $-\boldsymbol{n}$ と明記している．
```
:::

---

(section-1)=

## 1. 連続体力学での厳密な出発点

地盤の中の応力の状態は，点 $\boldsymbol{x}$ ごとのCauchyの応力テンソル

$$
\boldsymbol{\sigma}=\boldsymbol{\sigma}(\boldsymbol{x})
$$ (eq-start-stress-field)

で表す．すべり面に沿った応力の分布は，離散化する前から未知の関数である．この分布を連続体の解析として求めるには，つり合い式だけでなく，構成則，変位の適合条件，境界条件なども要る．LEMは，ふつう，この境界値問題をすべて解く代わりに，すべり土塊を有限個のスライスやカラムに分け，それぞれの合力とつり合いを扱う．

```{note}
**連続体力学とのつながり**

静止している連続体では，各点での力のつり合いは

$$
\nabla\!\cdot\!\boldsymbol{\sigma}+\rho\boldsymbol{b}=\boldsymbol{0}
$$

と書ける．ここで $\rho\boldsymbol{b}$ は単位体積あたりの物体力で，重力だけなら $\boldsymbol{b}=\boldsymbol{g}$ である．また，偶力を考えないふつうの連続体では，角運動量のつり合いから $\boldsymbol{\sigma}=\boldsymbol{\sigma}^{\mathsf T}$ が成り立つ．

ただし，この章でこの後に使うのは，次の節のCauchyの公式 $\boldsymbol{t}=\boldsymbol{\sigma}\boldsymbol{n}$ だけである．上の2つの式は，この章の出発点が，連続体力学のどこにつながっているかを示すために載せている．
```

---

(section-2)=

## 2. 応力テンソルから表面力を取り出す

すべり面上の点 $\boldsymbol{x}$ で，外向きの単位法線ベクトルを $\boldsymbol{n}(\boldsymbol{x})$ とする．この面に働く単位面積あたりの力を，**表面力**（traction）という．表面力は，Cauchyの公式から次のように求まる．

$$
\boxed{
\boldsymbol{t}(\boldsymbol{x},\boldsymbol{n})
=
\boldsymbol{\sigma}(\boldsymbol{x})\boldsymbol{n}(\boldsymbol{x})
}
$$ (eq-start-cauchy)

応力テンソル $\boldsymbol{\sigma}$ は2階のテンソルで，ある面に働く表面力 $\boldsymbol{t}$ はベクトルである．「応力」という語は，文脈によって，テンソルも，表面力も，その成分も指す．そのため，この章ではこれらを区別して書く．

```{figure} ./figures/fig_c01_stress_to_traction.svg
:name: fig-c01-stress-to-traction
:alt: 1つの点の応力を表す要素と，同じ点を向きの違う2つの面で切ったときに，それぞれの面に働く表面力

点の応力テンソルと，向きの違う2つの面に働く表面力 $\boldsymbol{t}=\boldsymbol{\sigma}\boldsymbol{n}$．面の向きが変わると，表面力の向きと大きさも変わる
```

---

(section-3)=

## 3. 表面力の法線成分とせん断成分

表面力の法線成分を，符号を含めて次のように書く．

$$
t_n
=
\boldsymbol{n}^{\mathsf T}\boldsymbol{t}
=
\boldsymbol{n}^{\mathsf T}\boldsymbol{\sigma}\boldsymbol{n}
$$ (eq-start-normal-component)

引張を正とする符号規約では，圧縮を受けると $t_n<0$ になる．そこで，地盤工学で使う，圧縮を正とする**垂直応力** $\sigma_n$ を，次のように定める．

$$
\boxed{
\sigma_n=-t_n
=
-\boldsymbol{n}^{\mathsf T}\boldsymbol{\sigma}\boldsymbol{n}
}
$$ (eq-start-sigma-n)

圧縮を受けていれば，$\sigma_n\ge 0$ である．土が引張を受けるときや，有効垂直応力が負になるときの扱いは，[第3章](lem-in-practice-mechanical-perspective.md)で数値上の注意点として扱う．

表面力は，法線成分と，接平面内のせん断成分に，一意に分けられる．

$$
\boxed{
\boldsymbol{t}
=
-\sigma_n\boldsymbol{n}+\boldsymbol{\tau}
}
$$ (eq-start-traction-split)

ここで，せん断成分 $\boldsymbol{\tau}$ は，次の式を満たす．

$$
\boldsymbol{\tau}\cdot\boldsymbol{n}=0
$$ (eq-start-tau-tangential)

:::{dropdown} 補足B：法線成分とせん断成分への分解と，射影行列
$\|\boldsymbol{n}\|=1$ とする．法線方向に射影する行列と，接平面に射影する行列は，次のとおりである．

$$
\boldsymbol{P}_n=\boldsymbol{n}\boldsymbol{n}^{\mathsf T},
\qquad
\boldsymbol{P}_t=\boldsymbol{I}-\boldsymbol{n}\boldsymbol{n}^{\mathsf T}
$$

表面力のうち，法線方向のベクトル成分は

$$
\begin{aligned}
\boldsymbol{t}_n
&=(\boldsymbol{n}^{\mathsf T}\boldsymbol{t})\boldsymbol{n}\\
&=\boldsymbol{n}\boldsymbol{n}^{\mathsf T}\boldsymbol{t}\\
&=\boldsymbol{P}_n\boldsymbol{t}
\end{aligned}
$$

で，せん断成分は

$$
\begin{aligned}
\boldsymbol{\tau}
&=\boldsymbol{t}-\boldsymbol{t}_n\\
&=(\boldsymbol{I}-\boldsymbol{n}\boldsymbol{n}^{\mathsf T})\boldsymbol{t}\\
&=(\boldsymbol{I}-\boldsymbol{n}\boldsymbol{n}^{\mathsf T})
\boldsymbol{\sigma}\boldsymbol{n}
\end{aligned}
$$

である．

$$
\boldsymbol{n}^{\mathsf T}\boldsymbol{\tau}=0
$$

が成り立つので，$\boldsymbol{\tau}$ は接平面内にある．引張を正とする符号規約では，$\boldsymbol{t}_n=t_n\boldsymbol{n}=-\sigma_n\boldsymbol{n}$ である．
:::

2次元では，接線の方向は，向き（符号）を除いて1つに決まる．一方，3次元の接平面内には，方向が無数にある．そのため，接平面の基底と，実際に仮定する局所的なすべり方向を区別しなければならない．この章では，

$$
\|\boldsymbol{m}\|=1,
\qquad
\boldsymbol{m}\cdot\boldsymbol{n}=0
$$ (eq-start-slip-direction)

を満たす $\boldsymbol{m}$ を，局所的なすべり方向として仮定する．すべりに抵抗するせん断成分は，次のように書く．

$$
\boxed{
\boldsymbol{\tau}_m=-\tau_m\boldsymbol{m}
}
$$ (eq-start-shear-traction)

:::{dropdown} 補足C：3次元での接平面の基底と，仮定した局所的なすべり方向
3次元の接平面は

$$
\left\{
\boldsymbol{v}\mid \boldsymbol{v}\cdot\boldsymbol{n}=0
\right\}
$$

である．直交する接線の基底 $\boldsymbol{t}_1,\boldsymbol{t}_2$ を使えば，接平面内のどのベクトルも

$$
\boldsymbol{v}=a\boldsymbol{t}_1+b\boldsymbol{t}_2
$$

と書ける．つまり，$\boldsymbol{n}$ だけでは $\boldsymbol{m}$ は決まらない．

例えば，土塊全体が動く方向 $\boldsymbol{d}$ を仮定し，それを各点の接平面に射影する方法がある．射影したベクトルを

$$
\boldsymbol{d}_{\mathrm{tan}}
=
(\boldsymbol{I}-\boldsymbol{n}\boldsymbol{n}^{\mathsf T})\boldsymbol{d}
$$

とし，$\boldsymbol{d}_{\mathrm{tan}}\ne\boldsymbol{0}$ のとき，

$$
\boxed{
\boldsymbol{m}
=
\frac{\boldsymbol{d}_{\mathrm{tan}}}
{\|\boldsymbol{d}_{\mathrm{tan}}\|}
}
$$

と定める．ただし，これは選び方の一例にすぎない．3次元のLEMでは，局所的なすべり方向の仮定や，せん断抵抗を射影する方法が，手法によって違うことがある．
:::

---

(section-4)=

## 4. 全応力から有効応力へ

飽和した土に，Terzaghiの有効応力の原理を当てはめる．圧縮を正とする全応力のテンソルを $\boldsymbol{\sigma}^{(c)}=-\boldsymbol{\sigma}$ とすると，有効応力のテンソルは次のようになる．

$$
\boxed{
\boldsymbol{\sigma}'^{(c)}
=
\boldsymbol{\sigma}^{(c)}-u\boldsymbol{I}
}
$$ (eq-start-effective-tensor)

これをすべり面の法線方向に射影すると，**有効垂直応力**が求まる．

$$
\boxed{
\sigma_n'
=
\sigma_n-u
}
$$ (eq-start-effective-normal)

つまり，「有効応力」はもともとテンソル全体を指し，$\sigma_n'$ は，ある1つの面についての有効応力の垂直成分である．間隙水圧は等方的に働くので，表面力のせん断成分を直接は変えない．

:::{dropdown} 補足D：有効応力のテンソルから有効垂直応力を求める
圧縮を正とする全応力のテンソルについて，

$$
\boldsymbol{\sigma}'^{(c)}
=
\boldsymbol{\sigma}^{(c)}-u\boldsymbol{I}
$$

とする．これを単位法線ベクトル $\boldsymbol{n}$ の方向に射影すると，次のようになる．

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

また，補足Aのとおり，実際の表面力は $\boldsymbol{t}=-\boldsymbol{\sigma}^{(c)}\boldsymbol{n}$ である．これに $\boldsymbol{\sigma}^{(c)}=\boldsymbol{\sigma}'^{(c)}+u\boldsymbol{I}$ を入れると，$u\boldsymbol{I}$ の部分による表面力は

$$
-u\boldsymbol{I}\boldsymbol{n}=-u\boldsymbol{n}
$$

になる．この表面力は，いつも $-\boldsymbol{n}$ の向き，つまりすべり土塊を押す向きに働く．そのため，等方的な間隙水圧は，接平面内のせん断成分をもたない．
:::

```{figure} ./figures/fig_c02_normal_shear_effective.svg
:name: fig-c02-normal-shear-effective
:alt: 表面力を法線成分とせん断成分の和に分けた図と，垂直応力が有効垂直応力と間隙水圧の和になることを示す図

左：表面力 $\boldsymbol{t}$ は，法線成分 $-\sigma_n\boldsymbol{n}$ とせん断成分 $\boldsymbol{\tau}$ の和．右：垂直応力 $\sigma_n$ は，有効垂直応力 $\sigma_n'$ と間隙水圧 $u$ の和．数値は6節の例
```

---

(section-5)=

## 5. Mohr–Coulomb則によるせん断強度

有効応力で表したMohr–Coulomb則では，今の有効垂直応力 $\sigma_n'$ のもとで発揮できる**せん断強度** $\tau_f$ を，次の式で表す．

$$
\boxed{
\tau_f
=
c'+\sigma_n'\tan\phi'
=
c'+(\sigma_n-u)\tan\phi'
}
$$ (eq-start-mohr-coulomb)

$\tau_f$ は，今働いているせん断応力ではなく，破壊するときに発揮できるせん断抵抗の上限である．同じ土でも，$\sigma_n'$ が増えれば粒子どうしの摩擦による抵抗が増し，$\tau_f$ は大きくなる．反対に，全垂直応力 $\sigma_n$ が同じでも，間隙水圧 $u$ が増えると，次のように $\tau_f$ は小さくなる．

$$
u\uparrow
\quad\Longrightarrow\quad
\sigma_n'\downarrow
\quad\Longrightarrow\quad
\tau_f\downarrow
$$ (eq-start-pore-pressure-effect)

---

(section-6)=

## 6. 安全率と動員せん断応力

LEMでは，発揮できるせん断強度 $\tau_f$ と，つり合いを保つために動員されているせん断応力 $\tau_m$ の比を，安全率とする．

$$
\boxed{
F_s=\frac{\tau_f}{\tau_m}
}
$$ (eq-start-fs-stress)

これを $\tau_m$ について解き，$\tau_f$ に式 {eq}`eq-start-mohr-coulomb` を入れると，次のようになる．

$$
\boxed{
\tau_m
=
\frac{c'+(\sigma_n-u)\tan\phi'}{F_s}
}
$$ (eq-start-mobilized-stress)

すべりに抵抗するせん断成分は，向きを含めたベクトルでは，次のように書ける．

$$
\boxed{
\boldsymbol{\tau}_m
=
-\frac{c'+(\sigma_n-u)\tan\phi'}{F_s}\boldsymbol{m}
}
$$ (eq-start-mobilized-vector)

```{note}
式 {eq}`eq-start-mobilized-stress` と式 {eq}`eq-start-mobilized-vector` は，今の $\tau_m$ を先に測ってから比をとる，という意味ではない．まず，せん断強度のうちどれだけが動員されているかを，未知の $F_s$ で表す．そのうえで，この表面力を受けた土塊が力とモーメントのつり合いを満たすように，$F_s$ とほかの未知の力を同時に求める．
```

```{figure} ./figures/fig_c03_strength_mobilization.svg
:name: fig-c03-strength-mobilization
:alt: 有効垂直応力とせん断応力の図に，Mohr–Coulomb則の直線と，6節の数値例の2つの状態を示した図

Mohr–Coulomb則の直線と，6節の数値例．水位が上がって $\sigma_n'$ が60 kPaから40 kPaに下がると，$\tau_f$ は44.6 kPaから33.1 kPaに，$F_s=\tau_f/\tau_m$ は1.49から1.10に下がる
```

```{admonition} 数値でたどる
ある底面で，全垂直応力 $\sigma_n=100$ kPa，間隙水圧 $u=40$ kPa，$c'=10$ kPa，$\phi'=30^\circ$ とする．このとき，

$$
\sigma_n'=100-40=60\ \text{kPa},
\qquad
\tau_f=10+60\tan 30^\circ=44.6\ \text{kPa}
$$

である．つり合いを保つのに必要なせん断応力が $\tau_m=30$ kPa なら，安全率は

$$
F_s=\frac{44.6}{30}=1.49
$$

になる．ここで水位が上がって $u=60$ kPa になり，つり合いに必要な $\tau_m$ は変わらないとする．すると，

$$
\sigma_n'=40\ \text{kPa},
\qquad
\tau_f=10+40\tan 30^\circ=33.1\ \text{kPa},
\qquad
F_s=\frac{33.1}{30}=1.10
$$

となる．土の強度定数 $c'$ と $\phi'$ は少しも変わっていないのに，安全率は1.49から1.10に下がる．つまり，5節で見た $u\uparrow\Rightarrow\tau_f\downarrow$ を，数値で確かめたことになる．
```

---

(section-7)=

## 7. 点の応力から，面積をもつ底面の合力へ

カラム $i$ の底面を $S_i$ とし，その面積を

$$
A_i=\int_{S_i}dA
$$ (eq-start-base-area)

とする．底面に働く表面力をすべて合わせた合力は，厳密に次の式で表せる．

$$
\boxed{
\boldsymbol{R}_i
=
\int_{S_i}\boldsymbol{t}\,dA
}
$$ (eq-start-resultant)

表面力のうち，圧縮の法線成分の合力と，すべりに抵抗するせん断成分の合力は，それぞれベクトルで次のように書ける．

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

$\boldsymbol{R}_i$ の式は厳密である．一方，$\boldsymbol{T}_i$ を式 {eq}`eq-start-shear-resultant` の形で書けるのは，各点のせん断成分が $-\boldsymbol{m}(\boldsymbol{x})$ の向きにそろう，つまり6節の動員の状態にあると仮定したときに限られる．この仮定のもとで，

$$
\boldsymbol{R}_i=\boldsymbol{N}_i+\boldsymbol{T}_i
$$ (eq-start-resultant-split)

が成り立つ．

曲面では，$\boldsymbol{n}$ が場所によって変わる．そのため，一般には次の不等式になる．

$$
\left\|\boldsymbol{N}_i\right\|
\le
\int_{S_i}\sigma_n\,dA
$$ (eq-start-resultant-bound)

等号が成り立つのは，底面全体で法線の方向が同じときなどに限られる．つまり，各点の垂直力の大きさをそのまま足したスカラーと，向きを考えて足したベクトルの合力の大きさは，区別しなければならない．

:::{dropdown} 補足E：曲面でのベクトルの合力とスカラーの積分
曲面 $S_i$ では，一般に $\boldsymbol{n}=\boldsymbol{n}(\boldsymbol{x})$ である．表面力の圧縮の法線成分を，ベクトルとして合わせた合力は

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

は，各点の大きさをそのまま足したスカラーである．三角不等式から，

$$
\|\boldsymbol{N}_i\|
\le
N_i^*
$$

が成り立つ．等号が成り立つのは，$\sigma_n>0$ の範囲で法線の方向が同じときなどに限られる．

底面全体で，代表の法線 $\boldsymbol{n}_i$ が一定だと仮定すると，

$$
\boldsymbol{N}_i
=
-\boldsymbol{n}_i\int_{S_i}\sigma_n\,dA
=
-N_i\boldsymbol{n}_i
$$

となる．これで，LEMで使うスカラーの $N_i$ と，ベクトルの合力が結び付く．
:::

```{figure} ./figures/fig_c04_surface_integration.svg
:name: fig-c04-surface-integration
:alt: 曲面の底面に分布する表面力，各点の垂直力をベクトルとして足した図，底面を1つの平面で表すLEMのモデル

左：曲面の底面に分布する表面力．中：各点の垂直力をベクトルとして足した合力 $\boldsymbol{N}_i$ は，大きさだけを足した $\int_{S_i}\sigma_n\,dA$ より短い．右：LEMは，底面を1つの平面と1つの向きで表し，垂直力の大きさを $N_i=\int_{S_i}\sigma_n\,dA$ とする
```

---

(section-8)=

## 8. LEMでの $N_i$，$U_i$，$T_i$

LEMでは，スライスやカラムの底面 $S_i$ が小さいとは仮定しない．その代わりに，次のように仮定する．

> **$S_i$ の中では，向き（$\boldsymbol{n},\boldsymbol{m}$）と材料定数（$c',\phi'$）を代表の値で一定とし，応力と間隙水圧は面積分した値 $N_i,U_i$ で表す．**

例えば，向きを

$$
\boldsymbol{n}(\boldsymbol{x})=\boldsymbol{n}_i,
\qquad
\boldsymbol{m}(\boldsymbol{x})=\boldsymbol{m}_i
\qquad (\boldsymbol{x}\in S_i)
$$ (eq-start-representative-direction)

とモデル化する．そして，垂直応力と間隙水圧を面積分したスカラーを，次のように定める．

$$
\boxed{
N_i=\int_{S_i}\sigma_n\,dA,
\qquad
U_i=\int_{S_i}u\,dA
}
$$ (eq-start-ni-ui)

このとき，すべり土塊に働く垂直力の合力は，ベクトルで次のように書ける．

$$
\boxed{
\boldsymbol{N}_i=-N_i\boldsymbol{n}_i
}
$$ (eq-start-ni-vector)

さらに，$\sigma_n$ と $u$ まで代表の値で一定だと仮定すれば，

$$
N_i=\sigma_{n,i}A_i,
\qquad
U_i=u_iA_i
$$ (eq-start-ni-uniform)

である．

```{note}
文献で $\boldsymbol{N}_i=N_i\boldsymbol{n}_i$ と書いてあるときは，法線の向きについて別の規約を使っている．例えば，$\boldsymbol{n}_i$ を，垂直力が働く向きにとっている．
```

一方，$S_i$ の中で $c_i'$，$\phi_i'$ が一定だとする．Mohr–Coulomb則を面積分すると，発揮できるせん断強度の合力の大きさは，次のようになる．

$$
\boxed{
T_{f,i}
=
c_i'A_i+(N_i-U_i)\tan\phi_i'
}
$$ (eq-start-base-strength)

さらに，$F_s$ がすべり面全体で共通だとすると，動員されているせん断力の大きさは

$$
\boxed{
T_i
=
\frac{c_i'A_i+(N_i-U_i)\tan\phi_i'}{F_s}
}
$$ (eq-start-base-shear)

になる．$\boldsymbol{m}_i$ が底面の中で一定なら，すべりに抵抗する向きを含めたベクトルは，次のとおりである．

$$
\boxed{
\boldsymbol{T}_i=-T_i\boldsymbol{m}_i
}
$$ (eq-start-base-shear-vector)

なお，スカラーの式 $T_{f,i}=c_i'A_i+(N_i-U_i)\tan\phi_i'$ を得るのに，$\sigma_n$ と $u$ の分布まで一定である必要はない．$c_i'$ と $\phi_i'$ が一定で，$N_i$ と $U_i$ を式 {eq}`eq-start-ni-ui` の積分で定めれば，式 {eq}`eq-start-base-strength` は成り立つ．

:::{dropdown} 補足F：Mohr–Coulomb則の面積分
底面 $S_i$ で，$c_i'$ と $\phi_i'$ が一定だとする．発揮できるせん断強度の合力の大きさは，次のように求まる．

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

途中で $\sigma_n$ と $u$ を一定とおいていないので，このスカラーの式は，$\sigma_n$ と $u$ が底面の中で分布していても成り立つ．さらに，$F_s$ が底面で一定だとする（共通の安全率の仮定）と，

$$
T_i
=
\int_{S_i}\frac{\tau_f}{F_s}\,dA
=
\frac{T_{f,i}}{F_s}
$$

となる．

ベクトルの式 $\boldsymbol{T}_i=-T_i\boldsymbol{m}_i$ まで簡単にするには，すべりに抵抗する向き $\boldsymbol{m}$ も，$S_i$ の中で一定だと仮定しなければならない．
:::

```{note}
実務のLEMでは，$A_i$ が小さいとは限らない．そのため，「$S_i$ が十分小さいので一定とみなせる」という数値積分の説明より，「底面ごとに向きと材料定数を代表の値で一定とし，応力は積分した値で表す」という説明のほうが，実務に合う．この仮定には，曲面の底面を1つの平面と1つの向きで代表させる，幾何学的な近似も含まれる．
```

:::{dropdown} 補足G：「底面が十分小さい」と「代表の値で一定」の違い
次の2つは，意味が違う．

1. **数値積分としての説明**：$S_i$ を十分小さくすれば，連続な量の変化が小さくなり，代表の値で積分を近似した結果がよくなる
2. **LEMのモデルの仮定**：$S_i$ が大きくても小さくても，その底面を，代表の法線，代表のすべり方向，代表の材料定数などで表す

実務のLEMでは，$A_i$ が小さいとは限らない．そのため，本文では後者で説明している．例えば，$S_i$ の中のモデルの仮定として

$$
\boldsymbol{n}(\boldsymbol{x})=\boldsymbol{n}_i,
\qquad
\sigma_n(\boldsymbol{x})=\sigma_{n,i}
$$

を置くと，

$$
\boldsymbol{N}_i
=
-\int_{S_i}\sigma_{n,i}\boldsymbol{n}_i\,dA
=
-\sigma_{n,i}A_i\boldsymbol{n}_i
$$

は，そのモデルの中では厳密に成り立つ．ただし，実際の曲面での向きや応力の分布に対しては，近似である．

カラムを細かく分ければ，形や積分の近似はよくなることがある．しかし，それだけでは，スライス間力についての仮定のような，LEMに固有の力学的な仮定はなくならない．
:::

---

(section-9)=

## 9. つり合い式と，LEMに固有の未知量の決め方

次の式を得ても，$N_i$，$T_i$，$F_s$ と，{term}`スライス間力`やカラム間力は，まだ分からない．

$$
T_i
=
\frac{c_i'A_i+(N_i-U_i)\tan\phi_i'}{F_s}
$$ (eq-start-strength-law-recap)

カラム $i$ に働く自重を $\boldsymbol{W}_i$，そのほかの既知の外力を $\boldsymbol{P}_i$，隣のカラム $j$ から受ける力を $\boldsymbol{Q}_{ij}$ とする．すると，力のつり合いは，模式的に次のように書ける．

$$
\boxed{
\boldsymbol{W}_i+\boldsymbol{P}_i
-N_i\boldsymbol{n}_i
-T_i\boldsymbol{m}_i
+\sum_j\boldsymbol{Q}_{ij}
=\boldsymbol{0}
}
$$ (eq-start-force-balance)

また，任意の基準点 $O$ のまわりのモーメントのつり合いは，次のとおりである．

$$
\boxed{
\sum_k
\boldsymbol{r}_k\times\boldsymbol{F}_k
=\boldsymbol{0}
}
$$ (eq-start-moment-balance)

LEMでは，これらの力とモーメントのつり合い式，強度の動員を表す式，手法ごとに加える仮定を組み合わせて，$F_s$ と各合力を求める．加える仮定には，例えば，スライス間のせん断力を無視する，スライス間力の向きや関係を仮定する，満たすつり合い式を一部に限る，といったものがある．Bishop，Janbu，Spencerなどの手法の違いは，この未知量の決め方の違いである．

つまり，LEMの離散化は，新しい未知量を生む操作ではない．もともと分からなかった連続的な応力の分布を，有限個の未知の合力に置き換える操作である．また，底面の面積分を有限個の量で表すことと，つり合い式だけでは足りない未知量を仮定で決めることは，別の問題である．

:::{dropdown} 補足H：離散化と，未知量の決め方
すべり面での

$$
\sigma_n(\boldsymbol{x}),
\qquad
\boldsymbol{\tau}(\boldsymbol{x})
$$

は，離散化する前から未知の連続な分布である．LEMの離散化は，これらを，各底面の

$$
N_i,
\qquad
T_i
$$

という有限個の未知の合力に置き換える．

しかし，離散化しただけでは，$N_i$ やスライス間力は決まらない．一般に，未知数の数が，独立なつり合い式の数より多いからである．そのため，次の2段階を区別しなければならない．

- **空間の離散化**：連続的な形，荷重，応力の分布を，有限個のスライスやカラムと合力で表す
- **不静定性の解消**（closure）：未知の合力を決められるように，スライス間力の向き，比，無視する成分などについて，手法ごとの仮定を加える．詳しくは第2章で扱う

```{note}
「応力が分からないので，細かく分ければ自動的に求まる」のではない．未知の連続分布を有限個の未知量に置き換えてから，つり合い式，強度の動員を表す式，加えた仮定を連立させて，$F_s$ と合力を求める．
```
:::

ここまでの流れをまとめると，次のようになる．

$$
\boxed{
\begin{array}{c}
\text{連続体の応力場と各点のつり合い}\\[1mm]
\boldsymbol{\sigma},\quad
\nabla\!\cdot\!\boldsymbol{\sigma}+\rho\boldsymbol{b}=\boldsymbol{0}
\\[2mm]
\downarrow\\[2mm]
\text{すべり面上の表面力}\\[1mm]
\boldsymbol{t}=\boldsymbol{\sigma}\boldsymbol{n}
\\[2mm]
\downarrow\\[2mm]
\text{法線成分とせん断成分に分ける}\\[1mm]
\sigma_n,\quad\boldsymbol{\tau}
\\[2mm]
\downarrow\quad\text{有効応力}\\[2mm]
\sigma_n'=\sigma_n-u
\\[2mm]
\downarrow\quad\text{Mohr--Coulomb則}\\[2mm]
\tau_f=c'+\sigma_n'\tan\phi'
\\[2mm]
\downarrow\quad\text{安全率}\\[2mm]
\tau_m=\tau_f/F_s
\\[2mm]
\downarrow\quad\text{面積分と，底面ごとのモデル化}\\[2mm]
N_i,\quad U_i,\quad T_i
\\[2mm]
\downarrow\quad\text{つり合い式と，LEMに固有の仮定}\\[2mm]
F_s\ \text{と各合力}
\end{array}
}
$$ (eq-start-summary)

---

## 確認問題

答えは問題をクリックすると開く．

:::{dropdown} 問1　応力テンソルと，ある面に働く表面力は，何が違うか
:icon: question

応力テンソル $\boldsymbol{\sigma}$ は，1つの点の応力の状態を表す2階のテンソルで，面を決めなくても定まる．一方，表面力 $\boldsymbol{t}$ は，法線が $\boldsymbol{n}$ の面に働く単位面積あたりの力のベクトルで，$\boldsymbol{t}=\boldsymbol{\sigma}\boldsymbol{n}$ のように，面の向きを決めて初めて求まる．同じ点でも，面の向きが変われば，表面力も変わる．（→[2節](#section-2)）
:::

:::{dropdown} 問2　有効垂直応力 $\sigma_n'$ は，全垂直応力と間隙水圧からどう決まるか
:icon: question

全垂直応力から間隙水圧を引いた，$\sigma_n'=\sigma_n-u$ で決まる．有効応力のテンソル $\boldsymbol{\sigma}'^{(c)}=\boldsymbol{\sigma}^{(c)}-u\boldsymbol{I}$ を，面の法線方向に射影すると得られる．（→[4節](#section-4)）
:::

:::{dropdown} 問3　Mohr–Coulomb則で求める $\tau_f$ は，今働いているせん断応力か，それとも別のものか
:icon: question

別のものである．$\tau_f$ は，今の有効垂直応力のもとで，破壊するときに発揮できるせん断抵抗の上限を表す．今働いているのは動員せん断応力 $\tau_m$ で，安定な斜面では $\tau_f$ より小さい．（→[5節](#section-5)，[6節](#section-6)）
:::

:::{dropdown} 問4　安全率 $F_s$ は，何と何の比として導入したか
:icon: question

発揮できるせん断強度 $\tau_f$ と，つり合いを保つために動員されているせん断応力 $\tau_m$ の比 $F_s=\tau_f/\tau_m$ である．教科書では抵抗力と滑動力の比として説明することもあるが，比をとる対象は手法によって違う．例えば簡易Bishop法は，円弧の中心まわりのモーメントの比をとる．（→[6節](#section-6)）
:::

:::{dropdown} 問5　$N_i$，$U_i$，$T_i$ は，点ごとの応力にどのような操作をして作ったか
:icon: question

底面 $S_i$ にわたって面積分した．$N_i$ は全垂直応力 $\sigma_n$ を，$U_i$ は間隙水圧 $u$ を，面積分した値である．$T_i$ は，$c_i'$ と $\phi_i'$ を底面で一定としてMohr–Coulomb則を面積分し，共通の安全率 $F_s$ で割って求めた．（→[7節](#section-7)，[8節](#section-8)）
:::

:::{dropdown} 問6　底面 $S_i$ で一定と仮定しなければならないのはどの量で，一定でなくてよいのはどの量か
:icon: question

スカラーの式 $T_{f,i}=c_i'A_i+(N_i-U_i)\tan\phi_i'$ を得るには，材料定数 $c_i'$ と $\phi_i'$ を一定と仮定する．一方，$\sigma_n$ と $u$ は，底面の中で分布していてよい．$T_i=T_{f,i}/F_s$ には，$F_s$ が底面で共通だという仮定も要る．ベクトルの式 $\boldsymbol{N}_i=-N_i\boldsymbol{n}_i$ と $\boldsymbol{T}_i=-T_i\boldsymbol{m}_i$ にするには，それぞれ $\boldsymbol{n}$ と $\boldsymbol{m}$ も一定と仮定する．（→[8節](#section-8)）
:::

:::{dropdown} 問7　8節の $T_i$ の式を得ても，まだ分からないものは何か
:icon: question

底面垂直力 $N_i$，安全率 $F_s$，スライス間力やカラム間力である．$T_i$ は，$N_i$ と $F_s$ が決まれば求まる．これらを決めるには，つり合い式に加えて，手法ごとの仮定が要る．（→[9節](#section-9)）
:::

:::{dropdown} 問8（計算してみよう）　6節の「数値でたどる」の底面で，間隙水圧が $u=20$ kPa に下がったとする．せん断強度 $\tau_f$ と安全率 $F_s$ を求めよ
:icon: question

$\sigma_n'=100-20=80$ kPa なので，$\tau_f=10+80\tan 30^\circ=56.2$ kPa である．$\tau_m=30$ kPa はそのままとすると，$F_s=56.2/30=1.87$ になる．間隙水圧が下がると，有効垂直応力が増え，安全率も上がる．（→[6節](#section-6)）
:::

---

## 次に読む

ここまでで，連続体の応力から，LEMで使う底面の合力と，強度の動員を表す式にたどり着いた．しかし，$N_i$，$F_s$，スライス間力やカラム間力は，まだ決まっていない．各手法がこれらを決めるためにどのような仮定を用いるかは，[第2章「極限平衡法とは何か」](what-is-limit-equilibrium-method.md)で扱う．
