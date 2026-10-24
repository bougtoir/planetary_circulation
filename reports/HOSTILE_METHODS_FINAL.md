# HOSTILE METHODS / STATISTICS REVIEW — FINAL (10-gate QC, Gate 1)

Tested against the current derived outputs (this session, same VM):
`analysis/derived/analysis_summary.json`, `spread_montecarlo.csv`,
`network_metrics.csv`, `pca_loo.csv`, `data/processed/coverage_stats.json`.

## M1. Persistence spread metric — consistent definition?
- Current definition: max−min spread over *dated cessation* intervals only;
  censored reservoirs excluded from the statistic (recorded separately).
  Monte Carlo uses the same statistic on 4,000 draws.
- Live outputs: MC medians Mars 0.92 [0.91–0.92], Mercury 0.83 [0.78–0.88],
  Moon 0.50 [0.32–0.75]; deterministic spreads 0.911 / 0.778 / 0.443.
- "Mars and Mercury show the widest spreads" is now literally true — Mars (1st),
  Mercury (2nd); Moon's larger uncertainty band is flagged in text.
- Disposition: **cleared — the earlier MAJOR (IQR-vs-extremes inconsistency) is closed.**

## M2. Venus dynamo inference contaminating the persistence statistic?
- Venus dynamo-off recorded as inferred, not dated → excluded from spread math,
  still shown (flagged) in Fig. 4. Mars "most spread" claim unaffected.
- Disposition: **cleared (fixed earlier; verified live).**

## M3. Coverage arithmetic
- 52/56 evaluable cells = 92.9%; 4 tier-D cells; quant_cells = 10 — all regenerated
  values read from `coverage_stats.json`, not literals in text.
- Disposition: **cleared.**

## M4. Ordination robustness (n=8)
- PCA variance 56.4 / 16.8 / 15.2 / 7.1%; LOO PC1 46.5–66.3% reported;
  supported counts Earth/Mars/Europa/Titan 7, Venus/Io 6, Mercury 5, Moon 4;
  n_components ≤ 4 (Moon, Mercury).
- Statistical wording is descriptive ("first axis orders bodies…"), not inferential.
- Disposition: **cleared — MINOR(negative)**.

## M5. Null tests vs size/mass/age
- Spearman: age ρ=−0.1769, p=0.675; mass ρ=0.2171, p=0.606. n=8 → wide CI;
  text reports both as null results without over-claiming power.
- Disposition: **cleared.**

## M6. MC uncertainty bands honest?
- 4,000 draws; Moon band [0.32–0.75] is correctly described as wide/uncertain;
  no squeezing of intervals in text.
- Disposition: **cleared.**

## M7. Multiplicativity / utility-form assumptions
- The activity–persistence–observability combination is presented as a
  comparative representation, not a fit; no regression coefficients claimed.
- Disposition: **cleared.**

## Reviewer verdict (simulated)
No standing FATAL/MAJOR. Remaining exposures are honest n=8 limits already
declared in the manuscript. **Gate-1 (methods) disposition: PASS**
