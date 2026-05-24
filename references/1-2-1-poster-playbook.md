# 1:2:1 Academic Poster Playbook

Use this reference after `SKILL.md` when a user wants a concrete poster plan, mockup, or production checklist.

## Public Guidance Synthesis

Open academic poster guidance is surprisingly consistent:

- Start with boxes on paper, then add content.
- Keep the story flowing left to right or top to bottom.
- Use only 2-3 colors, with strong contrast and no red/green pairing.
- Keep enough white space for readability, but sample-like academic posters should be information-rich and text-substantial: use roughly 15-25% empty space, 35-45% compact graphics/tables, and 30-40% readable text within the three-card body footprint.
- Distribute whitespace intentionally; do not leave most empty space as a large strip below the cards or at the bottom of one card.
- Make the title the largest text, keep it short, and avoid competing logos in the title area.
- Keep the main text readable from about 1.5m away.
- Use short bullets, not paper paragraphs.
- Include enough explanatory text that each section carries scientific content rather than becoming a decorative label.
- Keep figures proportional to their information value; do not enlarge sparse plots, screenshots, or low-evidence graphics just to fill space.
- Prefer a first-version/reference-like macro-block layout: a few strong sections per card with grouped text and visuals, not many small ledger rows or detached chips.
- Balance the three card stacks vertically: the left, center, and right cards should end at similar visual heights once content is laid out, not just share the same frame height.
- Treat tinted backgrounds and empty pale panels as whitespace, not content.
- Use the reference card recipes by default: motivation is a vertical text-plus-figure stack, method is an upper pipeline plus three unnumbered method subcards with no lower-half group heading, and experiment is vertical titled result blocks with near-full-width visuals.
- Fix the three main card header titles as `1、Motivation`, `2、Method`, and `3、Experiment`. Do not use paper-specific slogans in the blue header bars.
- Keep the gaps between the three cards narrow and sample-like, roughly the same visual scale as the outside breathing margin around the card cluster.
- Treat right-card bottom overflow as a hard render failure: no experiment title, sentence, figure, table, caption, or result block may cross or clip past the bottom border of the `3、Experiment` rounded rectangle. If it happens, proportionally shrink the right-card experiment visuals/tables until all content fits inside the card.
- Include the built-in `Reference CVPR Blue` palette as a selectable sample-matched scheme. Use it directly if the user selects it; otherwise show it as the first color option when asking for a palette.
- When a required region is short, first recover source-backed paper content, then enlarge typography, labels, and figure/table scale until the region is visibly full. If obvious blank space remains, scale the affected card or subcard typography proportionally until the blank pocket disappears. Do not leave a large box with tiny text.
- If the rendered poster looks like the current small-font failure case, increase the whole typography system by 4-8 pt, using +6 pt as the default starting correction. If the left card or center subcards still show lower blank space, continue proportional in-region font scaling beyond this correction.
- Put author/contact details, references, and QR code inside one of the three cards only if needed; the default composition has no separate header or footer band.
- Add a semantic check: can the poster answer the paper's core questions, not just look polished?

These rules are consistent with Barker & Phillips (2021), UNCW poster guidance, Purdue poster guidance, and the Frontiers analysis of "wall of text" posters. The billboard-style/BetterPoster literature also supports a minimalist, one-main-point layout, while noting that methods and limitations should still be present.

## Choosing The Skill Group

Choose `paper-poster` as the primary group because the artifact is a research communication deliverable, not a marketing banner or generic UI. Use design skills only as support:

- `paper-poster`: final PDF/PPTX/SVG production, conference poster export, LaTeX/tcbposter decisions.
- `paper-figure` or `nature-figure`: simplify plots, tables, heatmaps, and result panels.
- `paper-illustration`: create or refine the central method/architecture diagram.
- `design-system` / `ckm:design`: set venue colors, typography, and logo treatment when needed.

The 1:2:1 structure works best when one center-line method or result can carry the story and the side columns can stay compact. If the venue explicitly demands a conventional IMRAD poster, use `paper-poster` instead of forcing this layout.

## Input Checklist

Collect or infer these before layout:

- Paper title, authors, affiliations, venue, logos.
- One-sentence contribution claim.
- Task definition, problem context, and key bottleneck.
- Core method modules or pipeline stages.
- Key notation, equation meaning, or objective if needed to understand the method.
- Experimental setup: datasets, metrics, main baselines, and evaluation protocol.
- Main benchmark table and 1-2 supporting plots.
- 3-5 headline numbers that can be verified from the paper/results.
- Ablation interpretations, limitations, and final takeaway.
- Code/project URL, QR target, and contact email.

If data or affiliations are missing, mark placeholders explicitly instead of inventing them.

## Abstraction Worksheet

Before layout, convert the paper into poster decisions:

| Paper source | Poster decision |
| --- | --- |
| Title + abstract + contribution list | one claim line |
| Introduction + problem statement | 2-3 motivation bullets |
| Method overview + architecture figure | center hero diagram and 3-5 module labels |
| Main result table or headline plot | one primary evidence visual |
| Ablations or efficiency analysis | 1-2 small support visuals |
| Discussion or limitations | one takeaway or caution box |

For CS papers, use `references/poster-corpus-abstraction.md` before copywriting. If the target topic is narrow, generate a 20-50 item topic-neighbor sample and compare what nearby posters enlarge, compress, and omit.

## Text Ledger

Before drawing, create a text ledger that forces source coverage and prevents sparse posters:

