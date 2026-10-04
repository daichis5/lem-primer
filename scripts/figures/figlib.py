"""Shared drawing helpers for the figures in docs/ja/figures and docs/en/figures.

Each fig_*.py script computes its own geometry and draws one figure through
these helpers, so every figure shares one palette, one set of type sizes and
one kind of arrowhead. Coordinates passed to Figure are SVG pixels (y down);
View converts model coordinates (y up) into them.

A figure is drawn once and saved in both languages. Text that differs by
language is written L("垂直力", "base normal force"); any other argument to a
drawing method, such as a label's position, may be an L too, for English that
needs more room. text() draws nothing for an empty string, so L("…", "") is a
label in Japanese only. Figure.save() writes docs/ja/figures/<name>.svg and
docs/en/figures/<name>.svg.

Figures are drawn 760 px wide, about the width of the text column, so a
14 px label shows at about 14 px on the page.
"""

from __future__ import annotations

import functools
import math
import re
from pathlib import Path

DOCS = Path(__file__).resolve().parents[2] / "docs"
LANGS = ("ja", "en")
WIDTH = 760

# Colour carries meaning, the same in every figure (see _shared_conf.py).
INK = "#172033"  # text, outlines, the slip surface
MUTED = "#475569"  # secondary text
FAINT = "#94a3b8"  # guides, neglected forces
RULE = "#cbd5e1"  # light lines and frames
WEIGHT = "#d64545"  # weight: the side that drives sliding
RESIST = "#14916a"  # shear that resists sliding
NORMAL = "#2563eb"  # normal forces and stresses
INTER = "#7c3aed"  # forces between slices or columns
WATER = "#0891b2"  # pore-water pressure
UNIT = "#64748b"  # unit vectors n, m, d (dashed)
SOIL = "#f4e7c5"  # the sliding mass
SOIL_EDGE = "#8b7355"
GROUND = "#ece4d0"  # ground below the slip surface
TINT = "#f8fafc"  # panel background

FONTS = {
    "ja": "'Hiragino Sans','Hiragino Kaku Gothic ProN','Noto Sans JP','Yu Gothic',Meiryo,sans-serif",
    "en": "-apple-system,'Segoe UI',Helvetica,Arial,sans-serif",
}
MATH_FONT = "'STIX Two Text','Cambria','Times New Roman',serif"

LABEL = 14  # labels
SMALL = 13  # secondary labels
MATH = 17  # symbols


# --- vectors (model or screen; plain tuples) --------------------------------

def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def sub(a, b):
    return (a[0] - b[0], a[1] - b[1])


def mul(a, k):
    return (a[0] * k, a[1] * k)


def norm(a):
    return math.hypot(a[0], a[1])


def unit(a):
    n = norm(a)
    return (a[0] / n, a[1] / n)


def lerp(a, b, t):
    return (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t)


