---
title: "カラム法で3次元のすべり面の安全率を計算する：カラムの表を作り，無限斜面と2次元の値で確かめる"
lang: ja
series: "practice 3 of 3"
---

# カラム法で3次元のすべり面の安全率を計算する

**カラムの表を作り，無限斜面と2次元の値で確かめる**

この実践では，実践2の斜面を奥行き方向に延ばし，楕円体のすべり面について，3次元のカラム法で安全率を求めるコードを書く．カラムの表を作り，Hovland法と3次元の簡易Bishop法を実装する．まず，平面のすべり面では実践1の無限斜面に，円柱のすべり面では実践2の2次元の値に一致することを確かめる．そのうえで，球や楕円体のすべり面で，局所すべり方向，全体すべり方向，回転軸といった，3次元で新しく決めなければならない量の影響を見る．

この実践は，[第2資料](what-is-limit-equilibrium-method.md)と[第3資料](lem-in-practice-mechanical-perspective.md)の第3部を読み，[実践1](practice-infinite-slope.md)と[実践2](practice-slices-2d.md)を終えた前提で進める．用語と記号は，[用語集](lem-glossary.md)にまとめた．

(columns-goal)=

## 作るもの

斜面は，[実践2](practice-slices-2d.md)の斜面を，奥行き方向（$y$ 方向）にどこまでも延ばしたものである．座標は，$x$ を水平右向き，$y$ を水平奥向き，$z$ を鉛直上向きにとる．土塊は $x$ の負の向きへすべり，土の定数は実践1・実践2と同じとする．

{term}`すべり面`は，3つの軸が座標軸に平行な楕円体の下の面とする．中心は $(6, 0, 18)$ で，$x$ 方向と $z$ 方向の半径は実践2の円の半径 $R=19.31$ m，$y$ 方向の半径は $B$ とする．そのため，$y=0$ の断面は，実践2の円弧そのものになる．$B=R$ なら球で，$B$ を大きくするほど奥行き方向に長い楕円体になる．確かめのために，平面のすべり面と，実践2の円弧を長さ10 mだけ延ばした円柱のすべり面も使う．

{term}`全体すべり方向`は，斜面を下る向き $\boldsymbol{d}=(-1, 0, 0)$ とする．モーメントは，楕円体の中心 $O$ を通り，$\boldsymbol{d}$ に直交する水平な軸 $\boldsymbol{a}=\boldsymbol{d}\times\boldsymbol{e}_z=(0, 1, 0)$ のまわりにとる．$\boldsymbol{e}_z$ は鉛直上向きの単位ベクトルである．

```{figure} ./figures/fig_05_3d_column_forces.svg
:name: fig-columns-3d-forces
:alt: 傾いた底面をもつ3次元のカラムに働く自重，底面の垂直力とせん断力，側面のカラム間力

3次元のカラムに働く力．第2資料の図と同じで，底面のせん断力の向きは，強度の式からは決まらない．この実践では，側面のカラム間力の効果を無視するか，水平とする
```

作るものは，次のとおりである．

| 関数 | 求めるもの | 節 |
|---|---|---|
| `make_columns` | カラムの表 | 1節 |
| `dip_directions`，`projected_directions` | 各底面の局所すべり方向 | 2節 |
| `hovland` | Hovland法の安全率 | 3節 |
| `hovland_moment`，`bishop` | 回転軸まわりのモーメントで求めた安全率 | 4節 |
| `save_columns` | カラムの表を保存したファイル | 8節 |

(columns-setup)=

## 準備

[実践1](practice-infinite-slope.md)と[実践2](practice-slices-2d.md)で使ったフォルダ `lem-practice` を使う．このページのコードは，実践2の `slices.py` から斜面の形を読み込む．コードは，{download}`columns.py <examples/columns.py>` と {download}`test_columns.py <examples/test_columns.py>` にまとめてある．ここから始めるときは，{download}`infinite_slope.py <examples/infinite_slope.py>` と {download}`slices.py <examples/slices.py>` も，同じフォルダに置く．

---

(columns-section-1)=

## 1. カラムの表を作る

