# DATA–TEXT–FIGURE CONSISTENCY (Gate 7) — current artifact

Three-way comparison: canonical derived outputs ↔ manuscript text/abstract/
Results/Discussion/Conclusion/captions ↔ rendered figures, plus highlights
and cover letter.

## Values compared (all live-read from derived artifacts this audit)
| Quantity | Text | Figure/caption | Derived output | Status |
|---|---|---|---|---|
| Coverage | 52 of 56 = 92.9% | Fig.2 matrix | coverage_stats.json 92.9%, 4 tier-D | match |
| Quantitative cells | 10 | — | coverage_stats.json | match |
| PC1 | 56% | "PC1 (56% var)" | 56.4% | match (declared rounding) |
| PC2 | 17% | "PC2 (17% var)" | 16.8% | match |
| LOO PC1 | 46–66% | caption | 46.5–66.3% | match |
| Spread Mars | 0.91; band 0.91–0.92 | Fig.4 bars | 0.911; MC 0.92 [0.91–0.92] | match |
| Spread Mercury | 0.78; band 0.78–0.88 | Fig.4 | 0.778; MC 0.83 [0.78–0.88] | match |
| Spread Moon | 0.44; band 0.32–0.75 | Fig.4 | 0.443; MC 0.50 [0.32–0.75] | match |
| MC draws | 4,000 | Methods | spread_montecarlo.csv n | match |
| Supported counts | 7,7,7,7,6,6,5,4 | Fig.5 | network_metrics.csv | match |
| n_components | ≤4 (Moon, Mercury) | — | pca_loo.csv | match |
| ρ(age), p | −0.18, 0.68 | — | −0.1769, 0.675 | match |
| ρ(mass), p | 0.22, 0.61 | — | 0.2171, 0.606 | match |
| Io E4 | structurally_absent (Io total 6) | Fig.2 | activity/observability matrices | match |
| Cessations | Mars ~4.1 Ga; Moon band; Venus inferred | Fig.4 bars + dashed | persistence_matrix.csv | match |
| Highlights | 5 bullets ≤82 chars | — | consistent with abstract | match |

## Visual figure check
Rendered fig3/fig4 inspected: axes percentages, interval positions, censored
arrows and dashed inferred bars all consistent. Cosmetic: "Mars"/"Io" labels
nearly collide bottom-right of Fig.3 — non-blocking, no numeric impact.

## Discrepancies
None. Every reported value matches its derived source within declared rounding.

## Gate-7 status: PASS