| Source material | Poster destination | Required text payload |
| --- | --- | --- |
| Abstract + contribution list | left or center card intro | claim, novelty, one-sentence value proposition |
| Introduction | left column | task definition, why it matters, bottleneck, 2-4 contributions |
| Method | center column | module names, mechanism explanation, design rationale, key equation/notation meaning |
| Experiment | right column | datasets, metrics, baselines, main numbers, what the numbers mean |
| Ablations/analysis | right column | why the method works, efficiency/robustness/failure interpretation |
| Limitations/conclusion | right card or compact in-card note | caveat, deployment condition, or final takeaway |

For each destination, mark whether it has `definition`, `mechanism`, `evidence`, and `interpretation`. A poster can omit some labels, but it should not omit all interpretation.

## Correspondence Matrix

Build a short matrix before drafting text:

| Paper section | Poster zone | What changes |
| --- | --- | --- |
| Title/abstract | compact in-card claim line | compress into one sentence |
| Introduction | left column | keep only the bottleneck and why it matters |
| Method | center column | enlarge the core mechanism, reduce implementation detail |
| Results | right column | keep strongest evidence, cut redundant rows/plots |
| Limitations | right-card callout or compact in-card note | keep short and factual |

The matrix should answer four questions: what gets enlarged, what gets compressed, what gets reordered, and what gets omitted.

## Paper-Type Emphasis

After the correspondence matrix, choose the dominant poster evidence by paper type:

| Paper type | Poster should enlarge |
| --- | --- |
| Method or architecture paper | pipeline diagram, named modules, one proof table |
| Benchmark or dataset paper | data coverage, task taxonomy, representative examples, headline baselines |
| Efficiency or systems paper | runtime/memory/compute tradeoff, design bottleneck, deployment constraints |
| Vision or generation paper | qualitative strips, failure/success contrast, one metric panel |
| Theory or diagnostic paper | phenomenon plot, minimal equation, assumption-to-result path |

The 1:2:1 layout still applies: left explains why the evidence matters, center shows the mechanism or object of study, and right proves the claim.

## Canvas Model

Default landscape structure is body-only and measured by the three-card body footprint: three rounded rectangles, aligned top/bottom, with visible gutters.

When matching the provided reference image, use the union of the three rounded cards plus about 3% outer whitespace as the measurement box. Do not use the full image, title/authors/logo area, footer, email line, or any external wrapper as the proportion reference. The `1:2:1` rule applies to the three card widths inside this body footprint.

```text
canvas margin
  [ rounded left card ]   gutter   [      rounded center card      ]   gutter   [ rounded right card ]
  [ 1、Motivation     ]            [ 2、Method                     ]            [ 3、Experiment    ]
  [ problem/context   ]            [ hero pipeline / architecture  ]            [ tables/plots     ]
  [ contribution      ]            [ module details / equations    ]            [ ablations        ]
```

Width ratio: `1 : 2 : 1` for the three card widths. Gutters and outer margins are outside this ratio. Use exact arithmetic: `left_width = right_width = u`, `center_width = 2u`. Use the center as the visual anchor; side cards should feel supportive, not equally important.

Gutter rule: make the two inter-card gaps small and visually close to the outer breathing margin around the cluster. Do not leave wide lanes between cards. For normalized body-footprint geometry, each gutter should usually be `0.015-0.022` of footprint width and should not exceed about `0.025` unless the user explicitly asks for more spacing.

Required geometry:

| Element | Default |
| --- | --- |
| Body footprint | sample-matched three-card cluster plus about 3% outer whitespace |
| Outer margin | 2-4% of canvas width |
| Gutter between cards | 1.5-2.2% of body-footprint width each; hard upper limit about 2.5% |
| Card widths | strict 1:2:1 after subtracting margins/gutters; center = 2x either side |
| Card height | same top and bottom for all three cards |
| Card vertical span | fills usable body height after margins |
| Lower-half content | side cards have substantive lower-half content and bottom anchors; center lower half is exactly three filled method subcards with no group heading |
| Cross-card content balance | left, center, and right content stacks end at similar heights |
| Text/visual balance | 30-40% readable text, 35-45% compact visuals/tables, 15-25% whitespace |
| Corner radius | visually consistent, modest rounded rectangle |

Do not create separate top title areas, subtitle/author bands, metric strips, footers, QR strips, or full-width takeaway bars unless the user explicitly asks for a conventional conference poster.

Vertical fill rules:

- The three cards should extend from the top body margin to the bottom body margin. Do not let them float in the upper canvas.
- Keep final bottom margin visually similar to the top margin, usually within 2-4% of canvas width/height depending on format.
- Inside each card, target 85-95% content occupancy after padding.
- Avoid a single empty bottom zone larger than 5-6% of card height.
- The final non-background element in every card should sit in the lower 10% of the card.
- Give side cards a bottom anchor: takeaway, caveat, mini result, compact contact/citation note, or small diagnostic visual. In the center card, the closing/anchor text must live inside the three method subcards, not as a separate block.
- Do not count a tiny bottom anchor as sufficient vertical fill. Each side card also needs substantive lower-middle content below the midpoint, and the center lower half needs three filled subcard columns.
- The lower half should feel like a continuation of the card's narrative, not one small note floating at the bottom.
- Make the filled content heights of the three cards visually similar. A side card that ends much earlier than the center card should be stretched by content, not by background color.
- If the first render has too much bottom whitespace, rebalance inside the cards before changing canvas size.

Vertical packing model:

