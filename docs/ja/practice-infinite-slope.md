---
title: "無限斜面の安全率を計算する：表面力の分解から安全率までを，コードでたどる"
lang: ja
series: "practice 1 of 3"
---

# 無限斜面の安全率を計算する

**表面力の分解から安全率までを，コードでたどる**

この実践では，無限斜面の安全率を求めるPythonのコードを作成する．無限斜面は，同じ傾きの斜面がどこまでも続くとみなす，最も単純な斜面のモデルである．安全率の式はよく知られているが，ここでは第1章の筋道に沿って，すべり面に働く表面力を法線成分とせん断成分に分解するところから組み立てる．作った関数は，実践2と実践3で答えを確認するときにも使う．

この実践は，[第1章](continuum-mechanics-to-lem-start.md)を読んだ前提で進める．用語と記号は，[用語集](lem-glossary.md)にまとめている．

(infinite-goal)=

## 作るもの

傾き $\beta$ の地表から鉛直に深さ $z$ のところに，地表に平行な{term}`すべり面`を仮定し，その{term}`安全率` $F_s$ を求める．土の定数は，[第1章 6節](#section-6)と同じ $c'=10$ kPa，$\phi'=30^\circ$ とする．単位体積重量は $\gamma=18$ kN/m³ で，地下水位より下の土では $\gamma_{sat}=20$ kN/m³ である．実践2と実践3も，同じ $c'$，$\phi'$，$\gamma$ を使う．

```{figure} ./figures/fig_e1_infinite_slope.svg
:name: fig-e1-infinite-slope
:alt: 無限斜面から取り出した柱に働く自重，すべり面の垂直力とせん断力，両側の面の力と，地下水位があるときのすべり面の間隙水圧の2つの算定方法

無限斜面の柱に働く力と，すべり面の間隙水圧

左：両側の面の力は打ち消し合うので，自重 $W$ を，すべり面の垂直力 $N$ とせん断力 $T$ が支える．右：地下水位がすべり面から鉛直に $h_w$ の高さにあるときの，すべり面の点 P の間隙水圧を示す．斜面に平行に浸透するときは，P を通る等ポテンシャル線が斜面に直交する．
```

座標は，$x$ 軸を水平右向き，$z$ 軸を鉛直上向きにとる．すべり面の深さ $z$ は，この座標ではなく，地表から鉛直下向きに測った長さである．この座標で，地表は右に上がり，土塊は左下へすべる．すべり面の単位法線ベクトル $\boldsymbol{n}$ は，第1章と同じく{term}`すべり土塊`の外向きで，すべり面より下の地盤の側を向く．すべる向きの単位ベクトルが $\boldsymbol{m}$ である．

作る関数は，次の6つである．

| 関数 | 求めるもの | 節 |
|---|---|---|
| `plane_vectors` | すべり面の $\boldsymbol{n}$ と $\boldsymbol{m}$ | 1節 |
| `split_traction` | 表面力の法線成分とせん断成分 | 2節 |
| `base_stresses` | 柱の重さによる，すべり面の $\sigma_n$ と $\tau$ | 2節 |
| `factor_of_safety` | 安全率 $F_s$ | 3節 |
| `column_weight` | 地下水位があるときの柱の重さ | 4節 |
| `pore_pressure` | すべり面の間隙水圧の2つの算定方法 | 4節 |

(infinite-setup)=

## 準備

Python 3.11以上と，NumPyとpytestを使う．ここでは，Pythonの環境を作る道具uvを使い，実践1から実践3までのコードを1つのフォルダ `lem-practice` に置く．

```bash
uv init --bare --python 3.12 lem-practice
cd lem-practice
uv python pin 3.12
uv add numpy
uv add --dev pytest
```

1. フォルダ `lem-practice` を作り，その中に，プロジェクトの設定ファイル `pyproject.toml` だけを作る
2. 作ったフォルダに移る．この後のファイルはここに置き，コマンドもここで実行する
3. このプロジェクトで使うPythonを，3.12に固定する
4. 計算に使うNumPyを追加する
5. テストに使うpytestを追加する．`--dev` は，開発のときだけ使う道具として区別して記録する指定

uvを使わないときは，フォルダ `lem-practice` を作って移り，Python 3.11以上で仮想環境（`python3 -m venv .venv`）を作って有効にする．そのうえで `pip install numpy pytest` を実行し，この後のコマンドから `uv run` を外す．この実践のコードは，{download}`infinite_slope.py <examples/infinite_slope.py>` と {download}`test_infinite_slope.py <examples/test_infinite_slope.py>` にまとめてある．自分で実装したコードが動作しないときは，これらと比較するとよい．

---

(infinite-section-1)=

## 1. すべり面の向きを決定する

傾き $\beta$ のすべり面では，外向きの単位法線ベクトルと，すべる向きの単位ベクトルが次のようになる．

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

$\boldsymbol{n}$ は右下を向き，すべり面より下の地盤を指す．$\boldsymbol{m}$ は，すべり面に沿って左下を向く．2つは直交するので，$\boldsymbol{n}\cdot\boldsymbol{m}=0$ である．`infinite_slope.py` を作り，最初に次を記述する．

```{literalinclude} examples/infinite_slope.py
:language: python
:end-at: GAMMA_W =
```

続けて，式 {eq}`eq-infinite-vectors` を関数にする．角度は度で受け取り，`math.radians` でラジアンに変換する．

```{literalinclude} examples/infinite_slope.py
:language: python
:pyobject: plane_vectors
```

---

(infinite-section-2)=

## 2. すべり面の表面力を分解する

[第1章 3節](#section-3)で見たように，外向きの単位法線ベクトルが $\boldsymbol{n}$ の面に働く{term}`表面力`（traction） $\boldsymbol{t}$ は，圧縮を正とする{term}`垂直応力` $\sigma_n=-\boldsymbol{n}\cdot\boldsymbol{t}$ と，接平面内のせん断成分 $(\boldsymbol{I}-\boldsymbol{n}\boldsymbol{n}^{\mathsf T})\boldsymbol{t}$ に分解できる．これを関数にする．

```{literalinclude} examples/infinite_slope.py
:language: python
:pyobject: split_traction
```

次に，すべり面に働く表面力を求める．無限斜面から幅1 m，奥行き1 mの柱を1本取り出すと，柱の両側の面には，隣の柱から力が働く．しかし，斜面はどこまでも同じなので，左右の面の力は大きさが同じで，向きが逆になる．そのため，2つの力は打ち消し合い，柱の重さはすべて，すべり面より下の地盤が支える（図の左）．つまり，無限斜面では，{term}`スライス間力`を仮定しなくても，つり合いだけで底面の力が定まる．[第2章 3.1節](#what-section-3-1)で扱う{term}`静力学的不静定性`は，ここには現れない．

柱の水平面積あたりの重さを $w$ とする．乾いた土なら $w=\gamma z$ である．幅1 m，奥行き1 mの柱の重さは，$w$ [kN] になる．その下のすべり面の面積は $1/\cos\beta$ [m²] なので，地盤が柱を支える表面力は次のようになる．

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

これを `split_traction` で分解すると，垂直応力とせん断応力は次の値になる．

$$
\sigma_n=w\cos^2\beta,
\qquad
\tau=w\sin\beta\cos\beta
$$ (eq-infinite-stresses)

コードでは，式 {eq}`eq-infinite-traction` のとおりに，柱の重さをベクトルで表してから面積で割る．

```{literalinclude} examples/infinite_slope.py
:language: python
:pyobject: base_stresses
```

ここまでを，テストで確認する．`test_infinite_slope.py` を作り，最初に次を記述する．

```{literalinclude} examples/test_infinite_slope.py
:language: python
:end-at: import infinite_slope
```

続けて，2つのテストを実装する．1つ目は，押す成分と抵抗する成分を組み合わせた表面力が，元の2つの成分に分解できることを確認する．2つ目は，式 {eq}`eq-infinite-stresses` と比較するテストである．

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

`2 passed` と表示されれば，2つのテストが通っている．`pytest.approx` は，丸め誤差を許して値を比較する記法である．

---

(infinite-section-3)=

## 3. 安全率を求める

{term}`せん断強度`は，[第1章 5節](#section-5)の{term}`Mohr–Coulomb則`から，$\tau_f=c'+(\sigma_n-u)\tan\phi'$ と表せる．安全率は，[第1章 6節](#section-6)のとおり，$\tau_f$ と{term}`動員せん断応力` $\tau_m$ の比である．無限斜面では，2節の $\tau$ が $\tau_m$ にあたる．

$$
F_s=\frac{c'+(\sigma_n-u)\tan\phi'}{\tau}
$$ (eq-infinite-fs)

```{literalinclude} examples/infinite_slope.py
:language: python
:pyobject: factor_of_safety
```

乾いた斜面（$u=0$）で，$\beta=30^\circ$，$z=5$ mのときを計算する．$w=\gamma z=90$ kPa なので，式 {eq}`eq-infinite-stresses` から $\sigma_n=67.50$ kPa，$\tau=38.97$ kPa である．$\beta=\phi'$ のときは，摩擦による抵抗 $\sigma_n\tan\phi'$ が $\tau$ とちょうど等しい．そのため，$F_s$ は1に粘着力の分を加えた $1+10/38.97=1.257$ になる．

[第1章 6節](#section-6)の「数値でたどる」の底面も，無限斜面の底面とみなせる．そこでは $\sigma_n=100$ kPa，$\tau_m=30$ kPa だったので，式 {eq}`eq-infinite-stresses` の比 $\tau/\sigma_n=\tan\beta$ から，傾きは $\beta=16.70^\circ$ である．$w=\sigma_n/\cos^2\beta=109.0$ kPa とすれば，そこでの $F_s=1.49$（$u=40$ kPa）と1.10（$u=60$ kPa）が，そのまま出る．この2つの値と，粘着力のない乾いた砂が $\beta=\phi'$ でちょうど $F_s=1$ になることを，テストに追加する．

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

## 4. 地下水位を考慮する

地下水位が，すべり面から鉛直に測って $h_w$ の高さにあるとする（図の右）．地下水位より下の土の単位体積重量は $\gamma_{sat}$ なので，柱の水平面積あたりの重さは $w=\gamma(z-h_w)+\gamma_{sat}h_w$ である．

```{literalinclude} examples/infinite_slope.py
:language: python
:pyobject: column_weight
```

すべり面の{term}`間隙水圧` $u$ は，地下水の流れをどう仮定するかで算定方法が異なる．

- **斜面に平行な浸透**：地下水が斜面に平行に流れるとき，流れに直交する等ポテンシャル線は，斜面に直交する．等ポテンシャル線の上では，全水頭が等しい．すべり面の点 P を通る等ポテンシャル線が地下水位と交わる点では，水圧が0なので，全水頭はその点の高さになる．P からその点までの，斜面に直交する距離は $h_w\cos\beta$ で，その鉛直成分は $h_w\cos^2\beta$ になる．これが P の圧力水頭なので，$u=\gamma_w h_w\cos^2\beta$ である
- **鉛直の静水圧**：地下水位から鉛直に測った深さで，静水圧とする．$u=\gamma_w h_w$ である．これは，等ポテンシャル線を鉛直とみなすことにあたる．地下水位を線で与える{term}`LEM <極限平衡法>`のプログラムには，この算定方法を使うものがある．地下水位が傾いていれば実際には水が流れるので，斜面に平行な浸透の $1/\cos^2\beta$ 倍の $u$ を与えることになる

```{literalinclude} examples/infinite_slope.py
:language: python
:pyobject: pore_pressure
```

地下水位が地表にあるとき（$h_w=z=5$ m，$\beta=30^\circ$）を比較する．$w=\gamma_{sat}z=100$ kPa なので，$\sigma_n=75.00$ kPa，$\tau=43.30$ kPa である．斜面に平行な浸透では，$u=36.79$ kPa で $F_s=0.740$ になる．一方，鉛直の静水圧では $u=49.05$ kPa で，$F_s$ は0.577まで下がる．つまり，同じ地下水位でも，間隙水圧の算定方法だけで，安全率が2割以上異なる．2つの算定方法の比が $\cos^2\beta$ になることを，テストで確認する．

```{literalinclude} examples/test_infinite_slope.py
:language: python
:pyobject: test_the_two_water_rules_differ_by_cos_squared
```

---

(infinite-section-5)=

## 5. 有効垂直応力が負になるとき

地下水位が地表にあるとき，2つの算定方法の{term}`有効垂直応力` $\sigma_n-u$ は，式 {eq}`eq-infinite-stresses` から次のようになる．

$$
\text{斜面に平行な浸透：}
(\gamma_{sat}-\gamma_w)z\cos^2\beta,
\qquad
\text{鉛直の静水圧：}
(\gamma_{sat}\cos^2\beta-\gamma_w)z
$$ (eq-infinite-effective)

前者は，どの傾きでも正である．後者は，$\cos^2\beta<\gamma_w/\gamma_{sat}$ のとき負になる．$\gamma_{sat}=20$ kN/m³ では，$\beta>45.5^\circ$ がそれにあたる．

有効垂直応力が負になるのは，すべり面の土の骨格が引張を受けている状態である．土は引張をほとんど伝えないので，このまま計算しても力学的な意味はない．`factor_of_safety` は式 {eq}`eq-infinite-fs` のとおりに計算するため，摩擦の項が負になり，粘着力による抵抗を打ち消す向きに働く．急な斜面では，安全率そのものが負になることがある．[第3章 12.1節](#practice-section-12-1)にあるように，負の値を0とみなすか，テンションクラック（引張亀裂）を設けるかといった扱いは，別に決定しなければならない．鉛直の静水圧のときだけ負になることを，テストに追加する．

```{literalinclude} examples/test_infinite_slope.py
:language: python
:pyobject: test_only_the_vertical_rule_makes_the_effective_stress_negative
```

---

(infinite-section-6)=

## 6. 条件を変えて表示する

ここまでの関数を使い，条件を変えた値をまとめて表示する．{download}`run_infinite_slope.py <examples/run_infinite_slope.py>` をダウンロードして `lem-practice` に置き，実行する．

```bash
uv run python run_infinite_slope.py
```

```{literalinclude} examples/output/run_infinite_slope.txt
:language: text
```

1.から4.は，3節から5節で見た値である．5.では，地下水位を地表から2 mの深さに置き，すべり面の深さ $z$ を変えた．どの列でも，深いすべり面ほど安全率が小さい．$\sigma_n$ と $\tau$ はどちらも $z$ とともに増加するが，粘着力による抵抗 $c'$ は深さによらないからである．地下水位より深いところでは，間隙水圧が加わるので，さらに下がる．

つまり，無限斜面のモデルでは，すべり面を深くするほど安全率が下がり続ける．そのため，岩盤までの土の厚さのように，すべり面の深さの上限を別に与えなければならない．深さを変えて最も小さい安全率を探すことは，最も単純な{term}`臨界すべり面`の探索にあたる．[第3章 12.4節](#practice-section-12-4)にあるように，安全率の計算と，臨界すべり面の探索は，別の問題である．最後に，深いすべり面ほど安全率が小さいことを，テストに追加する．

```{literalinclude} examples/test_infinite_slope.py
:language: python
:pyobject: test_a_deeper_plane_is_less_stable
```

`uv run pytest` で `7 passed` と表示されれば，この実践のテストがすべて通っている．

---

(infinite-trouble)=

## 困ったとき

| 表示や様子 | 原因と対処 |
|---|---|
| `ModuleNotFoundError: No module named 'infinite_slope'` | `lem-practice` の外で実行しているか，ファイルの名前が異なる．`lem-practice` に移り，`infinite_slope.py` があることを確認する．（→[準備](#infinite-setup)） |
| `ModuleNotFoundError: No module named 'numpy'` | `uv run` を付けずに，NumPyのない環境のPythonで実行している．`uv run python …` や `uv run pytest` のように実行する．（→[準備](#infinite-setup)） |
| `AttributeError: module 'infinite_slope' has no attribute …` | テストが使う関数を，まだ `infinite_slope.py` に実装していない．関数の名前の綴りも確認する．（→[1節](#infinite-section-1)から[4節](#infinite-section-4)） |
| `ValueError: h_w は 0 以上 z 以下にする` | `column_weight` に，すべり面より下か，地表より上の地下水位を渡している．（→[4節](#infinite-section-4)） |
| 安全率が負になる，または表の値と大きく異なる | 角度を度のまま `math.sin`，`math.cos`，`math.tan` に渡していないかを確認する．`math.radians` でラジアンに変換する．（→[1節](#infinite-section-1)） |
| 安全率が表の値と少し異なる | 水の単位体積重量 `GAMMA_W` を，9.81 kN/m³にしているかを確認する．（→[1節](#infinite-section-1)，[4節](#infinite-section-4)） |

## まとめ

- すべり面の表面力は，外向きの単位法線ベクトルを使って，圧縮を正とする垂直応力とせん断成分に分解できる（→[2節](#infinite-section-2)）
- 無限斜面では，柱の両側の面の力が打ち消し合う．そのため，スライス間力を仮定しなくても，つり合いだけで底面の力が定まる（→[2節](#infinite-section-2)）
- 安全率は，せん断強度と動員せん断応力の比である．第1章 6節の底面の $\sigma_n$ と $\tau_m$ は，傾き16.70°の無限斜面の底面で得られる（→[3節](#infinite-section-3)）
- 間隙水圧は，地下水の流れの仮定で算定方法が異なる．斜面に平行な浸透と鉛直の静水圧の $u$ の比は，$\cos^2\beta$ である（→[4節](#infinite-section-4)）
- 鉛直の静水圧では，急な斜面で有効垂直応力が負になる．その扱いは，別に決定しなければならない（→[5節](#infinite-section-5)）
- 粘着力があると，深いすべり面ほど安全率が小さい．すべり面の深さの上限は，別に与えなければならない（→[6節](#infinite-section-6)）

---

## 確認問題

答えは問題をクリックすると開く．（やってみよう）は，`lem-practice` で取り組む．

:::{dropdown} 問1　無限斜面では，スライス間力を仮定しなくても，底面の力が定まるのはなぜか
:icon: question

柱の両側の面に働く力が，大きさが同じで向きが逆になり，打ち消し合うため．斜面がどこまでも同じなので，左右の面の状態も同じになる．そのため，柱の重さはすべてすべり面が支え，つり合いだけで $\sigma_n$ と $\tau$ が定まる．（→[2節](#infinite-section-2)）
:::

:::{dropdown} 問2　乾いた斜面で $\beta=25^\circ$，$z=3$ mのとき，$\sigma_n$，$\tau$，$F_s$ を求めよ．ほかの条件は3節と同じとする
:icon: question

$w=18\times3=54$ kPa なので，$\sigma_n=54\cos^2 25^\circ=44.36$ kPa，$\tau=54\sin 25^\circ\cos 25^\circ=20.68$ kPa である．$F_s=(10+44.36\tan 30^\circ)/20.68=1.722$ になる．`base_stresses(25.0, 54.0)` を `factor_of_safety` に渡しても，同じ値が出る．（→[2節](#infinite-section-2)，[3節](#infinite-section-3)）
:::

:::{dropdown} 問3（やってみよう）　地震時の慣性力として，すべる向きに水平な力 $kw$ を柱に加える．これを考慮した `base_stresses` を作り，3節の乾いた斜面で $k=0.2$ のときの $F_s$ を求めよ
:icon: question

柱の重さのベクトルに，すべる向き（$x$ の負の向き）の成分 $-kw$ を加える．`test_infinite_slope.py` の末尾に，次の関数を実装する．

```{literalinclude} examples/test_answers.py
:language: python
:pyobject: base_stresses_seismic
```

実装したら，`uv run python` でPythonを起動し，`from test_infinite_slope import base_stresses_seismic` として呼び出す．`base_stresses_seismic(30.0, 90.0, 0.2)` は $\sigma_n=59.71$ kPa，$\tau=52.47$ kPa を返し，$F_s=0.848$ になる．$k=0.1$ では1.022である．水平な力は，すべり面を押す成分を減少させ，すべらせる成分を増加させる．そのため，安全率の分子では $\sigma_n$ が下がり，分母では $\tau$ が上がる．（→[2節](#infinite-section-2)）
:::

:::{dropdown} 問4　同じ地下水位でも，斜面に平行な浸透と鉛直の静水圧で，間隙水圧が異なるのはなぜか
:icon: question

等ポテンシャル線の向きの仮定が異なるため．斜面に平行に浸透するときは，等ポテンシャル線が斜面に直交する．そのため，すべり面の点の圧力水頭は，その点を通る等ポテンシャル線が地下水位と交わる点との高さの差 $h_w\cos^2\beta$ になる．鉛直の静水圧は，等ポテンシャル線を鉛直とみなすことにあたる．つまり，地下水位までの鉛直の距離 $h_w$ が，そのまま圧力水頭になる．（→[4節](#infinite-section-4)）
:::

:::{dropdown} 問5（やってみよう）　有効垂直応力が負のとき0とみなすと，地下水位が地表にある $\beta=50^\circ$，$z=5$ mの斜面で，鉛直の静水圧の $F_s$ はどう変わるか
:icon: question

`factor_of_safety` に，$u$ の代わりに `min(u, sigma_n)` を渡す．こうすると，$\sigma_n-u$ が負のときだけ0になる．$\sigma_n-u=-7.73$ kPa なので，そのままでは $F_s=0.112$ だが，0とみなすと0.203になる．0とみなした後は，粘着力だけが抵抗する．（→[5節](#infinite-section-5)）
:::

:::{dropdown} 問6　粘着力のない乾いた斜面（$c'=0$）では，すべり面の深さで安全率は変わるか
:icon: question

変わらない．$c'=0$ なら $F_s=\tan\phi'/\tan\beta$ で，$z$ が式から消えるため．例えば $\phi'=35^\circ$，$\beta=30^\circ$ では，どの深さでも $F_s=1.213$ になる．（→[6節](#infinite-section-6)）
:::

---

## 次に読む

この実践では，1本の柱のつり合いだけで，すべり面の力が定まるモデルを扱った．円弧のすべり面では，{term}`スライス`ごとに底面の向きが異なり，スライス間力が打ち消し合わない．各手法の{term}`不静定性の解消`（closure）の仕方を，[実践2「スライス法で円弧すべりの安全率を計算する」](practice-slices-2d.md)でコードにする．平面のすべり面では，この実践の値に戻ることも確認する．
