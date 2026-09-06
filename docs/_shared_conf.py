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

# The mark is the LEM Lab icon with its values inverted -- same mountain, same
# dashed slip surface, sand on navy instead of green on cream. The shape says
# "same family", the inversion says "not the same repository", and the contrast
# survives being scaled down to a favicon. Both icons live in ``assets/`` rather
# than ``_static/`` because they are one set of brand assets; Sphinx resolves
# these paths against each edition's source directory and copies the file into
# the build's ``_static/``.
html_logo = "../../assets/lem-primer-icon.svg"
html_favicon = "../../assets/lem-primer-icon.svg"

# Palette. Two rules drive the choices below.
#
# First, the figures use colour to carry meaning: red is the driving side
# (weight), green the resisting shear, blue the base normal force. Furo's
# default brand colour is a saturated blue, which invites the reader to connect
# "the blue of a link" with "the blue of N_i". So the site's own accents avoid
# those three hues: the primary is the deep navy that the figures already use
# for ink and for the slip surface itself -- a colour that stands for structure
# rather than for any force -- and the secondary is the teal of the LEM Lab
# mark.
#
# Second, body text, muted text and borders take the exact values the figures
# use for the same roles, so a figure sits on the page as part of it rather than
# as a pasted-in image.
_INK = "#172033"  # figure body text, and the slip surface
_TEAL = "#356F68"  # the dark stop of the LEM Lab mountain gradient

html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "#1A5678",
        "color-brand-content": "#17527A",
        "color-brand-visited": "#7A5AA6",
        "color-foreground-primary": _INK,
        "color-foreground-secondary": "#475569",
        "color-foreground-muted": "#64748B",
        "color-foreground-border": "#94A3B8",
        "color-background-secondary": "#F1F4F6",
        "color-background-hover": "#E7EDF2",
        "color-background-hover--transparent": "#E7EDF200",
        "color-background-border": "#E2E8F0",
        # Where a cross-reference lands. Furo's default is a highlighter
        # yellow; equations and figures are cited by label throughout, so this
        # flashes often enough to be worth keeping in the palette.
        "color-highlight-on-target": "#E3EDEA",
        "color-highlighted-background": "#DCE9F2",
        # Furo's admonition titles are saturated material-design hues. Note is
        # by far the most used directive here, so it takes the quiet teal;
        # everything else is muted to the same degree.
        "color-admonition-title--note": _TEAL,
        "color-admonition-title-background--note": "rgba(53, 111, 104, .16)",
        "color-admonition-title--important": _TEAL,
        "color-admonition-title-background--important": "rgba(53, 111, 104, .16)",
        "color-admonition-title--tip": "#2F7D5F",
        "color-admonition-title-background--tip": "rgba(47, 125, 95, .16)",
        "color-admonition-title--hint": "#2F7D5F",
        "color-admonition-title-background--hint": "rgba(47, 125, 95, .16)",
        "color-admonition-title--seealso": "#1A5678",
        "color-admonition-title-background--seealso": "rgba(26, 86, 120, .16)",
        "color-admonition-title--warning": "#B45309",
        "color-admonition-title-background--warning": "rgba(180, 83, 9, .16)",
        "color-admonition-title--caution": "#B45309",
        "color-admonition-title-background--caution": "rgba(180, 83, 9, .16)",
        "color-admonition-title--danger": "#B3352C",
        "color-admonition-title-background--danger": "rgba(179, 53, 44, .16)",
        "color-admonition-title--attention": "#B3352C",
        "color-admonition-title-background--attention": "rgba(179, 53, 44, .16)",
        "color-admonition-title--error": "#B3352C",
        "color-admonition-title-background--error": "rgba(179, 53, 44, .16)",
        # The title of a bare ``{admonition}`` with a custom heading.
        "color-admonition-title": "#1A5678",
        "color-admonition-title-background": "rgba(26, 86, 120, .16)",
        "color-topic-title": _TEAL,
        "color-topic-title-background": "rgba(53, 111, 104, .16)",
    },
    "dark_css_variables": {
        "color-brand-primary": "#6FB3E0",
        "color-brand-content": "#7CBCE6",
        "color-brand-visited": "#B9A3DC",
        "color-foreground-primary": "#CFD5DB",
        "color-foreground-secondary": "#9AA5B1",
        "color-foreground-muted": "#7C8894",
        "color-foreground-border": "#5A6672",
        "color-background-primary": "#12171B",
        "color-background-secondary": "#171D22",
        "color-background-hover": "#1C242A",
        "color-background-hover--transparent": "#1C242A00",
        "color-background-border": "#2C363E",
        "color-highlight-on-target": "#1E3A36",
        "color-highlighted-background": "#103048",
        "color-admonition-background": "#171D22",
        "color-card-background": "#171D22",
        "color-admonition-title--note": "#7FBCAE",
        "color-admonition-title-background--note": "rgba(127, 188, 174, .16)",
        "color-admonition-title--important": "#7FBCAE",
        "color-admonition-title-background--important": "rgba(127, 188, 174, .16)",
        "color-admonition-title--tip": "#6FC69B",
        "color-admonition-title-background--tip": "rgba(111, 198, 155, .16)",
        "color-admonition-title--hint": "#6FC69B",
        "color-admonition-title-background--hint": "rgba(111, 198, 155, .16)",
        "color-admonition-title--seealso": "#6FB3E0",
        "color-admonition-title-background--seealso": "rgba(111, 179, 224, .16)",
        "color-admonition-title--warning": "#E0A458",
        "color-admonition-title-background--warning": "rgba(224, 164, 88, .16)",
        "color-admonition-title--caution": "#E0A458",
        "color-admonition-title-background--caution": "rgba(224, 164, 88, .16)",
        "color-admonition-title--danger": "#E88178",
        "color-admonition-title-background--danger": "rgba(232, 129, 120, .16)",
        "color-admonition-title--attention": "#E88178",
        "color-admonition-title-background--attention": "rgba(232, 129, 120, .16)",
        "color-admonition-title--error": "#E88178",
        "color-admonition-title-background--error": "rgba(232, 129, 120, .16)",
        "color-admonition-title": "#6FB3E0",
        "color-admonition-title-background": "rgba(111, 179, 224, .16)",
        "color-topic-title": "#7FBCAE",
        "color-topic-title-background": "rgba(127, 188, 174, .16)",
    },
}

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