- Top zone: title/claim, short setup, or section heading.
- Upper-middle zone: main figure, table, or mechanism.
- Lower-middle zone: explanation, interpretation, comparison, or caveat.
- Bottom zone: bottom anchor. This must be real content, not decorative whitespace; for the center card, the bottom zone is the bottom of the three subcard columns.
- Do not place all content above the vertical midpoint of a card.
- If the area between the upper-middle content and bottom anchor is blank in a side card, extend or move a source-backed explanation, figure caption, equation note, result interpretation, or caveat into the lower-middle zone. In the center card, put this content inside one of the three method subcards. Prefer extending an existing macro section before adding a new container.
- When matching the sample image, the real content stacks in the three cards should feel equally full. Use copy length, figure height, caption spacing, and font size to bring the cards into visual balance.

Macro-block style:

- Build each card from a small number of broad narrative regions, not a stack of separate little boxes.
- Side cards usually need 2-4 macro sections; the center card usually needs 3-5.
- A macro section can combine a heading, paragraph, bullets, caption, and a compact visual in one coherent group.
- Use strong section headers and generous internal alignment, but avoid ledger strips, badges, chips, and table-like rows unless the source material is truly tabular.
- When blank space remains, deepen an existing section with source-backed interpretation or move that section lower. Do not fill by sprinkling unrelated mini-panels.

Visual density rules:

- Treat text and figures as paired evidence units: a figure/table should sit near a caption, interpretation bullet, or takeaway sentence.
- Do not use one huge plot to occupy space. Except for a true center method/architecture hero, a single visual should usually stay below one third of its card height.
- If a figure has sparse marks, redundant axes, or little explanatory value, crop it, shrink it, annotate it, turn it into a mini table, or remove it.
- Prefer compact, well-captioned evidence panels over oversized low-information charts.
- Keep body text large enough to read at poster-session distance. If text becomes tiny, merge scattered blocks and shorten copy rather than enlarging figures.
- If the poster feels like a form, dashboard, or ledger, merge micro-panels into the broader section style used by the reference sample.
- If one card looks visibly emptier than the others, raise its content height before touching the others' backgrounds.

Fixed card recipes:

- Main card titles: set the three header labels exactly to `1、Motivation`, `2、Method`, and `3、Experiment`. Put paper-specific claims, subtitles, and section names below the fixed header, not inside it.
- Motivation card: use a pure vertical stack. The allowed ingredients are text blocks and 1-2 motivation figures, ordered top to bottom. Avoid internal multi-column grids, horizontal metric strips, side-by-side mini-panels, and dashboard-like layouts. The final real content must reach the lower 5-8% of the usable card area, and the lower half must contain real text/caption/figure marks rather than a tiny bottom note.
- Motivation order: section title, problem/context paragraph, 2-4 bottleneck or contribution bullets, 1-2 near-full-card-width figures, and one compact preliminary-observation or takeaway paragraph. If the lower half looks empty, first search the paper for another supported motivation point, example, contribution nuance, or observation, then enlarge typography, caption size, line height, and figure crop before leaving space blank. For the current failure mode, raise left-card body/bullet/caption text by 4-8 pt as a starting correction, then proportionally scale all left-card internal typography and spacing in 5-10% increments until the lower half stops looking empty.
- Method card: split the usable center-card body into exact equal halves after the header. The upper 1/2 is only the main pipeline/architecture figure and a minimal label/caption strip. If the source paper has a usable method or pipeline figure, simplify and reuse it; draw a new pipeline only when no suitable paper figure exists. Use fixed-height boxes or explicit grid rows; content should not decide the row heights.
- Pipeline fill: the pipeline figure must fill the upper 1/2 region both horizontally and vertically. Target 90-100% upper-region width and 85-100% upper-region height with real diagram marks, labels, and caption text. If it appears too small, crop internal whitespace, enlarge labels and module boxes, increase line weight, enlarge caption/type, or scale/redraw the paper-faithful figure before adding any other content.
- Method lower area: the lower 1/2 must contain exactly three horizontal, equal-width method subcards. The three subcard columns fill the entire lower-half region. If the paper has more modules, merge them into three conceptual groups. Do not add a visible lower-half heading such as `Three balanced method subpoints`, `Lower half`, or any similar label. Do not add `claim`, `validity`, result plots, side notes, or extra bottom anchors outside the three subcards in the method card.
- Method subpoint equality: the three subcards must have matched title size, body font, line height, bullet style, and similar word/line counts. Each subcard title must be an unnumbered semantic mini-title only, such as `Certify locally`, `Inject equally`, or `Judge by ranking`; do not prefix titles with `1.`, `2.`, `3.`, letters, badges, bullets, or step numbers. The viewer should perceive them as three equal peers.
- Method fill priority: if the lower 1/2 looks sparse, first search the paper for more mechanism details, design rationale, notation meaning, or module behavior for the three existing subcards; then enlarge title font, body font, caption font, line height, and bullet spacing within those subcards. For the current failure mode, raise all three subcard cards by 4-8 pt as a starting correction, then scale all three subcards together in 5-10% increments until their lower blank areas are no longer obvious. Keep their typography matched. Do not invent a fourth idea.
- Experiment card: use a vertical sequence of titled result blocks. Each block needs a clear title, 1-2 source-backed sentences, and a figure/table.
- Experiment visual width: the first headline result table and every later result visual should span about 90-100% of the card inner width. The first table/plot is a hard gate: force it to full-width table layout, enlarged table font/cell padding, cropped margins, or a full-width grouped result panel before accepting the render. If there are several small plots, group them into a full-width row/panel with a shared title and caption.
- Experiment overflow repair: after rendering, inspect the right-card bottom edge. If any result block crosses or clips past the rounded rectangle, scale down right-card figures/tables in 5-10% proportional passes, either as a group or only for the overflowing block. Preserve readable captions and the near-full-width appearance where possible; only after visual shrink should you tighten vertical gaps or trim redundant source-backed sentences.

