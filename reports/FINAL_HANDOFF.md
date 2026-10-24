# FINAL HANDOFF — planetary circulation network paper (EPSL)

Working tree: `wip/planetary_circulation/` (branch `devin/1790413216-planetary-circulation`)
Public mirror target: `bougtoir/planetary_circulation` via `.github/workflows/sync-to-repos.yml`
(BRANCH_MAP / SUBDIR_MAP entries added).

## What was produced

A complete EPSL submission package testing whether planetary dynamical states are better
represented as heterogeneous architectures of coupled circulation processes than as a single
active/inactive scalar. Eight bodies (Earth, Venus, Mars, Moon, Mercury, Io, Europa, Titan)
× seven edge classes (E1–E7) → three matrices (activity, persistence, observability),
plus ordination, persistence spectra with Monte Carlo over dating intervals, per-body
reservoir networks, and an energy-architecture null comparison.

## Headline results

1. **Asynchronous persistence**: Mars (spread 0.91) and Mercury (0.78) show strongly
   asynchronous subsystem cessation; Earth/Io/Europa/Titan sit at ~0 (everything running).
   "Planetary shutdown is not a point event."
2. **Architecture ≠ bulk properties**: activity counts correlate ~0 with age (ρ=−0.04,
   p=0.92) and only weakly/non-significantly with mass (ρ=0.35, p=0.40); energy-source
   geometry (tidal vs. radiogenic vs. stellar) organizes the coupling.
3. **Dominant gradient + genuine multidimensionality**: PC1 ≈ 56% of ordinal-matrix variance
   (robust under leave-one-body-out), ~44% residual structure — so a scalar summary is a
   first approximation, not the full picture.

## Key files

- Manuscript: `manuscript/EPSL_main_manuscript.docx/.pdf` (~1,830 words main text; 6 figures)
- Supplement: `manuscript/EPSL_supplement.docx/.pdf` (methods detail, full 56-cell table,
  LOO and Monte Carlo tables)
- `manuscript/highlights.txt` (5 bullets), `manuscript/cover_letter.docx`
- Data: `data/planetary_circulation_master.csv` (56 cells, per-cell tier/status/observability/
  persistence/reference), `data/measurement_dictionary.csv`, matrices CSVs
- Code: `analysis/scripts/{build_data,derive_matrices,analyze,figures_1_5_6,build_manuscript}.py`
- Reports: `reports/{JOURNAL_REQUIREMENTS,STUDY_PROTOCOL,MEASUREMENT_DICTIONARY,COVERAGE_GATE,
  DATA_QC,NOVELTY_AUDIT,HOSTILE_REVIEW,EPSL_FIT_AUDIT,FINAL_AUDIT}.md`
- Package: `submission/EPSL_submission_package_FINAL.zip`

## To submit (author-side)

1. Fill `[TO COMPLETE]` placeholders: author list, affiliations, CRediT roles, corresponding author.
2. Optional graphical abstract.
3. Submit at Editorial Manager → article type "Letter". Fallback if desk-rejected on fit:
   JGR: Planets (no restructuring needed).

## Reproduce

```bash
cd planetary_circulation
python3 analysis/scripts/build_data.py
python3 analysis/scripts/derive_matrices.py
python3 analysis/scripts/analyze.py
python3 analysis/scripts/figures_1_5_6.py
python3 analysis/scripts/build_manuscript.py
soffice --headless --convert-to pdf --outdir manuscript manuscript/*.docx
```

Coverage gate result: **GO** (53/56 = 94.6% Tier A–C). Outcome grade: **A** (EPSL-ready,
placeholders pending).
