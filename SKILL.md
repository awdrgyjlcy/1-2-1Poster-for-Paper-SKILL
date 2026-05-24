---
name: paper-poster-121
description: "Design and structure body-only 1:2:1 academic conference posters with three separated rounded rectangles: narrow left card, wide center card, narrow right card. Use when the user asks for a 1:2:1 poster, betterposter, academic poster layout, CVPR-style poster, or to turn a paper/outline/results into a three-card poster plan, a paper-to-poster correspondence map, strict fixed headers (1、Motivation, 2、Method, 3、Experiment), a strict width ratio where center = 2x either side card, sample-like text/visual density, macro-block narrative layout, balanced content heights, fixed motivation/method/experiment card recipes, right-card experiment overflow detection with proportional visual/table shrinking, global +4 to +8 pt font scaling plus proportional in-card font-fit scaling until obvious blank space disappears, narrow sample-like gutters, or a tighter vertical-fill layout that removes lower-half blank pockets inside cards without fragmenting the poster."
---

# Paper Poster 1:2:1

## Overview

Use this skill to turn a paper, abstract, method outline, or result dump into a 1:2:1 academic poster plan and production checklist. Treat `paper-poster` as the build/export skill; use this skill to decide the narrative, grid, content budget, figure hierarchy, and visual review standard.

## Evidence-Backed Defaults

- Treat the poster as a visual abstract, not a paper reprint, but do not make it text-starved.
- Aim for one main point, then support it with figures plus enough source-backed explanatory text for each major section.
- Match the provided reference image's body footprint exactly: measure the union of the three rounded rectangles plus about 3% outer whitespace on each edge. Do not use the full raster, title band, or footer as the sizing reference.
- Default to a body-only three-card composition: no separate top title band, subtitle/author band, metric strip, footer, or full-width bottom bar unless the user explicitly requests them.
- If a paper title/claim is needed, place it compactly inside one of the three cards; do not create a standalone title region.
- Fix the three main card header titles exactly as `1、Motivation`, `2、Method`, and `3、Experiment`. Do not replace them with paper-specific titles such as "Why...", "Certified...", or "Evidence..."; any paper-specific claim must move into the body area below the header.
- Use sample-like narrow gutters: the two gaps between cards should be small and close to the outer breathing margin around the three-card cluster. Default gutter is about 1.5-2.2% of the body-footprint width; hard upper limit 2.5% unless the user asks for more air.
- Fill the vertical canvas with the three cards; avoid large unused bottom whitespace or short cards floating in the upper area.
- Inside each card, distribute content vertically from top to bottom; do not let the lower half of a card stay mostly empty after the main figure or opening bullets.
- Lock the card recipes by default: left motivation card = pure vertical stack of text plus 1-2 figures; center method card = measured upper 1/2 pipeline figure plus measured lower 1/2 three equal unnumbered method subcards; right experiment card = vertical sequence of titled result blocks with near-full-width figures/tables and 1-2 sentence explanations.
- Treat right-card bottom overflow as a hard failure: no experiment title, sentence, plot, table, caption, or result block may cross or clip beyond the `3、Experiment` rounded rectangle. If overflow appears after render inspection, proportionally shrink the right-card experiment figures/tables as a group or per result block until all content fits inside the card.
- Treat the center method card as a hard measured half-split: after subtracting the center-card header and padding, the upper region is exactly 50% of usable height for the main method/pipeline figure, and the lower region is exactly 50% for three horizontal unnumbered method subcards. Approximate 45-55% splits fail unless the user explicitly overrides the sample rule.
- Treat content filling as part of the layout, not decoration: when a required region is short, first add or restore source-backed paper content, then enlarge font size, line height, label size, table font/cell scale, diagram line weight, plot labels, or figure crop until the assigned region is visibly occupied. If visible blank space remains, proportionally scale the typography inside that card or subcard until the blank pocket is no longer obvious. Never invent content, and do not leave small text or narrow tables floating inside large boxes.
- Use the original/reference style as the target: a few large, coherent narrative blocks with strong section headers, paragraphs/bullets, compact figures, and bottom takeaways. Do not turn the poster into a ledger of tiny strips.
- A bottom anchor alone does not fix an underfilled card; extend the existing narrative downward with source-backed explanation, interpretation, captions, or a coherent bottom block so the lower half reads as occupied. For the center card, that anchor must be embedded inside the three method subcards rather than added as a fourth section.
- Balance the visible content height across all three rounded cards: the left, center, and right content stacks should start and end at similar vertical positions, with no side card looking half-empty next to the center.
- Tinted panels, empty color fills, or oversized pale boxes do not count as content. Count only readable text, diagrams, plots, tables, captions, labels, and meaningful callouts.
- Match the reference's text/visual density: keep figures compact and explanatory, keep body text visibly substantial, and never enlarge weak figures just to occupy space.
- Use 2-3 colors max and avoid red/green pairings.
- Treat colors as semantic roles, not isolated hex values: primary/header, secondary/module, accent/highlight, background, surface, text, and chart colors.
- Include the built-in `Reference CVPR Blue` palette from the user's sample poster as a selectable default. If the user explicitly chooses this palette, use it directly; if no palette is chosen, include it as the first option in the color-choice checkpoint and ask the user to select.
- Target an information-rich academic balance: roughly 20-30% whitespace, 35-45% graphics/tables, and 25-35% text.
- Make the main body readable from about 1.5m away. If the first render resembles the user's sparse/small-text example, increase the entire poster typography scale by 4-8 pt, with +6 pt as the default correction; if the left card or center subcards still contain obvious lower blank space, continue proportional in-region font scaling beyond that starting correction until the blank space disappears.
- Prefer left-aligned text, clear section flow, visible contact details, and a QR code.

