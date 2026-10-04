# AGENTS.md

Instructions for agents (and people) editing this repository. The Japanese
phrasing rules are the lab handbook's (`lab-handbook`, AGENTS.md, Japanese
phrasing), applied to a primer with equations.

## Quick Commands

- `make all SPHINXOPTS="-W --keep-going"`: the build CI runs; any warning fails it
- `make examples`: run the practice pages' code, write its outputs and run its
  tests (needs `uv sync --group examples`); CI fails if an output changes
- `make serve`: build both editions and serve them at http://localhost:8000/

## Scope

Readers are civil-engineering students who have not studied LEM before: they
know 土質力学 and 材料力学 (垂直応力，せん断応力，有効応力，Mohr–Coulomb則)
but not stress tensors or LEM. The series depends on no analysis software.

The Japanese edition (`docs/ja/`) is the source. The English edition
(`docs/en/`) is a translation of it at a recorded commit, and does not
follow it; see English edition.

The three documents are 第1章, 第2章 and 第3章, under the caption 理論編;
the site as a whole is この資料 or このシリーズ. After them come three
practice pages (実践編), where readers write the methods in Python with
NumPy and check them with pytest. The code depends on no analysis software
either; how a particular program such as LEM Lab maps onto it belongs in
that program's documentation.

## Structure of a document

- A document opens with its title (H1), its subtitle as one bold line (not a
  heading), a lead paragraph saying what the document does, and one line
  naming the documents it builds on:
  「この章は，[第1章](continuum-mechanics-to-lem-start.md)を読んだ前提で進める．」
- The cards of the three documents and their questions, under 理論編, and
  the cards of the practice pages, under 実践編, live on the home page
  (`index.md`) only: one `grid-item-card` each, titled 第1章　… or
  実践1　…, with the question or what the page's code computes (ending
  〜を求める) as its text. Documents do not repeat them, and a part
  opens with its first section, not with a list of what it covers.
- A document ends with 確認問題 (see Review questions), then 次に読む, then
  参考文献 in the second and third. The third document's 次に読む points to
  実践1.
- Headings are Japanese. A part is an unnumbered `##` heading over numbered
  sections: a 章 ranks below a 部 in Japanese books, so 第1部 inside 第2章
  would read upside down. Sections keep their numbers, and the text refers
  to one as 6節. Reference entries keep the language of the work; where
  there is no DOI, the link text is 書誌情報.
- Keep labels (`(section-6)=`) and equation labels as they are: they are
  link targets.

## Practice pages

`practice-infinite-slope.md`, `practice-slices-2d.md` and
`practice-columns-3d.md` are 実践1, 実践2 and 実践3, listed under the
toctree caption 実践編. Each builds one model's code: the infinite slope,
2D slices on one circle, 3D columns on one ellipsoid; one slope, one slip
surface, one factor of safety.

- A practice page opens like a document: title, subtitle, lead, a line
  naming the documents and earlier practice pages it builds on
  (「この実践は，[第1章](…)を読んだ前提で進める．」), and the glossary line.
- The body runs 作るもの (the problem and its numbers, and a table of the
  functions with the sections that write them), 準備 (the folder
  `lem-practice`, the commands, the downloads), numbered sections, 困ったとき
  (a table 表示や様子 | 原因と対処, each row ending with the sections it
  draws on), まとめ (3 to 7 bullets, each ending with a link), 確認問題,
  次に読む (the next practice page; none after 実践3), and 参考文献 when
  the page cites works.
- Each practice checks its model against the one before: a plane slip
  surface gives the infinite slope, a cylinder gives the 2D values. Keep
  these checks when changing the code; they are what the pages teach.
- Labels take the page's prefix: `infinite-`, `slices-`, `columns-`
  (`slices-section-3`).
- Link each section of a document a practice page relies on, with the
  glossary's link text: `[第1章 3節](#section-3)`. Give the target heading
  a label if it has none.
- Restate an equation from a document on the practice page, with its own
  label, rather than citing it with `{eq}`: equation numbers restart in each
  document.

## Example code

