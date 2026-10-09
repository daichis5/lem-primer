---
title: "スライス法で円弧すべりの安全率を計算する：4つの手法を実装し，1つの枠組みでつり合いを確認する"
lang: ja
series: "practice 2 of 3"
---

# スライス法で円弧すべりの安全率を計算する

**4つの手法を実装し，1つの枠組みでつり合いを確認する**

この実践では，第1章の {numref}`fig-c00-slope-overview` の斜面と円弧について，2次元のスライス法で安全率を求めるコードを作成する．まずスライスの表を作り，Fellenius法，簡易Bishop法，簡易Janbu法を，教科書の式のとおりに実装する．続いて，スライス間力の傾きを変数にした1つの枠組みを作る．この枠組みで，簡易Bishop法と簡易Janbu法がその特別な場合になることと，Spencer法が力とモーメントのつり合いをともに満たすことを，残差で確認する．最後に，円弧以外のすべり面で，モーメントの中心の選択が安全率を変えることを見る．

この実践は，[第2章](what-is-limit-equilibrium-method.md)と[第3章](lem-in-practice-mechanical-perspective.md)を読み，[実践1](practice-infinite-slope.md)を終えた前提で進める．用語と記号は，[用語集](lem-glossary.md)にまとめている．

(slices-goal)=

## 作るもの

斜面は，第1章の {numref}`fig-c00-slope-overview` と同じである．のり尻が $x=0$，のり肩が $x=15$ m にあり，高さは10 m（勾配1:1.5）で，のり肩より右は平らに続く．{term}`すべり面`は，中心が $(6, 18)$，半径が19.31 m の円弧である．この円弧は，のり尻の左の $x=-1$ m で地表に出て，のり肩より右の $x=23.58$ m で地表に入る．土は[実践1](practice-infinite-slope.md)と同じく，$\gamma=18$ kN/m³，$c'=10$ kPa，$\phi'=30^\circ$ とし，5節の後半で地下水位を置くほかは，乾いた斜面とする．そのうえで，この円弧の{term}`安全率`を，4つの手法で求める．

```{figure} ./figures/fig_c00_slope_overview.svg
:name: fig-slices-slope-overview
:alt: 斜面に仮定した円弧のすべり面，すべり土塊，6つのスライスと，1つのスライスにはたらく自重・垂直力・せん断力

この実践で計算する斜面と円弧

土塊は左へすべる．図の6本のスライスで，1節の表を作る．
```

座標と向きは，実践1と同じである．$x$ を水平右向き，$z$ を鉛直上向きにとり，底面の単位法線ベクトル $\boldsymbol{n}_i$ は{term}`すべり土塊`の外向きにとる．すべる向きの単位ベクトルは $\boldsymbol{m}_i$ である．長さはm，力は奥行き1 mあたりのkN（kN/m）で表す．作るものは，次のとおりである．

| 関数とクラス | 求めるもの | 節 |
|---|---|---|
| `ground`，`Circle`，`Slices`，`make_slices` | 地表，円弧のすべり面，スライスの表 | 1節 |
| `cross` | 2次元のベクトルの外積 | 1節 |
| `fellenius`，`bishop`，`janbu` | 3つの手法の，教科書の式による安全率 | 2節 |
| `base_forces`，`residuals` | 傾き $\theta$ のスライス間力のもとでの底面の力と，つり合いの残差 | 3節 |
| `secant`，`fs_moment`，`fs_force` | 割線法と，モーメントまたは力の残差を0にする安全率 | 3節 |
| `spencer` | 力とモーメントの残差をともに0にする安全率と $\theta$ | 4節 |
| `Line` | 平面のすべり面 | 6節 |
| `Ellipse`，`fellenius_about` | 楕円のすべり面と，任意の点まわりのモーメントで求めた，Fellenius法の安全率 | 7節 |

(slices-setup)=

## 準備

[実践1](practice-infinite-slope.md)で作ったフォルダ `lem-practice` を使う．この実践のコードは，{download}`slices.py <examples/slices.py>` と {download}`test_slices.py <examples/test_slices.py>` にまとめてある．なお，テストと6節では実践1の `infinite_slope.py` を読み込むので，実践1から始めていないときは，{download}`infinite_slope.py <examples/infinite_slope.py>` も同じフォルダに置く．

---

(slices-section-1)=

## 1. スライスの表を作る

