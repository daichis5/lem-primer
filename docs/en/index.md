---
title: "LEM Primer"
lang: en
---

# LEM Primer

## The limit equilibrium method, from first principles to reading real results

```{admonition} Under construction
:class: warning

The English edition is being prepared. The complete series is currently
available in Japanese only.

<a href="../ja/index.html">Read the Japanese edition</a>
```

## What this series covers

The limit equilibrium method (LEM) is the most widely used approach for
assessing slope stability. Textbook factor-of-safety formulas, however, rarely
explain where those formulas come from, what they assume, and what they do not
guarantee.

This series is written for readers who have not studied LEM before. It follows a
single thread from the stress tensor of continuum mechanics through to the
practical question of how to read the numbers a solver reports.

| Document | Central question |
|---|---|
| 1. From continuum mechanics to where LEM begins | How do stress and a failure criterion become forces on a slice base? |
| 2. What the limit equilibrium method is | Which assumption does each method use to close the remaining unknowns? |
| 3. Using the limit equilibrium method in practice | How should general slip surfaces, sliding direction, and discretization be interpreted? |

A shared glossary accompanies the three documents.

## About

This series is independent of any particular analysis software. For one
implementation, see the slope-stability codebase
[LEM Lab](https://github.com/daichis5/lem-lab).