## Skill Group

- Primary group: `paper-poster` / research communication.
- Supporting skills: use `paper-figure` for plot selection, `paper-illustration` for method diagrams, and `design-system` or `ckm:design` only when brand/color systems are needed.
- Prefer this skill over generic design skills when the deliverable is a research poster with title/authors, method figure, experiments, and conference branding.

## Quick Workflow

1. Distill the story into one claim:
   `problem -> key idea -> evidence -> takeaway`.
2. Lock the 1:2:1 canvas:
   use the sample-matched body footprint as the reference box, defined by the three rounded rectangles plus about 3% outer whitespace; then place exactly three side-by-side rounded rectangles with visible gaps; left motivation card, center wide method card, right experiments/evidence card; card width ratio must be `1:2:1`.
   Compute this ratio only from the three card rectangles: `left_width = right_width = u`, `center_width = 2u`. Exclude outer whitespace, card padding, borders, shadows, and inter-card gutters from the ratio.
   Set the two inter-card gutters narrowly, approximately equal to the outer breathing margin around the cluster and normally 1.5-2.2% of the body-footprint width.
3. Allocate content by role:
   left = why it matters, center = how it works, right = why it is convincing.
4. Select visuals before writing copy:
   one center hero method pipeline, one or two motivation visuals, and a vertical stack of main experimental result visuals. A visual earns space only if it directly explains the claim, mechanism, or evidence.
5. Build a vertical packing map for each card:
   top intro, middle core visual or argument, lower explanation/evidence, bottom anchor; no card should end immediately after its main figure.
   For the center card, replace the generic packing map with the exact two-zone map: upper 1/2 pipeline and lower 1/2 three unnumbered method subcards. Do not place a visible lower-half heading above those subcards.
   Keep the map macro-block based: usually 2-4 broad sections in a side card and 3-5 broad sections in the center card. If the lower half still looks empty, expand or move an existing source-backed section downward before adding any new box.
6. Build the paper-to-poster correspondence matrix:
   map title/abstract, intro, method, results, and limitations into poster zones; decide what gets enlarged, compressed, reordered, or omitted before you write poster copy.
7. Run the text sufficiency checkpoint:
   extract enough important source-backed text from the paper for every poster zone; set a word budget and section-level text floor before layout rendering.
8. Run the visual density checkpoint:
   set a sample-like image/text budget before rendering. Reject layouts where a large plot, table, or screenshot is used as filler, where text becomes tiny, or where information is scattered into many weak micro-boxes.
9. Run the vertical fill checkpoint:
   set card height, internal section stacking, and content density so the three cards use the available poster height without leaving a large bottom blank region.
   Treat a card as underfilled if the lower-middle zone is blank or if the lower half contains only a tiny bottom note, but fix it by extending coherent content rather than creating ledger rows. In the center card, fix underfill only by enriching and scaling the three method subcards, not by adding extra rows or a group heading.
10. Run the card content balance checkpoint:
   compare the visible content top, bottom, and span of the three cards. The final meaningful content in all cards should end within about 3-4% of card height of each other, and each content stack should span about 85-95% of the usable card height.
11. Run the fixed card recipe checkpoint:
   verify that the motivation card is a pure vertical text-plus-figure stack with no empty lower half, the method card is a measured exact upper 1/2 pipeline plus lower 1/2 three unnumbered method subcards with no lower-half group heading, and the experiment card is a vertical sequence of titled result blocks whose first table and later figures/tables span most of the card width.
12. Run the right-card overflow checkpoint:
   after rendering, inspect the `3、Experiment` card bottom edge. If any experiment block crosses, clips, or visually touches past the rounded rectangle, do not move the card border or shrink all text first; reduce the right-card figures/tables proportionally by 5-10% passes, preserving 90-100% width where possible, until all blocks fit inside the card.
13. Run the title and typography checkpoint:
   the three card headers must read exactly `1、Motivation`, `2、Method`, and `3、Experiment`; all font classes should be 4-8 pt larger than the too-small baseline unless the user supplies a different target. Then run a proportional font-fit loop: if the left card body or the center lower-half subcards still show visible lower blank space, scale the typography inside the affected card/subcards together in 5-10% increments until no obvious blank pocket remains.
14. Run the color direction checkpoint:
   if the user explicitly chose `Reference CVPR Blue`, use it directly and continue; otherwise, based on the paper topic, venue, domain, figures, and logos, propose at least 3 distinct visual color schemes with `Reference CVPR Blue` as the first built-in option; generate a separate palette preview image for each scheme; ask the user to choose one before any final drawing or rendering continues.
