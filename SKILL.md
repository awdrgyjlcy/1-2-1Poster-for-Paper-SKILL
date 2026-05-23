---
name: paper-poster-121
description: "Design and structure body-only 1:2:1 academic conference posters with three separated rounded rectangles: narrow left card, wide center card, narrow right card. Use when the user asks for a 1:2:1 poster, betterposter, academic poster layout, conference poster layout, CVPR-style poster, or to analyze accessible paper-poster pairs and public poster corpora to turn a paper/outline/results into a three-card poster plan and paper-to-poster correspondence map."
---

# Paper Poster 1:2:1

## Overview

Use this skill to turn a paper, abstract, method outline, or result dump into a 1:2:1 academic poster plan and production checklist. Treat `paper-poster` as the build/export skill; use this skill to decide the narrative, grid, content budget, figure hierarchy, and visual review standard.

## Evidence-Backed Defaults

- Treat the poster as a visual abstract, not a paper reprint, but do not make it text-starved.
- Aim for one main point, then support it with figures plus enough source-backed explanatory text for each major section.
- Default to a body-only three-card composition: no separate top title band, subtitle/author band, metric strip, footer, or full-width bottom bar unless the user explicitly requests them.
- If a paper title/claim is needed, place it compactly inside one of the three cards; do not create a standalone title region.
- Fill the vertical canvas with the three cards; avoid large unused bottom whitespace or short cards floating in the upper area.
- Inside each card, distribute content vertically from top to bottom; do not let the lower half of a card stay mostly empty after the main figure or opening bullets.
- Use 2-3 colors max and avoid red/green pairings.
- Treat colors as semantic roles, not isolated hex values: primary/header, secondary/module, accent/highlight, background, surface, text, and chart colors.
- Target an information-rich academic balance: roughly 20-30% whitespace, 35-45% graphics/tables, and 25-35% text.
- Make the main body readable from about 1.5m away.
- Prefer left-aligned text, clear section flow, visible contact details, and a QR code.

## Skill Group

- Primary group: `paper-poster` / research communication.
- Supporting skills: use `paper-figure` for plot selection, `paper-illustration` for method diagrams, and `design-system` or `ckm:design` only when brand/color systems are needed.
- Prefer this skill over generic design skills when the deliverable is a research poster with title/authors, method figure, experiments, and conference branding.

## Quick Workflow

1. Distill the story into one claim:
   `problem -> key idea -> evidence -> takeaway`.
2. Lock the 1:2:1 canvas:
   exactly three side-by-side rounded rectangles with visible gaps; left motivation card, center wide method card, right experiments/evidence card; width ratio must be `1:2:1`.
3. Allocate content by role:
   left = why it matters, center = how it works, right = why it is convincing.
4. Select visuals before writing copy:
   one center hero diagram, one or two compact result tables/plots, and only small supporting observations on the sides.
5. Build a vertical packing map for each card:
   top intro, middle core visual or argument, lower explanation/evidence, bottom anchor; no card should end immediately after its main figure.
6. Build the paper-to-poster correspondence matrix:
   map title/abstract, intro, method, results, and limitations into poster zones; decide what gets enlarged, compressed, reordered, or omitted before you write poster copy.
7. Run the text sufficiency checkpoint:
   extract enough important source-backed text from the paper for every poster zone; set a word budget and section-level text floor before layout rendering.
8. Run the vertical fill checkpoint:
   set card height, internal section stacking, and content density so the three cards use the available poster height without leaving a large bottom blank region.
9. Run the color direction checkpoint:
   based on the paper topic, venue, domain, figures, and logos, propose at least 3 distinct visual color schemes; generate a separate palette preview image for each scheme; ask the user to choose one before any final drawing or rendering continues.
10. Run the corpus-grounded abstraction pass:
   apply the corpus-derived paper-to-poster compression rules and compare them against the correspondence matrix; when refreshing the skill or doing broad genre learning, search 1000+ accessible paper-poster pairs from official CS conference virtual sites; for a specific paper, optionally sample 20-50 topic-neighbor posters before copywriting.
