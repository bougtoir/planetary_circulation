# PUBLIC REPRODUCIBILITY AUDIT (Gate 3) — current artifact

Public repo: https://github.com/bougtoir/planetary_circulation — public, readable.
Public HEAD at audit (2026-10-24 ~13:00 UTC fetch):
`6495cdb8f3d0dbe68ec3ea6ef1e97e825f0ba749` (sync commit 2026-10-22 15:28) —
contains the current revision incl. `EPSL_submission_package_FINAL_10GATE_AUDITED.zip`
and `EPSL_main_manuscript_FINAL_QC.docx/.pdf`. The public submission ZIP is
**byte-identical** to the canonical zip in wip (verified by binary compare).

## Fresh clone run (separate temp dir on the same VM)
- `git clone https://github.com/bougtoir/planetary_circulation /tmp/pc_fresh`
- Documented pipeline (README → reports/FINAL_HANDOFF.md; scripts under
  `analysis/scripts/`):
  `python3 analysis/scripts/{build_data,derive_matrices,analyze,figures_1_5_6,build_manuscript,build_inline}.py`
- Exit status: all six stages OK (logs /tmp/fresh_*.log). No missing inputs;
  all required data ships in the public repo (`data/processed/` + inputs).

## Output comparison vs canonical (wip @ de2ab26d)
| Artifact | Result |
|---|---|
| `analysis/derived/spread_montecarlo.csv` | byte-identical |
| `analysis/derived/network_metrics.csv` | byte-identical |
| `data/processed/coverage_stats.json` | 0 material diffs (10 keys) |
| `analysis/derived/analysis_summary.json` | 128 keys, 0 material diffs (float last-bit rep only) |
| `analysis/derived/pca_loo.csv` | 8 rows differ by ≤ 4.4e-16 (BLAS last-bit noise; LOO PC1 range 46.5–66.3% unchanged) |
| manuscript docx text | paragraph-identical to canonical |
| submission zip | byte-identical to canonical zip |

## Defects / limitations
- Earlier audit run found the mirror one sync cycle behind; the cron has since
  synced (15:28 UTC), and the public HEAD now carries the current revision.
  This residual is closed.
- pca_loo.csv last-bit float noise across environments — cosmetic only.

## Gate-3 status: PASS — fresh public clone reproduces the current submission
artifacts; public HEAD SHA matches the synced revision.
