"""Settings shared by the per-language Sphinx projects under ``docs/``.

Sphinx resolves ``language`` once per build, so each language gets its own
``conf.py``; everything that does not depend on the language lives here.
"""

from pathlib import Path

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

# Number equations per document rather than continuously across the whole
# project: each of the three documents is written to be readable on its own, so
# its first equation should be (1). Labelled equations are referenced with the
# ``{eq}`` role, which renders the number and links to it.
math_numfig = False

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# Overrides for Sphinx's own UI strings; see ``_locale/ja/LC_MESSAGES/sphinx.po``.
# Paths are relative to each edition's source directory.
locale_dirs = ["../_locale"]

html_theme = "furo"

# Furo shows this as the sidebar brand and Sphinx puts it in the browser tab.
# It carries no edition suffix: the switcher under it already names the
# language, and every page title is written in its own language anyway.
html_title = "LEM Primer"

# Both editions share the templates and stylesheet one level up.
templates_path = ["../_templates"]
html_static_path = ["../_static"]
html_css_files = [
    "language-switch.css",
    "sidebar-brand.css",
    "sidebar-links.css",
]

# Furo's default sidebar (see its ``theme.conf``) with the language switcher
# inserted under the brand, so it sits above the search box on every page.
html_sidebars = {
    "**": [
        "sidebar/brand.html",
        "sidebar/language.html",
        "sidebar/search.html",
        "sidebar/scroll-start.html",
        "sidebar/navigation.html",
        "sidebar/links.html",
        "sidebar/ethical-ads.html",
        "sidebar/scroll-end.html",
        "sidebar/variant-selector.html",
    ]
}

# linkcheck: DOIs are permanent identifiers by design, and the publishers they
# resolve to (ASCE, Emerald, NRC Research Press, OUP) answer 403 to automated
# requests. Checking them only produces noise that hides real breakage, so skip
# the resolver and let linkcheck report on the links that genuinely can rot.
linkcheck_ignore = [
    r"https://doi\.org/.*",
    # lem-lab is a private repository: GitHub answers 404 to unauthenticated
    # requests, so CI cannot verify this link. Remove this entry if it becomes
    # public.
    r"https://github\.com/daichis5/lem-lab",
]
linkcheck_retries = 2
linkcheck_timeout = 30


# The editions published under ``_site/<code>/``, in the order they are shown.
# ``fallback_hint`` is written in the target language: it is read by someone who
# is about to leave for that edition.
EDITIONS = {
    "ja": {
        "label": "日本語",
        "caption": "言語",
        "fallback_hint": "このページの日本語版はまだありません。日本語版のトップへ移動します。",
    },
    "en": {
        "label": "English",
        "caption": "Language",
        "fallback_hint": "This page is not translated yet; opens the top page of the English edition.",
    },
}


# Related destinations shown at the foot of the sidebar, per language.
SIDEBAR_LINKS = {
    "ja": [
        ("LEM Lab（実装例）", "https://github.com/daichis5/lem-lab"),
        ("このサイトのソース", "https://github.com/daichis5/lem-primer"),
        ("CC BY 4.0", "https://creativecommons.org/licenses/by/4.0/"),
    ],
    "en": [
        ("LEM Lab (implementation)", "https://github.com/daichis5/lem-lab"),
        ("Source of this site", "https://github.com/daichis5/lem-primer"),
        ("CC BY 4.0", "https://creativecommons.org/licenses/by/4.0/"),
    ],
}


def _add_language_editions(app, pagename, templatename, context, doctree):
    """Give each page the URLs of its counterparts in the other editions.

    Editions are separate Sphinx projects, so no cross-project resolution is
    available: the counterpart is found by looking for a source file with the
    same docname under ``docs/<code>/``. Pages that do not exist yet fall back
    to that edition's top page rather than a 404, which is what the
    under-construction English edition needs.
    """
    docs_root = Path(app.confdir).parent
    this_language = app.config.language
    # From ``_site/<code>/<pagename>.html`` up to ``_site/``.
    to_site_root = "../" * (pagename.count("/") + 1)

    editions = []
    for code, edition in EDITIONS.items():
        if code == this_language:
            editions.append({"code": code, "label": edition["label"], "url": None})
            continue
        exact = any(
            (docs_root / code / f"{pagename}{suffix}").exists()
            for suffix in (".md", ".rst")
        )
        target = f"{pagename}.html" if exact else "index.html"
        editions.append(
            {
                "code": code,
                "label": edition["label"],
                "url": f"{to_site_root}{code}/{target}",
                "exact": exact,
                "fallback_hint": edition["fallback_hint"],
            }
        )
    context["language_editions"] = editions
    context["language_caption"] = EDITIONS[this_language]["caption"]
    context["sidebar_links"] = [
        {"label": label, "url": url}
        for label, url in SIDEBAR_LINKS.get(this_language, ())
    ]

    # ``rel="alternate"`` for the counterparts that really exist, so a reader who
    # lands on the wrong edition from a search result is offered the right one.
    # Furo renders ``metatags`` inside ``<head>``; the URLs stay relative because
    # the site has no configured base URL.
    alternates = "".join(
        f'\n    <link rel="alternate" hreflang="{edition["code"]}" href="{edition["url"]}">'
        for edition in editions
        if edition["url"] and edition["exact"]
    )
    if alternates:
        context["metatags"] = context.get("metatags", "") + alternates


def setup(app):
    app.connect("html-page-context", _add_language_editions)
    return {"parallel_read_safe": True, "parallel_write_safe": True}
