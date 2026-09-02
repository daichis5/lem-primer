"""Settings shared by the per-language Sphinx projects under ``docs/``.

Sphinx resolves ``language`` once per build, so each language gets its own
``conf.py``; everything that does not depend on the language lives here.
"""

project = "LEM Primer"
author = "daichis5"
copyright = "2026, daichis5"
release = "0.1.0"

extensions = [
    "myst_parser",
    "sphinx_design",
    "sphinx.ext.mathjax",
]

myst_enable_extensions = ["dollarmath", "amsmath", "colon_fence"]
myst_heading_anchors = 6

# Auto-number captioned figures so pages can cite them with ``{numref}``.
numfig = True

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "furo"
html_static_path = []

# linkcheck: DOIs are permanent identifiers by design, and the publishers they
# resolve to (ASCE, Emerald, NRC Research Press, OUP) answer 403 to automated
# requests. Checking them only produces noise that hides real breakage, so skip
# the resolver and let linkcheck report on the links that genuinely can rot.
linkcheck_ignore = [r"https://doi\.org/.*"]
linkcheck_retries = 2
linkcheck_timeout = 30
