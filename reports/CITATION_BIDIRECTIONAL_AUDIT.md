# BIDIRECTIONAL MAIN-TEXT CITATIONS (Gate 5) — current artifact

Input: `submission/EPSL_main_manuscript_FINAL.docx` (the actual submission docx;
not markdown; bibliography section itself excluded from the citation corpus).
Machine table: `reports/citation_bidirectional_final.csv` (60 rows, all "cited").

## Method
- Split docx paragraphs at the "References" heading; parsed 60 list entries.
- Extracted all in-text citation forms: `(Author, year)` and
  `(Author and Author, year)` parentheticals (incl. multi-part `et al.`),
  narrative `Author (year)` / `Author et al. (year)`, and lowercase-name
  entries ("de Pater").
- Both directions checked: bibliography→text and text→bibliography.

## Result
- Bibliography total: **60**
- Unique cited works resolving to a listed entry: all in-text pairs resolve.
- Orphan references (listed, never cited): **0**
- Unmatched citations (cited, not listed): **0**
- Matcher notes: Banerdt, Vaucher, Way & Del Genio were verified manually —
  each is cited in body text (et-al./two-author forms).

## Gate-5 status: PASS — 0 orphans / 0 unmatched on the current docx.
