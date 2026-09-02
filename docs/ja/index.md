---
title: "LEM Primer（日本語）"
lang: ja
---

# LEM Primer

## 極限平衡法を，基礎から実務での読み方まで

<a href="../en/index.html">English</a>

極限平衡法（limit equilibrium method; LEM）は，斜面の安定性を評価する最も広く使われる手法である．一方で，教科書に載る安全率の式だけを見ても，その式がどこから来て，何を仮定し，何を保証しないのかは分かりにくい．

このシリーズは，**LEMをまだ学んだことがない読者**を対象に，連続体力学の応力から出発して，実際の解析結果を読むところまでを一本の道筋としてつなぐことを目的とする．3つの資料と，共通の用語集からなる．

```{toctree}
:maxdepth: 1

continuum-mechanics-to-lem-start
what-is-limit-equilibrium-method
lem-in-practice-mechanical-perspective
lem-glossary
```

## 各資料の役割

| 資料 | 中心となる問い |
|---|---|
| 1. [連続体力学から極限平衡法のスタート地点まで](continuum-mechanics-to-lem-start.md) | 応力と破壊規準は，底面の力へどう変換されるか |
| 2. [極限平衡法とは何か](what-is-limit-equilibrium-method.md) | 残った未知量を，各手法はどの仮定で決めるか |
| 3. [極限平衡法を実際に使うとき](lem-in-practice-mechanical-perspective.md) | 任意形状，すべり方向，離散化をどう解釈するか |

用語と記号の定義は[用語集](lem-glossary.md)にまとめている．

## 読み方

第1資料から順に読むことを想定しているが，各資料は独立しても読める．すでにスライス法を知っている読者は，第2資料から始めてもよい．

各資料は，本文と折りたたみの補足で構成される．補足は式展開や符号規約の詳細で，初読では飛ばしてよい．

## この資料について

本シリーズは特定の解析ソフトウェアに依存しない，一般的なLEMの解説である．実装の一例としては，斜面安定解析コードベース [LEM Lab](https://github.com/daichis5/lem-lab) を参照．
