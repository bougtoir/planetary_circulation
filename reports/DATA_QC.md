# DATA_QC.md — Phase 5

Checks applied to `data/processed/planetary_circulation_master.csv` (56 cells).

## Passed
- Units preserved verbatim in `current_activity_unit`; no cross-unit mixing in any analysis.
- Body radius/mass/age taken from standard values (NASA fact-sheet consistent); internally
  consistent across rows per body.
- Geological ages stored as Ga-before-present consistently (`last_major_activity_age_Gyr`);
  persistence fraction computed as (age − cessation)/age only for non-censored processes.
- Present-vs-paleo separated by `currently_active`/`right_censored` flags and by
  `current_activity_status` vocabulary.
- Intrinsic vs induced fields separated in `body_attributes.json`; Europa induction is not
  counted as dynamo evidence anywhere.
- Flux vs inventory: no inventory-only quantities are used as activity fluxes; cells lacking a
  comparable flux carry Tier C with empty quantitative fields.
- No invented values: quantitative_estimate is NA wherever no defensible published number
  exists (10 of 56 cells carry a quantitative estimate or a measured zero; corrected from
  a stale "32" during the 2026-10-17 hard-code audit).

## Known caveats recorded
- Venus dynamo persistence treated as ~0 (no detected intrinsic dynamo ever); coded as
  cessation interval 4.0–4.5 Ga for the internal-state indicator — flagged as an
  interpretation, not a measured cessation.
- Io E4 "subsurface liquid" = debated asthenospheric melt layer (Khurana 2011 induction),
  not a confirmed ocean; flagged in notes.
- Europa plumes and Titan cryovolcanism coded probable_active at O1–O2, reflecting contested
  status.
- Moon E5 coded none_detected rather than absent: no atmosphere exists, but the edge class
  ("atmosphere→surface deposition") is vacuous — noted as effectively structural.
- Heat-flow values mix measured (Earth/Mars/Moon/Io) and modelled (Venus/Mercury/Europa/Titan)
  — only used qualitatively in the energy-architecture comparison, never in the quantitative
  activity subset.

## Denominators
- Persistence fraction denominator = body age (Table of `body_age_Gyr`).
- Turnover rates used only where reservoir size exists (documented per cell in dictionary).
- No normalization to Earth anywhere.
