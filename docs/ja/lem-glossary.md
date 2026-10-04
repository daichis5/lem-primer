---
title: "用語集"
lang: ja
---

# 用語集

3つの資料で共通して使う用語と記号を，ここにまとめる．定義は，このシリーズでの使い方である．文献によっては，書き方や符号規約が違うことがある．

各項目の1行目には，記号と英語の用語を書いた．末尾の（→）は，その用語を説明している本文の節へのリンクである．

## すべり面と離散化

```{glossary}
すべり面
  slip surface

  斜面の中に仮定する，崩れるときにすべると想定した曲面．円弧，楕円体，複合面，自由曲面など，表し方は手法や実装によって違う．LEMは，この面を与えられたものとして，安全率を計算する（→[第1資料「LEMの全体像」](#overview)）

すべり土塊
  sliding mass

  すべり面より上の土の塊．すべり面に沿って動くと想定する（→[第1資料「LEMの全体像」](#overview)）

スライス
  slice

  2次元の解析で，すべり土塊を鉛直に分けた細片（→[第1資料「LEMの全体像」](#overview)）

カラム
  column

  3次元の解析で，すべり土塊を水平面内の2方向に分けた柱状の要素．スライスを3次元にしたもの（→[第1資料「LEMの全体像」](#overview)，[第2資料 7節](#what-section-7)）

空間の離散化
  spatial discretization

  連続的な形，荷重，応力の分布を，有限個のスライスやカラムと合力で表す操作（→[第1資料 9節](#section-9)，[第2資料 10節](#what-section-10)）

一般形状のすべり面
  general slip surface

  円弧に限らず，楕円，折れ線，複合面などの形をとるすべり面．任意形状のすべり面ともいう．ただし，スライスやカラムに分けられ，各底面の面積，法線，接線を定められるなどの条件が要る（→[第3資料 3節](#practice-section-3)，[4節](#practice-section-4)）

臨界すべり面
  critical slip surface

  探索したすべり面の族の中で，安全率が最小になる面．安全率の計算と，臨界すべり面の探索は，別の問題である（→[第3資料 12.4節](#practice-section-12-4)）
```

## 応力と強度

```{glossary}
応力テンソル
  $\boldsymbol{\sigma}$　stress tensor

  点ごとに定まる2階のテンソル．ある面に働く力そのものではなく，どの面に働く力も，ここから取り出せる（→[第1資料 1節](#section-1)，[2節](#section-2)）

表面力
  $\boldsymbol{t}$　traction

  ある面に働く，単位面積あたりの力のベクトル．応力テンソルと外向きの単位法線ベクトル $\boldsymbol{n}$ から，Cauchyの公式 $\boldsymbol{t}=\boldsymbol{\sigma}\boldsymbol{n}$ で決まる（→[第1資料 2節](#section-2)）

垂直応力
  $\sigma_n$　normal stress

  表面力の法線成分の大きさ．このシリーズでは，地盤工学の慣例に従い，圧縮を正とする（→[第1資料「記号と符号規約」](#notation)，[3節](#section-3)）

間隙水圧
  $u$　pore water pressure

  土の間隙を満たす水の圧力．等方的に働くので，表面力のせん断成分を直接は変えない（→[第1資料 4節](#section-4)）

有効垂直応力
  $\sigma_n'$　effective normal stress

  全垂直応力から間隙水圧を引いた値 $\sigma_n'=\sigma_n-u$．土粒子の骨格が実際に受け持つ垂直応力で，せん断強度を左右する（→[第1資料 4節](#section-4)）

Mohr–Coulomb則
  Mohr–Coulomb failure criterion

  今の有効垂直応力のもとで発揮できるせん断強度を，$\tau_f=c'+\sigma_n'\tan\phi'$ で与える破壊規準．$c'$ は有効粘着力，$\phi'$ は有効内部摩擦角（→[第1資料 5節](#section-5)）

せん断強度
  $\tau_f$　shear strength

  破壊するときに発揮できるせん断抵抗の上限．今働いているせん断応力ではない（→[第1資料 5節](#section-5)）

動員せん断応力
  $\tau_m$　mobilized shear stress

  つり合いを保つために，実際に働いているせん断応力．強度のうち，どれだけが使われているかを表す（→[第1資料 6節](#section-6)）
```

## 安全率

```{glossary}
安全率
  $F_s$　factor of safety

  {term}`せん断強度` $\tau_f$ と{term}`動員せん断応力` $\tau_m$ の比 $F_s=\tau_f/\tau_m$．標準的なLEMでは，すべり面全体で共通の1つの値と仮定する．入門的には，抵抗力と滑動力の比として説明する．ただし，実際に比をとる対象は手法によって違い，Fellenius法（簡便分割法）や簡易Bishop法では，円弧の中心まわりのモーメントの比になる（→[第1資料「LEMの全体像」](#overview)，[6節](#section-6)）

抵抗力
  resisting force

  すべりに抵抗する側の力．{term}`滑動力`と対にして，安全率を「抵抗力÷滑動力」と説明するときに使う（→[第1資料「LEMの全体像」](#overview)）

滑動力
  driving force

  すべり土塊をすべらせようとする側の力．自重のすべり面に沿う成分などにあたる．つり合っている土塊では，すべり面が動員しているせん断力と大きさが等しい（→[第1資料「LEMの全体像」](#overview)）
```

