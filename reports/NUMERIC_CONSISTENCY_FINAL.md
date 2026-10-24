# NUMERIC CONSISTENCY — FINAL (10-gate QC, Gate 7)

Three-way check: manuscript text ↔ rendered figures ↔ derived outputs
(`analysis/derived/*.json|csv`, `data/processed/coverage_stats.json`).

## Cross-checked values (all live-verified)
| Quantity | Text | Figure | Derived | Match |
|---|---|---|---|---|
| PC1 variance | 56% | Fig.3 axis "PC1 (56% var)" | 56.4% | ✓ |
| PC2 variance | 15–17% usage consistent | Fig.3 axis "PC2 (17% var)" | 16.8% | ✓ |
| LOO PC1 | 46–66% | — | 46.5–66.3% | ✓ |
| spread Mars | 0.91, band 0.91–0.92 | Fig.4 Mars intervals | 0.911 / 0.92[0.91–0.92] | ✓ |
| spread Mercury | 0.78, band 0.78–0.88 | Fig.4 Mercury interval | 0.778 / 0.83[0.78–0.88] | ✓ |
| spread Moon | 0.44, band 0.32–0.75 | Fig.4 Moon long bar | 0.443 / 0.50[0.32–0.75] | ✓ |
| coverage | 52/56 = 92.9% | Fig.2 matrix cells | 92.9%, 4 tier-D | ✓ |
| quantitative cells | 10 | — | 10 | ✓ |
| supported counts | 7/7/7/7,6/6,5,4 | Fig.5 | identical vector | ✓ |
| age ρ / p | −0.18 / 0.68 | — | −0.1769 / 0.675 | ✓ |
| mass ρ / p | 0.22 / 0.61 | — | 0.2171 / 0.606 | ✓ |
| cessations | Mars ~4.1 Ga; Moon band | Fig.4 bars | persistence_matrix.csv | ✓ |

## Visual figure inspection (rendered PNGs)
- Fig.3 ordination: 8 points, PC1 = dominant Earth-vs-rest gradient; PC2 separates
  Europa/Titan; matches the text ordering claim. Axis labels round 56.4→56 and
  16.8→17, consistent.
- Fig.4 persistence spectra: censored arrows, dated red intervals, dashed
  "inferred, not dated" for Venus dynamo — matches Methods conventions.
  Mars dynamo ~0.1, Moon dynamo band ~0.22–0.77, volcanism 0.58–0.78 — consistent
  with the stored intervals.
- Cosmetic note: "Mars" and "Io" labels nearly collide at bottom-right of Fig.3
  (points ~1.0 and ~1.5 on PC1). Non-blocking; flagged for optional polish.
- Figs 1, 2, 5, 6: consistent with text descriptions (matrix values, supported
  counts, dom_driver colors).

## Disposition
**PASS — text/figure/derived outputs numerically consistent; one MINOR cosmetic
label overlap recorded, no correction required for submission.**
