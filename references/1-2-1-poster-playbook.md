# 1:2:1 Academic Poster Playbook

Use this reference after `SKILL.md` when a user wants a concrete poster plan, mockup, or production checklist.

## Public Guidance Synthesis

Open academic poster guidance is surprisingly consistent:

- Start with boxes on paper, then add content.
- Keep the story flowing left to right or top to bottom.
- Use only 2-3 colors, with strong contrast and no red/green pairing.
- Keep enough white space for readability, but academic posters can be information-rich: use roughly 20-30% empty space, 35-45% graphics/tables, and 25-35% text when the reference style is text-dense.
- Make the title the largest text, keep it short, and avoid competing logos in the title area.
- Keep the main text readable from about 1.5m away.
- Use short bullets, not paper paragraphs.
- Include enough explanatory text that each section carries scientific content rather than becoming a decorative label.
- Provide author/contact details, references, and a QR code for follow-up material.
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
| Abstract + contribution list | header/intro | claim, novelty, one-sentence value proposition |
| Introduction | left column | task definition, why it matters, bottleneck, 2-4 contributions |
| Method | center column | module names, mechanism explanation, design rationale, key equation/notation meaning |
| Experiments | right column | datasets, metrics, baselines, main numbers, what the numbers mean |
| Ablations/analysis | right column | why the method works, efficiency/robustness/failure interpretation |
| Limitations/conclusion | right/footer | caveat, deployment condition, or final takeaway |

For each destination, mark whether it has `definition`, `mechanism`, `evidence`, and `interpretation`. A poster can omit some labels, but it should not omit all interpretation.

## Correspondence Matrix

Build a short matrix before drafting text:

| Paper section | Poster zone | What changes |
| --- | --- | --- |
| Title/abstract | header + claim line | compress into one sentence |
| Introduction | left column | keep only the bottleneck and why it matters |
| Method | center column | enlarge the core mechanism, reduce implementation detail |
| Results | right column | keep strongest evidence, cut redundant rows/plots |
| Limitations | footer/callout | keep short and factual |

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

Default landscape structure:

```text
+-------------------------------------------------------------------+
| Logos | Title, authors, affiliations                       Venue   |
+------------------+--------------------------------+---------------+
| 1. Motivation    | 2. Method                      | 3. Experiments|
| narrow, light    | wide, visual, explanatory      | narrow, dense |
|                  |                                |               |
| observations     | hero pipeline / architecture   | tables/plots  |
| contribution     | module details / equations     | ablations     |
+------------------+--------------------------------+---------------+
| optional footer: project URL / QR / email / acknowledgements       |
+-------------------------------------------------------------------+
```

Width ratio: `1 : 2 : 1`. Use the center as the visual anchor; side columns should feel supportive, not equally important.

Typical vertical allocation:

| Region | Height Share | Purpose |
| --- | ---: | --- |
| Title band | 12-16% | identity, conference signal, authors, logos |
| Body | 76-84% | three-column story |
| Footer | 0-6% | email, QR, short URL, optional acknowledgement |

## Column Recipes

### Left Column: Motivation

Purpose: make the problem and bottleneck obvious in 15 seconds.

Good ingredients:

- A compact task/context paragraph or 3-5 bullets explaining why the task is hard.
- One small observation plot, schematic, or motivating example.
- A bold "preliminary observation" or "key bottleneck" callout.
- 3-4 contribution bullets when the paper has multiple contributions.
- One takeaway sentence that tells the viewer why the poster matters.
- Optional short related-work contrast if it clarifies the bottleneck.

Avoid:

- Long related-work paragraphs.
- Definitions the audience already knows.
- More than two figures.

### Center Column: Method

Purpose: explain the idea visually; this column justifies the `2` in `1:2:1`.

Good ingredients:

- One hero method figure spanning most of the center width.
- 3-5 module blocks below or beside the figure.
- Captions that describe actions and design rationale.
- One equation only if it clarifies selection, routing, loss, or objective, with a one-sentence meaning note.
- 120-180 words of explanatory text around the hero figure when the method is not obvious from the diagram alone.

Figure guidance:

- Use a single visual grammar: consistent arrows, tokens, colors, and labels.
- Label modules with names that match the paper.
- Crop aggressively; remove decorative whitespace and redundant legends.
- Prefer vector PDF/SVG for LaTeX and 300 DPI PNG for PPTX.
- Keep the hero visual clearly larger than any supporting panel.

### Right Column: Experiments

Purpose: prove the claim with compact evidence.