class Slope:
    """A slope with a circular slip surface, cut into equal vertical slices.

    Model units are metres, y up. The ground is flat at 0 left of the toe,
    rises to `height` at the crest, and stays flat beyond it. The circle
    leaves the ground at x = exit_x, left of the toe.
    """

    def __init__(self, height=10.0, crest=15.0, center=(6.0, 18.0), exit_x=-1.0, n=6):
        self.h, self.crest, self.c, self.n = height, crest, center, n
        self.r = math.hypot(exit_x - center[0], center[1])
        self.x0 = exit_x
        self.x1 = center[0] + math.sqrt(self.r**2 - (center[1] - height) ** 2)
        self.b = (self.x1 - self.x0) / n

    def ground(self, x):
        return min(max(x, 0.0), self.crest) * self.h / self.crest

    def slip(self, x):
        return self.c[1] - math.sqrt(self.r**2 - (x - self.c[0]) ** 2)

    def ground_pts(self, xa, xb):
        pts = [(xa, self.ground(xa))]
        pts += [(xk, self.ground(xk)) for xk in (0.0, self.crest) if xa < xk < xb]
        return pts + [(xb, self.ground(xb))]

    def arc_pts(self, xa, xb, steps=60):
        return [(xa + (xb - xa) * k / steps, self.slip(xa + (xb - xa) * k / steps)) for k in range(steps + 1)]

    def mass(self):
        return self.ground_pts(self.x0, self.x1) + self.arc_pts(self.x1, self.x0)

    def edges(self, k):
        """x of the left and right sides of slice k (0-based)."""
        return self.x0 + k * self.b, self.x0 + (k + 1) * self.b

    def slice(self, k):
        xa, xb = self.edges(k)
        return [(xa, self.slip(xa)), (xb, self.slip(xb))] + self.ground_pts(xa, xb)[::-1]

    def chord(self, k):
        """The base chord of slice k: midpoint and inclination alpha (radians)."""
        xa, xb = self.edges(k)
        pa, pb = (xa, self.slip(xa)), (xb, self.slip(xb))
        return ((pa[0] + pb[0]) / 2, (pa[1] + pb[1]) / 2), math.atan2(pb[1] - pa[1], pb[0] - pa[0])


class SliceModel:
    """One slice with vertical sides and a straight base, and its forces.

    Model units are metres and kN per metre run. The slice slides down the
    base, to the left; the base rises to the right at alpha. W comes from
    the area; E and X are chosen (E_{i-1}, X_{i-1} on the left side push
    right and up; E_i, X_i on the right push left and down). N and T then
    follow from the slice's two force equations, so W, N, T, E and X close.
    """

    def __init__(self, b=3.0, alpha_deg=25.0, top=(4.0, 6.0), gamma=18.0,
                 e=(110.0, 85.0), x=(60.0, 48.0), h=(1.0, 1.6)):
        self.b = b
        self.alpha = math.radians(alpha_deg)
        sa, ca = math.sin(self.alpha), math.cos(self.alpha)
        self.base_l, self.base_r = (0.0, 0.0), (b, b * math.tan(self.alpha))
        self.top_l, self.top_r = (0.0, top[0]), (b, top[1])
        self.pts = [self.base_l, self.base_r, self.top_r, self.top_l]
        self.g, area = centroid(self.pts)
        self.W = gamma * area
        self.E, self.X, self.h = e, x, h
        self.mid = (b / 2, self.base_r[1] / 2)
        self.n = (sa, -ca)  # outward normal of the base
        self.m = (-ca, -sa)  # sliding direction, down the base
        a_, b_ = e[1] - e[0], self.W - x[0] + x[1]
        self.N = -sa * a_ + ca * b_
        self.T = ca * a_ + sa * b_

    def thrust_points(self):
        return add(self.base_l, (0, self.h[0])), add(self.base_r, (0, self.h[1]))


def centroid(pts):
    """Centroid and area of a simple polygon."""
    a2 = cx = cy = 0.0
    for (xa, ya), (xb, yb) in zip(pts, pts[1:] + pts[:1]):
        cr = xa * yb - xb * ya
        a2 += cr
        cx += (xa + xb) * cr
        cy += (ya + yb) * cr
    return (cx / (3 * a2), cy / (3 * a2)), abs(a2) / 2


def add3(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


def sub3(a, b):
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])


def mul3(a, k):
    return (a[0] * k, a[1] * k, a[2] * k)


def dot3(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


def cross3(a, b):
    return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])


def unit3(a):
    n = math.sqrt(dot3(a, a))
    return (a[0] / n, a[1] / n, a[2] / n)


class Oblique:
    """A cabinet projection of model space (x right, y into the page, z up)
    onto SVG pixels: y recedes up and to the right at `angle`, shortened by
    `depth`, so faces normal to y keep their true shape."""

    def __init__(self, scale, origin, angle=30.0, depth=0.5):
        self.k = scale
        self.ox, self.oy = origin
        self.cy = depth * math.cos(math.radians(angle))
        self.sy = depth * math.sin(math.radians(angle))

    def p(self, q):
        x, y, z = q
        return (self.ox + self.k * (x + self.cy * y), self.oy - self.k * (z + self.sy * y))


