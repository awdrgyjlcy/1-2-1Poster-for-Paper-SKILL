# Poster Corpus Abstraction Notes

This note captures poster-side reduction patterns that recur across searchable paper/poster pairs from public computer-science conference sites.

## Corpus Window

Public official conference virtual poster pages sampled for this skill:

- NeurIPS 2024 virtual papers/posters index: 4,538 poster links, https://nips.cc/virtual/2024/papers.html?filter=titles
- NeurIPS 2023 virtual papers/posters index: 3,585 poster links, https://nips.cc/virtual/2023/papers.html?filter=titles
- ICLR 2024 virtual papers/posters index: 2,296 poster links, https://iclr.cc/virtual/2024/papers.html?filter=titles
- CVPR 2024 virtual papers/posters index: 2,716 poster links, https://cvpr.thecvf.com/virtual/2024/papers.html?filter=titles

Total accessible poster pages found across these four official index pages: 13,135.

Counts were obtained by extracting unique `/virtual/YYYY/poster/ID` links from official index HTML. Sampled poster pages expose the poster artifact plus a linked paper path such as OpenReview, proceedings, or a poster PDF.

Refresh command:

```bash
python scripts/collect_poster_corpus.py --output references/poster-corpus-scan.json
python scripts/collect_poster_corpus.py --include-links --output references/poster-corpus-index.json
python scripts/collect_poster_corpus.py --query "<task method domain evidence>" --top-k 30 --output references/topic-neighbor-sample.json
```

Use `poster-corpus-scan.json` for lightweight verification and `poster-corpus-index.json` for full URL-level sampling.
Use `topic-neighbor-sample.json` as project scratch evidence for one target paper; regenerate it per topic instead of treating a bundled sample as universal guidance.

Example verified pages:

- NeurIPS 2024 sample: https://nips.cc/virtual/2024/poster/92923
- NeurIPS 2023 sample: https://nips.cc/virtual/2023/poster/69865
- ICLR 2024 sample: https://iclr.cc/virtual/2024/poster/17365
- CVPR 2024 sample: https://cvpr.thecvf.com/virtual/2024/poster/29177

## Core Abstraction Moves

| Paper element | Poster element |
| --- | --- |
| Title | Claim-level headline |
| Abstract | One-sentence value proposition |
| Introduction | 2-3 motivation bullets |
| Problem statement | One bottleneck callout |
| Method sections | One hero diagram + module labels |
| Algorithm details | Short action labels, not full steps |
| Main results | One compact table or plot |
| Ablations | 1-2 support plots or mini tables |
| Discussion | One takeaway or caution box |
| Appendix material | Usually omitted unless essential |

## Paper-To-Poster Compression Checklist

Use this checklist after reading the target paper and before writing poster copy. The goal is to decide what earns space.

1. Claim line:
   - Source: title, abstract, contribution list, main result paragraph.
   - Poster decision: write one sentence with task, method idea, and evidence.
   - Keep if it can be read as `we solve [problem] by [idea], supported by [result]`.

2. Motivation block:
   - Source: introduction, problem statement, first motivating figure, failure examples.
   - Poster decision: keep 2-3 bullets that explain the bottleneck a viewer must understand.
   - Drop broad related-work taxonomies, historical setup, and generic importance claims.

3. Center hero method:
   - Source: method overview, algorithm box, architecture figure, pipeline figure.
   - Poster decision: make one diagram with 3-5 labeled actions or modules.
   - Convert implementation detail into verbs: `sample`, `score`, `route`, `aggregate`, `align`, `verify`.

4. Evidence block:
   - Source: main benchmark table, headline plot, ablations, efficiency analysis.
   - Poster decision: keep one primary result visual plus 1-2 support visuals.
   - Highlight rows, columns, or curves that prove the claim; move full tables to QR or paper.

5. Takeaway and caveat:
   - Source: discussion, limitations, conclusion, failure cases.
   - Poster decision: write one final takeaway and, if needed, one short caution.
   - Keep caveats factual and small; do not create a full limitations section unless the venue expects it.

6. Viewer questions:
   - Source: the likely questions a conference visitor asks in the first minute.
   - Poster decision: make sure the poster answers 3-5 questions without reading the paper.
   - Typical questions: What is the problem? What is new? How does it work? What proves it? When might it fail?

## Paper-Poster Correspondence Logic

The useful learning signal is not just what posters look like, but how authors transform paper structure into poster structure.

When reading a paper/poster pair, extract four things:

1. Salience shift:
   - What the paper treats as central versus what the poster enlarges.
   - Example pattern: a long method section becomes one hero figure and 3-5 labels.

2. Order shift:
   - What gets moved earlier on the poster because viewers need it sooner.
   - Example pattern: motivation and claim appear before detailed setup or notation.

3. Density shift:
   - What gets compressed into bullets, icons, short callouts, or a single equation.
   - Example pattern: a full benchmark table becomes one highlighted table slice plus one callout.

4. Omission shift:
   - What disappears entirely because it does not help the poster's one-minute job.
   - Example pattern: lengthy derivations, secondary baselines, and appendix-style detail.