11. Rewrite text into poster language:
   compact paragraphs, bullets, labels, callouts, numbers, and figure captions; preserve key definitions, mechanism explanations, result interpretation, and caveats.
12. Produce a `POSTER_121_PLAN.md` before implementation:
   include card map, text ledger, figure list, word budget, color/type choices, card geometry, gutter sizes, vertical fill plan, and review risks.
13. Build in the user's target stack:
   use LaTeX/tcbposter for print PDF, HTML/CSS for fast visual iteration, or PPTX/SVG when editability matters.
14. Run a vertical fill audit on the rendered artifact if available:
   use `scripts/audit_vertical_fill.py` or equivalent to verify each card has lower-half content and the bottom blank fraction stays under threshold before final delivery.
15. Review visually:
   check 60-second comprehension, center-column dominance, readability from distance, alignment, no clipping, no unsupported numbers, and no excessive bottom blank space.
16. Review semantically:
   ask 3-5 core questions about the paper and verify the poster lets a viewer answer them without reading the full paper.

## Text Sufficiency Checkpoint

Before final layout rendering, build a source-backed text ledger and prevent underfilled sections.

1. Extract a text bank from the paper:
   problem context, task definition, bottleneck, contribution list, method modules, objective/equation meaning, datasets, metrics, baselines, headline numbers, ablation interpretation, limitations, and final takeaway.
2. Map the text bank to poster zones:
   left = motivation, task setup, bottleneck, and contributions; center = method mechanism, module explanations, notation/equation meaning, and design rationale; right = experimental setup, main results, ablations, efficiency/robustness, limitations, and takeaway.
3. Set an information-rich word budget:
   default A0/A1 target is 900-1300 body words excluding author affiliations and table cell text; for a text-dense reference poster, allow 1100-1500 words if readability survives.
4. Use section-level text floors:
   left card 200-320 words, center card 380-560 words, right card 320-460 words, optional in-card contact/caveat note 20-80 words. Every major body section should have at least 80 words or at least 5 meaningful bullets/caption sentences unless it is purely a figure/table label.
5. Preserve scientific payload:
   keep enough text for a viewer to answer what the problem is, what is new, how it works, what evidence supports it, and when it may fail.
6. Rewrite, do not paste:
   use compact academic prose, bullets, and captions; avoid copying full paper paragraphs, but also avoid reducing a section to icons, one-line slogans, or empty callouts.
7. If the first mockup looks sparse:
   return to the source paper and add missing definitions, module explanations, experimental setup details, result interpretations, or caveats before changing decoration.
8. If a card still looks vertically sparse:
   add a lower-third in-card block such as a mini table, micro-figure, method rationale, result interpretation, caveat, or compact citation note before reducing font size or shrinking the card.

## Color Direction Checkpoint

Before final layout rendering, create a color-choice checkpoint and stop for user selection.

1. Infer visual directions from the paper:
   domain metaphors, target venue, topic mood, method keywords, existing logos, and figure colors.
2. Generate at least 3 named schemes:
   each scheme must include primary/header, secondary/module, accent/highlight, background, surface/card, body text, muted text, grid/border, and chart/table highlight colors.
3. Keep schemes meaningfully different:
   for example `Conference Navy`, `Scientific Teal`, `High-Contrast Graphite`, `Warm Data`, or a domain-specific option such as `Medical Green` or `Robotics Amber`.
4. Check contrast before showing:
   body text on surfaces should target WCAG AA contrast; large poster titles and header text must remain legible from distance.
5. Generate visual preview images:
   for each scheme, create a PNG/SVG/HTML-screenshot swatch board that shows color chips, semantic roles, a mini three-rounded-card 1:2:1 poster mockup, section headers, callout boxes, a sample chart/table highlight, and sample body/caption text.