class View:
    """Maps model coordinates (y up) to SVG pixels (y down)."""

    def __init__(self, scale, origin):
        self.k = scale
        self.ox, self.oy = origin

    def p(self, pt):
        return (self.ox + pt[0] * self.k, self.oy - pt[1] * self.k)

    def d(self, vec):
        """A model direction or offset in pixels."""
        return (vec[0] * self.k, -vec[1] * self.k)


# --- text measurement (an estimate, for spacing only) ------------------------

def text_width(s, size):
    w = 0.0
    for ch in s:
        if ord(ch) > 0x2E80:
            w += 1.0
        elif ch in " ":
            w += 0.3
        elif ch in "il.,;:'|!()[]":
            w += 0.32
        elif ch.isdigit():
            w += 0.55
        elif ch.isupper():
            w += 0.68
        else:
            w += 0.55
    return w * size


# --- math labels ---------------------------------------------------------------
#
# A small markup, enough for the symbols in the text:
#   N_i, T_{f,i}, x^2       subscript and superscript (one character or {...})
#   \v{n}                   a vector: bold italic, as \boldsymbol in the text
#   \r{tan}                 upright text inside a formula
#   \t{方向}                 words in the label font, for a label with
#                           symbols in it (r"x\t{ 方向}")
# Latin and Greek letters are italic; digits and signs are upright.

_TOKEN = re.compile(r"\\([vrt])\{([^{}]*)\}|([_^])(\{(?:[^{}]|\{[^{}]*\})*\}|.)|(.)", re.S)


def _runs(src, level=0):
    runs = []
    for m in _TOKEN.finditer(src):
        kind, body, script, arg, ch = m.groups()
        if kind == "t":
            runs.extend((c, "t", False, level) for c in body)
        elif kind:
            for c in body:
                runs.append((c, kind == "v", kind != "r" and _italic(c), level))
        elif script:
            inner = arg[1:-1] if arg.startswith("{") else arg
            shift = 1 if script == "_" else 2
            runs.extend((c, b, i, shift) for c, b, i, _ in _runs(inner, shift))
        else:
            runs.append((ch, False, _italic(ch), level))
    return runs


def _italic(c):
    return c.isalpha() and ord(c) < 0x2E80


def _esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def fmt(x):
    s = f"{x:.1f}"
    s = s[:-2] if s.endswith(".0") else s
    return "0" if s == "-0" else s


# --- two languages ------------------------------------------------------------

class L:
    """A value that differs by language: L("垂直力", "base normal force")."""

    def __init__(self, ja, en):
        self.ja, self.en = ja, en


def pick(x, lang):
    """x with every L in it (also inside lists and tuples) replaced by its value in lang."""
    if isinstance(x, L):
        return getattr(x, lang)
    if isinstance(x, (list, tuple)):
        return type(x)(pick(y, lang) for y in x)
    return x


def _each_language(method):
    """Run a drawing method once per language, with its L arguments picked.
    A call from inside another drawing method runs once, in that language."""

    @functools.wraps(method)
    def run(self, *args, **kwargs):
        if self.lang:
            return method(self, *args, **kwargs)
        for self.lang in LANGS:
            method(self, *pick(args, self.lang), **{k: pick(v, self.lang) for k, v in kwargs.items()})
        self.lang = None

    return run


