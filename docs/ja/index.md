---
title: "LEM入門"
lang: ja
---

# LEM入門

**極限平衡法の基礎から実際の使われ方まで**

極限平衡法（limit equilibrium method，LEM）は，斜面の安定性を評価する方法として，最も広く使われている．しかし，教科書に載っている安全率の式を見ただけでは，その式をどう導くのか，何が仮定されているのか，どこまでが適用範囲なのかは分かりにくい．

この資料は，LEMをまだ学んだことがない人が，連続体力学の応力から出発して，実際の解析結果を読み解くところまでを，1本の道筋で辿れるようになるための資料である．理論編の3つの章と，それをコードで確かめる実践編，用語集などの付録からなる．

```{toctree}
:maxdepth: 1
:hidden:
:caption: 理論編

continuum-mechanics-to-lem-start
what-is-limit-equilibrium-method
lem-in-practice-mechanical-perspective
```

```{toctree}
:maxdepth: 1
:hidden:
:caption: 実践編

practice-infinite-slope
practice-slices-2d
practice-columns-3d
```

```{toctree}
:maxdepth: 1
:hidden:
:caption: 付録

lem-glossary
three-dimensional-equilibrium
```

## 理論編

::::{grid} 1
:gutter: 2

:::{grid-item-card} 第1章　連続体力学から極限平衡法の出発点まで
:link: continuum-mechanics-to-lem-start
:link-type: doc

応力と破壊規準は，底面の力にどう変わるか
:::

:::{grid-item-card} 第2章　極限平衡法とは何か
:link: what-is-limit-equilibrium-method
:link-type: doc

残った未知量を決めるために，各手法はどのような仮定を用いるか
:::

:::{grid-item-card} 第3章　極限平衡法を実際に使うとき
:link: lem-in-practice-mechanical-perspective
:link-type: doc

円弧以外のすべり面，すべり方向，離散化をどう読み解くか
:::

::::

理論編は，第1章から順に読むことを想定している．各章は，本文と折りたたんだ補足からなっている．補足には，式の展開や符号規約の細部を書いている．用語と記号は，[用語集](lem-glossary.md)にまとめている．

## 実践編

::::{grid} 1
:gutter: 2

:::{grid-item-card} 実践1　無限斜面の安全率を計算する
:link: practice-infinite-slope
:link-type: doc

表面力の分解から，無限斜面の安全率までを求める
:::

:::{grid-item-card} 実践2　スライス法で円弧すべりの安全率を計算する
:link: practice-slices-2d
:link-type: doc

1つの円弧について，4つの手法の安全率と，つり合いの残差を求める
:::

:::{grid-item-card} 実践3　カラム法で3次元のすべり面の安全率を計算する
:link: practice-columns-3d
:link-type: doc

楕円体のすべり面について，カラムの表を作り，3次元の安全率を求める
:::

::::

実践編では，PythonとNumPyでコードを書き，理論編で見た式と考え方を，数値で確かめる．実践2と実践3の値は，平面のすべり面で無限斜面に戻すなどして，1つ前の実践の値で確かめる．実践1は第1章を読めば始められ，実践2と実践3は，第3章までを読んでから進めるとよい．

## このシリーズについて

このシリーズは，特定の解析ソフトウェアによらない，LEMの一般的な解説である．実装の一例として，斜面安定解析のコード[LEM Lab](https://github.com/ibaraki-kozo-lab/lem-lab)がある．