The practice pages' code lives in `docs/ja/examples`: one module
(`infinite_slope.py`, `slices.py`, `columns.py`), one test file and one run
script (`run_*.py`) per page, and `save_table.py`, which 実践3 8節 runs to
save a column table. `test_answers.py` pins the numbers that review answers
quote and runs `save_table.py`; readers do not download it.

- Pages never paste code or output. They include it with `literalinclude`:
  a function with `:pyobject:`, a file's head with `:end-at:`, and a run
  script's output from `docs/ja/examples/output` with `:start-at:` and
  `:end-before:` on its numbered headings.
- `make examples` runs every `run_*.py` with warnings as errors, writes what
  it prints to `docs/ja/examples/output`, and runs the tests. CI runs it and
  fails if an output differs from the committed file. Run it before
  `make figures`: `fig_e2` reads `output/run_slices.txt`.
- Python 3.11 or later with NumPy, and pytest for the tests. Docstrings and
  comments are Japanese; names follow the text's symbols (`W`, `N`, `alpha`,
  `l`, `m_alpha`), and vectors follow its conventions: `n` outward from the
  sliding mass, `m` the direction of sliding, compression positive.
- Keep lines within 88 display columns, a Japanese character counting as two,
  so code blocks on the page do not scroll. `ruff format --line-length 88`
  counts that way.

## Japanese phrasing

Write Japanese for the reader. The first drafts came from English, so
translationese crept in: English sentence structure in Japanese words.
`docs/ja/continuum-mechanics-to-lem-start.md` follows the rules below;
compare a document with it.

- Write in the である style with full-width `，．`. End a body sentence with
  a predicate (である, a verb, or an adjective such as ない or よい), and vary
  the endings: follow a である． with a different ending, and where three
  sentences in a row end in a verb, join two of them or open one with a
  connective or a linking phrase (そのため，, つまり，, 円弧では，). Noun
  endings (体言止め) are for tables, captions, glossary entries, list items,
  and review answers (see Review questions).
- A list item and a caption have no closing ．; a sentence inside one that
  another follows keeps its ．.
- Link each sentence to the one before when the link is a cause, a
  condition, a contrast or the next step:
  「…滑動力とつり合っている．つまり，両者の大きさは等しい．」
- Give each sentence one topic. Where the topic changes after 〜であり，,
  〜で， or a verb stem, end the sentence:
  「Cauchyの公式は（式）である．表面力の法線成分は，符号を含めて（式）になる．」
  (from 「Cauchyの公式は（式）であり，符号付き法線成分は（式）である．」).
- In body text, end a cause with 〜からである and a purpose with
  〜ためである. Keep a cause and a purpose in separate sentences.
  Neighbouring sentences take turns with ので，, ため， and そのため，.
- Where a document says how it is written or where something is in the
  series, write the present, as Japanese textbooks do:
  「用語と記号は，用語集にまとめている．」「補足には，…を書いている．」
  (not まとめた，書いた). The past stays for what an earlier section or
  document did (「第1章では，…を導いた」), and for a document's closing
  look back at its own sections (「この章では，…を整理した」).
- A parenthesis may stay mid-sentence when it is short and holds no ． and
  no link: a term (「単位面積あたりの力を，**表面力**（traction）という」)
  or a brief aside. A remark with its own ．, or a link, goes at the end of
  its clause or sentence, or in a sentence of its own.
- Write the Japanese phrase, not the English one read through:
  この章 (not 本章，本稿), 満たす (not 満足する), 違う (not 異なる),
  確かめる (not 確認する), できる (not 可能である), とき (not 場合，際),
  次の (not 以下の), と・や (not および), つまり (not すなわち),
  〜のもとで・〜とき (not 〜の下で), 〜での・〜の (not 〜における),
  〜ことがある (not 〜し得る), 決める (not 決定する). A cleft sentence
  (「重要なのは，…ことである」) becomes the plain statement.
- Between equations, say what was done (「これを $\tau_m$ について解くと」
  「式 {eq}`eq-start-mohr-coulomb` を入れると」) rather than したがって.
  A consequence in prose takes そのため， or つまり，.
