# PUBLIC REPOSITORY REPRODUCIBILITY — FINAL (10-gate QC, Gate 3)

## What was actually executed (single VM, sequential, clean dirs)

### A. Live public HEAD at audit time
- `git clone https://github.com/bougtoir/planetary_circulation /tmp/pc_pub`
- HEAD: `ab2bb9e747b25dd4037e4d942ba906bf63550114` (2026-10-17) — **the pre-expansion
  revision** (still contains supplement files). The wip sync branch carrying the
  current revision is pushed (`devin/1790413216-planetary-circulation` @ 8dd95f759);
  the mirror updates on the sync-to-repos cron (manual dispatch is not permitted
  by the session token — HTTP 403).
- Pipeline on this public revision: `build_data → derive_matrices → analyze →
  figures_1_5_6 → build_manuscript → build_inline` — all six ran clean
  (`/tmp/pub_*.log`). This verifies the *published* pipeline executes end-to-end,
  but the revision is one sync cycle behind the manuscript.

### B. Pending public revision (what the mirror will contain)
- Materialized via `git archive origin/devin/1790413216-planetary-circulation
  planetary_circulation` → `/tmp/pc_pending` (same filtered content the sync
  workflow pushes; the sync compares a deterministic commit-tree of this subdir).
- Same six-script pipeline: all ran clean (`/tmp/pend_*.log`).
- Output comparison vs canonical wip tree:
  - `spread_montecarlo.csv`: identical
  - `coverage_stats.json`: identical
  - `analysis_summary.json`: 128 keys, 0 diffs beyond last-bit float
    representation (rel tol 1e-9) — numpy BLAS-version noise, not real
  - manuscript docx text: identical to the committed revision
    (the working-tree abstract trim 299→247 landed in the subsequent commit;
    pipeline correctness unaffected).

## Environment / commands recorded
- Platform: Devin Linux VM (same VM as the audit).
- Commands: `python3 analysis/scripts/<script>.py` for the six stages above;
  python-docx used for text comparison.

## Discrepancies
1. Public mirror lags one sync cycle (stale, self-healing on next cron) —
   residual issue, recorded in the readiness table.
2. Float last-bit noise in `analysis_summary.json` across environments —
   cosmetic, no effect on any reported value.

## Disposition
**VERIFIED (with recorded caveat)** — pipeline executes end-to-end on the
public code and the pending public revision reproduces the canonical derived
outputs. Not labeled a bare PASS for the live mirror because the mirror's HEAD
still holds the older revision at audit time; the discrepancy is documented
rather than hidden.