6. Present the previews together:
   save them under a clear folder such as `poster/color-options/` and summarize tradeoffs in `POSTER_121_COLOR_OPTIONS.md`.
7. Stop and ask the user to choose:
   do not continue to final poster drawing, LaTeX/HTML/PPTX production, or figure recoloring until the user explicitly selects a scheme or asks for revisions.

Palette preview requirements:

- Show the same miniature poster structure for every option so the choice is about color, not layout.
- Include hex codes and role names on each preview.
- Avoid relying on color alone to encode experimental meaning; pair color with labels, line styles, or symbols.
- Respect venue or institution brand colors when logos require them, but do not let brand colors overwhelm paper readability.

## Vertical Fill Checkpoint

Before final rendering, prevent bottom-heavy empty space and keep the three-card layout proportionally balanced.

1. Define the usable body box:
   after subtracting outer margins, the three cards should occupy the full usable height. The card bottoms should sit within 2-3% of canvas height from the intended bottom margin.
2. Use equal card height:
   left, center, and right cards must share the same top and bottom coordinates unless the user explicitly asks for staggered cards.
3. Fill each card internally:
   target 85-95% internal content occupancy after padding. Empty space inside a card should be distributed as intentional breathing room between sections, not concentrated as one large blank area at the bottom.
4. Use a four-zone internal grid:
   every card must contain top, upper-middle, lower-middle, and bottom-anchor zones. Equal-height card frames alone do not pass if the lower half is visually empty.
5. If bottom blank space appears:
   first expand or move content downward within the card, then increase figure/table height, add source-backed captions or interpretation bullets, split dense text into subblocks, or rebalance section heights. Do not solve it by adding an external footer band.
6. Use bottom anchors:
   every card should have a meaningful lower anchor such as a takeaway, caveat, mini table, compact citation/contact note, or small diagnostic figure placed inside the card.
7. Render-check the result:
   after exporting PDF/PNG/SVG, inspect the full page. If the empty area below the three cards or at the bottom of any card exceeds about 5-6% of card height, revise layout before final delivery.
8. Audit as a hard gate:
   if a rendered image exists, run `scripts/audit_vertical_fill.py` or an equivalent check. If any card lacks lower-half content or fails the blank-space threshold, regenerate/rebalance the layout before delivery.

## Corpus-Grounded Abstraction Pass

When the topic is in computer science or a nearby technical field, ground the poster plan in a searchable paper-poster corpus before final copywriting.

1. For normal poster generation, read `references/poster-corpus-abstraction.md` first and apply its reduction rules.
2. If the paper topic is niche or the user asks for a fresh corpus refresh, search only accessible paper/poster pairs from official conference virtual sites, proceedings pages, or equivalent public conference pages.
3. Prefer CS venues with paired paper and poster artifacts such as NeurIPS, CVPR, ICLR, ICML, ACL, ECCV, and ICCV.
4. Use a large sample when updating the skill, ideally 1000+ accessible pairs; for one target poster, a focused 20-50 topic-neighbor sample is usually enough.
5. For topic-neighbor sampling, query with the paper's task, method noun, evidence type, and domain keywords; avoid generic terms such as only `deep learning` or `large model`.
6. Extract how posters compress the source paper:
   title becomes the claim, abstract becomes a value proposition, intro becomes task context plus 3-5 motivation/contribution bullets, method becomes one hero figure plus module labels and lower-half explanation blocks, results become one compact table or plot plus 2-4 interpretation bullets, and limitations become a short caution or takeaway.
7. Save the synthesis in `references/poster-corpus-abstraction.md` and reuse it to cut material, not just to style it.
8. Do not use inaccessible, unpaired, or non-paper poster examples.
9. Do not let the corpus override the paper's actual claims or venue constraints.

## Layout Defaults

