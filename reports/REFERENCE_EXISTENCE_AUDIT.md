# REFERENCE EXISTENCE AND CLAIM SUPPORT (Gate 4) — current artifact

Input: `submission/EPSL_main_manuscript_FINAL.docx` References section
(60 entries, incl. one lowercase-initial "de Pater" entry — counted).
Row-level table: `reports/reference_audit.csv` (60 rows; columns:
reference, first_author, exists, main_text_cited, claim_support, context).

## Method
Each entry checked against Crossref (`api.crossref.org/works/{doi}`) and/or
publisher records; citation contexts checked for claim support during the
expansion-phase audit and re-validated for this gate on the current docx.

## Result
- Verified exists: **60/60** — DOI or stable publisher record resolved for every item.
- main_text_cited: 60/60 PASS (see Gate 5 bidirectional table).
- claim_support: 60/60 PASS.
- Unverifiable references: none. Metadata discrepancies: none recorded.
- Fabricated references: 0.

## Gate-4 status: PASS — 60/60 verified.
