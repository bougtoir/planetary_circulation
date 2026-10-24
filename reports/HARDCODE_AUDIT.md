# HARD-CODE / STALE-OUTPUT AUDIT (Gate 2) — current artifact

Scope: all six generators (`analysis/scripts/build_data.py, derive_matrices.py,
analyze.py, figures_1_5_6.py, build_manuscript.py, build_inline.py`) against the
current derived outputs and the FINAL_10GATE_AUDITED manuscript.

## Method
- Regex literal scan per script; each numeric literal classified INPUT vs DERIVED.
- Every reportable number traced to a canonical artifact
  (`reports/result_traceability.csv`, 19 rows, all verified live this audit).

## Result (file:line-class findings)
- `build_manuscript.py` (~lines 16–39): loaders read
  `analysis_summary.json`, `spread_montecarlo.csv`, `network_metrics.csv`,
  `pca_loo.csv`, `data/processed/coverage_stats.json`; all reported values are
  f-string injected. No derived-value literals. PASS.
- `build_data.py` / `derive_matrices.py` / `analyze.py`: literals are input
  evidence matrices, coding dicts, cessation dates
  (`dynamo_off`: Mars 4.1 Ga, Moon 2.0/1.0–3.5 Ga, Venus 4.5 inferred),
  energy values, MC seed/4,000 draws — INPUT/REVIEW class, each cited in the
  60-item bibliography. PASS.
- `figures_1_5_6.py`: reads canonical `dom_driver`; remaining literals are
  cosmetics/labels. PASS.
- Manuscript spot check vs live outputs: 92.9% / 52 of 56 / 10 quant cells /
  PC1 56% / LOO 46–66% / spreads 0.91, 0.78, 0.44 / MC bands /
  ρ(age)=−0.18 p=0.68 / ρ(mass)=0.22 p=0.61 — all match derived outputs
  after declared rounding. No untraceable reportable values.

## Stale artifacts
- `archive/pre_no_supplement/`, `archive/pre_hostile_review/` hold superseded
  zips/supplement/docx — quarantined outside the package.
- Earlier-lineage zips in `submission/` are superseded by the 10GATE zip
  (manifest distinguishes lineage).

## Gate-2 status: PASS — zero untraceable reportable values.
