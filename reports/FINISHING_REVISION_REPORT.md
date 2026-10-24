# FINISHING REVISION REPORT

Date: 2026-09-26 (UTC). Performed on the canonical tree `planetary_circulation/` via edits to
`analysis/scripts/build_manuscript.py` followed by full regeneration — no text was patched in
the DOCX directly, so prose and numbers remain reproducible.

## 1. Exact changes made

All prose changes are in `build_manuscript.py`; outputs regenerated:
`EPSL_main_manuscript.docx/.pdf`, `EPSL_main_manuscript_inline_revised.docx/.pdf`
(and `EPSL_main_manuscript_inline.docx` synced to the revised text),
`EPSL_supplement.docx/.pdf`, `highlights.txt`, `cover_letter.docx`.

## 2. Engineered/augmented habitability paragraph

Inserted as a single Discussion paragraph immediately after the falsifiability paragraph and
before the explicit-limitations paragraph ("These conclusions carry explicit limits…").
It follows the required conceptual flow circulation architecture → retained functions →
missing functions → "augmentation gap" → future engineered-habitability assessment, uses only
restrained language ("may provide a physical basis", "could provide a starting state", "beyond
the scope of this Letter"), introduces the term "augmentation gap" once without defining a
metric, and adds no figure. Cited once to Cockell et al. (2016) for the conventional
habitability framing. Not mentioned in Abstract or Conclusions.

## 3. H1 / dimensionality wording

- Abstract: "…but a substantial multidimensional residual (~44%): comparative planetary state
  is not adequately one-dimensional" → "…while ~44% of ordination variance lies outside that
  axis and carries architecture-specific information. A single activity axis is a useful
  first-order summary but does not capture the full comparative structure."
- Results 3.2: "reject both extremes of H1 — the state is not adequately scalar" → "H1 is
  answered in the middle: a dominant activity gradient exists and a single axis provides a
  useful first-order summary, but a substantial share of variance lies outside it."

## 4. Former "~44% multidimensional residual"

All occurrences replaced by the literal formulation:
- Abstract: "~44% of ordination variance lies outside that axis"
- Discussion limits: "the ~44% of ordination variance outside the first axis should be read
  as indicating further structure, not as a measurement of dimensionality"
- Conclusions: "with ~44% of ordination variance on other axes"
- Highlights: "Dominant activity gradient, but ~44% of ordination variance lies off-axis"
- Cover letter: "with ~44% of ordination variance on other axes"
No occurrence of "multidimensional residual" remains.

## 5. Mercury–Titan age wording

"Mercury is older than Titan by the usual formation chronology yet retains an internal dynamo
that Titan lacks…" → "Mercury and Titan are both ancient Solar-System bodies yet retain
radically different circulation architectures — Mercury keeps an internal dynamo that Titan
lacks, while Titan supports a far richer surface–atmosphere circulation." The H4 argument now
rests on contrasting energy-source architectures, not relative formation ages.

## 6. H3 / decoupling calibration

- Abstract: "which subsystems have decoupled or shut down" → "which subsystems have shut down".
- Results 3.4: present-architecture claim retained ("bodies differ in which reservoir
  couplings exist"), plus explicit boundary sentence: "(these architectures may arise through
  progressive loss, persistence, or reconfiguration of couplings, which the present data do
  not reconstruct)". No claim of a demonstrated universal fragmentation sequence remains.
- Fig. 5 caption now says "Current circulation-network connectivity".

## 7. Numerical corrections

None needed: all numbers were already templated from `analysis_summary.json` (PC1 56%,
PC2 17%, LOO 46–66%, spreads 0.91/0.78/0.44, ρ age −0.33 / mass 0.08 — updated in the
previous review-fix pass to the count-based metric). Verified against canonical outputs.

## 8. Analysis reruns

No analysis code changed in this pass (the review-fix pass earlier already corrected the
network aggregation and null-correlation metric and reran `analyze.py` + figures). This
revision is text-only; only document builders were rerun.

## 9. New references

One added: Cockell et al., 2016, *Astrobiology* 16, 89–117 (DOI verified). It supports only
the conceptual habitability sentence; no habitability literature review added.
reference_audit.csv updated (60 entries).

## 10. Remaining author-only placeholders

Unchanged: author names/affiliations, corresponding author, CRediT contributions,
acknowledgements, competing-interests verification — `[TO COMPLETE]`/`[VERIFY]` on the title
page and declarations. Optional graphical abstract not produced (kept optional per EPSL).

## Quality check

- No new unsupported claims; no augmentability index, ranking, terraforming, or colonization
  statements; Abstract/Conclusions contain no habitability material.
- Main-text length ~2,030 words — well within EPSL's 6,500-word limit.
- DOCX and PDF regenerated and non-empty; inline revised versions included in the submission zip.