15. Run the corpus-grounded abstraction pass:
   apply the corpus-derived paper-to-poster compression rules and compare them against the correspondence matrix; when refreshing the skill or doing broad genre learning, search 1000+ accessible paper-poster pairs from official CS conference virtual sites; for a specific paper, optionally sample 20-50 topic-neighbor posters before copywriting.
16. Rewrite text into poster language:
   compact paragraphs, bullets, labels, callouts, numbers, and figure captions; preserve key definitions, mechanism explanations, result interpretation, and caveats.
17. Produce a `POSTER_121_PLAN.md` before implementation:
   include card map, text ledger, figure list, figure-size budget, right-card overflow repair plan, word budget, color/type choices, card geometry, gutter sizes, fixed recipe conformance, vertical fill plan, content-height balance plan, and review risks.
18. Build in the user's target stack:
   use LaTeX/tcbposter for print PDF, HTML/CSS for fast visual iteration, or PPTX/SVG when editability matters.
19. Run visual budget, content balance, right-card overflow, and vertical fill audits on the rendered artifact if available:
   verify that text is not visually dominated by oversized low-information figures, that each figure has nearby caption/interpretation text, and that information blocks are grouped rather than scattered.
   use `scripts/audit_vertical_fill.py` or equivalent to verify each card has lower-half content, no right-card content crosses the bottom border, the bottom blank fraction stays under threshold, and the three content stacks have similar bottom and span ratios before final delivery.
20. Review visually:
   check 60-second comprehension, center-column dominance, readability from distance, alignment, no clipping, no unsupported numbers, no right-card bottom overflow, no excessive bottom blank space, and no card whose content ends visibly higher than the others.
21. Review semantically:
   ask 3-5 core questions about the paper and verify the poster lets a viewer answer them without reading the full paper.

## Text Sufficiency Checkpoint

Before final layout rendering, build a source-backed text ledger and prevent underfilled sections.

1. Extract a text bank from the paper:
   problem context, task definition, bottleneck, contribution list, method modules, objective/equation meaning, datasets, metrics, baselines, headline numbers, ablation interpretation, limitations, and final takeaway.
2. Map the text bank to poster zones:
   left = motivation, task setup, bottleneck, and contributions; center = method mechanism, module explanations, notation/equation meaning, and design rationale; right = experimental setup, main results, ablations, efficiency/robustness, limitations, and takeaway.
3. Set an information-rich word budget:
   default sample-matched body-footprint target is 900-1300 body words excluding author affiliations and table cell text; for a text-dense reference poster, allow 1100-1500 words if readability survives.
4. Use section-level text floors:
   left card 240-360 words, center card 420-620 words, right card 320-480 words, optional in-card contact/caveat note 20-60 words. Every major body section should have at least 80 words or at least 5 meaningful bullets/caption sentences unless it is purely a figure/table label.
5. Preserve scientific payload:
   keep enough text for a viewer to answer what the problem is, what is new, how it works, what evidence supports it, and when it may fail.
6. Rewrite, do not paste:
   use compact academic prose, bullets, and captions; avoid copying full paper paragraphs, but also avoid reducing a section to icons, one-line slogans, or empty callouts.
7. If the first mockup looks sparse:
   return to the source paper and add missing definitions, module explanations, experimental setup details, result interpretations, or caveats before changing decoration.
8. If a card still looks vertically sparse:
   extend one of the existing macro sections with a source-backed paragraph, caption, result interpretation, caveat, or compact table. Add a new lower-third block only if it is a coherent section, not a tiny filler label.

## Macro-Block Layout Checkpoint

Before rendering, make the layout resemble the stronger first-version/reference style: three large cards containing a small number of strong academic sections.

1. Use macro sections, not ledger rows:
   a card should read as a few named narrative regions such as `Problem`, `Key Observation`, `Method Pipeline`, `Module Rationale`, `Main Evidence`, or `Takeaway`. These regions may contain paragraphs, bullets, captions, and small visuals together; they do not need separate boxes.
2. Keep section count low:
   side cards usually need 2-4 macro sections; the center card usually needs 3-5. If more sections appear necessary, merge related facts under a stronger heading before drawing.
3. Preserve the first-version feel:
   prefer broad headers, compact explanatory paragraphs, and grouped bullets over many pale cards, badges, chips, metric strips, or form-like rows.
4. Fix blank space by deepening content:
   when a card has lower blank space, first enlarge the existing section's text/caption area, move a relevant explanation downward, add interpretation to a nearby figure, or create one coherent bottom takeaway. Do not solve blank space by scattering many tiny boxes.
5. Keep figures in service of text:
   one method diagram can be large, but ordinary plots should stay compact and paired with interpretation. A figure that is enlarged only to occupy a macro section should be shrunk or replaced with explanation.
6. Run a scatter review:
   if the viewer's eye has to jump between many disconnected fragments, merge them into fewer macro sections before final export.

## Visual Density Checkpoint

