# HOSTILE EDITOR REVIEW — EPSL desk-rejection perspective
Date: 2026-10-17 (UTC). Target: current EPSL submission package (`EPSL_submission_package_FINAL.zip`,
main manuscript `EPSL_main_manuscript_submission_final.docx`).

## Likely desk-rejection reasons (ranked)

### E1. "Descriptive catalogue in network clothing" — severity: MAJOR, fixable
An editor can say: eight bodies, seven process classes, hand-built status matrix — this is a
review article compressed into Letter form. **Fix:** emphasize that the paper's contribution
is an explicit falsifiable test (H1–H4) run on a frozen dataset, not the catalogue; the
manuscript already frames H1–H4 in §1 and answers each in §3 — retained, and the targeted
revision strengthens the Methods definition of the persistence-spread statistic and the E4
ontology so the test reads as measurement, not narrative. Also the coverage gate (94.6% →
92.9% after the E4 correction) shows the matrix is a data product with a pass/fail bar.

### E2. n = 8 — severity: MODERATE, partially fixable
Any inferential reading is hopeless at n = 8. Manuscript already restricts itself to
descriptive statistics, leave-one-body-out sensitivity, and explicit "descriptive only"
labels on the Spearman nulls. Retained as an honest limitation; do not add machinery to hide it.

### E3. PCA on ordinal evidence states — severity: MODERATE, fixable
Treating D/P/R/0 states as an ordinal interval scale then standardizing for PCA is
methodologically soft; structurally-absent cells are imputed by column medians — a choice a
Reviewer-1 type will attack. **Fix applied/kept:** PCA is labelled exploratory, the headline
is the *existence* of off-axis structure (~44% residual variance), not a dimensional proof;
median imputation is now stated explicitly in Methods; LOO range (46–66%) is reported.

### E4. Novelty boundary — severity: MODERATE, fixable
"Networks + planets" exists (Earth climate networks), and "vitality/metabolism" vocabulary is
loaded. **Fix:** the manuscript already demotes vitality to an umbrella metaphor and never
claims "first". NOVELTY_HOSTILE_AUDIT.md confirms no prior common-ontology × multi-body ×
activity × persistence × observability × connectivity × single-axis test. Wording kept honest.

### E5. Claims broader than data — severity: MODERATE→FIXED
Two phrases were vulnerable: "Energy-source architecture *organizes the sample better*" and
"Mars and Mercury are *the most spread* in the sample" (false as computed — Venus's assumed
dynamo cessation produced spread 0.99 > Mars 0.91). Both are corrected in the targeted
revision (dated-cessation rule for the spread statistic; calibrated energy-architecture
wording).

### E6. Fit vs JGR: Planets — severity: MINOR, manageable
A framework pilot could be said to belong to JGR: Planets or Icarus. Counter: the Letter has
one concise take-home result (asynchronous per-subsystem cessation on a common measurement
basis) suitable for EPSL's broad readership. Fallback documented in EPSL_FINAL_READINESS.md.

### E7. Structural defects in the package itself — severity: was MAJOR, FIXED
Package inspection found: (a) supplement's "Asynchronous Persistence Index" (IQR) contradicted
the main text's range-like spread statistic — same construct, two metrics; (b) Io's E4 cell
coded a silicate partial-melt layer under "Subsurface Liquid", breaking the volatile-reservoir
ontology; (c) the packaged `energy_architecture.csv` carried a stale `dom = stellar` column
for all bodies. All three corrected in the targeted revision.

## Editorial verdict
No desk-rejection-grade defect survives after the targeted revision. The paper remains a
pilot/framework Letter; its claims are now internally consistent and calibrated.
Classification input to synthesis: **B → A** (EPSL-ready after targeted fixes).
