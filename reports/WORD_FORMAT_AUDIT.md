# WORD FORMAT AUDIT (Gates 8–10) — current artifact

Inputs: `submission/EPSL_main_manuscript_FINAL.docx` and
`EPSL_main_manuscript_FINAL_inline.docx` (submission-facing docx XML, all parts).

## §OMML (Gate 8)
Evidence: `word/document.xml` scanned for `m:oMath`/`m:oMathPara` — count **0**
in both docx files. Inventory of mathematical content: all symbolic material
is inline editable text ("max − min persistence spread", "ρ = −0.1769,
p = 0.675", "52/56 = 92.9%"); there are no display equations and none requiring
OMML encoding. EPSL rule (JOURNAL_REQUIREMENTS.md): equations as editable text,
solidus for small fractions — satisfied by construction.
**Status: NOT APPLICABLE** (evidence recorded; zero OMML is not a failure here).

## §Asterisks / formatting remnants (Gate 9)
All XML story parts scanned (document, headers, footers, footnotes, endnotes,
styles, numbering): literal `*` count = **0** in both files; no `**`,
`*…*` markdown emphasis, backticks, or stray formatting markers in paragraph
text; no strikethrough/underline runs (EPSL constraint).
**Status: PASS.**

## §Character-grid / line spacing (Gate 10)
- `word/document.xml`: `w:docGrid` appears once in `sectPr` as
  `<w:docGrid w:linePitch="360"/>` — a page-layout declaration with no
  `type`/`charSpace` attribute, so it does NOT enable characters-per-line
  layout; it only declares a line-pitch grid that nothing snaps to.
- `w:snapToGrid`: 0 occurrences in document.xml and styles.xml — no style or
  run inherits grid snapping; effective line spacing is conventional
  paragraph spacing.
- `w:spacing`/`w:lineRule`: normal single-spacing rules from default styles;
  `eastAsia` font slots (73) are template font-fallbacks, not active grid layout.
- Rendered spot check: regenerated `EPSL_main_manuscript.pdf` pages show normal
  line spacing, no compression/overlap, captions and references render cleanly.
**Status: PASS.**