## Column Recipes

### Left Column: Motivation

Purpose: make the problem and bottleneck obvious in 15 seconds.

Good ingredients:

- A compact task/context paragraph or 3-5 bullets explaining why the task is hard.
- One or two vertically stacked motivation figures, each near-full-card-width.
- A bold "preliminary observation" or "key bottleneck" callout.
- 3-4 contribution bullets when the paper has multiple contributions.
- One takeaway sentence that tells the viewer why the poster matters.
- Optional short related-work contrast if it clarifies the bottleneck.
- Enlarged body/caption typography that makes the lower half visibly occupied; do not allow tiny text at the top followed by blank lower space. If blank remains after the global correction, proportionally scale the left-card text system until the lower blank pocket disappears.

Avoid:

- Any internal two-column layout, metric dashboard, horizontal strip, or side-by-side mini-panels.
- Long related-work paragraphs.
- Definitions the audience already knows.
- More than two figures.
- A large plot that replaces the motivation text. Motivation figures should support the bottleneck, not dominate the card.

### Center Column: Method

Purpose: explain the idea visually; this column justifies the `2` in `1:2:1`.

Good ingredients:

- One hero method pipeline/architecture figure occupying the exact upper 1/2 of the usable center-card body, measured after the header and padding.
- Exactly three equal method subcards occupying the exact lower 1/2, arranged horizontally as three equal-width columns, with no visible group heading above them.
- Captions and labels inside those two regions that describe actions and design rationale.
- One equation only if it clarifies selection, routing, loss, or objective; place its meaning note inside the relevant pipeline label or one of the three subcards.
- Source-backed mechanism text distributed across the three subcards, with similar line counts and matched typography.
- Enlarged subcard typography: titles, body bullets, captions, and closing notes should be 4-8 pt larger than the small-font baseline when the subcards otherwise look empty. If blank remains, scale all three subcard text systems together by 1.05-1.10x per pass until each subcard looks filled.

Figure guidance:

- Use a single visual grammar: consistent arrows, tokens, colors, and labels.
- Label modules with names that match the paper.
- Crop aggressively; remove decorative whitespace and redundant legends.
- Prefer vector PDF/SVG for LaTeX and 300 DPI PNG for PPTX.
- Keep the hero visual clearly larger than any supporting panel, while still confined to the exact upper 1/2 region.
- The hero should be a method/architecture explanation by default. Do not make a result plot the center hero unless the paper is primarily diagnostic or benchmark-driven.
- If the paper already has a usable method figure, use that figure as the basis and simplify it. Draw a new pipeline only when the paper lacks a usable method/pipeline visual.
- If the pipeline looks too small, crop whitespace, enlarge labels/module boxes/line weights/caption type, or redraw the pipeline at the same conceptual granularity; do not compensate by adding a separate center-card section.
- Place exactly three balanced explanatory subcards directly below it; do not leave the lower half as thin labels, scattered boxes, a group heading, or a fourth claim/validity block.
- The three subcards should look almost interchangeable in weight: same title size, comparable bullet count, comparable line count, matched body typography, and equal column height.

### Right Column: Experiment

Purpose: prove the claim with compact evidence.

Good ingredients:

- One headline result table or plot at the top, spanning 90-100% of the right-card inner width.
- Use tables only when the audience expects benchmark rows/columns; highlight them heavily.
- A short experimental setup note naming datasets, metrics, and baselines.
- Efficiency-versus-performance block.
- 1-2 small ablation or analysis plots.
- 2-4 result interpretation bullets and one boxed conclusion.
- Keep methods or limitations visible somewhere on the poster, even if they are compact.
- Each result block should be vertical: title, 1-2 explanatory sentences, then a full-width or near-full-width figure/table.
- Experiment figures/tables should usually fill 90-100% of the card inner width. If the first table renders narrow, rebuild it as a full-width highlighted table/panel or a composed multi-block result panel before doing any final export.
- Experiment table composition: when a table is the chosen result visual, prefer composing related metrics, subresults, or diagnostic rows into one wider table/panel with aligned columns, merged headers, or stacked subrows so the table fills the width without forcing a large font jump. Use cell padding, row height, header grouping, and panel composition to fill width before increasing the table font. Keep the table text visually close to the nearby explanation text so the table and prose read as one system, not as two mismatched typographic scales.
- After the first render, run a bottom-edge overflow check on the right card. If the lower experiment visual/table extends beyond the rounded rectangle or is clipped by it, shrink the experiment visuals/tables proportionally instead of moving the card boundary or adding an outside footer. Width should remain near-full when possible; the primary repair knob is height/scale.

Avoid:

- Full experimental setup paragraphs.
- Raw tables that require slow reading.
- Tables with too many rows/columns to understand at poster distance.
- Metrics not tied to the main claim.
- Enlarging a bar chart, scatter plot, or heatmap to fill the card. Evidence panels should be compact and accompanied by result interpretation.
- Narrow charts floating in the center of the right card. Crop or group them into full-width panels.
- Letting a right-card figure, table, caption, or result block extend below the card border. Overflow is not a layout compromise; it must be repaired by proportional visual/table shrink before export.

## Content Budget

Default target: 900-1300 body words, excluding table text and author affiliations. If matching a text-dense sample poster, allow 1100-1500 words as long as the body remains readable from poster-session distance and no text clips.

Area target inside the three-card body footprint:

| Area Type | Target Share | Failure Sign |
| --- | ---: | --- |
| Readable text, captions, labels | 30-40% | text looks tiny or incidental next to graphics |
| Figures, tables, diagrams | 35-45% | one sparse plot dominates a card |
| Intentional whitespace/gutters | 15-25% | information floats in disconnected islands |

