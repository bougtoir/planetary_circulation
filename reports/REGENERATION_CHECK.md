# REGENERATION CHECK (one controlled test)
Date: 2026-10-17 (UTC).

## Procedure
1. Snapshot `data/processed/`, `analysis/derived/`, `manuscript/` to /tmp.
2. Rerun the full pipeline once:
   `build_data.py → derive_matrices.py → analyze.py → figures_1_5_6.py → build_manuscript.py`
3. Compare.

## Result
- `data/processed/` — **byte-identical** on every file (diff -r clean).
- `analysis/derived/` — **byte-identical** on every file (diff -r clean; MC seeded, deterministic).
- `manuscript/` docx — zip member payload bytes identical; only zip-container metadata
  (entry timestamps) differs between the two writes, as expected. Extracted paragraph/table
  text identical. `highlights.txt` byte-identical.

## Verdict
PASS — one clean rerun reproduces all submission-facing outputs with no numeric drift and
no manual intervention. The pipeline is deterministic (PCA/MC seeded via
`np.random.default_rng(7)`; LibreOffice PDF conversion deterministic per docx).

## Post-expansion regeneration (2026-10-22)
build_manuscript.py + build_inline.py re-run cleanly after the expansion and supplement removal; docx rebuilt, PDFs regenerated via soffice. The supplement-generation block was deleted and manuscript/EPSL_supplement.docx removed from the tree — a regen now produces no supplement artifact, matching the NO_SUPPLEMENT package. PASS.

## Update 2026-10-22/24 (evidence-bundle pass)
Full pipeline re-run on fresh PUBLIC clone `/tmp/pc_fresh` @ 6495cdb8: all 6
stages OK; derived artifacts byte-identical except pca_loo.csv (≤4.4e-16 BLAS
last-bit noise); manuscript docx text identical; submission zip byte-identical
to canonical. See PUBLIC_REPRODUCIBILITY_AUDIT.md.
