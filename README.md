# LEM Primer

A primer on the **limit equilibrium method** (LEM) for slope stability: from the
stress tensor of continuum mechanics through to reading the numbers a solver
reports.

The primer is written for readers who have not studied LEM before, and is
independent of any particular analysis software.

| Edition | Status |
|---|---|
| [Japanese (日本語)](https://ibaraki-kozo-lab.github.io/lem-primer/ja/) | Complete, and the source (`docs/ja/`) |
| [English](https://ibaraki-kozo-lab.github.io/lem-primer/en/) | A translation of the Japanese at the commit each page records (`docs/en/`); brought in line on request |

## Contents

Each title is the English edition's, with the Japanese edition's in
parentheses.

**Theory**

1. **Chapter 1: From continuum mechanics to where the limit equilibrium
   method begins** (第1章　連続体力学から極限平衡法の出発点まで) — how
   stress and a failure criterion become the forces $N_i$, $U_i$, $T_i$ on a
   slice base
2. **Chapter 2: What is the limit equilibrium method?**
   (第2章　極限平衡法とは何か) — what assumptions each method uses to
   determine the unknowns that equilibrium leaves
3. **Chapter 3: Using the limit equilibrium method in practice**
   (第3章　極限平衡法を実際に使うとき) — general slip surfaces, the
   direction of sliding, discretization, and how to read a result

**Practice**

1. **Practice 1: Computing the factor of safety of an infinite slope**
   (実践1　無限斜面の安全率を計算する) — from splitting the traction to the
   factor of safety
2. **Practice 2: Computing the factor of safety of a circular slip with the
   method of slices** (実践2　スライス法で円弧すべりの安全率を計算する) —
   Fellenius, simplified Bishop, simplified Janbu and Spencer on one circle
3. **Practice 3: Computing the factor of safety of a 3D slip surface with
   the method of columns** (実践3　カラム法で3次元のすべり面の安全率を計算する)
   — Hovland and 3D simplified Bishop on one ellipsoid

The practice pages write the methods in Python; Practices 2 and 3 check
their values against the earlier practices.

**Appendix**

- **Glossary** (用語集) — the terms and symbols the pages share

## Building locally

```bash
uv sync --group docs --group examples   # or, with pip 25.1+: pip install --group docs --group examples
make examples             # runs the practice code: outputs and tests
make all                  # builds _site/ja and _site/en
make preview              # builds both, then opens the Japanese edition
make serve                # builds, then serves it at http://localhost:8000/
```

The practice pages include the code under `docs/ja/examples` (and its English
copy, `docs/en/examples`) and what its `run_*.py` scripts print, from
`output/` beside it. `make examples` writes those outputs and runs the tests;
run it after changing the code, and before `make figures`, which plots one of
the outputs.

`make ja` and `make en` build a single edition, and goals chain, so `make ja
open` builds just that edition and opens it. `make preview` is `all` plus
`open` in one word (`EDITION=en` on either one opens the English edition
instead).

Both open the edition's page directly rather than `_site/index.html`, because
that root page redirects to `./ja/` and only a web server resolves that to an
index page. `make serve` is therefore the faithful check before pushing: over
HTTP the redirect, the clean URLs, and search all behave as they will on Pages.

Each language is a separate Sphinx project under `docs/`, because Sphinx
resolves `language` once per build; settings that do not depend on the language
live in `docs/_shared_conf.py`.

## Related

One implementation of the method described here is the slope-stability
codebase [LEM Lab](https://github.com/ibaraki-kozo-lab/lem-lab).

## License

Text and figures are released under
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