## スライス・カラムに働く力

```{glossary}
底面垂直力
  $N_i$　base normal force

  第 $i$ 要素の底面にわたって，{term}`全垂直応力 <垂直応力>`を面積分した値．すべり土塊に働く力は，ベクトルで書くと $-N_i\boldsymbol{n}_i$（→[第1資料 8節](#section-8)）

底面の間隙水圧の合力
  $U_i$　pore water force on the base

  第 $i$ 要素の底面にわたって，{term}`間隙水圧`を面積分した値．$N_i-U_i$ が有効垂直力になる（→[第1資料 8節](#section-8)）

底面せん断力
  $T_i$　base shear force

  第 $i$ 要素の底面で動員されているせん断力の大きさ．底面で発揮できる{term}`せん断強度`の合力を，{term}`安全率`で割った値（→[第1資料 8節](#section-8)）

内力
  internal force

  すべり土塊を分けた要素どうしが，その境界で互いに及ぼし合う力．LEMでは，スライス間力とカラム間力を指す．つり合い式だけでは，分布が決まらない（→[第2資料 2節](#what-section-2)，[3.1節](#what-section-3-1)）

スライス間力
  $E$，$X$　interslice force

  隣り合うスライスが互いに及ぼし合う内力．2次元では，境界の面に垂直な成分 $E$（スライス間の垂直力）と，せん断成分 $X$ に分ける．3次元では，2方向の境界のそれぞれで考え，カラム間力と呼ぶ（→[第2資料 2節](#what-section-2)，[7.2節](#what-section-7-2)）
```

## 不静定性と手法

```{glossary}
静力学的不静定性
  static indeterminacy

  未知量の数が独立なつり合い式の数より多く，つり合いだけでは{term}`内力`の分布が一意に決まらない状態（→[第2資料 3.1節](#what-section-3-1)）

不静定性の解消
  closure

  内力の一部を無視する，内力の向きや成分の比を仮定する，使うつり合いの条件を一部に限る，といった仮定を加えて，問題を解ける形にする操作．LEMの各手法の違いは，主にここにある（→[第1資料 9節](#section-9)，[第2資料 3.3節](#what-section-3-3)）

簡便法
  simplified method

  内力の一部や，満たすつり合いの条件の一部を省く手法の総称．Fellenius法，簡易Bishop法，簡易Janbu法など．名前が似た簡便分割法は，このうちのFellenius法だけを指す（→[第2資料 4節](#what-section-4)，[6節](#what-section-6)）

静力学的に完全な方法
  complete equilibrium method

  内力の向きを仮定したうえで，力とモーメントのつり合いをすべて満たす手法．Spencer法，Morgenstern–Price法など．厳密法（rigorous method）とも呼ぶ．ただし，ここでの「完全」や「厳密」は，仮定した内力のモデルの中での話で，連続体としての厳密解という意味ではない（→[第2資料 5.1節](#what-section-5-1)）

GLE
  general limit equilibrium

  一般極限平衡法．Morgenstern–Price法と同じく，{term}`スライス間力`のせん断成分と垂直成分の比を $X/E=\lambda f(x)$ で表し，力とモーメントのつり合いをともに満たす枠組み．このシリーズでは，Morgenstern–Price法と同じ系統として扱う（→[第2資料 5.2節](#what-section-5-2)，[8.4節](#what-section-8-4)）
```

## モーメントの中心とすべり方向

```{glossary}
モーメントの中心
  centre of moments

  モーメントのつり合いを考える基準の点．円弧では，円弧の中心を使う．3次元では，どの軸（回転軸）のまわりのつり合いを使うかも決める．力のつり合いをすべては満たさない手法では，選び方によって安全率が変わることがある（→[第3資料 6節](#practice-section-6)）

全体すべり方向
  $\boldsymbol{d}$　direction of sliding

  3次元で，すべり土塊全体が動くと仮定した代表の向き．安全率を左右する，定式化の中の変数で，結果を見せるための矢印ではない（→[第3資料 8節](#practice-section-8)，[9節](#practice-section-9)）

局所すべり方向
  $\boldsymbol{m}_i$　local direction of sliding

  各カラムの底面の接平面内で仮定した，すべりの向き．{term}`全体すべり方向`を，底面の接平面に射影して定める方法などがある（→[第3資料 8節](#practice-section-8)）
```