平面図を，一辺 $h$ の正方形に分ける．正方形の中心で，すべり面が地表より下にあれば，その正方形を{term}`カラム`にする．各カラムの底面は，中心を通る鉛直線とすべり面の交点と，そこでの接平面で代表させる．実践2で，{term}`スライス`の底面を幅の中央の点で代表させたことの3次元版である．

楕円体の中心を $(c_x, c_y, c_z)$，半径を $(a, b, c)$ とすると，鉛直線 $(x, y)$ との下の交点の高さと，外向きの単位法線ベクトルは次のようになる．

$$
z_s=c_z-c\sqrt{1-\left(\frac{x-c_x}{a}\right)^2-\left(\frac{y-c_y}{b}\right)^2},
\qquad
\boldsymbol{n}\propto
\begin{bmatrix}
(x-c_x)/a^2\\
(y-c_y)/b^2\\
(z_s-c_z)/c^2
\end{bmatrix}
$$ (eq-columns-ellipsoid)

$\boldsymbol{n}$ は楕円体の外向きで，底面では下を向き，{term}`すべり土塊`の外向きにもなる．`columns.py` を作り，最初に次を書く．

```{literalinclude} examples/columns.py
:language: python
:end-at: return slices.ground
```

```{literalinclude} examples/columns.py
:language: python
:pyobject: Ellipsoid
```

カラムの表は，次の量からなる．底面積 $A_i$ は，一辺 $h$ の正方形の上にある接平面の面積で，$h^2/|n_{z,i}|$ になる．実践2の $l_i=b_i/\cos\alpha_i$ にあたる．重さは，中心で測った柱の高さを使い，$W_i=\gamma h^2(z_g-z_s)$ とする．

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

`centres` は，正方形の並びを，すべり面がありうる範囲の中点について対称にする．こうしておくと，$y=0$ について対称なすべり面で，表も対称になる．表を手で確かめるテストを書く．`test_columns.py` を作り，次を書く．

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

## 2. 局所すべり方向を決める