| Area | Target Words | Visual Priority |
| --- | ---: | --- |
| Title/subtitle | 12-18 | title should be readable first |
| Motivation | 240-360 | context, bottleneck, contributions, lower-half observation/takeaway |
| Method | 420-620 | exact upper-half pipeline plus exact lower-half three subcards |
| Experiment | 320-480 | setup, results, ablations, interpretation, full-width headline table |
| In-card contact/caveat | 20-80 | QR/email/project/caveat if needed |

Copy rules:

- Use a mix of compact paragraphs, bullets, and captions; do not make every section a one-line slogan.
- Use numbers where possible: `42% less FLOPs`, not "significantly more efficient".
- Use active labels: `Select cubes`, `Route salient tokens`, `Skip redundant FFNs`.
- Keep captions explanatory and source-backed; a key figure caption can be 20-45 words.
- Remove generic AI prose and vague intensifiers.
- Left-align body text; avoid full justification if it creates ugly gaps.
- If a section has fewer than 80 words or fewer than 5 meaningful bullets/caption sentences, check the paper again before final rendering.
- If the center card lower half is not exactly three filled method subcard columns, it is too sparse or structurally wrong.
- If a figure occupies a large area but has fewer than 20-45 caption/interpretation words nearby, shrink or replace it.
- If a source-backed region is still sparse, enlarge font size, line height, caption size, table type, figure labels, and diagram geometry before accepting empty space.
- If the left or right card ends far above the center card, it needs more source-backed content and/or denser typography.
- If the poster's type feels small overall, apply a global +4 to +8 pt font correction across headers, section headings, body, captions, tables, plot labels, and diagram labels. Use +6 pt by default. This is not an upper limit: for underfilled left-card and center-subpoint regions, keep scaling typography proportionally until the blank space is not obvious.

## Visual System

Use a restrained academic design:

- Three top-level cards: left, center, right. These are the only major containers.
- Header titles: exactly `1、Motivation`, `2、Method`, and `3、Experiment`.
- Keep title/authors/logos out of the canvas by default; if required, place them compactly inside the relevant card.
- Cards: rounded rectangles, subtle shadow or border, strong header bar or left accent stripe.
- Color: one dark primary color for headers, one accent for highlights, neutral background.
- Built-in sample palette: `Reference CVPR Blue` uses white cards, `#2F5D99` header bars, dark body text, blue-gray modules, teal/cool supporting accents, and restrained orange highlights.
- Rhythm: repeat card padding, title size, line weight, and caption style.
- Figures: align baselines and keep captions visually consistent.
- Tables: highlight only the rows/columns that support the claim.
- Information grouping: arrange each card as a few coherent macro sections, not many detached micro-boxes. Related claims, numbers, and captions should sit together under shared headings.
- Card recipes: left is pure vertical motivation, center is exact upper 1/2 method pipeline plus exact lower 1/2 three equal unnumbered subcards, and right is vertical titled experiment blocks with wide visuals.
- Gutters: use narrow sample-like card gaps, visually close to the outer breathing margin. Large lanes between cards fail the style match.
- Vertical rhythm: distribute sections from top to bottom; do not stack everything at the top and leave the lower card empty.
- The center card is not free-form vertical rhythm: it uses two fixed rows of equal height after the header. The upper row is the pipeline; the lower row is exactly three unnumbered subcards with no group heading.
- Start the center lower half directly with the three subcards; do not render a visible line like `Three balanced method subpoints`, `Lower half`, or any equivalent wrapper label before them.
- If the center hero figure sits high or looks small, enlarge the pipeline figure's labels, module boxes, line weight, crop, and caption type inside the upper half. Do not add a separate lower-middle strip.
- If the center lower half looks empty, recover source-backed module rationale, notation meaning, or design tradeoff for the three existing subcards, then enlarge their typography and spacing. If blank remains, scale all three subcard typography systems together until the lower 1/2 is visibly filled. Do not add a fourth box or visible lower-half heading.
- The left and right cards should not look like they ran out of material halfway down. Their visible content should be expanded until the three cards read as a matched trio.

For a sample-like body-only poster, use the three-card cluster plus about 3% outer whitespace as the visible body footprint, with a neutral canvas background, three separated rounded white or lightly tinted cards, and compact dark text with restrained accent rules.

For sample-like density, the poster should feel like a compact academic explanation: diagrams and plots are important, but text blocks should remain visibly substantial. A figure that is only large because the layout has space is a layout failure.

Built-in palette: `Reference CVPR Blue`

| Role | Hex / value | Use |
| --- | --- | --- |
| background | `#F7F9FC` | page outside the three cards |
| card surface | `#FFFFFF` | main rounded rectangles |
| primary/header | `#2F5D99` | card header bars and main section labels |
| header text | `#FFFFFF` | text on blue headers |
| body text | `#111827` | main readable text |
| muted text | `#374151` | captions and secondary notes |
| border/grid | `#D8E2EE` | borders, table rules, plot gridlines |
| soft panel | `#EEF4FA` | subtle module backgrounds only when they contain content |
| secondary/module | `#AFC4DE` | method blocks, table highlights, module fills |
| cool highlight | `#8FD3D6` | selected tokens, light method accents, heatmap low/mid color |
| accent/highlight | `#F26A21` | key arrows, best results, caution/takeaway outlines |
| shadow | `rgba(17, 24, 39, 0.18)` | restrained card shadow |
| chart colors | `#2F5D99`, `#8FD3D6`, `#AFC4DE`, `#F26A21`, `#7C8DA6` | plots/tables |