Before final layout rendering, match the reference poster's image/text relationship and prevent oversized filler graphics.

1. Use a sample-like area budget:
   target roughly 30-40% text, 35-45% figures/tables, and 15-25% intentional whitespace within the three-card body footprint. Do not let figures exceed half of the footprint unless the center method diagram is genuinely the paper's main contribution.
2. Cap individual visual size:
   the center method hero may be the largest visual, but result plots, bar charts, scatter plots, screenshots, and diagnostic panels should stay compact. A single non-method plot should not occupy more than about one third of its card height.
3. Ban filler enlargement:
   a figure cannot be enlarged merely to fill blank space. If the figure has sparse marks, redundant axes, low interpretive value, or no direct claim support, shrink it, combine it with a caption, convert it to a mini-table, or replace it with source-backed explanation.
4. Pair every visual with interpretation:
   each figure/table must have a nearby caption, label, or 2-4 bullets explaining what to notice and why it supports the claim. Uncaptioned large visuals fail.
5. Group information into coherent blocks:
   each card should have a small number of named macro sections with a clear reading path. Avoid many isolated micro-boxes, distant labels, ledger strips, or weak boxes that scatter one idea across the card.
6. Preserve readable text scale:
   if text has to become tiny to fit many scattered blocks, merge blocks and rewrite. Do not solve crowding by shrinking body text while enlarging figures.
7. Prefer dense academic panels over decorative scale:
   use compact diagrams, cropped plots, highlighted tables, and explanatory callouts. Oversized low-information charts are worse than smaller charts plus interpretation text.

## Card Content Balance Checkpoint

Before final rendering, balance the actual content height across the three rounded rectangles. This is a hard visual requirement for matching the reference sample.

1. Measure real content, not colored area:
   content means readable text, equations, labels, plots, tables, diagrams, captions, and meaningful callouts. Empty tinted rectangles, section backgrounds, borders, and large pale panels count as whitespace.
2. Align content stacks:
   after the in-card header, each card's first real body content should begin at a similar y-position, and each card's final meaningful content should reach the lower 5-8% of the usable card area.
3. Match the three content bottoms:
   the final meaningful content in left, center, and right cards should end within about 3-4% of card height of each other. If one card stops much higher, it fails even if the card frame itself is full height.
4. Match the content spans:
   each card's real content stack should span about 85-95% of usable card height, and the three spans should differ by no more than about 8%. A side card that only uses the top half must be regenerated.
5. Use density knobs in this order:
   add source-backed text/captions/interpretation, then enlarge typography, line height, figure labels, table type, and diagram geometry inside the assigned region; after that crop figure whitespace and rebalance section heights. Do not add decorative panels.
6. Adjust typography deliberately:
   if content is short, increase body font, line height, bullet spacing, caption size, table font, or diagram labels until the region is visibly filled within readability and professional limits. For this skill's current baseline, raise every text class by 4-8 pt first, then run proportional in-card font fitting. Scale the affected card's internal text system by 1.05-1.10x per pass until trailing blank space is not visually obvious. If the right experiment card overflows below its border, proportionally shrink only the right-card figures/tables first, then crop figure whitespace and reduce decorative padding before changing body text. For other overflows, crop figure whitespace, reduce decorative padding, or merge redundant bullets before shrinking fonts. Keep body text visually similar across the three cards.
7. Keep the sample-like feel:
   the result should look like three equally worked academic cards. The center remains wider and more important, but the side cards must not look abandoned or half-filled.

## Fixed Card Recipe Checkpoint

Use these card recipes unless the user explicitly asks for a different poster structure.

1. Motivation card:
   make the left card a pure vertical stack. Use text blocks and 1-2 motivation figures only, ordered from top to bottom. Do not use multi-column subgrids, horizontal metric strips, or side-by-side mini-panels inside the motivation card. The final real content must reach the lower 5-8% of the usable card area, and the lower half must contain substantive text/caption/figure content rather than a small note over blank space.
2. Motivation content order:
   use a compact problem/context paragraph, 2-4 bottleneck or contribution bullets, 1-2 full-card-width or near-full-card-width figures, and one preliminary-observation/takeaway paragraph. Figures should support the motivation, not replace the text. If the lower half is empty, first recover a source-backed example, bottleneck detail, preliminary observation, or contribution nuance, then enlarge font size, line height, captions, and figure crop to fill the vertical space.
   The left card fails if its lower half is filled by pale background but not by readable text/figure marks. After source-backed content is selected, enlarge the left-card body/bullets/captions by 4-8 pt as a starting correction, then proportionally scale all left-card internal text, line height, bullet spacing, caption text, and callout text together until the lower-half blank pocket is no longer obvious. Do not stop just because the first +4-8 pt increase was applied.
3. Method card:
   split the usable center-card area below the header into exactly two equal-height regions. The upper 1/2 is only the main method pipeline/architecture figure plus minimal labels/caption. If the paper contains a suitable architecture/pipeline figure, use and simplify that figure; only draw a new pipeline when the paper has no usable method figure. Use fixed-height boxes or explicit grid rows rather than auto-flow content sizing; measured split error should stay within about 1% of center-card usable height.