[第2資料 7.1節](#what-section-7-1)で見たように，3次元では，強度の式が決めるのは{term}`底面せん断力`の大きさだけで，向きは決めない．そのため，各底面の{term}`局所すべり方向` $\boldsymbol{m}_i$ を，別に仮定しなければならない．この実践では，2つの決め方を作る．

- **鉛直面の中で下る向き**：全体すべり方向 $\boldsymbol{d}$ を含む鉛直面で，底面が下る向きをとる．Hovland (1977) の取り方である．この向きは，$\boldsymbol{d}$ に直交する水平な軸 $\boldsymbol{a}$ のまわりに土塊が回るときの向きと同じで，$\boldsymbol{m}_i\propto\boldsymbol{a}\times\boldsymbol{n}_i$ になる
- **接平面への射影**：$\boldsymbol{d}$ を各底面の接平面に射影し，$\boldsymbol{m}_i\propto(\boldsymbol{I}-\boldsymbol{n}_i\boldsymbol{n}_i^{\mathsf T})\boldsymbol{d}$ とする．[第3資料 8.2節](#practice-section-8-2)の決め方である

```{literalinclude} examples/columns.py
:language: python
:pyobject: rotation_directions
```

```{literalinclude} examples/columns.py
:language: python
:pyobject: dip_directions
```

```{literalinclude} examples/columns.py
:language: python
:pyobject: projected_directions
```

どちらの向きも，底面の接平面の中にあり，$\boldsymbol{d}$ の向きへ進む．底面が横に傾いていない（$n_{y,i}=0$ の）カラムでは，2つは一致する．横に傾いたカラムでは違い，その差が{term}`安全率`にどう表れるかを7節で見る．まず，2つが接平面の中にあることを確かめる．

```{literalinclude} examples/test_columns.py
:language: python
:pyobject: test_both_local_directions_lie_in_the_base
```

---

(columns-section-3)=

## 3. Hovland法

[第2資料 8.1節](#what-section-8-1)のHovland法は，Fellenius法を3次元に広げた方法である．カラム間力の効果を無視し，{term}`底面垂直力`を，自重の法線方向の成分 $N_i=W_i\,(\boldsymbol{g}\cdot\boldsymbol{n}_i)$ とする．$\boldsymbol{g}=(0, 0, -1)$ は重力の向きである．そのうえで，各カラムの{term}`抵抗力`と，自重の $\boldsymbol{m}_i$ 方向の成分（{term}`滑動力`）を，それぞれ足し合わせて比をとる．

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

ここで $U_i=u_iA_i$ である．底面が横に傾いていないカラムでは，$\boldsymbol{g}\cdot\boldsymbol{n}_i=\cos\alpha_i$，$\boldsymbol{g}\cdot\boldsymbol{m}_i=\sin\alpha_i$ になり，実践2の式 {eq}`eq-slices-fellenius` と同じ形になる．`hovland(col, m)` を書く．`m` は，2節のどちらかの局所すべり方向である．

:::{dropdown} 実装の例
```{literalinclude} examples/columns.py
:language: python
:pyobject: hovland
```
:::

テストは，5節でまとめて書く．

---

(columns-section-4)=

## 4. 回転軸まわりのモーメントと，3次元の簡易Bishop法

3次元の簡易Bishop法は，[第2資料 8.2節](#what-section-8-2)で見たように，{term}`回転軸 <モーメントの中心>`まわりのモーメントのつり合いから $F_s$ を求める．そこで，まずモーメントの腕を作る．軸 $\boldsymbol{a}$ は点 $O$ を通るとし，$O$ から底面の点までの位置ベクトルを $\boldsymbol{r}_{b,i}$，カラムの高さの中央の点までを $\boldsymbol{r}_{g,i}$ とする．底面のせん断力，自重，底面の垂直力の，単位の大きさあたりの $\boldsymbol{a}$ まわりのモーメントは，次の3つである．

$$
\ell_{t,i}=(\boldsymbol{r}_{b,i}\times\boldsymbol{m}_i)\cdot\boldsymbol{a},
\qquad
\ell_{w,i}=(\boldsymbol{r}_{g,i}\times\boldsymbol{g})\cdot\boldsymbol{a},
\qquad
\ell_{n,i}=(\boldsymbol{r}_{b,i}\times\boldsymbol{n}_i)\cdot\boldsymbol{a}
$$ (eq-columns-arms)

ここでの $\boldsymbol{m}_i$ は，軸 $\boldsymbol{a}$ のまわりの回転の向き（2節の1つ目）である．カラム間力は{term}`内力`なので，土塊全体のモーメントでは打ち消し合う．そのため，$\boldsymbol{a}$ まわりのモーメントのつり合いは，$\sum_i(W_i\ell_{w,i}-N_i\ell_{n,i}-T_i\ell_{t,i})=0$ になる．$T_i=[c_i'A_i+(N_i-U_i)\tan\phi_i']/F_s$ を入れて $F_s$ について解くと，次のようになる．

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

$N_i$ に式 {eq}`eq-columns-hovland` のHovland法の値を使うと，Hovland法をモーメントの比で書いた形になる．実践2の `fellenius_about` の3次元版である．

```{literalinclude} examples/columns.py
:language: python
:pyobject: hovland_moment
```

3次元の簡易Bishop法では，$N_i$ を，各カラムの鉛直方向の力のつり合いから求める．カラム間力は水平とする．底面の垂直力 $-N_i\boldsymbol{n}_i$ とせん断力 $-T_i\boldsymbol{m}_i$ の鉛直成分が，自重とつり合うので，$N_i$ は次のようになる．

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

横に傾いていない底面では $-n_{z,i}=\cos\alpha_i$，$m_{z,i}=-\sin\alpha_i$ なので，$m_{\alpha,i}$ は実践2の式 {eq}`eq-slices-bishop` の $m_{\alpha,i}$ と同じになる．

```{literalinclude} examples/columns.py
:language: python
:pyobject: vertical_normal_force
```

この $N_i$ を式 {eq}`eq-columns-moment` に入れると，右辺にも $F_s$ が現れる．そのため，実践2の簡易Bishop法と同じく，反復して求める．`bishop(col, center, axis)` を書く．

:::{dropdown} 実装の例
```{literalinclude} examples/columns.py
:language: python
:pyobject: bishop
```
:::

---

(columns-section-5)=

## 5. 平面と円柱で確かめる

平面と円柱のすべり面を作る．`Plane` は，実践2の `Line` を奥行き方向に延ばした平面で，`Cylinder` は，実践2の円弧を長さ `length` だけ延ばし，両端を鉛直な面で切った面である．

```{literalinclude} examples/columns.py
:language: python
:pyobject: Cylinder
```

```{literalinclude} examples/columns.py
:language: python
:pyobject: Plane
```

{download}`run_columns.py <examples/run_columns.py>` をダウンロードして `lem-practice` に置き，実行する．

```bash
uv run python run_columns.py
```

出力の1.と2.が，この節の確かめである．

```{literalinclude} examples/output/run_columns.txt
:language: text
:start-at: 1. a plane
:end-before: 3. ellipsoids
```

平面では，3つの値がすべて，実践1の{term}`無限斜面`の値1.2566に一致する．どのカラムも同じ形で，各カラムが実践1の柱と同じように単独でつり合うからである．どの底面も同じ向きなので，せん断力の腕 $\ell_{t,i}$ もどのカラムでも同じ（$O$ から平面までの距離）になり，モーメントの比が力の比に一致する．

円柱では，底面が横に傾かないので，奥行き方向のどの帯も，実践2の2次元の問題になる．そのため，Hovland法は実践2のFellenius法に，3次元の簡易Bishop法は実践2の簡易Bishop法に，0.1%ほどの差で一致する．差が残るのは，正方形のカラムが，円弧の出口と入口にぴったり合わないからである．この2つを，テストに足す．

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

## 6. 球と楕円体で，3次元の効果を見る

中央の断面（$y=0$）が実践2の円弧になる楕円体で，$y$ 方向の半径 $B$ を変える．

```{literalinclude} examples/output/run_columns.txt
:language: text
:start-at: 3. ellipsoids
:end-before: 4. local direction
```

実践2の中央断面の値は，Fellenius法が1.888，簡易Bishop法が2.063だった．球（$B=R$）では，Hovland法が1.816で中央断面より小さく，3次元の簡易Bishop法は2.142で大きい．同じすべり面で，3次元の値と2次元の値の大小が，手法によって逆になっている．

Hovland法の値が小さくなるのは，球の奥の断面が，中心の高さが同じで半径の小さい円弧になるからである．そうした浅い円弧は，この斜面では中央断面より安全率が小さく，Hovland法の値は，それらを足し合わせたものになる．一方，3次元の簡易Bishop法では，横に傾いた底面ほど，鉛直方向のつり合いから求まる $N_i$ が大きくなる．Hovland法の $N_i$ と比べると，次のようになる．

```{literalinclude} examples/output/run_columns.txt
:language: text
:start-at: 7. base normal force
```

横の傾きが30°を超えるカラムでは，$N_i$ がHovland法の1.6倍になり，摩擦による抵抗が増える．[第2資料 9節](#what-section-9)で見たように，「3次元の安全率は，必ず2次元より大きい」という決まりはない．この例のように，大小はすべり面の形と手法によって逆にもなる．

$B$ を大きくしても，値は中央断面の値には近づかない．楕円体を奥行き方向に長くしても，断面が奥ほど浅い円弧になることは変わらないからである．中央断面の2次元の値と比べたいときは，5節の円柱を使う．球の値を，テストに足す．

```{literalinclude} examples/test_columns.py
:language: python
:pyobject: test_the_sphere
```

---

(columns-section-7)=

## 7. 局所すべり方向と全体すべり方向を変える

球で，2節の2つの局所すべり方向を比べる．

```{literalinclude} examples/output/run_columns.txt
:language: text
:start-at: 4. local direction
:end-before: 5. azimuth
```

同じカラムの表，同じ全体すべり方向で，局所すべり方向の決め方だけを変えると，安全率が1.816から2.122へ17%変わる．横に傾いた底面では，$\boldsymbol{d}$ を接平面に射影した向きが横の成分をもち，下る成分が小さくなる．例えば，$\boldsymbol{n}=(0.3, 0.6, -0.742)$ の底面では，$\boldsymbol{g}\cdot\boldsymbol{m}$ が，鉛直面の中で下る向きで0.375，射影で0.233になる．そのため，射影を使うと滑動力が小さくなり，安全率が大きくなる．[第3資料 9節](#practice-section-9)で見たように，局所すべり方向は，結果を見せるための矢印ではなく，安全率を決める定式化の一部である．

次に，全体すべり方向 $\boldsymbol{d}$ を，水平面内で回す．

```{literalinclude} examples/output/run_columns.txt
:language: text
:start-at: 5. azimuth
:end-before: 6. column size
```

どちらの決め方でも，斜面を真っすぐ下る向き（0°）で安全率が最小になり，左右に対称である．すべり面が $y=0$ について対称だからである．[第3資料 8.1節](#practice-section-8-1)のとおり，対称な斜面では，対称面から全体すべり方向の候補が決まる．非対称な斜面では，いくつかの方位を試して最小を探すか，つり合いから方向を解かなければならない．このことを，テストに足す．

```{literalinclude} examples/test_columns.py
:language: python
:pyobject: test_a_symmetric_slip_surface_is_least_stable_straight_down_the_slope
```

最後に，カラムの大きさ $h$ を変える．

```{literalinclude} examples/output/run_columns.txt
:language: text
:start-at: 6. column size
:end-before: 7. base normal force
```

$h$ を1 mから0.25 mにしても，値の変化は0.2%ほどである．[第3資料 11.5節](#practice-section-11-5)で見たように，分割を変えて値が落ち着くことを確かめてから，ほかの条件の影響を比べる．

---

(columns-section-8)=

## 8. カラムの表を保存して，ほかの実装と比べる

カラムの表と，モーメントの基準点と回転軸を，NumPyの `.npz` 形式で保存する．

```{literalinclude} examples/columns.py
:language: python
:pyobject: save_columns
```

```python
import numpy as np

import columns
import slices

R = slices.Circle().radius
centre = np.array([6.0, 0.0, 18.0])
col = columns.make_columns(columns.Ellipsoid(centre, (R, 2 * R, R)), 0.5)
columns.save_columns("columns.npz", col, centre, np.array([0.0, 1.0, 0.0]))
```

保存した表は，ほかの実装のソルバーに渡して，同じすべり面の安全率を比べるのに使える．[第3資料 1節](#practice-section-1)で見たように，底面の面積，法線，重さ，{term}`間隙水圧`，強度，位置ベクトルがあれば，力とモーメントを足し合わせられるからである．ただし，値を比べる前に，次の取り決めを確かめる．

1. 法線の向き：すべり土塊の外向き（この実践）か，上向きか
2. 局所すべり方向：回転軸から決めるか，全体すべり方向の射影か．すべる向きにとるか，すべりに抵抗する向きにとるか
3. 間隙水圧の合力：$U_i=u_iA_i$（この実践）か，[実践2 5節](#slices-section-5)の $u_ib_i\cos\alpha_i$ のような別の形か
4. モーメントの基準点と回転軸：どこにとり，すべり面の大きさに合わせて動くか
5. 求まらないときの返し方：反復が収束しないときに，無限大などの特別な値を返す実装がある．それは「非常に安全」という意味ではない（[第3資料 11.4節](#practice-section-11-4)）

5.は，特に注意が要る．例えば，円柱のように横の傾きがない表を，横方向の未知量をもつ3次元の定式化に渡すと，その未知量が式に効かず，反復が解けないことがある．研究室で開発している斜面安定解析のコード[LEM Lab](https://github.com/daichis5/lem-lab)も，カラムの表とソルバーを分けて組み立ててある．LEM Labのドキュメントには，この実践で保存した表を読み込み，そのソルバーで解き直す手順がある．保存した表が元のカラムを再現することを，テストで確かめる．

```{literalinclude} examples/test_columns.py
:language: python
:pyobject: test_the_saved_table
```

`uv run pytest` で，実践1から実践3までのテストが，すべて通ることを確かめる．

---

(columns-trouble)=

## 困ったとき

| 表示や様子 | 原因と対処 |
|---|---|
| `ModuleNotFoundError: No module named 'slices'` | 実践2の `slices.py` が，同じフォルダにない．（→[準備](#columns-setup)） |
| `ValueError: m_alpha が 0 以下になるカラムがある` | 3次元の簡易Bishop法の反復で，$F_s$ が小さくなりすぎたか，底面が急に上るカラムがある．初期値 `fs` を大きくするか，すべり面を見直す．（→[4節](#columns-section-4)） |
| 計算に時間がかかる | カラムの数は $h^2$ に反比例して増える．$h=0.25$ mの球で約9200本である．確かめの途中は $h=0.5$ mや1 mで試す．（→[7節](#columns-section-7)） |
| 値が表と少し違う | $h$ と，カラムの並び（`centres`）を確かめる．並びが対称でないと，左右に回した全体すべり方向の値もずれる．（→[1節](#columns-section-1)） |

## まとめ

- カラムの表は，底面の代表点，法線，底面積，重さ，間隙水圧，強度からなる．底面積は $h^2/|n_z|$ で，2次元の $b/\cos\alpha$ にあたる（→[1節](#columns-section-1)）
- 3次元では，局所すべり方向を別に仮定する．鉛直面の中で下る向きと，接平面への射影は，横に傾いた底面で違う（→[2節](#columns-section-2)）
- Hovland法は，カラム間力を無視し，各カラムの抵抗力と滑動力を足し合わせる．3次元の簡易Bishop法は，各カラムの鉛直方向のつり合いから $N_i$ を求め，回転軸まわりのモーメントの比をとる（→[3節](#columns-section-3)，[4節](#columns-section-4)）
- 平面のすべり面では無限斜面の値に，円柱のすべり面では2次元の値に一致する．新しい手法は，1つ前の模型に戻ることで確かめる（→[5節](#columns-section-5)）
- 球では，Hovland法の値が2次元の中央断面より小さく，3次元の簡易Bishop法の値は大きい．3次元と2次元の大小は，すべり面の形と手法で逆にもなる（→[6節](#columns-section-6)）
- 同じ表でも，局所すべり方向の決め方で安全率が17%変わる．対称なすべり面では，斜面を真っすぐ下る全体すべり方向で安全率が最小になる（→[7節](#columns-section-7)）
- ほかの実装と比べるときは，法線の向き，局所すべり方向，間隙水圧の合力，回転軸，求まらないときの返し方を，先に確かめる（→[8節](#columns-section-8)）

---

## 確認問題

答えは問題をクリックすると開く．（やってみよう）は，`lem-practice` で取り組む．

:::{dropdown} 問1　3次元のカラム法で，局所すべり方向を別に決めなければならないのはなぜか
:icon: question

Mohr–Coulomb則による強度の式が決めるのは，底面せん断力の大きさだけで，接平面の中の向きは決めないため．2次元では，向きは断面の中の接線に沿う2つに限られ，すべりを妨げる側に決まる．3次元の接平面には向きが無数にあるので，仮定しなければならない．（→[2節](#columns-section-2)）
:::

:::{dropdown} 問2（計算してみよう）　一辺 $h=0.25$ mのカラムの底面が，水平から30°傾いている．底面積はいくらか
:icon: question

$|n_z|=\cos 30^\circ$ なので，$A=0.25^2/\cos 30^\circ=0.0722$ m² である．水平な正方形の面積0.0625 m²より，傾いた分だけ大きい．（→[1節](#columns-section-1)）
:::

:::{dropdown} 問3　平面のすべり面で，Hovland法，そのモーメントの形，3次元の簡易Bishop法が，どれも無限斜面の値に一致するのはなぜか
:icon: question

どのカラムも同じ形で，各カラムが無限斜面の柱と同じように単独でつり合うため．カラム間力がなくても各カラムがつり合うので，カラム間力の扱い方の違いが値に表れない．どの底面も同じ向きなので，モーメントの腕も同じになり，モーメントの比が力の比に一致する．（→[5節](#columns-section-5)）
:::

:::{dropdown} 問4　球のすべり面で，Hovland法の値が2次元の中央断面の値より小さくなったのはなぜか．「3次元の安全率は2次元より大きい」といえるか
:icon: question

球の奥の断面が，中心の高さが同じで半径の小さい，浅い円弧になり，この斜面ではその安全率が中央断面より小さいため．Hovland法の値は，それらを足し合わせたものになる．一方，同じ球で，3次元の簡易Bishop法の値は中央断面より大きい．そのため，3次元と2次元の大小は，すべり面の形と手法によって逆にもなり，「必ず大きい」とはいえない．（→[6節](#columns-section-6)）
:::

:::{dropdown} 問5　球で，局所すべり方向の決め方を変えると，安全率が17%も変わったのはなぜか
:icon: question

横に傾いた底面では，全体すべり方向を接平面に射影した向きが横の成分をもち，下る成分が，鉛直面の中で下る向きより小さくなるため．その分だけ自重の滑動力が小さくなり，安全率が大きくなる．横に傾いていない底面では，2つの向きは一致する．（→[2節](#columns-section-2)，[7節](#columns-section-7)）
:::

:::{dropdown} 問6（やってみよう）　地下水位を $z=4$ mの水平な線に置き，球のHovland法と3次元の簡易Bishop法の値を求めよ．実践2の地下水位のある値と比べるとどうか
:icon: question

`make_columns(columns.Ellipsoid(centre, (R, R, R)), 0.25, water_level=4.0)` で表を作る．Hovland法は1.336，3次元の簡易Bishop法は1.590になる．実践2の同じ地下水位の値は，Fellenius法が1.287，簡易Bishop法が1.388だった．Hovland法では，乾いたときと逆に，3次元の値が2次元より大きくなる．簡易Bishop法では，差が乾いたときの0.079から0.202に広がる．球の奥の断面は浅く，底面のうち地下水位より下にある部分が少ないので，間隙水圧の影響を受けにくいため．（→[6節](#columns-section-6)，[実践2 5節](#slices-section-5)）
:::

:::{dropdown} 問7（やってみよう）　球で，回転軸の基準点 $O$ を2 m上に動かすと，Hovland法，そのモーメントの形，3次元の簡易Bishop法の値はどう変わるか
:icon: question

基準点を `centre + np.array([0.0, 0.0, 2.0])` にして計算する．力の和で比をとるHovland法は，基準点を使わないので1.816のままである．モーメントの形は1.816から1.849に，3次元の簡易Bishop法は2.142から2.122に変わる．どちらも，水平方向の力のつり合いを満たしていないため．実践2 7節と同じく，中心を動かすとモーメントが $-\boldsymbol{a}\times\sum\boldsymbol{F}$ だけ変わる．すべり面の大きさに合わせて基準点が動く実装では，この影響が値に表れることがある．（→[4節](#columns-section-4)，[実践2 7節](#slices-section-7)）
:::

:::{dropdown} 問8　保存したカラムの表をほかの実装のソルバーに渡すとき，安全率を比べる前に何を確かめるか
:icon: question

- 法線の向き（すべり土塊の外向きか，上向きか）
- 局所すべり方向の決め方と，その向き（すべる向きか，抵抗する向きか）
- 間隙水圧の合力の書き方
- モーメントの基準点と回転軸の取り方
- 反復が収束しないときに返す値

（→[8節](#columns-section-8)）
:::

---

## 参考文献

1. Hovland, H. J. (1977). “Three-Dimensional Slope Stability Analysis Method.” *Journal of the Geotechnical Engineering Division*, 103(9), 971–986. [https://doi.org/10.1061/AJGEB6.0000493](https://doi.org/10.1061/AJGEB6.0000493)
2. Hungr, O. (1987). “An extension of Bishop's simplified method of slope stability analysis to three dimensions.” *Géotechnique*, 37(1), 113–117. [https://doi.org/10.1680/geot.1987.37.1.113](https://doi.org/10.1680/geot.1987.37.1.113)