Good ingredients:

- One compact result table or plot at the top.
- Use tables only when the audience expects benchmark rows/columns; highlight them heavily.
- A short experimental setup note naming datasets, metrics, and baselines.
- Efficiency-versus-performance block.
- 1-2 small ablation or analysis plots.
- 2-4 result interpretation bullets and one boxed conclusion.
- Keep methods or limitations visible somewhere on the poster, even if they are compact.

Avoid:

- Full experimental setup paragraphs.
- Raw tables that require slow reading.
- Tables with too many rows/columns to understand at poster distance.
- Metrics not tied to the main claim.

## Content Budget

Default target: 650-950 body words, excluding table text and author affiliations. If matching a text-dense sample poster, allow 750-1100 words as long as the body remains readable from poster-session distance and no text clips.

| Area | Target Words | Visual Priority |
| --- | ---: | --- |
| Title/subtitle | 12-18 | title should be readable first |
| Motivation | 130-220 | context, bottleneck, contributions |
| Method | 240-360 | hero figure plus module explanations |
| Experiments | 200-320 | setup, results, ablations, interpretation |
| Footer/contact | 20-60 | QR/email/project/caveat |

Copy rules:

- Use a mix of compact paragraphs, bullets, and captions; do not make every section a one-line slogan.
- Use numbers where possible: `42% less FLOPs`, not "significantly more efficient".
- Use active labels: `Select cubes`, `Route salient tokens`, `Skip redundant FFNs`.
- Keep captions explanatory and source-backed; a key figure caption can be 20-45 words.
- Remove generic AI prose and vague intensifiers.
- Left-align body text; avoid full justification if it creates ugly gaps.
- If a section has fewer than 45 words or fewer than 3 meaningful bullets/caption sentences, check the paper again before final rendering.

## Visual System

Use a restrained academic design:

- Top band: logos left/right, centered title, authors below, affiliations in smaller type.
- Keep logos out of the title cluster when possible so the title stays dominant.
- Section cards: small radius, subtle shadow, strong header bar or left accent stripe.
- Color: one dark primary color for headers, one accent for highlights, neutral background.
- Rhythm: repeat card padding, title size, line weight, and caption style.
- Figures: align baselines and keep captions visually consistent.
- Tables: highlight only the rows/columns that support the claim.

For a CVPR-like example, use navy headers, white body cards, compact black text, and conference/organization logos in the title band.

## Production Flow

1. Draft `POSTER_121_PLAN.md`.
2. Produce 3+ color-direction previews and stop for user choice.
3. Build the text ledger and confirm text sufficiency for each column.
4. Confirm the figure list, corpus abstraction decisions, and missing placeholders.
5. Build a low-fidelity layout first: boxes, section titles, figure slots, table slots, and text blocks.
6. Insert figures, tables, and source-backed text before polishing layout.
7. Rewrite copy to fit the actual boxes without deleting essential definitions, mechanism explanations, or result interpretations.
8. Render to PDF/PNG and visually review.
9. Export final PDF, editable PPTX/SVG, and source files as requested.

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

## Canvas
- Size/orientation:
- Venue/theme:
- Column ratio: 1:2:1
- Header/footer needs:

## Color Direction
- Options generated:
- Selected scheme:
- Contrast/readability notes:

## Left: Motivation
- Purpose:
- Bullets:
- Paragraph/caption text:
- Visuals:

## Center: Method
- Hero figure:
- Module blocks:
- Explanation text:
- Equations/callouts:

## Right: Experiments
- Main table/plot:
- Supporting plots:
- Setup/result interpretation text:
- Takeaway:

## Risks
- Missing data:
- Overfull areas:
- Readability concerns:
```

## Review Rubric

Pass/fail checks:

- Can a viewer understand the contribution in 60 seconds?
- Is the center column clearly the hero?
- Are all numbers traceable to the source material?
- Is every figure readable at poster-session distance?
- Are tables compact, highlighted, and readable at poster distance?
- Does the title remain the strongest element in the header band?
- Are side columns supporting, not competing with, the method column?
- Are headers, gutters, baselines, and card edges aligned?
- Is there no clipped text, tiny caption, broken logo, or unexplained acronym?
- Does the poster avoid paper-like paragraphs?
- Does each major section contain enough source-backed text to explain its role?
- Does the poster include task definition, method rationale, experiment setup, result interpretation, and at least one caveat/takeaway?
- Can a viewer answer 3-5 core questions about the paper from the poster alone?

If any pass/fail check fails, revise the plan or layout before export.