Record each pair with:

- paper section,
- poster zone,
- transformation type,
- compression action,
- evidence retained,
- evidence dropped,
- resulting viewer question answered.

Use this correspondence logic to update the skill, not just to fill poster boxes.

### Paired-Content Examples

Use these official pairs as calibration examples when revising this skill:

- TimeChat, CVPR 2024:
  poster page `https://cvpr.thecvf.com/virtual/2024/poster/30015`;
  paper page `https://openaccess.thecvf.com/content/CVPR2024/html/Ren_TimeChat_A_Time-sensitive_Multimodal_Large_Language_Model_for_Long_Video_CVPR_2024_paper.html`.
  Correspondence pattern: the paper's architecture, instruction-data, and benchmark claims become left task motivation, center architecture/data blocks, and right performance/qualitative evidence.

- Vista-LLaMA, CVPR 2024:
  poster page `https://cvpr.thecvf.com/virtual/2024/poster/29676`.
  Correspondence pattern: the paper's hallucination problem and equal-distance visual-token mechanism become a left problem panel, a large framework panel, qualitative examples, and compact quantitative tables plus diagnostic heatmaps.

- BESA, ICLR 2024:
  poster page `https://iclr.cc/virtual/2024/poster/18153`.
  Correspondence pattern: the paper's pruning motivation, blockwise differentiable sparsity allocation, and efficiency results become left sensitivity plots, a central method diagram/equation, and right result/ablation tables.

Across these pairs, the poster follows viewer questions rather than paper chronology. The poster may split one paper contribution across several zones, or merge several paper subsections into one visual block, if that makes the one-minute explanation clearer.

## 1:2:1 Mapping Rules From The Corpus

- Left column gets the audience problem, bottleneck, motivating example, and contribution bullets.
- Center column gets the method hero, module labels, minimal equations, and the clearest explanation of novelty.
- Right column gets the main table or plot, ablations, efficiency or robustness analysis, and final takeaway.
- Footer gets QR/contact/references; do not spend body column space on follow-up material.
- If a section does not answer the claim, method, evidence, or caveat question, cut it or move it behind the QR code.

## Topic-Neighbor Sampling

For a target paper, sample 20-50 nearby official poster pages to tune abstraction choices without rerunning large-scale learning.

Good query ingredients:

- task terms: `long video understanding`, `semantic segmentation`, `code generation`;
- method terms: `token merging`, `retrieval`, `diffusion`, `graph neural network`;
- evidence terms: `efficiency`, `robustness`, `benchmark`, `ablation`;
- domain terms: `medical`, `robotics`, `multimodal`, `systems`, `security`.

Use the returned neighbor titles and poster pages to ask:

- Do nearby posters make the task or method the title-level hook?
- Do they reserve the largest visual for architecture, qualitative examples, or result comparison?
- Which metrics become large callouts, and which stay inside small tables?
- How much setup do they keep before showing the method?
- What do they omit that the paper spends pages on?

Do not copy a neighbor poster's claims, layout, or visual identity. Use the sample to calibrate compression.

## Example Transformations

These examples are patterns, not claims about a specific paper.

| Source paper material | Poster rewrite |
| --- | --- |
| Abstract says the method improves performance and efficiency across several benchmarks. | Headline claim plus one result callout: `Adaptive routing improves long-context reasoning while reducing token cost.` |
| Method section describes many algorithmic substeps. | Center diagram with 3-5 verbs: `encode -> score -> route -> aggregate -> answer`. |
| Main results table has many datasets and baselines. | One compact table with the strongest rows highlighted and a separate `+X accuracy / -Y compute` callout. |
| Ablation section has six variants. | One small plot or mini table showing the two variants that explain why the method works. |
| Limitations mention expensive preprocessing. | Small caution box: `Best when preprocessing can be amortized.` |

## What Repeats In Strong Posters

- One readable main claim.
- One visual center of gravity.
- Side columns that explain and prove, not compete.
- Short bullets instead of abstract paragraphs.
- Figures that do the storytelling.
- Metrics that support the claim, not every number in the paper.
- Visible contact, QR, and references for follow-up.

## Common Failure Modes

- Copying the paper abstract into the poster.
- Equal-width columns that flatten the story.
- Too many small figures.
- Too many colors with no semantic roles.
- Tiny tables that cannot be read at poster distance.
- Titles crowded by logos or subtitles.
- Sections that mirror the paper instead of serving the viewer.

## How To Use This Note

Use the corpus pass to decide what to cut.

1. For ordinary poster creation, use this note as the learned corpus prior.
2. For a topic-specific refinement, sample 20-50 nearby official paper/poster pairs.
3. For skill updates or broad style learning, refresh with 1000+ accessible pairs.
4. Find the paper's true claim.
5. Map the paper sections to poster roles.
6. Keep the method hero figure dominant.
7. Collapse experiments into a small number of high-value visuals.
8. Remove anything that does not help the viewer answer the paper's core question quickly.

## Related Source

Paper2Poster and similar benchmarks show why this matters: they pair recent conference papers with author-designed posters and evaluate whether a poster can convey the core paper content, not just look polished.
