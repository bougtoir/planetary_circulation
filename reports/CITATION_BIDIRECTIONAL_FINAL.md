# BIDIRECTIONAL CITATION AUDIT — FINAL (10-gate QC, Gate 5)

Target: `submission/EPSL_main_manuscript_FINAL.docx` (the actual submission docx,
not markdown). Machine table: `reports/citation_bidirectional_final.csv`.

## Method
- Parsed the docx: split body vs References section; extracted 60 list entries.
- Extracted every in-text citation (both `(Author, year)` parenthetical —
  including `Author and Author` two-part names and multi-part `et al.` — and
  narrative `Author (year)` / `Author et al. (year)` forms).
- Both directions checked.

## Result
- References listed: **60** (incl. one lowercase-initial "de Pater" entry — counts toward the 60)
- In-text citation pairs found: all resolve to a listed entry
- Orphans (listed, never cited): **0** — earlier candidate misses
  (Banerdt, Vaucher, Way & Del Genio) were matcher artifacts; each is cited
  in body text.
- Missing (cited, not listed): **0**
- Reference count vs EPSL cap (≤70): **60 ≤ 70 ✓**

## Disposition
**PASS — bidirectional closure, 0 orphans / 0 missing on the final docx.**