- Unpack a 漢語 compound made by translating an English phrase
  (幾何学的入力可能性 → 形を入力できるか, 強度動員式 → 強度の動員を表す
  式), unless it is in the term table below.
- Leave human actions to people, who may stay unnamed:
  「手法名だけでは，定式化は分からない」 (from 「手法名は定式化を特定しない」).
  A method or a solver doing its own job stays the subject:
  「Spencer法は，力とモーメントのつり合いをすべて満たす」.
- Use the terms readers meet in Japanese textbooks and standards (the
  table below), and explain each where it first appears in a document.
- Name what each word points to: which section (5節で見た, not 前節の),
  which force, which document (第1章, not 前章).
- Split a sentence past about 100 characters, not counting inline math, or
  one with a remark in parentheses inside a modifier, into two joined by a
  connective.
- Say each thing once.

### Notation

- Numbers are Arabic: 1つ, 2本, 3次元, 6つの層, 2階のテンソル. Kanji stay
  inside words: 一定, 一般, 一意, 一致, 一部, 一方, 唯一, 一次文献,
  二重計上.
- A half-width space separates inline math and an equation reference from
  Japanese text: 「底面 $S_i$ の」「式 {eq}`eq-start-goal` の分子」. No space
  goes before full-width punctuation or brackets (「$F_s$，」), or between a
  Latin word and Japanese (「LEMでは」「Spencer法」).
- Join items with ・ or a word (と, や, または), not ／.
- A display equation ends without punctuation; the sentence around it
  carries the ．or ，. Commas between equations on one line stay.

### Terms

| Use | Not | Note |
|---|---|---|
| 2次元，3次元 | 2D，3D | also in names: 3次元のSpencer法, 3次元のLEM |
| Fellenius法（簡便分割法） | 通常分割法 | the parenthesis at its first use |
| 簡易Bishop法，簡易Janbu法 | Bishop簡便法，Janbu簡便法 | as in 鵜飼・細堀 (1988) |
| Spencer法，Morgenstern–Price法，Mohr–Coulomb則，Cauchyの公式 | カタカナ | person names stay in Latin letters |
| 垂直応力，有効垂直応力，全垂直応力 | 法線応力 | $\sigma_n$, $\sigma_n'$ |
| 底面垂直力，垂直力 | 底面法線力，法線力 | $N_i$; also スライス間の垂直力 $E$, said at its first use to be normal to the boundary |
| 法線ベクトル，法線方向，法線成分 | | the vector $\boldsymbol{n}$ and components along it keep 法線 |
| 滑動力 | 駆動力 | the pair of 抵抗力: $F_s$＝抵抗力／滑動力 |
| 内力 | 内部力 | |
| 簡便分割法 | 簡易分割法 | as in the Japanese title of Ugai et al. (1986) |
| つり合いの一部だけを満たす方法 | 簡便法 | the class of Fellenius法, 簡易Bishop法 and 簡易Janbu法, set against 静力学的に完全な方法; Japanese standards use 簡便法 for Fellenius法 alone, so the word appears only where the text reports that usage (第2章 4.1節, the glossary entry) |
| テンションクラック（引張亀裂） | 張力亀裂 | |
| 表面力 | traction | gloss （traction） at its first use |
| 不静定性の解消 | closure, 力学的な未知量の決定 | gloss （closure） at its first use |
| 第1章，この章，この資料，このシリーズ | 本章，本稿，前章，本資料，本シリーズ | この章 is one document; この資料 and このシリーズ are the whole site |
| LEMの各手法 | 各LEM | |
| 任意形状，一般形状 | 任意の形 | as in 任意形状のすべり面 |
| 元の手法 | 原法 | |
| 射影 | 投影 | projecting onto a plane, as in 補足C |
| 実践1，実践2，実践3，この実践 | 演習，課題 | the practice pages, and a practice page referring to itself |

## Review questions

Every document ends its body with `## 確認問題`, opened by the line
「答えは問題をクリックすると開く．」.