Use this palette when the user asks for the sample/reference/CVPR-blue look. If no palette is selected, show it first among the color previews and ask the user to choose.

Palette rules:

- Use blue header bars on all three cards with white section titles.
- Keep card surfaces white so figures and text stay crisp.
- Use orange sparingly for one emphasis channel only.
- Use blue-gray and teal for method modules and grouped chart categories.
- Keep institutional or venue logo colors subordinate unless the user asks for brand matching.

Typography balancing:

- Start from a larger typography baseline than the current small-font output: globally increase card headers, section headings, body text, bullets, captions, table text, plot labels, and diagram labels by 4-8 pt; +6 pt is the default repair.
- Treat +4-8 pt as a starting correction, not a ceiling. When the left card or a center method subcard still has visible lower blank space, scale the affected card/subcard typography proportionally in 1.05-1.10x passes until the blank pocket is no longer obvious.
- Keep the same typographic scale across the three cards unless there is a clear role difference for headers or captions.
- If a side card or method subcard region is too empty after source-backed content is selected, increase body font size, line height, caption size, table type, or label scale as an active fill tool while keeping the system visually consistent. For the three center subcards, always scale the three cards together with the same multiplier.
- If the right experiment card is overfull at the bottom, shrink right-card figures/tables proportionally before reducing body text. For other overfull areas, reduce body font size in small steps, tighten line height, crop figure whitespace, or shorten redundant bullets.
- Do not make one card look sparse by using a tiny font while another card uses oversized body text. The sample-like look depends on consistent text density.

## Vertical Fill Tactics

When the rendered poster has too much blank space at the bottom:

- Increase figure/table height inside the card only if the figure is information-rich and still readable; otherwise add explanation, interpretation, or a compact table instead.
- Move a takeaway, caveat, or compact contact note to the card bottom as an anchor.
- Split a dense paragraph into two smaller subblocks and place the second lower in the card.
- Add source-backed caption text or result interpretation bullets where the paper has material to support them.
- Rebalance section heights so figures, captions, and callouts form a top-to-bottom rhythm.
- If one card is much shorter internally, add a small in-card diagnostic, mini table, equation note, or limitation box from the paper.
- If one card is much shorter internally, first enlarge or split its existing sections, then only add a small in-card diagnostic or mini table if needed.
- Keep the three top-level cards the same height; do not solve bottom blank space by shortening one card.
- If the lower half of the center card is mostly empty, do not add a second visual row or any extra strip. Recover source-backed method details for the three existing subcards, then enlarge their title/body/caption typography and spacing. If blank remains, proportionally scale all three subcards together until the lower 1/2 is full.
- If the left card lower half is mostly empty, enlarge the existing source-backed text, captions, and bullet spacing by 4-8 pt before changing structure. If blank remains, scale all left-card internal typography and spacing by 1.05-1.10x per pass until the lower blank area is not obvious.
- If any center subcard has a large blank lower area, enlarge all three subcards together by 4-8 pt and tune line height so their filled heights match. If blank remains, keep scaling all three subcards together until no subcard has an obvious lower blank pocket.
- If the right card crosses its bottom border, do the opposite of the underfill repair: keep the card geometry fixed and proportionally shrink experiment figures/tables in 5-10% passes until every title, sentence, caption, plot, and table is inside the rounded rectangle. Prefer shrinking the overflowing visual block first; if several blocks together cause overflow, apply one shared visual scale factor to the right-card visuals/tables.
- If right-card overflow remains after visual/table shrink, crop plot whitespace, slightly tighten vertical gaps and caption line height, then remove only redundant source-backed explanation text. Do not move content outside the card, lower the card bottom, or shrink the whole poster.
- If any card has only one small element below the midpoint, it still fails. Move or extend an existing explanation section downward before adding a new box.
- If the lower half contains a large empty pocket, extend the nearest macro section into lower-middle and bottom-anchor zones instead of enlarging gutters or adding outside footer material.
- If any card's final content block ends above 90% of card height, revise before export.
- Do not let the center card end after the hero figure; the exact lower 1/2 must be filled by the three unnumbered method subcard columns.
- Do not solve empty space by scaling up a weak plot. A large figure must add explanatory value through annotations, labels, or readable detail.
- Do not solve empty space by converting the card into many small boxed rows. The desired repair is "first-version macro layout, with less internal blank space."
- Do not let the left and right cards keep large empty lower regions while the center card is full; rebalance typography, figure sizes, and copy density until the trio feels even.

## Production Flow

