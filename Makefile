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

.PHONY: help ja en all clean linkcheck

help:
	@echo "Usage:"
	@echo "  make ja         # Build the Japanese edition into $(SITEDIR)/ja/"
	@echo "  make en         # Build the English edition into $(SITEDIR)/en/"
	@echo "  make all        # Build both, plus the root redirect"
	@echo "  make linkcheck  # Check external links in both editions"
	@echo "  make clean      # Remove built files"

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

linkcheck:
	$(SPHINXBUILD) -b linkcheck docs/ja "$(SITEDIR)/../_build/linkcheck-ja" $(SPHINXOPTS)
	$(SPHINXBUILD) -b linkcheck docs/en "$(SITEDIR)/../_build/linkcheck-en" $(SPHINXOPTS)

clean:
	rm -rf "$(SITEDIR)" _build