- 3 to 8 questions, about one per main section. Each is a collapsed dropdown
  with the answer inside, so readers try before they look:

  ```text
  :::{dropdown} 問1　応力テンソルと，ある面に働く表面力は，何が違うか
  :icon: question

  （答え）（→[2節](#section-2)）
  :::
  ```
- Mix questions that check understanding (why something holds) with small
  calculations marked （計算してみよう）, using numbers like those in the
  text. Work each one through before printing its answer.
- End an answer with a link to the section it draws on:
  （→[6節](#section-6)）. Give that heading an explicit label. Labels are
  shared by the whole site, so the second and third documents prefix theirs
  (`what-section-3-1`, `practice-section-6`).
- In an answer, a reason ends 〜ため．, and a list of items may end without
  a predicate.
- On a practice page, a task done in code is marked （やってみよう）, and
  the opening line goes on 「（やってみよう）は，`lem-practice` で取り組む．」.
  Run each answer's code and pin the numbers it quotes in
  `docs/ja/examples/test_answers.py`.

## Glossary

`docs/ja/lem-glossary.md` collects the terms the documents share. It is a
Sphinx glossary, not a Markdown table, so every term is a target for
`{term}`; `docs/_static/glossary.css` lays it out as a table. It is not one
of the documents: it has no subtitle, builds-on line or 確認問題.

- Terms sit in groups under `##` headings, one `{glossary}` block per group.
  Within a group, a term follows the terms its definition builds on
  (静力学的不静定性 before 不静定性の解消, 全体すべり方向 before
  局所すべり方向).
- One term per entry: the stylesheet pairs each term with one definition,
  so name a synonym in the definition (任意形状のすべり面ともいう).
- An entry has two paragraphs. The first gives the symbol and the English
  term, split by a full-width space, or the English term alone; the
  stylesheet sets it small and grey. The second is the definition, which
  ends in links to the sections that explain the term, with no ．:

  ```text
  安全率
    $F_s$　factor of safety

    （定義）（→[第1章「LEMの全体像」](#overview)，[6節](#section-6)）
  ```
- Link text names the document, then the section: 第1章 6節, or the
  heading in 「」 for a section without a number, and 実践1 2節 for a
  practice page. A second section of the same document drops the document's
  name. Give each target heading a label, as for review questions. A linked
  section explains the term; where none does, add the explanation to the
  text.
- The English term is the one the English literature uses (slip surface,
  interslice force, direction of sliding), in American spelling
  (mobilized, center), as in the English edition.
- Keep the equations in a definition short: in the narrow column a long
  one breaks across lines. Link to the section that derives it instead.
- In a definition, link each other term at its first mention with
  `{term}`, except the terms of the first group, LEMの枠組み: すべり面 and
  スライス come up in almost every entry. Where the wording differs, name
  the entry: `` {term}`全垂直応力 <垂直応力>` ``.
- In each document and practice page, the first use of a term the page does
  not explain (its entry links only to other pages) links to the entry with
  `{term}`; later uses stay plain. Count only the main text: not the lead
  (up to the line that links the glossary), headings, tables, equations,
  captions or dropdowns. A use is the term itself, its abbreviation, a
  name its entry gives, or another form of the same words (LEM,
  任意形状のすべり面, 回転軸; 離散化, 不静定性を解消, 局所的なすべり方向);
  for all but the term itself, name the entry, as in
  `` {term}`LEM <極限平衡法>` ``. A word inside a use of another term is
  not a use (間隙水圧 in 間隙水圧の合力), and neither is a common word
  that stands for the term only in context (土塊, 強度, 基準点).
- A term gets an entry when readers may meet it away from the section that
  explains it: another document uses it, the same document uses it far
  from that section, or LEM uses it more narrowly than 土質力学 or
  材料力学 do (内力).

## English edition

`docs/en/` translates `docs/ja/` page for page. It does not follow changes
to the Japanese edition: a page is brought in line only when someone asks
for it.

- Each page's front matter records the Japanese commit it was translated
  from and the date, and the page shows them above its title, linking the
  Japanese page at that commit. Quote the commit: YAML reads an all-digit
  hash as a number.

  ```text
  translated_from: "56298d2"
  translated_on: 2026-10-04
  ```

  To bring a page in line, read `git diff <translated_from>..HEAD --
  docs/ja/<page>.md`, change the English to match, and record the new
  commit and date. The commit must stay on `main`, so merge a PR that
  records one with a merge commit, not a squash; after a squash, record
  the squashed commit instead.
- A page keeps its Japanese counterpart's file name, labels, equation
  labels and figure names: the language switcher pairs pages by file name,
  and the same labels keep the diff readable.
- The figures are not translations: `make figures` writes both
  `docs/ja/figures/` and `docs/en/figures/` from the same scripts, so a
  change to a figure reaches both editions at once. The practice code is a
  copy: `docs/en/examples/` has English docstrings, comments and printed
  text, and the Japanese code's names (`centres`, `fellenius`), so the two
  copies diff cleanly. `make examples` runs both.
- Write plain American English for the same readers: present tense, no
  "we", short sentences. Spell in American English (center, analyze,
  modeling, behavior, color) in prose; code keeps its names.
- Names of the parts:

  | Japanese | English |
  |---|---|
  | 第1章，この章 | Chapter 1, this chapter |
  | この資料，このシリーズ | this primer |
  | 6節；第1章 6節 | Section 6; Chapter 1, Section 6 |
  | 理論編，実践編，付録 | Theory, Practice, Appendix |
  | 実践1，この実践 | Practice 1, this practice |
  | 用語集 | Glossary |
  | 確認問題，次に読む，参考文献 | Review questions, What to read next, References |
  | （計算してみよう），（やってみよう） | (Calculate), (Try it) |
  | 補足A | Supplement A |

- Terms are the glossary's English terms (the first paragraph of each entry
  in `docs/ja/lem-glossary.md`), in American spelling. The English
  glossary names each entry by its term, lower case but for proper names
  (`factor of safety`, `Mohr–Coulomb failure criterion`), and `{term}`
  roles use those names. An entry's first paragraph is the symbol, a
  full-width space, the English term and the Japanese term in full-width
  parentheses: `$F_s$　factor of safety（安全率）`. Method names follow the English literature: Fellenius method
  (ordinary method of slices), simplified Bishop method, simplified Janbu
  method, Spencer method, Morgenstern–Price method.