4. Pipeline fill:
   the pipeline figure must fill the upper 1/2 region both horizontally and vertically. Target 90-100% of the upper-region width and 85-100% of its height with real diagram marks, labels, or caption text. If it appears too small, crop internal whitespace, enlarge labels and module boxes, increase line weight, enlarge figure-caption type, or scale/redraw the paper-faithful figure before adding any other content.
5. Method three-subcard row:
   the lower 1/2 of the center card must contain exactly three method subcards arranged horizontally as equal-width columns. These three columns should fill the full lower-half height and width. Do not add a visible group heading above them such as `Three balanced method subpoints`, `Lower half`, `Three subpoints`, or any similar label. Do not add `claim`, `validity`, result plots, side notes, or extra bottom anchors outside the three subcards in the method card.
6. Method subcard equality:
   the three method subcards must use the same title style, body font, line height, bullet style, and comparable content amount. Each subcard title must be an unnumbered semantic mini-title only, such as `Certify locally`, `Inject equally`, or `Judge by ranking`; do not prefix titles with `1.`, `2.`, `3.`, letters, bullets, badges, or step numbers. Target similar word counts and line counts; no subcard should look visibly longer, shorter, larger, or more important than the others unless the user requests emphasis.
7. Method fill priority:
   if the lower 1/2 looks sparse, first search the paper for relevant mechanism details, design rationale, notation meaning, or module behavior for the three existing subcards; then enlarge body font, title font, line height, caption text, and bullet spacing within those subcards. For the current failure mode, increase all three subcards by 4-8 pt as a starting correction, then scale all three subcards together by the same multiplier in 5-10% increments until each subcard's real text occupies most of its height and no obvious lower blank area remains. Do not invent a fourth idea and do not leave small text floating at the top of a large pale subcard.
8. Experiment card:
   make the right card a vertical sequence of main experimental result blocks. Each block should have a clear title, a 1-2 sentence source-backed explanation, and a figure/table that spans most of the card's inner width.
9. Experiment visual width:
   every experiment visual, including the first headline result table, should normally occupy 90-100% of the card inner width. The first table/plot is a hard width gate: set it to full card width with responsive table width, grouped supporting numbers, or a composed multi-block panel before accepting the render. Avoid narrow charts or small tables floating in the middle; if several small plots belong together, group them into one full-width row or panel with a shared title and caption.
10. Experiment table composition:
   when a table is the chosen experiment visual, prefer composing related metrics, subresults, or diagnostic rows into one wider table/panel with aligned columns, merged headers, or stacked subrows so the table fills the width without forcing a large font jump. The table's text should stay visually close to the nearby explanation text; use cell padding, row height, header grouping, and panel composition to fill width before increasing the table font. If the table text must differ, keep the gap small enough that it still reads as part of the same typographic system.
11. Right-card overflow repair:
   after rendering, detect any experiment content whose bottom y-coordinate passes the right-card inner bottom padding or crosses/clips beyond the rounded rectangle. Repair by scaling down right-card visuals/tables, not by moving the card border, adding outside footer space, or shrinking the entire poster. Use 5-10% proportional shrink passes on the experiment figures/tables as a group first; if only one result block causes the overflow, shrink that block's visual/table and its internal crop proportionally. Keep captions readable and preserve near-full-width layout where possible. If overflow remains after visual shrink, tighten vertical gaps and caption line height slightly, then trim redundant source-backed explanation sentences only as a last resort.
12. Recipe failure:
   reject any render where the left card has a large empty lower half, the center card is not a measured exact 1/2 pipeline + 1/2 three-subcard split, the center lower half contains a group heading or extra sections outside the three subcards, the subcard titles are numbered, the right card contains a narrow headline table/figure, or any experiment content crosses the right-card bottom border.

## Font Scaling And Fill Priority

Use typography as an active layout tool after source-backed content is selected.

0. Apply the global correction first:
   increase the whole poster's typography scale by 4-8 pt relative to the too-small baseline, with +6 pt as the default. Apply this to card header titles, section headings, body text, bullets, captions, table text, plot labels, and diagram labels. Do not selectively enlarge only titles while leaving body/caption text tiny.
0.5. Apply proportional in-card font fitting when blank space remains:
   after the global correction, inspect the left card and the three center method subcards. If any target region still has an obvious lower blank pocket, scale that region's typography proportionally by 1.05-1.10x per pass, including titles, body text, bullets, captions, callouts, line height, and bullet spacing. For the center method subcards, scale all three subcards together with the same multiplier to preserve equality. Repeat until the trailing blank space is no longer visually obvious or the text is close to clipping; if clipping starts, reduce only the last multiplier slightly.
1. If a required area is sparse, first recover missing paper content:
   definitions, motivation evidence, module mechanism, design rationale, notation meaning, experimental setup, or result interpretation.
2. If the source-backed content is still short, enlarge presentation:
   increase body font size, line height, bullet spacing, figure label size, table font size, table cell padding, plot label size, caption size, and diagram line weight until the required region is visibly occupied.
