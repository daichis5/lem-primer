# LEM Primer

A primer on the **limit equilibrium method** (LEM) for slope stability: from the
stress tensor of continuum mechanics through to reading the numbers a solver
reports.

The series is written for readers who have not studied LEM before, and is
independent of any particular analysis software.

| Edition | Status |
|---|---|
| 日本語 | Complete (3 documents + 3 practice pages + glossary) |
| English | Under construction |

## Contents

1. **連続体力学から極限平衡法の出発点まで** — how stress and a failure
   criterion become the forces $N_i$, $U_i$, $T_i$ on a slice base
2. **極限平衡法とは何か** — which assumption each method uses to close the
   remaining static indeterminacy
3. **極限平衡法を実際に使うとき** — general slip surfaces, sliding direction,
   discretization, and how to read a result
4. **実践編** — three practice pages that write the methods in Python: the
   infinite slope, slices on one circle (Fellenius, simplified Bishop and
   Janbu, Spencer), and columns on one ellipsoid (Hovland, 3D simplified
   Bishop); the second and third check their values against the one before
5. **用語集** — shared glossary of terms and symbols

## Building locally

```bash
uv sync --group docs --group examples   # or, with pip 25.1+: pip install --group docs --group examples
make examples             # runs the practice code: outputs and tests
make all                  # builds _site/ja and _site/en
make preview              # builds both, then opens the Japanese edition
make serve                # builds, then serves it at http://localhost:8000/
```

The practice pages include the code under `docs/ja/examples` and what its
`run_*.py` scripts print, from `docs/ja/examples/output`. `make examples`
writes those outputs and runs the tests; run it after changing the code, and
before `make figures`, which plots one of the outputs.

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