- The structure rules above hold in English too: the opening (title, bold
  subtitle, lead, the line naming the chapters it builds on: "This chapter
  assumes that you have read [Chapter 1](…)."), the review questions, the
  glossary links on first use, and the link texts (Chapter 1, Section 6).
  - A review question reads `Q1. …`, or `Q2. (Calculate) …`, and the
    questions open with "Click a question to see its answer.".
  - An answer and a glossary definition end with `(→[Section 6](#section-6))`.
  - An equation is cited as Eq. {eq}`…`, or Eqs. for two.

## Figures

Each SVG in `docs/ja/figures/` and `docs/en/figures/` is written by a
script in `scripts/figures/`. Edit the script and run `make figures`; never
edit an SVG by hand. CI writes the figures again and fails if they differ
from the committed files.

- `scripts/figures/figlib.py` holds what the figures share: the colours, type
  sizes, arrowheads and math labels, plus the slope with its slip circle, the
  slice of 第2章 and a 3D projection.
- Text that differs by language is `L(ja, en)`; a position or anchor may be
  one too, where English needs another place. English labels use the
  glossary's English terms in American spelling.
- Compute geometry rather than place it by eye. A normal is perpendicular to
  its surface, a vector sum is drawn as one, and an arrow's length is
  proportional to its force. Where only the place of an unknown matters, as
  in fig_02, every arrow gets the same length.
- Colours carry meaning: red for weight, green for shear resisting sliding,
  blue for normal forces, purple for interslice forces, cyan for pore
  pressure, and grey dashes for unit vectors (n, m, d).
- A figure is 760 px wide, the width of the text column, so labels show at
  their set size (14 px, 13 px for secondary text). It has no title inside;
  the caption carries it.
- Labels, `<title>` and `<desc>` follow the terms and notation of the body.
  After a change, look at the figure in both languages in a browser: no
  label may cross an arrow or leave its panel.