1. Draft `POSTER_121_PLAN.md`.
2. If the user has selected `Reference CVPR Blue`, use it directly; otherwise produce 3+ color-direction previews with `Reference CVPR Blue` first and stop for user choice.
3. Build the text ledger and confirm text sufficiency for each column.
4. Confirm the figure list, corpus abstraction decisions, and missing placeholders.
5. Build a low-fidelity layout first: three rounded 1:2:1 cards, gutters, large section titles, figure slots, table slots, and macro text blocks.
6. Set fixed card headers to exactly `1、Motivation`, `2、Method`, and `3、Experiment`.
7. Apply the global typography correction: increase all font classes by 4-8 pt from the small-font baseline, normally +6 pt.
8. Build a visual budget map: figure/table slots, expected size share, nearby caption/interpretation text, and reason each visual earns its area.
9. Build a fixed recipe map: left pure vertical stack, center exact upper 1/2 pipeline plus exact lower 1/2 three equal unnumbered method subcards with no lower-half heading, right vertical result blocks with a 90-100% width headline table/plot.
10. Build a narrow-gutter geometry map: exact 1:2:1 card widths with two gutters around 1.5-2.2% of body-footprint width.
11. Build a vertical packing map: top zone, upper-middle zone, lower-middle zone, and bottom anchor for side cards; exact two-zone upper/lower half map for the center card, with no visible lower-half heading.
12. Build a cross-card balance map: expected content top, content bottom, and content span for left, center, and right cards.
13. Insert figures, tables, and source-backed text before polishing layout.
14. Rewrite copy to fit the actual boxes without deleting essential definitions, mechanism explanations, or result interpretations.
15. Run a macro-block pass: merge ledger rows, detached chips, and scattered micro-boxes into fewer coherent sections.
16. Run a visual density pass: reject oversized filler figures, tiny text, and scattered micro-boxes.
17. Run a fixed-recipe pass: reject a dashboard-like motivation card, an approximate center split, missing/unequal method subcards, numbered subcard titles, a lower-half group heading, extra center-card sections outside the subcards, or narrow right-card experiment charts/tables.
18. Run a proportional font-fill pass: verify the left-card lower half and all three center subcards are filled by enlarged readable text/caption marks, not pale empty backgrounds. If any target area still has obvious trailing blank space, scale the affected typography system by 1.05-1.10x and re-render until it passes.
19. Run a card-balance pass: adjust copy length, font size, line height, figure crop, caption depth, and section heights until the three cards' real content stacks end at similar heights.
20. Run a right-card overflow pass: inspect whether any `3、Experiment` content crosses or clips past the card bottom; if so, shrink right-card figures/tables proportionally by 5-10% and re-render until the card fits.
21. Run a vertical fill pass: check bottom margin, internal card occupancy, lower-half content, side-card bottom anchors, center-card embedded anchor text, and font/table/label scaling in sparse regions.
22. Render to PDF/PNG and visually review.
23. Run `scripts/audit_vertical_fill.py` or an equivalent rendered-image audit using the actual card boxes.
24. Export final PDF, editable PPTX/SVG, and source files as requested.

Example audit command, replacing coordinates with the real card boxes:

```bash
python scripts/audit_vertical_fill.py poster/main.png \
  --card left:0.03,0.04,0.256,0.96 \
  --card center:0.274,0.04,0.726,0.96 \
  --card right:0.744,0.04,0.97,0.96 \
  --max-content-bottom-spread 0.04 \
  --max-content-span-spread 0.08 \
  --min-content-span 0.82 \
  --min-gutter-ratio 0.008 \
  --max-gutter-ratio 0.025 \
  --max-gutter-spread 0.006 \
  --max-side-width-spread 0.008 \
  --max-center-ratio-error 0.015
```

If the audit fails, the poster is not ready. Add lower-half source-backed content, enlarge typography/labels/tables/figures inside their assigned regions, move side-card bottom anchors, enrich the center-card subcards, or shrink right-card experiment visuals/tables when the right card overflows before export.

Recommended plan template:

```markdown
# POSTER_121_PLAN

## Claim
[problem -> method -> evidence -> takeaway]

## Corpus Abstraction
- Source sample:
- What to enlarge:
- What to compress:
- What to omit:

## Text Ledger
- Problem/task text:
- Method/module text:
- Experiment/setup text:
- Result interpretation text:
- Limitation/takeaway text:
- Total body word target:

## Visual Budget
- Target text/visual/whitespace share:
- Visuals kept:
- Visuals removed or shrunk:
- Largest visual and why it earns that size:
- Caption/interpretation text for each visual:
- Scatter-risk blocks to merge:
- Macro sections per card:

## Canvas
- Size/orientation:
- Venue/theme:
- Body footprint reference: three rounded cards plus about 3% outer whitespace, excluding any title/footer wrapper
- Top-level structure: three rounded rectangles only
- Fixed card headers: `1、Motivation`, `2、Method`, `3、Experiment`
- Card ratio: strict 1:2:1
- Card width formula: `left_width = right_width = u`, `center_width = 2u`; exclude gutters, shadows, borders, and outer whitespace
- Outer margins:
- Inter-card gutters:
- Gutter target and measured value:
- Card height / vertical span:
- Bottom margin:
- Internal occupancy target:
- Vertical packing map:
- Content height balance target:
- Content top/bottom/span by card:
- Font-size/line-height adjustment plan:
- Global font increase applied: +[4-8] pt starting correction
- Proportional font-fit loop applied:
- Center half split measured:
- Upper pipeline fill strategy:
- Lower three-subcard fill strategy:
- Right headline table width:
- Font/table/label scaling used:
- Lower-half narrative:
- Left-card lower-half font-fill check:
- Left-card proportional scale factor:
- Center subcard font-fill check:
- Center subcard shared scale factor:
- Bottom anchors:
- Vertical fill audit command:
- Vertical fill audit result:
- Corner radius:
- In-card title/contact needs:

## Fixed Card Recipes
- Main card headers exact:
- Motivation vertical stack:
- Motivation figures, count and order:
- Method pipeline source: paper figure / newly drawn
- Method pipeline height share: exact upper 1/2
- Method pipeline width/height fill:
- Three method subcards:
- Subcard titles unnumbered:
- No lower-half group heading:
- Lower-half three-column fill:
- Method subcard word/line count balance:
- Method subcard font-size/line-height fill:
- No extra center sections outside subcards:
- Experiment result blocks:
- Experiment visual width target:
- First/headline table measured width:
- Right-card bottom overflow check:
- Right experiment visual/table scale factor:
- Right-card post-shrink fit result:

## Color Direction
- Options generated:
- Selected scheme:
- Built-in `Reference CVPR Blue` used or shown:
- Contrast/readability notes:

## Left: Motivation
- Purpose:
- Bullets:
- Paragraph/caption text:
- Visuals:
- Pure vertical stack check:
- Visual size cap:
- Interpretation text:

## Center: Method
- Hero figure:
- Pipeline source:
- Pipeline height share:
- Three equal method subcards:
- Subcard typography/word-count balance:
- Explanation text:
- Equations/callouts:
- Visual size cap:

## Right: Experiment
- Main table/plot:
- Supporting plots:
- Titled vertical result blocks:
- 1-2 sentence explanation per block:
- Figure/table width fill:
- Bottom overflow detected:
- Proportional visual/table shrink applied:
- Post-shrink bottom inside card:
- Setup/result interpretation text:
- Takeaway:
- Visual size cap:

## Risks
- Missing data:
- Overfull areas:
- Right-card bottom overflow:
- Excess bottom whitespace:
- Imbalanced card content heights:
- Excessive inter-card gutters:
- Fixed recipe violation:
- Failed vertical fill audit:
- Readability concerns:
- Oversized filler figure risk:
- Scattered information risk:
```

