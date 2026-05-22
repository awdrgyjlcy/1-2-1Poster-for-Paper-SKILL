---
name: paper-poster-121
description: "Design and structure 1:2:1 academic conference posters with narrow side columns and a wide center column for method-heavy research stories. Use when the user asks for a 1:2:1 poster, betterposter, billboard-style poster, academic poster layout, conference poster layout, CVPR-style poster, or to analyze accessible paper-poster pairs and public poster corpora to turn a paper/outline/results into a three-zone poster plan and paper-to-poster correspondence map."
---

# Paper Poster 1:2:1

## Overview

Use this skill to turn a paper, abstract, method outline, or result dump into a 1:2:1 academic poster plan and production checklist. Treat `paper-poster` as the build/export skill; use this skill to decide the narrative, grid, content budget, figure hierarchy, and visual review standard.

## Evidence-Backed Defaults

- Treat the poster as a visual abstract, not a paper reprint.
- Aim for one main point, then support it with a few figures and short callouts.
- Keep the title short, clear, and the largest text on the page.
- Use 2-3 colors max and avoid red/green pairings.
- Treat colors as semantic roles, not isolated hex values: primary/header, secondary/module, accent/highlight, background, surface, text, and chart colors.
- Target roughly 30-40% whitespace, 40-50% graphics, and 20-25% text.
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
   top title band, left motivation column, center wide method column, right experiments column, small footer/contact strip.
3. Allocate content by role:
   left = why it matters, center = how it works, right = why it is convincing.
4. Select visuals before writing copy:
   one center hero diagram, one or two compact result tables/plots, and only small supporting observations on the sides.
5. Build the paper-to-poster correspondence matrix:
   map title/abstract, intro, method, results, and limitations into poster zones; decide what gets enlarged, compressed, reordered, or omitted before you write poster copy.
6. Run the color direction checkpoint:
   based on the paper topic, venue, domain, figures, and logos, propose at least 3 distinct visual color schemes; generate a separate palette preview image for each scheme; ask the user to choose one before any final drawing or rendering continues.
7. Run the corpus-grounded abstraction pass:
   apply the corpus-derived paper-to-poster compression rules and compare them against the correspondence matrix; when refreshing the skill or doing broad genre learning, search 1000+ accessible paper-poster pairs from official CS conference virtual sites; for a specific paper, optionally sample 20-50 topic-neighbor posters before copywriting.
8. Compress text into poster language:
   bullets, labels, callouts, numbers, and figure captions; avoid abstract-style paragraphs.
9. Produce a `POSTER_121_PLAN.md` before implementation:
   include title band, section map, figure list, word budget, color/type choices, and review risks.
10. Build in the user's target stack:
   use LaTeX/tcbposter for print PDF, HTML/CSS for fast visual iteration, or PPTX/SVG when editability matters.
11. Review visually:
   check 60-second comprehension, center-column dominance, readability from distance, alignment, no clipping, and no unsupported numbers.
12. Review semantically:
   ask 3-5 core questions about the paper and verify the poster lets a viewer answer them without reading the full paper.

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
   for each scheme, create a PNG/SVG/HTML-screenshot swatch board that shows color chips, semantic roles, a mini 1:2:1 poster mockup, section headers, callout boxes, a sample chart/table highlight, and sample body/caption text.
6. Present the previews together:
   save them under a clear folder such as `poster/color-options/` and summarize tradeoffs in `POSTER_121_COLOR_OPTIONS.md`.
7. Stop and ask the user to choose:
   do not continue to final poster drawing, LaTeX/HTML/PPTX production, or figure recoloring until the user explicitly selects a scheme or asks for revisions.

Palette preview requirements:

- Show the same miniature poster structure for every option so the choice is about color, not layout.
- Include hex codes and role names on each preview.
- Avoid relying on color alone to encode experimental meaning; pair color with labels, line styles, or symbols.
- Respect venue or institution brand colors when logos require them, but do not let brand colors overwhelm paper readability.

## Corpus-Grounded Abstraction Pass

When the topic is in computer science or a nearby technical field, ground the poster plan in a searchable paper-poster corpus before final copywriting.

1. For normal poster generation, read `references/poster-corpus-abstraction.md` first and apply its reduction rules.
2. If the paper topic is niche or the user asks for a fresh corpus refresh, search only accessible paper/poster pairs from official conference virtual sites, proceedings pages, or equivalent public conference pages.
3. Prefer CS venues with paired paper and poster artifacts such as NeurIPS, CVPR, ICLR, ICML, ACL, ECCV, and ICCV.
4. Use a large sample when updating the skill, ideally 1000+ accessible pairs; for one target poster, a focused 20-50 topic-neighbor sample is usually enough.
5. For topic-neighbor sampling, query with the paper's task, method noun, evidence type, and domain keywords; avoid generic terms such as only `deep learning` or `large model`.
6. Extract how posters compress the source paper:
   title becomes the claim, abstract becomes a value proposition, intro becomes 2-3 motivation bullets, method becomes one hero figure plus module labels, results become one compact table or plot plus 1-2 support visuals, and limitations become a short caution or takeaway.
7. Save the synthesis in `references/poster-corpus-abstraction.md` and reuse it to cut material, not just to style it.
8. Do not use inaccessible, unpaired, or non-paper poster examples.
9. Do not let the corpus override the paper's actual claims or venue constraints.

## Layout Defaults

- Use a 1:2:1 width ratio for body columns. For landscape posters, this usually means side columns around 22-25% each and the center around 46-52%.
- Make the center column visually dominant: large architecture/method figure on top, then 2-3 concise module explanations underneath.
- Keep the left column lighter: motivation, bottleneck, preliminary observation, or contribution bullets.
- Keep the right column evidence-heavy: compact result table or plot, efficiency/performance comparison, ablation/analysis plots, and one compact takeaway.
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

Useful corpus commands:

```bash
python scripts/collect_poster_corpus.py --output references/poster-corpus-scan.json
python scripts/collect_poster_corpus.py --include-links --output references/poster-corpus-index.json
python scripts/collect_poster_corpus.py --query "<task method domain evidence>" --top-k 30 --output references/topic-neighbor-sample.json
```

## Guardrails

- Do not fabricate claims, metrics, affiliations, logos, or citations.
- Do not dump paper prose into the poster; rewrite into short bullets and callouts.
- Do not let equal-width grids override the 1:2:1 story. The center column must earn its width.
- Do not build a wall-of-text IMRAD poster unless the venue explicitly requires it.
- Do not start final rendering until the claim, column roles, and figure list are explicit.
- Ask at most one clarifying question only when the missing information would otherwise force fabricated results or branding.
- Do not rerun corpus collection for ordinary poster drafting; use the learned abstraction note unless a refresh is explicitly needed.