class Figure:
    def __init__(self, name, height, title, desc, width=WIDTH):
        self.name = name
        self.w = width
        self.h = height
        self.title = title
        self.desc = desc
        self.items = {lang: [] for lang in LANGS}
        self.lang = None  # the language being drawn, inside a drawing method

    # primitives -------------------------------------------------------------

    @_each_language
    def add(self, s):
        self.items[self.lang].append(s)

    @staticmethod
    def _stroke(color, width, dash):
        s = f' stroke="{color}" stroke-width="{fmt(width)}"'
        if dash:
            s += f' stroke-dasharray="{dash}"'
        return s

    @_each_language
    def line(self, p, q, color=INK, width=1.5, dash=None, cap="round"):
        self.add(
            f'<line x1="{fmt(p[0])}" y1="{fmt(p[1])}" x2="{fmt(q[0])}" y2="{fmt(q[1])}"'
            f'{self._stroke(color, width, dash)} stroke-linecap="{cap}"/>'
        )

    @_each_language
    def polyline(self, pts, color=INK, width=1.5, dash=None, fill="none", join="round"):
        d = " ".join(f"{fmt(x)},{fmt(y)}" for x, y in pts)
        self.add(
            f'<polyline points="{d}" fill="{fill}"{self._stroke(color, width, dash)}'
            f' stroke-linejoin="{join}" stroke-linecap="round"/>'
        )

    @_each_language
    def polygon(self, pts, fill="none", color=None, width=1.5, dash=None, opacity=None):
        d = " ".join(f"{fmt(x)},{fmt(y)}" for x, y in pts)
        stroke = self._stroke(color, width, dash) if color else ""
        op = f' fill-opacity="{opacity}"' if opacity is not None else ""
        self.add(f'<polygon points="{d}" fill="{fill}"{op}{stroke} stroke-linejoin="round"/>')

    @_each_language
    def path(self, d, fill="none", color=INK, width=1.5, dash=None):
        stroke = self._stroke(color, width, dash) if color else ""
        self.add(f'<path d="{d}" fill="{fill}"{stroke} stroke-linejoin="round" stroke-linecap="round"/>')

    @_each_language
    def circle(self, c, r, fill=INK, color=None, width=1.5):
        stroke = self._stroke(color, width, None) if color else ""
        self.add(f'<circle cx="{fmt(c[0])}" cy="{fmt(c[1])}" r="{fmt(r)}" fill="{fill}"{stroke}/>')

    @_each_language
    def rect(self, x, y, w, h, fill=TINT, color=RULE, width=1, r=8):
        stroke = self._stroke(color, width, None) if color else ""
        self.add(
            f'<rect x="{fmt(x)}" y="{fmt(y)}" width="{fmt(w)}" height="{fmt(h)}" rx="{fmt(r)}"'
            f' fill="{fill}"{stroke}/>'
        )

    @_each_language
    def arrow(self, p, q, color=INK, width=2.6, dash=None, head=1.0):
        """An arrow from p to q (pixels); the head's tip sits exactly on q."""
        u = unit(sub(q, p))
        length = (3.4 * width + 5) * head
        half = (1.5 * width + 2.6) * head
        base = sub(q, mul(u, length))
        n = (-u[1], u[0])
        # Stop the shaft inside the head so its square end cannot show.
        self.line(p, add(base, mul(u, 0.6 * length)), color, width, dash, cap="butt")
        self.polygon([q, add(base, mul(n, half)), sub(base, mul(n, half))], fill=color)

    @_each_language
    def unit_vector(self, p, q, color=UNIT):
        self.arrow(p, q, color, width=1.4, dash="5 4", head=0.85)

    @_each_language
    def text(self, p, s, size=LABEL, color=INK, anchor="start", weight=None, vcenter=False):
        if not s:  # a label in one language only: L("…", "")
            return
        y = p[1] + (0.36 * size if vcenter else 0)
        wt = f' font-weight="{weight}"' if weight else ""
        self.add(
            f'<text x="{fmt(p[0])}" y="{fmt(y)}" class="t" font-size="{size}" fill="{color}"'
            f' text-anchor="{anchor}"{wt}>{_esc(s)}</text>'
        )

    @_each_language
    def math(self, p, src, size=MATH, color=INK, anchor="start", vcenter=False):
        """A formula in the markup above, placed like text()."""
        y = p[1] + (0.33 * size if vcenter else 0)
        out = []
        current = 0.0
        for c, style, italic, level in _merge(_runs(src)):
            fs = size * (0.7 if level else 1.0)
            shift = {0: 0.0, 1: 0.28 * size, 2: -0.42 * size}[level]
            dy = shift - current
            current = shift
            attrs = []
            if dy:
                attrs.append(f'dy="{fmt(dy)}"')
            if level:
                attrs.append(f'font-size="{fmt(fs)}"')
            attrs.append(f'font-style="{"italic" if italic else "normal"}"')
            if style == "t":
                attrs.append('class="t"')
                if not level:
                    attrs.append(f'font-size="{fmt(LABEL if size >= LABEL else size)}"')
            elif style:
                attrs.append('font-weight="bold"')
            out.append(f"<tspan {' '.join(attrs)}>{_esc(c)}</tspan>")
        self.add(
            f'<text x="{fmt(p[0])}" y="{fmt(y)}" class="m" font-size="{size}" fill="{color}"'
            f' text-anchor="{anchor}">{"".join(out)}</text>'
        )

    # composites -------------------------------------------------------------

    @_each_language
    def angle_arc(self, c, r, a0, a1, color=INK, width=1.3):
        """An arc around c (pixels) from screen angle a0 to a1, in degrees
        measured counter-clockwise from +x with y up."""
        p0 = (c[0] + r * math.cos(math.radians(a0)), c[1] - r * math.sin(math.radians(a0)))
        p1 = (c[0] + r * math.cos(math.radians(a1)), c[1] - r * math.sin(math.radians(a1)))
        large = 1 if abs(a1 - a0) > 180 else 0
        sweep = 0 if a1 > a0 else 1
        self.path(
            f"M{fmt(p0[0])} {fmt(p0[1])} A{fmt(r)} {fmt(r)} 0 {large} {sweep} {fmt(p1[0])} {fmt(p1[1])}",
            color=color,
            width=width,
        )

    @_each_language
    def legend(self, x, y, items, gap=26):
        """Arrow samples with their meaning, in one row from (x, y)."""
        for color, dashed, label in items:
            if dashed:
                self.unit_vector((x, y), (x + 30, y), color)
            else:
                self.arrow((x, y), (x + 30, y), color, width=2.4)
            self.text((x + 38, y), label, SMALL, MUTED, vcenter=True)
            x += 38 + text_width(label, SMALL) + gap

    # output -----------------------------------------------------------------

    def svg(self, lang):
        head = (
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.w}" height="{self.h}"'
            f' viewBox="0 0 {self.w} {self.h}" role="img" aria-labelledby="title desc">\n'
            f'  <title id="title">{_esc(pick(self.title, lang))}</title>\n'
            f'  <desc id="desc">{_esc(pick(self.desc, lang))}</desc>\n'
            f"  <style>.t{{font-family:{FONTS[lang]}}}.m{{font-family:{MATH_FONT}}}</style>\n"
            f'  <rect width="{self.w}" height="{self.h}" fill="#fff"/>\n'
        )
        return head + "".join(f"  {s}\n" for s in self.items[lang]) + "</svg>\n"

    def save(self):
        for lang in LANGS:
            out = DOCS / lang / "figures"
            out.mkdir(parents=True, exist_ok=True)
            (out / f"{self.name}.svg").write_text(self.svg(lang), encoding="utf-8")


def _merge(runs):
    """Join neighbouring characters that share a style into one tspan."""
    merged = []
    for c, b, i, lv in runs:
        if merged and merged[-1][1:] == (b, i, lv):
            merged[-1] = (merged[-1][0] + c, b, i, lv)
        else:
            merged.append((c, b, i, lv))
    return merged