- Use exactly three top-level rounded rectangles as the visible poster body. Do not add a separate title/header band, metric strip, footer/contact strip, QR strip, or full-width bottom takeaway bar by default.
- Use a strict 1:2:1 width ratio for the three cards. For landscape posters, allocate available inner width as `left:gutter:center:gutter:right`, with the card widths in `1:2:1` and gutters excluded from the ratio.
- Put clear whitespace between cards: use gutters around 2.5-4% of canvas width each, and outer margins around 2-4% of canvas width. The three cards should not touch.
- Make all three cards aligned to the same top and bottom edges, with consistent rounded corners. Use a modest radius (roughly 12-24 px for screen previews, or visually equivalent in print units).
- The three cards should fill the usable vertical body. Avoid layouts where the cards or their content stop early and leave a large empty strip at the bottom.
- The center card should be the vertically densest card; it must continue past its hero figure with explanation, interpretation, or a lower anchor block.
- Put any required title, authors, QR, references, or caveats inside the three cards only when necessary; never create a separate outside band unless the user asks for a conventional conference poster.
- Make the center card visually dominant: large architecture/method figure on top or center, then concise module explanations underneath or beside it.
- Keep the left card focused on motivation, bottleneck, preliminary observation, or contribution bullets.
- Keep the right card evidence-heavy: compact result table or plot, efficiency/performance comparison, ablation/analysis plots, and one compact takeaway.
- Use numbered section headers such as `1. Motivation`, `2. Method`, `3. Experiments` when the paper story is linear.

## Detailed Playbook

Read `references/1-2-1-poster-playbook.md` when the user needs any of:

- a detailed layout recipe or content budget,
- a fill-in poster planning template,
- figure selection and simplification guidance,
- visual design rules for cards, typography, colors, and logos,
- a final review rubric before export or printing.

Read `references/public-poster-guidance.md` when you want the public-source basis for the defaults in this skill.

Read `references/poster-corpus-abstraction.md` when you want the corpus-grounded paper-to-poster abstraction rules, topic-neighbor sampling commands, or a summary of the accessible paper/poster sample.

Use `scripts/collect_poster_corpus.py` when you want to refresh or extend the corpus summary from official conference virtual poster pages.

Use `scripts/audit_vertical_fill.py` after rendering a PNG preview to enforce the no-large-bottom-blank rule. Pass the actual normalized or pixel boxes of the three cards; if any card fails, revise the layout before delivery.

Useful corpus commands:

```bash
python scripts/collect_poster_corpus.py --output references/poster-corpus-scan.json
python scripts/collect_poster_corpus.py --include-links --output references/poster-corpus-index.json
python scripts/collect_poster_corpus.py --query "<task method domain evidence>" --top-k 30 --output references/topic-neighbor-sample.json
```

Useful vertical audit command:

```bash
python scripts/audit_vertical_fill.py poster/main.png \
  --card left:0.03,0.04,0.25,0.96 \
  --card center:0.28,0.04,0.72,0.96 \
  --card right:0.75,0.04,0.97,0.96
```

## Guardrails

- Do not fabricate claims, metrics, affiliations, logos, or citations.
- Do not dump paper prose into the poster; rewrite into short bullets and callouts.
- Do not let equal-width grids override the 1:2:1 story. The center column must earn its width.
- Do not place a standalone title area, metrics band, footer, or bottom takeaway strip outside the three rounded 1:2:1 cards unless explicitly requested.
- Do not leave a large bottom blank area. If content is short, enlarge/rebalance in-card figures, captions, takeaway blocks, or source-backed explanations inside the three cards.
- Do not let any card terminate right after a hero figure or opening bullets. Every card needs at least one lower-half content block.
- Do not build a wall-of-text IMRAD poster unless the venue explicitly requires it.
- Do not start final rendering until the claim, column roles, and figure list are explicit.
- Ask at most one clarifying question only when the missing information would otherwise force fabricated results or branding.
- Do not rerun corpus collection for ordinary poster drafting; use the learned abstraction note unless a refresh is explicitly needed.