すべり面を $n$ 本の等幅の{term}`スライス`に分割し，各スライスの底面を，幅の中央の点と，そこでの接線で代表させる．[第1章 8節](#section-8)の言い方なら，底面ごとに向きを代表の値で一定とする仮定である．底面の傾き $\alpha_i$ は右上がりを正とし，正の $\alpha_i$ の底面は，土塊を左へすべらせる．このとき，法線とすべる向きは，実践1の式と同じ形になる．

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

幅を $b_i$ とすると，底面の長さは $l_i=b_i/\cos\alpha_i$ である．重さ $W_i$ は，幅の中央で測った柱の高さに $\gamma b_i$ を掛けて求める．`slices.py` を作り，最初に，斜面の地表と円弧のすべり面を実装する．

```{literalinclude} examples/slices.py
:language: python
:end-at: return np.clip
```

```{literalinclude} examples/slices.py
:language: python
:pyobject: Circle
```

次に，スライスの表を実装する．どの量も，左のスライスから順に並べたNumPyの配列にする．`@dataclass` は，名前の付いた入れ物を短く記述する記法である．

```{literalinclude} examples/slices.py
:language: python
:pyobject: Slices
```

```{literalinclude} examples/slices.py
:language: python
:pyobject: make_slices
```

地下水位 `water_level` を与えたときは，底面の{term}`間隙水圧`を，地下水位から鉛直に測った深さの静水圧とする．これは，実践1の `pore_pressure` の `"vertical"` と同じ算定方法である．地下水位が地表より高いところでは，地下水位を地表に合わせ，地表の上の水は考えない．土の単位体積重量は，地下水位より下でも $\gamma$ のままとする．5節で，間隙水圧の影響だけを取り出すためである．

{numref}`fig-slices-slope-overview` の6本で表を作ると，次のようになる．この実践に載せている出力は，7節の終わりで実行する `run_slices.py` のものである．

```{literalinclude} examples/output/run_slices.txt
:language: text
:start-at: 1. slice table
:end-before: 2. factor of safety
```

3本目のスライスを手で確認する．表より1桁細かく表記すると，幅は $b=4.0964$ m，幅の中央は $x=9.241$ m である．地表の高さは $9.241\times10/15=6.161$ m，円弧の高さは $-1.039$ m なので，$W=18\times4.0964\times(6.161+1.039)=530.9$ kN/m になる．傾きは，$\tan\alpha=(9.241-6)/(18+1.039)=0.170$ から $9.66^\circ$ である．

最後の行は，円の中心から各底面の点への位置ベクトル $\boldsymbol{r}_i$ と，法線 $\boldsymbol{n}_i$ の外積の大きさが，どの底面でも $10^{-12}$ m より小さいことを示す．丸め誤差の大きさしかないので，{term}`底面垂直力`の作用線は，どれも中心を通っている．これは，[第3章 2節](#practice-section-2)で見た，円弧に特有の性質である．この2つを，テストとして実装する．`test_slices.py` を作り，次を記述する．

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

`cross` は，2次元のベクトルの外積を求める関数で，3節と7節でも使う．`slices.py` に追加しておく．

```{literalinclude} examples/slices.py
:language: python
:pyobject: cross
```

---

(slices-section-2)=

## 2. 3つの式を実装する

[第2章 4節](#what-section-4)で見た，{term}`つり合いの一部だけを満たす方法`の3つを，教科書の式のとおりに実装する．どれも，スライス間のせん断力を無視するか，簡略化する方法である．Fellenius法（簡便分割法）は，{term}`スライス間力`の効果をすべて無視し，円弧の中心まわりのモーメントの比をとる．

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

ここで，$U_i=u_il_i$ は{term}`底面の間隙水圧の合力`である．簡易Bishop法（Bishop, 1955）は，各スライスの鉛直方向の力のつり合いから $N_i$ を求め，円弧の中心まわりのモーメントの比をとる．右辺にも $F_s$ が現れるので，反復して求める．

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

補正係数を掛けない簡易Janbu法（Janbu, 1973）は，同じ $N_i$ を使い，全体の水平方向の力のつり合いから $F_s$ を求める．

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

3つを，`fellenius(s)`，`bishop(s)`，`janbu(s)` という関数にする．`s` は1節のスライスの表である．`fellenius` には，5節で使うキーワード引数 `effective_weight` も付け，`True` のときは，有効垂直力を，$W_i\cos\alpha_i-u_il_i$ の代わりに $(W_i-u_ib_i)\cos\alpha_i$ とする．反復では，前の $F_s$ で右辺を計算し，値の変化が十分小さくなったら止める．$m_{\alpha,i}$ が0以下のスライスでは，$N_i$ が無限大になるか，符号が逆になって，意味をもたない．そのため，そのときは計算を止めて知らせる．実装したら，次のテストで確認する．

```{literalinclude} examples/test_slices.py
:language: python
:pyobject: test_the_three_formulas_on_the_circle_of_figure_1
```

:::{dropdown} 実装の例
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

分割数を変えた値は，5節の表にまとめる．$n=50$ では，Fellenius法が1.888，簡易Bishop法が2.063，簡易Janbu法が1.868になる．

---

(slices-section-3)=

## 3. スライス間力の傾きを変数にして，1つの枠組みにまとめる

2節の3つの式は，手法ごとに別々に導出されたように見える．しかし，[第2章 3.3節](#what-section-3-3)で見たように，手法の違いは{term}`不静定性の解消`（closure）の仕方の違いである．Fredlund and Krahn (1977)は，この見方で2次元の各手法を1つの枠組みにまとめ，比較した．そこで，この実践でも，[第2章 5.1節](#what-section-5-1)のSpencer法の仮定を，変数のまま使う．各スライスにはたらくスライス間力の合力 $Q_i$ が，どのスライスでも同じ向き

$$
\boldsymbol{d}=
\begin{bmatrix}
\cos\theta\\
\sin\theta
\end{bmatrix}
$$ (eq-slices-direction)

をもつとする．$\theta$ は，水平からはかった合力の傾きである．

スライス $i$ にはたらく力は，自重 $W_i$，底面の垂直力 $-N_i\boldsymbol{n}_i$，{term}`底面のせん断力 <底面せん断力>` $T_i\boldsymbol{e}_i$，スライス間力の合力 $Q_i\boldsymbol{d}$ である．ここで $\boldsymbol{e}_i=-\boldsymbol{m}_i$ は，すべりに抵抗する向きを表す．$T_i$ は，[第1章 8節](#section-8)の強度の動員を表す式で $N_i$ と結び付く．

$$
T_i=\frac{c_i'l_i+(N_i-U_i)\tan\phi_i'}{F_s}
$$ (eq-slices-shear)

$\boldsymbol{d}$ に直交する向き $\boldsymbol{p}=(-\sin\theta,\ \cos\theta)$ で力のつり合いをとると，$Q_i$ が式から消える．これを $N_i$ について解くと，次のようになる．

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

$\theta=0$ なら $\boldsymbol{p}$ は鉛直上向きで，$D_i$ は式 {eq}`eq-slices-bishop` の $m_{\alpha,i}$ に一致する．つまり，式 {eq}`eq-slices-normal` は，簡易Bishop法の $N_i$ を，傾いたスライス間力に拡張したものである．一方，各スライスの $\boldsymbol{d}$ を底面に平行にとる（$\theta$ をスライスごとに $\alpha_i$ とする）と，$D_i=1$ で，$N_i=W_i\cos\alpha_i$ になる．これはFellenius法の $N_i$ である．$\theta$ がスライスごとに異なるので，Fellenius法は，全スライスで共通の $\theta$ を使うこの枠組みには入らない．

```{literalinclude} examples/slices.py
:language: python
:pyobject: base_forces
```

もう1つの向き $\boldsymbol{d}$ のつり合いからは，$Q_i$ が得られる．スライス間力は{term}`内力`なので，土塊全体では打ち消し合う．そのため，土塊全体の力のつり合いは，$\sum_i Q_i=0$ と同じになる．この表では，自重も，底面の代表点を通る鉛直線上にはたらくとする．すると，スライス $i$ の自重と底面の力の，点 $O$ のまわりのモーメントの和は，$-\boldsymbol{r}_i\times Q_i\boldsymbol{d}$ になる．ここで $\boldsymbol{r}_i$ は，$O$ から底面の代表点への位置ベクトルである．つまり，$O$ のまわりのモーメントのつり合いは，$\sum_i \boldsymbol{r}_i\times Q_i\boldsymbol{d}=\boldsymbol{0}$ と同じになる．この2つの和を，力の残差とモーメントの残差と呼ぶ．

```{literalinclude} examples/slices.py
:language: python
:pyobject: residuals
```

$\theta$ を固定すれば，残差は $F_s$ だけの関数になる．モーメントの残差を0にする $F_s$ を $F_m(\theta)$，力の残差を0にする $F_s$ を $F_f(\theta)$ と表記する．どちらも，割線法で求める．割線法は，2点を通る直線が0になる点を次の点とする反復で，ニュートン法の微分を差分に置き換えたものにあたる．

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

$\theta=0$ で，2節の式と比較する．

```{literalinclude} examples/output/run_slices.txt
:language: text
:start-at: 3. one framework
:end-before: 4. F_m and F_f
```

$F_m(0)$ は簡易Bishop法と，$F_f(0)$ は補正係数を掛けない簡易Janbu法と，6桁まで一致する．$\theta=0$ の枠組みは，スライス間力を水平とし，各スライスの鉛直方向のつり合いで $N_i$ を決定する．そのうえで，簡易Bishop法は全体のモーメントのつり合いを，簡易Janbu法は全体の水平方向の力のつり合いを満たす．2つの手法の違いは，満たす全体のつり合いの違いだけである．これを，テストに追加する．

```{literalinclude} examples/test_slices.py
:language: python
:pyobject: test_theta_zero_gives_simplified_bishop_and_janbu
```

---

(slices-section-4)=

## 4. Spencer法：力とモーメントのつり合いをともに満たす

$\theta$ を変えながら，$F_m(\theta)$ と $F_f(\theta)$ を求める．

```{literalinclude} examples/output/run_slices.txt
:language: text
:start-at: 4. F_m and F_f
:end-before: 5. water table
```

```{figure} ./figures/fig_e2_theta_curves.svg
:name: fig-e2-theta-curves
:alt: スライス間力の合力の傾きを横軸に，モーメントのつり合いと力のつり合いから求めた安全率を描いた2本の曲線と，簡易Bishop法，簡易Janbu法，Spencer法の点

スライス間力の合力の傾き $\theta$ と，2つのつり合いから求めた安全率
```

2本の曲線が交わる点では，同じ $F_s$ と $\theta$ で，力とモーメントの残差がともに0になる．これが，[第2章 5.1節](#what-section-5-1)のSpencer法（Spencer, 1967）の解である．交点は，$F_m(\theta)-F_f(\theta)=0$ を，$\theta$ について割線法で解けば得られる．`spencer(s, center)` を実装し，テストで確認する．

```{literalinclude} examples/test_slices.py
:language: python
:pyobject: test_spencer_satisfies_both_force_and_moment_equilibrium
```

:::{dropdown} 実装の例
```{literalinclude} examples/slices.py
:language: python
:pyobject: spencer
```
:::

交点は $\theta=18.27^\circ$，$F_s=2.059$ である．図を見ると，$F_m$ は $\theta$ を変えてもほとんど変わらず，$F_f$ は大きく変わる．[第3章 2節](#practice-section-2)で見たように，円弧では，モーメントのつり合いがスライス間力の仮定の影響を受けにくいからである．円弧の中心まわりでは，底面垂直力のモーメントが0で，せん断力の腕はどれも半径なので，$\theta$ は $N_i\tan\phi_i'$ を通してしか $F_m$ に入らない．そのため，簡易Bishop法（2.063）とSpencer法（2.059）が近くなる．一方，力のつり合いだけを使う簡易Janbu法（1.868）は，Spencer法から離れる．スライス間力の効果をすべて無視するFellenius法（1.888）も，小さめの値になる．

---

(slices-section-5)=

## 5. 分割数と地下水位を変える

分割数 $n$ を変えると，4つの手法の値は次のようになる．

```{literalinclude} examples/output/run_slices.txt
:language: text
:start-at: 2. factor of safety
:end-before: 3. one framework
```

どの手法も，$n=50$ を超えると3桁目までほとんど変わらない．{numref}`fig-slices-slope-overview` の6本でも，値の違いは2%ほどにとどまる．[第3章 11.5節](#practice-section-11-5)で見たように，分割数を変えて値が落ち着くことを確認してから，手法どうしを比較する．

次に，地下水位を $z=4$ m の水平な線に置く．1節で定めたとおり，地下水位より下の土も $\gamma=18$ kN/m³ のままとする．

```{literalinclude} examples/output/run_slices.txt
:language: text
:start-at: 5. water table
:end-before: 6. slices with
```

どの手法の値も，乾いたときより25%ほど下がる．Fellenius法の2つの値は，底面の有効垂直力 $N_i'$ の近似が異なる．1つ目は，自重の法線成分から間隙水圧の合力 $U_i=u_il_i$ を引いた $W_i\cos\alpha_i-u_il_i$ である．2つ目は，自重から $u_ib_i$ を引いた有効重量を，底面の法線方向に分解した $(W_i-u_ib_i)\cos\alpha_i$ を使う．後者は $W_i\cos\alpha_i-u_il_i\cos^2\alpha_i$ と同じで，合力 $U_i$ の代わりに $U_i\cos^2\alpha_i$ を引いている．そのため，急な底面ほど間隙水圧の効果を小さく見積もり，値が大きくなる．2つは，同じ量の表し方の違いではなく，異なる近似である．ほかの実装と比較するときは，どちらの近似かを確認しなければならない．

最後に，[第3章 5.2節](#practice-section-5-2)のとおり，安全率のほかに，底面の有効垂直力 $N_i-U_i$ を確認する．それが負になるスライスの $x$ を，乾いた斜面と地下水位のある斜面で表示する．

```{literalinclude} examples/output/run_slices.txt
:language: text
:start-at: 6. slices with
:end-before: 7. a plane
```

負になるのは，どれも右端のスライスである．このスライスは底面が急で，柱が低い．そのため，式 {eq}`eq-slices-normal` の分子で，粘着力によるせん断力の項が自重の項を上回る．$\theta=0$ の簡易Bishop法では，出力の最後の行のとおり，その鉛直成分 $c_i'l_i\sin\alpha_i/F_s$ が自重 $W_i$ より大きい．Fellenius法の $N_i=W_i\cos\alpha_i$ には，この項がない．このコードは，負の値をそのまま使っている．しかし，[実践1 5節](#infinite-section-5)で見たように，有効垂直力が負になるのは，土が引張を受けている状態である．そのため，テンションクラック（引張亀裂）を設けるか，接触を切るかといった扱いを，別に決定しなければならない（[第3章 12.1節](#practice-section-12-1)）．

---

(slices-section-6)=

## 6. 平面のすべり面で，無限斜面と比較する

傾き $30^\circ$ の平面の地表から，鉛直に5 mの深さに平行なすべり面を置き，8本のスライスに分割する．`Line` は，そのための平面のすべり面である．

```{literalinclude} examples/slices.py
:language: python
:pyobject: Line
```

```{literalinclude} examples/output/run_slices.txt
:language: text
:start-at: 7. a plane
:end-before: 8. an ellipse
```

3つの手法がすべて，実践1の{term}`無限斜面`の値1.2566に一致する．どのスライスも同じ形なので，各スライスが，実践1の柱と同じように単独でつり合う．つまり，どのスライスでも $Q_i=0$ で，スライス間力をどう仮定しても値が変わらない．同じ理由で，この面ではSpencer法の $\theta$ が定まらない．どの $\theta$ でも，$F_s=1.2566$ で2つの残差がともに0になるからである．この一致を，テストに追加する．

```{literalinclude} examples/test_slices.py
:language: python
:pyobject: test_a_plane_under_a_planar_slope_gives_the_infinite_slope
```

---

(slices-section-7)=

## 7. 円弧以外のすべり面と，モーメントの中心

同じ出口 $x=-1$ を通る楕円のすべり面を考える．中心は円と同じ $(6, 18)$ で，鉛直の半径を20 mとする．

```{literalinclude} examples/slices.py
:language: python
:pyobject: Ellipse
```

```{literalinclude} examples/output/run_slices.txt
:language: text
:start-at: 8. an ellipse
:end-before: 9. moving
```

1行目は，式 {eq}`eq-slices-bishop` に，楕円の底面の角度を代入した値である．一方，2行目では，式 {eq}`eq-slices-normal` の枠組みで，中心 $(6, 18)$ まわりのモーメントの残差を0にした．2つは，[第3章 5.1節](#practice-section-5-1)で見た「Bishopで非円弧を計算した」の2つの読み方にあたり，1.994と1.922で4%異なる．円弧の式は，底面垂直力の作用線が中心を通ること，せん断力の腕がどれも半径 $R$ であること，自重の腕が $R\sin\alpha_i$ であることを使って導出したものである．楕円では，この3つが成り立たない．前の2つは，[第3章 3節](#practice-section-3)で見たとおりである．Fellenius法でも，式 {eq}`eq-slices-fellenius` は1.733，中心まわりのモーメントに戻ると1.803になる．後者の `fellenius_about` は，底面垂直力 $N_i=W_i\cos\alpha_i$ のモーメントも含める．

```{literalinclude} examples/slices.py
:language: python
:pyobject: fellenius_about
```

円弧の中心まわりでは，`fellenius_about` が式 {eq}`eq-slices-fellenius` に戻ることを，テストに追加する．

```{literalinclude} examples/test_slices.py
:language: python
:pyobject: test_fellenius_about_the_centre_of_a_circle_is_the_formula
```

次に，{term}`モーメントの中心`を，$(6, 18)$ から上に7 m，右に4 m移動させる．

```{literalinclude} examples/output/run_slices.txt
:language: text
:start-at: 9. moving
```

Fellenius法は，どちらに移動させても値が変わる．簡易Bishop法は，上へなら変わるが，右へなら変わらない．Spencer法は，どちらへでも変わらない．この違いは，[第3章 6節](#practice-section-6)の式で説明できる．中心を $\boldsymbol{a}$ だけ移動させると，モーメントは $-\boldsymbol{a}\times\sum\boldsymbol{F}$ だけ変わる．ここで $\sum\boldsymbol{F}$ は，土塊全体で残った力である．

- Spencer法は力のつり合いを満たすので，$\sum\boldsymbol{F}=\boldsymbol{0}$ で，どこに移動させても変わらない
- 簡易Bishop法は，各スライスの鉛直方向のつり合いを満たし，スライス間力を水平とする．そのため，残った力 $\sum\boldsymbol{F}$ は水平で，水平に移動させたときだけ $\boldsymbol{a}\times\sum\boldsymbol{F}=\boldsymbol{0}$ になる
- Fellenius法は，各スライスで，底面に垂直な向きのつり合いだけを満たす．その向きはスライスごとに異なるので，$\sum\boldsymbol{F}$ に鉛直成分も水平成分も残り，上に移動させても右に移動させても変わる

円弧では，円の中心をモーメントの中心にとれば，この問題は表に出にくい．しかし，円弧以外の面では，力のつり合いを満たさない方法ほど，中心の選択が値に表れる．3次元でも，回転軸と基準点を決定する手法では，同じことが起こる．このことを，テストに追加する．

```{literalinclude} examples/test_slices.py
:language: python
:pyobject: test_the_moment_centre_matters_only_where_force_equilibrium_is_missing
```

ここまでで，`run_slices.py` が使う関数がそろった．{download}`run_slices.py <examples/run_slices.py>` をダウンロードして `lem-practice` に置き，実行する．

```bash
uv run python run_slices.py
```

この実践に載せている出力と同じ値が表示されれば，ここまでの関数が正しく実装できている．最後に，`uv run pytest` で，この実践のテストと実践1のテストが，すべて通ることを確認する．

---

(slices-trouble)=

## 困ったとき

| 表示や様子 | 原因と対処 |
|---|---|
| `ValueError: m_alpha が 0 以下になるスライスがある` | 反復の途中で $F_s$ が小さくなりすぎたか，出口の近くで底面が急に上るスライスがある．初期値 `fs` を大きくするか，すべり面の形を見直す．（→[2節](#slices-section-2)） |
| `ValueError: 分母 D が 0 以下になるスライスがある` | 割線法が，小さすぎる $F_s$ か大きすぎる $\theta$ を試した．`fs` の初期値を，簡易Bishop法の値の近くにする．（→[3節](#slices-section-3)） |
| `RuntimeError: 割線法で，2点の値が同じになった` | 割線法の2点で，解く式の値が同じになった．平面のすべり面で `spencer` を使うと，$F_m(\theta)-F_f(\theta)$ がどの $\theta$ でも0になり，これが起こる．（→[6節](#slices-section-6)） |
| `TypeError: fellenius() got an unexpected keyword argument 'effective_weight'` | `fellenius` に，5節で使う引数 `effective_weight` を付けていない．（→[2節](#slices-section-2)） |
| `ModuleNotFoundError: No module named 'infinite_slope'` | 実践1の `infinite_slope.py` が，同じフォルダにない．（→[準備](#slices-setup)） |
| 値が表と少し異なる | 分割数 $n$ と，底面の代表点を幅の中央にとっているかを確認する．重さも，幅の中央の高さで求める．（→[1節](#slices-section-1)） |

## まとめ

- スライスの表は，底面の代表点，傾き，法線とすべる向き，長さ，重さ，間隙水圧からなる．円弧では，どの底面の法線も中心を通る（→[1節](#slices-section-1)）
- Fellenius法，簡易Bishop法，簡易Janbu法は，教科書の式のとおりに実装できる．後の2つは右辺にも $F_s$ が現れるので，反復して求める（→[2節](#slices-section-2)）
- スライス間力の合力の傾き $\theta$ を変数にすると，各スライスの $N_i$ が1本の式で定まる．$\theta=0$ でモーメントの残差を0にすると簡易Bishop法に，力の残差を0にすると簡易Janbu法になる（→[3節](#slices-section-3)）
- $F_m(\theta)$ と $F_f(\theta)$ の交点がSpencer法の解で，力とモーメントの残差がともに0になる．円弧では $F_m$ が $\theta$ にほとんどよらないので，簡易Bishop法とSpencer法が近い（→[4節](#slices-section-4)）
- 分割数を増加させて値が落ち着くことと，有効垂直力が負になる底面がないことを確認してから，手法を比較する．Fellenius法の値は，地下水位があるとき，有効垂直力の近似の仕方でも変わる（→[5節](#slices-section-5)）
- 平面のすべり面では，どの手法も無限斜面の値に一致する．どのスライスも単独でつり合うからである（→[6節](#slices-section-6)）
- 円弧以外の面では，力のつり合いを満たさない方法ほど，モーメントの中心の選択が値に表れる（→[7節](#slices-section-7)）

---

## 確認問題

答えは問題をクリックすると開く．（やってみよう）は，`lem-practice` で取り組む．

:::{dropdown} 問1　円弧の中心まわりのモーメントの式に，底面垂直力が現れないことを，コードでどう確認したか
:icon: question

円の中心から各底面の点への位置ベクトル $\boldsymbol{r}_i$ と，底面の法線 $\boldsymbol{n}_i$ の外積が，どのスライスでも丸め誤差の大きさしかないことを確認した．外積が0なので，底面垂直力の作用線は中心を通り，中心まわりのモーメントをもたない．（→[1節](#slices-section-1)）
:::

:::{dropdown} 問2（やってみよう）　{numref}`fig-slices-slope-overview` の6本のスライスで，簡易Bishop法の解での $m_{\alpha,i}$ をスライスごとに求めよ．最も小さいのはどのスライスか
:icon: question

`s = make_slices(Circle(), 6)` と `fs = bishop(s)` を求める．そのうえで，`np.cos(s.alpha) + np.sin(s.alpha) * s.tan_phi / fs` を計算する．左から順に0.894，0.987，1.033，1.032，0.973，0.822で，最も小さいのは，底面が最も急な6本目（$\alpha=53.5^\circ$）である．出口側の1本目は，$\alpha=-14.9^\circ$ と緩いので0.894にとどまる．$m_{\alpha,i}$ が0に近づくのは，出口の近くで底面が急に上るとき（$\alpha_i$ が大きな負の値のとき）である．（→[2節](#slices-section-2)）
:::

:::{dropdown} 問3　$\theta=0$ の枠組みで，モーメントの残差を0にすると，簡易Bishop法と同じ値になるのはなぜか
:icon: question

$\theta=0$ では $\boldsymbol{p}$ が鉛直になり，各スライスの鉛直方向のつり合いから，簡易Bishop法と同じ $N_i$ が得られるため．そのうえで，モーメントの残差を0にすることは，土塊全体の，円の中心まわりのモーメントのつり合いを満たすことにあたる．これは，簡易Bishop法が使うつり合いと同じである．（→[3節](#slices-section-3)）
:::

:::{dropdown} 問4（やってみよう）　$n=50$ の簡易Bishop法の解で，力の残差を求めよ．何を表しているか
:icon: question

`residuals(s, bishop(s), 0.0, (6.0, 18.0))` の1つ目が力の残差で，86.7 kN/m になる．土塊の重さの合計2415.6 kN/m の3.6%にあたる．これは，簡易Bishop法が，全体の水平方向の力のつり合いを満たしていないことを表す．各スライスの $Q_i$ は，両側のスライス間の垂直力の差である．これを左から順に加えていくと，右の端で0に戻らない．（→[3節](#slices-section-3)）
:::

:::{dropdown} 問5（やってみよう）　$\phi'=25^\circ$ にすると，4つの手法の値と，その大小の順はどうなるか
:icon: question

`make_slices(Circle(), 50, phi_deg=25.0)` で表を作る．Fellenius法1.594，簡易Bishop法1.734，簡易Janbu法1.575，Spencer法1.731（$\theta=17.9^\circ$）になる．小さい順に，簡易Janbu法，Fellenius法，Spencer法，簡易Bishop法で，$\phi'=30^\circ$ のときと同じである．どの値も，$\phi'=30^\circ$ のときの0.84倍ほどになる．$\tan\phi'$ の比0.81より下がり方が小さいのは，粘着力による抵抗が変わらないため．（→[2節](#slices-section-2)，[4節](#slices-section-4)）
:::

:::{dropdown} 問6　平面のすべり面で，Spencer法の $\theta$ が定まらないのはなぜか
:icon: question

どのスライスも同じ形で，各スライスが単独でつり合うため．どのスライスでも $Q_i=0$ になり，どの $\theta$ でも，$F_s=1.2566$ で力とモーメントの残差がともに0になる．（→[6節](#slices-section-6)）
:::

:::{dropdown} 問7　楕円のすべり面で，モーメントの中心を右に移動させても，簡易Bishop法の値が変わらないのはなぜか
:icon: question

簡易Bishop法は，各スライスの鉛直方向のつり合いを満たし，スライス間力を水平とするため．土塊全体で残る力 $\sum\boldsymbol{F}$ は水平になる．中心を水平に移動させると，その移動 $\boldsymbol{a}$ と $\sum\boldsymbol{F}$ が平行になり，モーメントの変化 $-\boldsymbol{a}\times\sum\boldsymbol{F}$ が0になる．上に移動させたときは，$\boldsymbol{a}$ と $\sum\boldsymbol{F}$ が平行でないので，値が変わる．（→[7節](#slices-section-7)）
:::

:::{dropdown} 問8（やってみよう）　円の中心を $(4, 16)$ に移動させ，同じ出口 $x=-1$ を通る円弧で，簡易Bishop法の $F_s$ を求めよ．この実践の円弧は，臨界すべり面といえるか
:icon: question

`bishop(make_slices(Circle((4.0, 16.0)), 50))` は1.790で，この実践の円弧（2.063）より小さい．つまり，この実践の円弧は{term}`臨界すべり面`ではない．臨界すべり面は，中心や出口を変えた多くの円弧について安全率を計算し，最小のものを探して初めて分かる．安全率の計算と，臨界すべり面の探索は，別の問題である．（→[第3章 12.4節](#practice-section-12-4)）
:::

:::{dropdown} 問9（やってみよう）　地下水位を $z=4$ m に置くと，Spencer法の解で，右端のスライスの $N_i-U_i$ が負になる．乾いた斜面では正である．このスライスの底面は地下水位より上にあるのに，なぜ負になるか
:icon: question

`s = make_slices(Circle(), 50, water_level=4.0)` と `fs, theta = spencer(s, (6.0, 18.0))` を求める．`p = np.array([-np.sin(theta), np.cos(theta)])` として，右端のスライスについて，式 {eq}`eq-slices-normal` の分子の2つの項 `s.W[-1] * p[1]` と `s.c[-1] * s.l[-1] * (-s.m[-1] @ p) / fs` を計算する．$u_i=0$ なので，$U_i$ の項はない．乾いた斜面では4.36と3.86 kN/m で，自重の項が大きく，$N_i-U_i=0.56$ kN/m になる．地下水位があると4.40と5.26 kN/m で，粘着力の項が上回り，$N_i-U_i=-0.91$ kN/m になる．つまり，負になるのは，地下水位によって $F_s$ が2.059から1.544に下がり，$1/F_s$ に比例する粘着力の項が増加したため．このスライスに間隙水圧が直接はたらくためではない．（→[5節](#slices-section-5)，[第3章 12.1節](#practice-section-12-1)）
:::

---

## 次に読む

この実践では，2次元のスライスで，手法の違いが不静定性の解消の仕方の違いであることを，残差で確認した．3次元では，すべり土塊を{term}`カラム`に分割し，底面のせん断力の向きと回転軸を，新しく決定しなければならない．[実践3「カラム法で3次元のすべり面の安全率を計算する」](practice-columns-3d.md)で，この実践の円弧を奥行き方向に延ばし，カラムの表を作る．円柱のすべり面では，この実践の値に戻ることも確認する．

## 参考文献

1. Bishop, A. W. (1955). “The use of the slip circle in the stability analysis of slopes.” *Géotechnique*, 5(1), 7–17. [https://doi.org/10.1680/geot.1955.5.1.7](https://doi.org/10.1680/geot.1955.5.1.7)
2. Janbu, N. (1973). “Slope Stability Computations.” In R. C. Hirschfeld and S. J. Poulos (eds.), *Embankment-Dam Engineering: Casagrande Volume*, pp. 47–86. New York: Wiley.
3. Spencer, E. (1967). “A method of analysis of the stability of embankments assuming parallel inter-slice forces.” *Géotechnique*, 17(1), 11–26. [https://doi.org/10.1680/geot.1967.17.1.11](https://doi.org/10.1680/geot.1967.17.1.11)
4. Fredlund, D. G., and Krahn, J. (1977). “Comparison of slope stability methods of analysis.” *Canadian Geotechnical Journal*, 14(3), 429–439. [https://doi.org/10.1139/t77-045](https://doi.org/10.1139/t77-045)
