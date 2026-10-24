# STALE RESULT / VERSION-CROSSING AUDIT
Date: 2026-10-17 (UTC).

## Found and handled

| Artifact | Problem | Action |
|---|---|---|
| `manuscript/EPSL_main_manuscript_submission_final.docx/.pdf` | pre-hostile-review copy (old numbers, old ontology) | moved to `archive/pre_hostile_review/` |
| `manuscript/EPSL_main_manuscript_inline_revised.docx/.pdf` | superseded ad-hoc inline copy | moved to `archive/pre_hostile_review/` |
| `submission/EPSL_submission_package_FINAL.zip` | pre-hostile-review package | moved to `archive/pre_hostile_review/` |
| `submission/EPSL_submission_package_FINAL_HOSTILE_REVIEWED.zip` | superseded by hard-code-audited package | moved to `archive/pre_hostile_review/` |
| `manuscript/fig2/4/5/6*.png` | STALE: differed byte-wise from `analysis/figures/` canonical PNGs | refreshed from `analysis/figures/` |
| `tables/` copies of `api_montecarlo.csv`, `asynchronous_persistence_index.csv` | deleted metric files | deleted (previous pass) |
| `tables/energy_architecture.csv` | stale (`dom=stellar` for all bodies) | replaced by canonical derived CSV (previous pass) |
| `figures/` top-level copies | matched canonical after refresh | verified byte-identical |

## Verified NOT stale
- `analysis/derived/*` — all regenerated this session; byte-identical on re-run.
- `data/processed/*` — regenerated; Io E4 row carries new ontology; byte-identical on re-run.
- `manuscript/EPSL_main_manuscript.docx`, `EPSL_supplement.docx`, `cover_letter.docx`,
  `highlights.txt`, `EPSL_main_manuscript_inline.docx` — regenerated post-fix.
- `data/processed/body_attributes.json` — unchanged inputs.
- `literature/*.csv` — reference audit and novelty matrix (unchanged, still current).
- `reports/*` — historical reports retained as documents (do not feed the pipeline).

## Notes
- The archive directory is clearly marked `pre_hostile_review/`; nothing in the pipeline
  reads from it.
- Old review/QC reports (`HOSTILE_REVIEW.md`, `DATA_QC.md`, etc.) remain as history;
  the one live QC statement affected ("32 of 56") is corrected in DATA_QC.md.

## Post-expansion stale scan (2026-10-22)
Submission package rebuilt as EPSL_submission_package_FINAL_NO_SUPPLEMENT.zip (14 files: FINAL docx/pdf, FINAL inline docx/pdf, cover letter, highlights, figures/). Prior FINAL-named artifacts and the supplement files moved to archive/pre_no_supplement/. No stale "32/56", "95%", or pre-Io-fix numbers appear in the regenerated manuscript (grep-verified). PASS.

## Update 2026-10-22/24 (evidence-bundle pass)
Earlier mirror-lag residual CLOSED: public HEAD advanced ab2bb9e → 6495cdb8
(2026-10-22 15:28 sync); public submission zip is byte-identical to the
canonical FINAL_10GATE_AUDITED zip. No stale public revision remains.
