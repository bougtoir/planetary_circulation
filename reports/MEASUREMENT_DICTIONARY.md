# MEASUREMENT_DICTIONARY.md — Phase 2

Machine-readable dictionary: `data/processed/measurement_dictionary.csv` (56 rows, generated
by `analysis/scripts/derive_matrices.py` from the curated master table).

## Inventory vs flux discipline
- Ocean mass ≠ ocean circulation (Europa/Titan E4 carries state + observability, no flux).
- Atmospheric mass ≠ circulation (Venus E3 residual despite ~93 bar inventory).
- Magnetic field ≠ circulation flux (dynamo handled as internal-state observable only).
- Young terrain ≠ current activity (Europa/Titan young surfaces ⇒ probable, not direct).
- A precisely measured zero is Tier A (Moon/Mercury E1).

## Normalization choices
- Reservoir turnover (`flux/reservoir_size`) is used only where a defensible reservoir size and
  flux exist (Earth E3 hydrological turnover ≈ 496,000 km³/yr over ocean ≈ 1.335e9 km³ →
  ~2.7e-4/yr). Elsewhere the raw physical quantity plus units is preserved.
- No Earth-normalization of scores; Earth is one row of eight.

## Key interpretive conventions
- `structurally_absent` (Venus/Moon/Mercury E4; Moon E5) is distinguished from `unknown` —
  excluded from coverage denominators where noted but retained in tables for transparency.
- Europa induced magnetic response is coded `induced_magnetic_response`, NOT dynamo evidence.
- Contested detections (Europa plumes, Titan cryovolcanism) are `probable_active` at low
  confidence (O1–O2), never `direct_active`.
