# COVERAGE_GATE.md — Phase 3 go/no-go

Computed by `analysis/scripts/derive_matrices.py` → `data/processed/coverage_stats.json`.

## Result: **GO**

- Tier A–C coverage: **53 / 56 cells = 94.6%** (A=8, B=19, C=26, D=3)
- Bodies with ≥4 evaluable process classes: **8 / 8**
- Both predefined GO criteria exceeded (thresholds: ≥70% cells and ≥5 bodies).

Tier-D cells (structural absences, not missing data):
- Venus E4, Moon E4, Mercury E4 — no subsurface-liquid reservoir.

## Weakest edge classes (for the record)
- E4 (subsurface liquid exchange): 3 structural absences + all surviving cells Tier C.
- E7 (chemical/redox cycling): quantitative fluxes rare; mostly state-level (Tier C).

No ontology consolidation is required by the gate. E4 absences are scientifically meaningful
(they *are* the network-decoupling signal for H3), so E4 is retained rather than collapsed.

## Decision
Proceed to full analysis per protocol. No redesign.
