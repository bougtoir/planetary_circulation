# EPSL FINAL FINISHING REPORT

Date: 2026-09-26 (UTC). Canonical tree `planetary_circulation/`; all changes via
`analysis/scripts/build_manuscript.py` then full document regeneration.

## 1. Abstract closing revision

Old: "…than as a position on a single active/inactive axis."
New: "…than by a single active/inactive axis alone."

## 2. Conclusion closing revision

Old: "…— not a scalar."
New: "…— and is not fully captured by a scalar description."

## 3. Verified canonical Spearman values

`analysis/derived/null_correlations.json` (count-based, post-review-fix):
age ρ = −0.33, p = 0.42; mass ρ = 0.08, p = 0.85 — n = 8, descriptive only.
Verified against `analysis/scripts/analyze.py`: predictor = `sup_cnt` (count of supported
process classes per body, statuses direct_active/probable_active/residual); ages and masses
from `body_attributes.json`. Abstract, Results 3.6, highlights.txt, and cover letter all use
these canonical values.

## 4. Why values differ from the earlier draft

The first manuscript version used the *sum of ordinal evidence-state codes* (0–4 per cell)
rather than the count of supported processes, giving ρ = −0.04 (age) and 0.35 (mass). A Devin
Review finding flagged the metric/claim mismatch; the analysis was corrected to the
process-count metric and manuscript numbers updated accordingly. The qualitative conclusion
(no ordering by age or mass) is unchanged.

## 5. Analysis reruns

None in this pass — the change was text-only. The canonical numeric outputs were verified
(read from `analysis_summary.json`/`null_correlations.json`, matching the regenerated text).

## 6. Numerical values changed

None. Consistency verified for: 8 bodies, 7 classes, 56 cells, 53/56 (94.6%), PC1 56%,
PC2 17%, PC3 ~15%, LOO PC1 46–66%, Mars dynamo 4.1 Ga, Mercury volcanism 3.5 Ga, lunar mare
1.2–2.0 Ga, spreads 0.91/0.78/0.44, supported counts 4–7.

## 7. Placeholder / internal-artifact sweep

DOCX text scanned for VERIFY/TO COMPLETE/TODO/TBD/FIXME/Devin/internal note/placeholder/
"multidimensional residual"/"not a scalar"/"not adequately one-dimensional"/"Mercury is
older"/"planetary death"/"terraforming"/"colonization":

- Remaining `[TO COMPLETE]`/`[VERIFY]` occurrences are strictly author-supplied metadata:
  author names, affiliations, corresponding author, acknowledgements, CRediT, and the
  competing-interests declaration (left marked for local confirmation).
- Cover letter contains one `[TO COMPLETE]` in "all authors … approve submission" — author
  action, retained.
- No Devin/AI/internal notes in any submission-facing document.

## 8. Figure / render check

- Fig. 2: six-state legend (D / P / R / 0 / ? / —) matches the corrected colormap.
- Fig. 3: titled "exploratory, n=8"; PC1/PC2 axis labels show 56%/17%, matching the text.
- Fig. 4: censored (blue arrow) vs cessation intervals (red) visually distinct; caption
  accurate.
- Fig. 5: caption now reads "Current circulation-network connectivity".
- Fig. 6: no numeric annotations that could drift from canonical values.
- `EPSL_main_manuscript_submission_final.pdf` renders 11 pages; `pdftotext` shows clean
  Greek ρ, en-dashes, and arrows — no malformed symbols or obvious layout artifacts.

## 9. Habitability paragraph

Preserved as a single restrained Discussion paragraph (Cockell et al., 2016 cited correctly).
Not in Abstract or Conclusions; no index, ranking, terraforming, or colonization claims.

## 10. Remaining local-author actions

1. Fill author names, affiliations, corresponding author, acknowledgements, CRediT roles.
2. Confirm the competing-interests declaration.
3. Optional graphical abstract; submit via Editorial Manager ("Letter").

## Final EPSL readiness judgment

**A — EPSL-ready.** Claims calibrated to the n=8 pilot; numbers internally consistent;
package clean of internal artifacts.