3. Preserve consistency:
   scale related elements together so one card does not use tiny text while another uses large text. Method subcard typography must remain matched across all three subcards.
4. Do not fabricate:
   never add unsupported claims, fake mechanisms, invented metrics, or decorative filler to occupy space.
5. Do not accept tiny text in empty boxes:
   if a box is large and text is small, enlarge the text and line spacing before declaring the layout done.
6. Do not accept natural-size figures/tables when the layout requires fill:
   fixed card regions should control content scale. Use `width=100%`, `\linewidth`, `tabularx`, `resizebox`, SVG viewBox crops, or equivalent renderer controls so pipeline figures and headline experiment tables fill their assigned areas.
7. Treat left-card and center-subpoint blank space as a font-scale failure:
   if the left card lower half or any of the three center subcards has more than about 5-8% trailing internal blank space, increase text size, line height, and bullet spacing proportionally before changing the layout. Pale subcard backgrounds do not count as filled content.

## Color Direction Checkpoint

Before final layout rendering, create a color-choice checkpoint and stop for user selection.

1. Check for an explicit palette choice:
   if the user says to use the sample/reference/CVPR blue palette, select the built-in `Reference CVPR Blue` scheme and do not ask for color selection. Continue to final drawing with that palette.
2. Use the built-in sample palette as an option:
   if the user has not selected a palette, include `Reference CVPR Blue` as the first option in the color previews.
3. Infer visual directions from the paper:
   domain metaphors, target venue, topic mood, method keywords, existing logos, and figure colors.
4. Generate at least 3 named schemes:
   each scheme must include primary/header, secondary/module, accent/highlight, background, surface/card, body text, muted text, grid/border, and chart/table highlight colors. Count `Reference CVPR Blue` as one of the options when it is shown.
5. Keep schemes meaningfully different:
   for example `Conference Navy`, `Scientific Teal`, `High-Contrast Graphite`, `Warm Data`, or a domain-specific option such as `Medical Green` or `Robotics Amber`.
6. Check contrast before showing:
   body text on surfaces should target WCAG AA contrast; large poster titles and header text must remain legible from distance.
7. Generate visual preview images:
   for each scheme, create a PNG/SVG/HTML-screenshot swatch board that shows color chips, semantic roles, a mini three-rounded-card 1:2:1 poster mockup, section headers, callout boxes, a sample chart/table highlight, and sample body/caption text.
8. Present the previews together:
   save them under a clear folder such as `poster/color-options/` and summarize tradeoffs in `POSTER_121_COLOR_OPTIONS.md`.
9. Stop and ask the user to choose:
   do not continue to final poster drawing, LaTeX/HTML/PPTX production, or figure recoloring until the user explicitly selects a scheme or asks for revisions.

Built-in palette: `Reference CVPR Blue`

Use this palette to match the user's sample poster. It is a clean CVPR-style academic scheme with white cards, deep blue headers, blue-gray supporting modules, restrained orange highlights, and high-contrast dark text.

| Role | Hex / value | Use |
| --- | --- | --- |
| background | `#F7F9FC` | page outside the three cards |
| card surface | `#FFFFFF` | main rounded rectangles |
| primary/header | `#2F5D99` | card header bars and main section labels |
| header text | `#FFFFFF` | text on blue headers |
| body text | `#111827` | main readable text |
| muted text | `#374151` | captions, affiliations, secondary notes |
| border/grid | `#D8E2EE` | card borders, table rules, plot gridlines |
| soft panel | `#EEF4FA` | subtle module backgrounds only when they contain content |
| secondary/module | `#AFC4DE` | method blocks, table highlights, module fills |
| cool highlight | `#8FD3D6` | selected tokens, light method accents, heatmap low/mid color |
| accent/highlight | `#F26A21` | key arrows, best results, caution/takeaway outlines |
| shadow | `rgba(17, 24, 39, 0.18)` | restrained card shadow |
| chart colors | `#2F5D99`, `#8FD3D6`, `#AFC4DE`, `#F26A21`, `#7C8DA6` | plots/tables |

Rules for `Reference CVPR Blue`:

- Use blue header bars on all three cards with white section titles.
- Keep card surfaces white, not tinted, so figures and text stay crisp.
- Use orange sparingly for one emphasis channel only: key arrows, best result strokes, or bottom caution boxes.
- Use blue-gray and teal for method modules and grouped chart categories.
- Do not let logos or venue colors override the palette unless the user explicitly asks for institutional branding.

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
   target 85-95% internal content occupancy after padding. Empty space inside a card should be distributed as intentional breathing room between sections, not concentrated as one large blank area at the bottom or as a big blank pocket in the lower half.
   The lower half of every card should contain substantive source-backed content; it may be part of a larger macro section and should not require extra boxed fragments.
   Content occupancy means real text/visual marks, not merely a tinted background region.
4. Use explicit internal grids:
   left and right cards use top, upper-middle, lower-middle, and bottom-anchor zones. The center card instead uses the exact two-zone grid: upper 1/2 pipeline and lower 1/2 three unnumbered subcards. Equal-height card frames alone do not pass if the lower half is visually empty.
   The lower-middle zone must contain real explanation, comparison, or evidence, not a decorative caption. In the center card, this content must live inside the three method subcards rather than in an extra section or visible group heading.
