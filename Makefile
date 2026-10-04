# Build the Japanese and English editions into _site/<lang>/.
#
# Each language is a separate Sphinx project because ``language`` is resolved
# once per build; shared settings live in docs/_shared_conf.py.

SPHINXBUILD ?= $(firstword \
  $(wildcard .venv/bin/sphinx-build) \
  $(wildcard .venv/Scripts/sphinx-build.exe) \
  sphinx-build)
SPHINXOPTS ?=
SITEDIR    := _site

# Whatever the platform uses to hand a file or URL to the default browser.
# ``echo`` is the fallback: it at least prints what to open by hand.
BROWSER ?= $(firstword \
  $(shell command -v open 2>/dev/null) \
  $(shell command -v xdg-open 2>/dev/null) \
  echo)
PORT ?= 8000

# Which edition ``make open`` shows; ``make open EDITION=en`` for the other one.
EDITION ?= ja

# The practice pages' example code, one copy per edition (the English one with
# English comments and output). The interpreter is an absolute path because the
# scripts run from inside each directory, where they import each other.
EXAMPLES := docs/ja/examples docs/en/examples
PYTHON ?= $(firstword $(abspath $(wildcard .venv/bin/python)) python3)

.PHONY: help ja en all clean linkcheck open preview serve figures examples

help:
	@echo "Usage:"
	@echo "  make ja         # Build the Japanese edition into $(SITEDIR)/ja/"
	@echo "  make en         # Build the English edition into $(SITEDIR)/en/"
	@echo "  make all        # Build both, plus the root redirect"
	@echo "  make open       # Open $(SITEDIR)/$(EDITION)/ in a browser (EDITION=en for English)"
	@echo "  make preview    # Build both, then open $(SITEDIR)/$(EDITION)/ (no server)"
	@echo "  make serve      # Build, serve on http://localhost:$(PORT)/, and open it"
	@echo "  make linkcheck  # Check external links in both editions"
	@echo "  make figures    # Write docs/{ja,en}/figures/*.svg from scripts/figures/"
	@echo "  make examples   # Run the practice pages' code: write its outputs, run its tests"
	@echo "  make clean      # Remove built files"
	@echo ""
	@echo "Chain goals to build and look in one step, e.g. 'make ja open'."
	@echo "'make serve' is the faithful check: over file:// the root redirect"
	@echo "cannot resolve ./ja/ to a page, which is why 'make open' skips it."

ja:
	$(SPHINXBUILD) -b html docs/ja "$(SITEDIR)/ja" $(SPHINXOPTS)

en:
	$(SPHINXBUILD) -b html docs/en "$(SITEDIR)/en" $(SPHINXOPTS)

# The site root redirects to the Japanese edition, which is the source language.
# Sphinx writes the favicon link into the pages it generates, but this page is
# written here, so it needs its own -- otherwise a bookmark of the site root is
# the one entry point without the mark.
# Files under assets/ are published verbatim at $(SITEDIR)/assets/. They belong to
# neither edition -- they are brand assets that other services fetch by URL -- so
# they bypass both Sphinx projects rather than riding along in html_static_path.
all: ja en
	@printf '%s\n' \
	  '<!doctype html>' \
	  '<html lang="ja">' \
	  '<head>' \
	  '<meta charset="utf-8">' \
	  '<title>LEM Primer</title>' \
	  '<meta http-equiv="refresh" content="0; url=./ja/">' \
	  '<link rel="canonical" href="./ja/">' \
	  '<link rel="icon" type="image/svg+xml" href="./assets/lem-primer-icon.svg">' \
	  '</head>' \
	  '<body><p><a href="./ja/">日本語</a> / <a href="./en/">English</a></p></body>' \
	  '</html>' > "$(SITEDIR)/index.html"
	@mkdir -p "$(SITEDIR)/assets" && cp assets/* "$(SITEDIR)/assets/"
	@echo "Site built in $(SITEDIR)/"

# Opens the edition's page file itself rather than $(SITEDIR)/index.html: that
# root page redirects to ``./ja/``, which only a web server resolves to an index
# page. Over file:// the browser hands the bare directory to the file manager
# instead. Use ``make serve`` to exercise the redirect the way Pages runs it.
open:
	@page="$(SITEDIR)/$(EDITION)/index.html"; \
	  if [ ! -f "$$page" ]; then \
	    echo "$$page does not exist: run 'make $(EDITION)' first." >&2; \
	    exit 1; \
	  fi; \
	  echo "Opening $$page"; \
	  $(BROWSER) "$$page"

# ``all`` then ``open`` in one word. Recursive rather than a prerequisite list,
# so the build still finishes before the browser opens under ``make -j``.
preview:
	@$(MAKE) all
	@$(MAKE) open

# Serving over HTTP rather than file:// keeps the built site behaving the way it
# will on Pages. The browser is opened from a subshell so the server itself stays
# in the foreground and Ctrl-C stops it.
serve: all
	@echo "Serving $(SITEDIR) at http://localhost:$(PORT)/ - Ctrl-C to stop"
	@( sleep 1; $(BROWSER) "http://localhost:$(PORT)/" >/dev/null 2>&1 & )
	@python3 -m http.server $(PORT) --directory "$(SITEDIR)" --bind 127.0.0.1

# Every SVG under docs/ja/figures and docs/en/figures is written by a script
# under scripts/figures, which writes both languages; the scripts use only the
# standard library, so any python3 will do.
figures:
	@for f in scripts/figures/fig_*.py; do python3 "$$f" >/dev/null || exit 1; done
	@echo "Figures written to docs/ja/figures/ and docs/en/figures/"

# The practice pages include what each run_*.py prints, from output/ in each of
# $(EXAMPLES), so a page cannot show numbers its code no longer produces.
# Warnings are errors: a reader would see them in the output. Run this before
# `make figures`, which reads some of these outputs. Needs `uv sync --group examples`.
examples:
	@for d in $(EXAMPLES); do \
	  for f in $$d/run_*.py; do \
	    name=$$(basename "$$f" .py); \
	    (cd $$d && "$(PYTHON)" -W error "$$name.py") > "$$d/output/$$name.txt" || exit 1; \
	  done; \
	  (cd $$d && "$(PYTHON)" -W error -m pytest -q -p no:cacheprovider) || exit 1; \
	  echo "Example outputs written to $$d/output/"; \
	done

linkcheck:
	$(SPHINXBUILD) -b linkcheck docs/ja "$(SITEDIR)/../_build/linkcheck-ja" $(SPHINXOPTS)
	$(SPHINXBUILD) -b linkcheck docs/en "$(SITEDIR)/../_build/linkcheck-en" $(SPHINXOPTS)

clean:
	rm -rf "$(SITEDIR)" _build
