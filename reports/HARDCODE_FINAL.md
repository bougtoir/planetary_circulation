# HARD-CODE / SINGLE-SOURCE AUDIT — FINAL (10-gate QC, Gate 2)

Scope: `analysis/scripts/{build_data,derive_matrices,analyze,figures_1_5_6,build_manuscript,build_inline}.py`,
post-expansion NO_SUPPLEMENT build.

## Method
1. Regex scan of every script for numeric literals, classifying each as
   INPUT (literature-sourced constants, seed, coding dict, figure cosmetics) or
   DERIVED (a value that should come from pipeline output).
2. Cross-check every reportable number in the manuscript against live derived
   outputs (result_traceability_final.csv).

## Findings

### build_manuscript.py
- All reportable numbers are f-string injected from `analysis_summary.json`,
  `spread_montecarlo.csv`, `network_metrics.csv`, `pca_loo.csv`,
  `coverage_stats.json` (loaders at lines ~16–39). No derived-value literals.
- Remaining numerics: word-count/section constants and format settings only.
- **PASS**

### analyze.py / derive_matrices.py / build_data.py
- Literals found: input evidence matrices, coding dicts
  (`dynamo_off` cessation dates: Mars 4.1 Ga, Moon 2.0/1.0–3.5 Ga, Venus 4.5
  inferred), energy values, seeds (MC 4,000 draws, fixed seed).
- Classification: **INPUT — legitimate, REVIEW-class** (literature-sourced;
  each cited in the 60-item bibliography). No derived outputs hard-coded.
- **PASS**

### figures_1_5_6.py
- Reads canonical `dom_driver` from processed data (duplicate `dom` dict removed
  in an earlier pass). Remaining literals: axis labels, colors, geometry.
- **PASS**

### build_inline.py
- Copies the built docx; no numbers of its own.
- **PASS**

## Stale/literal check on the rendered manuscript
Manuscript numbers vs live outputs — all match after rounding (see
result_traceability_final.csv): 92.9%, 52/56, 10 quant cells, PC1 56%/44%,
LOO 46–66%, spreads 0.91/0.78/0.44, MC bands, ρ/p pairs, 4.1/3.5 Ga inputs.

## Disposition
**PASS — no hard-coded derived results; single-source-of-truth pipeline intact.**