5. If bottom blank space appears:
   first expand or move content downward within the card, then add source-backed captions or interpretation bullets, rebalance section heights, or add one coherent bottom takeaway. Do not solve it by adding an external footer band or a stack of small boxes.
   If the lower half has one large blank pocket, extend an existing macro section through that space or move a relevant explanation into it before creating new visual containers.
6. Use bottom anchors without breaking the fixed recipes:
   left and right cards should have a meaningful lower anchor such as a takeaway, caveat, mini table, compact citation/contact note, or small diagnostic figure placed inside the card. In the center card, the lower anchor must be embedded as the closing line/caption inside the three method subcards, not added as a fourth method-card section.
7. Render-check the result:
   after exporting PDF/PNG/SVG, inspect the full page. If the empty area below the three cards or at the bottom of any card exceeds about 5-6% of card height, revise layout before final delivery.
   Also reject cards whose lower half is mostly blank even if the final line reaches the bottom edge. Reject any right-card experiment content that crosses or clips beyond the bottom card border; repair this by proportionally shrinking right-card figures/tables until the content fits.
8. Audit as a hard gate:
   if a rendered image exists, run `scripts/audit_vertical_fill.py` or an equivalent check. If any card lacks lower-half content, fails the blank-space threshold, or has content height far out of balance with the other cards, regenerate/rebalance the layout before delivery.

## Lower-Half Anti-Blank Rule

- Treat a card as underfilled if the lower-middle zone is empty, even when a tiny bottom note exists.
- Require substantive lower-half content in each card, but do not require it to be multiple boxed blocks.
- Make the lower-middle content explain, compare, or interpret; make the bottom anchor conclude, caution, or summarize.
- If a blank pocket remains between upper content and the bottom anchor, move or extend one real macro section downward before changing margins, adding decorations, or creating extra boxes.
- For the center card, lower-half anti-blank means the three unnumbered method subcards themselves fill the lower 1/2; do not repair it by adding a fourth box, result strip, standalone bottom note, or group heading above the subcards.

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
- Use the reference-image body footprint as the hard default: the target box is the three-card cluster plus about 3% outer whitespace on each edge. Valid output can live inside a larger wrapper, but title/header/footer zones are outside the measured footprint.
- Use a strict 1:2:1 width ratio for the three cards. For landscape posters, allocate available inner width as `left:gutter:center:gutter:right`, with the card widths in `1:2:1` and gutters excluded from the ratio.
- Enforce the card-width formula: if each side card has width `u`, the center card must have width `2u`; left and right must match each other. Only renderer rounding is acceptable.
- Do not substitute A0/A1 or any venue-template aspect ratio if it conflicts with the sample-matched body footprint, unless the user explicitly asks to follow that venue format.
- Put clear but narrow whitespace between cards: use gutters around 1.5-2.2% of the body-footprint width each, approximately matching the outer breathing margin around the three-card cluster. The hard upper limit is 2.5% unless the user asks for more separation. The three cards should not touch.
- Make all three cards aligned to the same top and bottom edges, with consistent rounded corners. Use a modest radius (roughly 12-24 px for screen previews, or visually equivalent in print units).
- The three cards should fill the usable vertical body. Avoid layouts where the cards or their content stop early and leave a large empty strip at the bottom, or where a card has a broad blank pocket in its lower half.
- The real content stacks inside the three cards should be vertically balanced. The left and right cards must not have visibly shorter filled content than the center card.
- The center card should be the vertically densest card, but its density must come from the fixed two-zone method layout: exact upper 1/2 pipeline and exact lower 1/2 three unnumbered subcards.
- Put any required title, authors, QR, references, or caveats inside the three cards only when necessary; never create a separate outside band unless the user asks for a conventional conference poster.
- Make the center card visually dominant: large architecture/method figure on top or center, then concise module explanations underneath or beside it.
- The center method figure must be a pipeline/architecture visual occupying the exact upper 1/2 of the usable center-card body. Use the paper's figure when present; otherwise draw a simplified pipeline with paper-faithful module names. If the figure is too small, enlarge labels/modules/crop/line weight to fill the upper half.
- The center lower 1/2 must be exactly three horizontally arranged, equal-width method subcards with matched typography and content amount. No lower-half title line, group heading, or extra method-card sections are allowed below, above, or around those three subcards by default.
- Start the center lower half directly with the three subcards; do not render a visible line like `Three balanced method subpoints`, `Lower half`, or any equivalent wrapper label before them.
- The center card's dominance should come from the method's explanatory structure, not from enlarging a low-information chart. Only the method/architecture figure may be hero-sized by default.
- Keep the left card focused on motivation, bottleneck, preliminary observation, or contribution bullets, arranged as a pure vertical text-plus-1-2-figures stack.
- Keep the right card evidence-heavy: vertically stacked titled result blocks, each with 1-2 explanatory sentences and a plot/table that nearly fills the card width.
- Use exactly these three main card headers: `1、Motivation`, `2、Method`, and `3、Experiment`. The card headers are fixed labels, not paper-specific titles.
- Use a larger sample-matched typography scale than the current sparse output: default to +6 pt across all text classes, with an allowed +4 to +8 pt starting correction range. If blank space remains, keep proportionally scaling typography inside the underfilled card/subcards until the blank area is not obvious.

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

