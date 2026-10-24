# ASTERISK / FORMATTING-REMNANT SCAN — FINAL (10-gate QC, Gate 9)

## Method
Scanned every XML story part of both submission docx files
(`EPSL_main_manuscript_FINAL.docx`, `EPSL_main_manuscript_FINAL_inline.docx`):
document.xml, headers, footers, footnotes, endnotes, styles — literal `*` count.

## Result
- Literal `*` in document.xml (both files): **0**
- Literal `*` in ANY XML story part (both files): **0**
- No markdown remnants (`**`, `*…*`, `##`, backticks) in paragraph text
  (markdown-style emphasis is not used by the builder; italics are real run properties).
- No strikethrough/underline runs (EPSL constraint) — checked via run properties.

## Disposition
**PASS — zero asterisk/formatting remnants across all docx story parts.**