## Review Rubric

Pass/fail checks:

- Can a viewer understand the contribution in 60 seconds?
- Is the center column clearly the hero?
- Are all numbers traceable to the source material?
- Is every figure readable at poster-session distance?
- Does every large figure earn its area with dense information, annotations, or nearby interpretation text?
- Is any plot/table/screenshot oversized merely to fill blank space?
- Are tables compact, highlighted, and readable at poster distance?
- Are there exactly three top-level rounded cards in strict 1:2:1 ratio?
- Are the three main card headers exactly `1、Motivation`, `2、Method`, and `3、Experiment`?
- Is the center card exactly twice either side card, with left and right card widths equal, after excluding gutters and outer whitespace?
- Is the sample-matched proportion measured from the three-card body footprint plus about 3% outer whitespace, not from the full image?
- Are the gutters between the three cards narrow, visibly empty, consistent, and roughly the same visual scale as the outer breathing margin?
- Does the rendered geometry audit pass the narrow-gutter thresholds?
- Does the motivation card use a pure vertical text-plus-1-2-figures stack?
- Does the motivation card lower half contain substantive source-backed text/caption/figure content instead of blank space?
- Did the motivation card use enlarged body/caption/bullet typography and proportional in-card scaling to remove lower-half blank space?
- Does the method card use a paper-derived pipeline figure when available, with a newly drawn pipeline only when needed?
- Does the method pipeline occupy the exact upper 1/2 of the usable center-card body, not an approximate 45-55% region?
- Does the method card have exactly three matched unnumbered subcards below the pipeline with similar font, line count, and content amount?
- Do the three method subcard titles use only semantic mini-titles, with no `1.`, `2.`, `3.`, letters, bullets, badges, or step numbers?
- Did all three method subcards use matched enlarged typography, line height, and shared proportional scale factors to fill their lower-half subcards?
- Are there no extra center-card sections, lower-half group headings, result strips, validity blocks, or standalone bottom anchors outside the three subcards?
- Does the experiments card use vertical titled result blocks with 1-2 sentence explanations and near-full-width figures/tables?
- Does the first/headline experiment table or plot span 90-100% of the right-card inner width?
- Does every right-card experiment block, figure, table, caption, and sentence remain inside the `3、Experiment` rounded rectangle, with nothing crossing or clipping beyond the bottom border?
- If the right card initially overflowed, was it repaired by proportional shrinking of right-card visuals/tables before moving borders, adding outside space, or shrinking all poster text?
- Do the three cards fill the usable body height with no large bottom blank strip?
- Is each card internally occupied enough, with no bottom empty zone larger than about 5-6% of card height?
- Do the left, center, and right cards have similar real content heights, with content bottoms aligned within about 3-4% of card height?
- Does each card's real content span about 85-95% of usable card height, excluding empty tinted backgrounds?
- Does every card include substantive lower-half content, not just top-clustered content or a tiny bottom tag?
- Is the center card split into exact upper 1/2 pipeline and exact lower 1/2 three filled method subcards, with any anchor text embedded inside those subcards?
- Is every card's final content block placed near the bottom, with no bottom empty zone larger than about 5-6% of card height?
- Do side cards have meaningful bottom anchors, and does the center card embed its closing/anchor text inside the three subcards?
- Does the rendered-image vertical fill audit pass?
- Are separate title, metric, footer, and full-width takeaway bands absent unless explicitly requested?
- Are side columns supporting, not competing with, the method column?
- Are headers, gutters, baselines, and card edges aligned?
- Are card contents grouped into coherent macro sections rather than scattered micro-boxes, chips, or ledger strips?
- Is the image/text balance sample-like, with body text visually substantial rather than incidental?
- If no custom palette was chosen, was `Reference CVPR Blue` shown as the first palette option?
- Are font size, line height, caption depth, and figure scale balanced so the three cards look like one matched system?
- Was the overall typography scale increased by 4-8 pt from the small-font baseline, then further proportionally scaled in underfilled cards/subcards unless clipping made that impossible?
- Are pale panels used only behind real content, not as empty fill to fake density?
- Is there no clipped text, tiny caption, broken logo, or unexplained acronym?
- Does the poster avoid paper-like paragraphs?
- Does each major section contain enough source-backed text to explain its role?
- When a region is sparse, did the layout first recover source-backed paper content and then enlarge font/line height/table/label/figure scale, including proportional in-card scaling where blank space remained, without inventing content?
- Does the poster include task definition, method rationale, experiment setup, result interpretation, and at least one caveat/takeaway?
- Can a viewer answer 3-5 core questions about the paper from the poster alone?

If any pass/fail check fails, revise the plan or layout before export.