Use `scripts/audit_vertical_fill.py` after rendering a PNG preview to enforce the no-large-bottom-blank, cross-card content-height balance, and narrow-gutter rules. Pass the actual normalized or pixel boxes of the three cards; if any card fails, revise the layout before delivery.

Useful corpus commands:

```bash
python scripts/collect_poster_corpus.py --output references/poster-corpus-scan.json
python scripts/collect_poster_corpus.py --include-links --output references/poster-corpus-index.json
python scripts/collect_poster_corpus.py --query "<task method domain evidence>" --top-k 30 --output references/topic-neighbor-sample.json
```

Useful vertical audit command:

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

## Guardrails

- Do not fabricate claims, metrics, affiliations, logos, or citations.
- Do not dump paper prose into the poster; rewrite into short bullets and callouts.
- Do not size the sample-like 1:2:1 poster against the full image raster; size it against the card cluster plus its ~3% outer whitespace.
- Do not let equal-width grids override the 1:2:1 story. The center column must earn its width.
- Do not approximate the three card widths by eye. Measure or compute the main card boxes so the center card is twice each side card, excluding gutters and outer whitespace.
- Do not let card gutters become wide empty lanes. The gap between cards should be small and sample-like, about the same visual scale as the outer breathing margin around the three-card cluster.
- Do not place a standalone title area, metrics band, footer, or bottom takeaway strip outside the three rounded 1:2:1 cards unless explicitly requested.
- Do not make the motivation card a dashboard. It must be a vertical stack of text plus 1-2 figures.
- Do not rename the three main card headers. They must remain exactly `1、Motivation`, `2、Method`, and `3、Experiment`.
- Do not use a generated method diagram if the source paper already has a usable method/pipeline figure.
- Do not let the center card's three method subcards have visibly different font size, line count, or content amount.
- Do not add a visible lower-half group heading such as `Three balanced method subpoints`; the three method subcards must begin directly in the lower half.
- Do not number method subcard titles. Use only short semantic mini-titles without `1.`, `2.`, `3.`, letters, badges, or step numbers.
- Do not place narrow experimental charts or headline tables in the right card when they can be cropped, scaled, or grouped to fill the card width.
- Do not allow any right-card experiment result block, figure, table, caption, or text to cross or clip past the bottom border of the `3、Experiment` rounded rectangle.
- Do not fix right-card bottom overflow by moving the card border, adding an external footer, or shrinking the entire poster first; shrink the right-card experiment visuals/tables proportionally until the content fits inside the card.
- Do not put extra `claim`, `validity`, bottom-anchor, or result-plot sections in the center card below the method subcards. The lower half is exactly the three method subcards.
- Do not let auto layout shrink the center pipeline below its exact upper-half region or place the method subcards in anything other than the exact lower-half region.
- Do not accept a first experiment table that uses its natural narrow width; force it to 90-100% of the right card inner width or rebuild it as a full-width highlighted table/panel.
- Do not leave tiny text in large boxes; increase font size and line height after source-backed content has been selected.
- Do not leave the left card lower half or the three center subcards with large pale empty areas; after source-backed content is present, enlarge typography by 4-8 pt, then continue proportional in-region scaling until the area is actually filled.
- Do not use the old small-font baseline. Increase all poster fonts by 4-8 pt as the first correction, then continue proportional card-internal scaling in underfilled regions unless doing so causes unavoidable clipping after layout compaction.
- Do not use oversized plots, screenshots, or empty panels as filler. Shrink or replace any figure that does not earn its area with clear explanatory value.
- Do not scatter information into many disconnected micro-boxes, ledger strips, metric chips, or form-like rows. Merge related facts into macro sections with headings, captions, and interpretation bullets.
- Do not leave a large bottom blank area or a large lower-half blank pocket inside any card. If content is short, enlarge/rebalance in-card figures, captions, takeaway blocks, or source-backed explanations inside the three cards.
- Do not accept a poster where one or two cards have real content ending much higher than the others. Balance content heights by changing copy, captions, figure crops, section heights, and typography.
- Do not treat pale section backgrounds or empty tinted rectangles as filled content.
- Do not let any card terminate right after a hero figure or opening bullets. Left and right cards need substantive lower-half content and a meaningful bottom anchor; the center card's anchor must be embedded inside the three lower-half method subcards.
- Do not build a wall-of-text IMRAD poster unless the venue explicitly requires it.
- Do not start final rendering until the claim, column roles, and figure list are explicit.
- Ask at most one clarifying question only when the missing information would otherwise force fabricated results or branding.
- Do not rerun corpus collection for ordinary poster drafting; use the learned abstraction note unless a refresh is explicitly needed.
