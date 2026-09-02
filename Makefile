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

.PHONY: help ja en all clean linkcheck open preview serve

help:
	@echo "Usage:"
	@echo "  make ja         # Build the Japanese edition into $(SITEDIR)/ja/"
	@echo "  make en         # Build the English edition into $(SITEDIR)/en/"
	@echo "  make all        # Build both, plus the root redirect"
	@echo "  make open       # Open $(SITEDIR)/$(EDITION)/ in a browser (EDITION=en for English)"
	@echo "  make preview    # Build both, then open $(SITEDIR)/$(EDITION)/ (no server)"
	@echo "  make serve      # Build, serve on http://localhost:$(PORT)/, and open it"
	@echo "  make linkcheck  # Check external links in both editions"
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
all: ja en
	@printf '%s\n' \
	  '<!doctype html>' \
	  '<html lang="ja">' \
	  '<head>' \
	  '<meta charset="utf-8">' \
	  '<title>LEM Primer</title>' \
	  '<meta http-equiv="refresh" content="0; url=./ja/">' \
	  '<link rel="canonical" href="./ja/">' \
	  '</head>' \
	  '<body><p><a href="./ja/">日本語</a> / <a href="./en/">English</a></p></body>' \
	  '</html>' > "$(SITEDIR)/index.html"
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

linkcheck:
	$(SPHINXBUILD) -b linkcheck docs/ja "$(SITEDIR)/../_build/linkcheck-ja" $(SPHINXOPTS)
	$(SPHINXBUILD) -b linkcheck docs/en "$(SITEDIR)/../_build/linkcheck-en" $(SPHINXOPTS)

clean:
	rm -rf "$(SITEDIR)" _build
