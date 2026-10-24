# FINAL 10-GATE QC REPORT — EPSL submission (planetary circulation)

Artifact: `submission/EPSL_submission_package_FINAL_10GATE_AUDITED.zip`
SHA-256 `a813a52cc73dc81ca8dbbd4f08ad29fe0a2b472e4d85d41420e1658f4cacca8f`.
Wip commit `de2ab26d`; public HEAD `6495cdb8`.

| Gate | Status | Evidence report | Exact evidence | Open issue |
|---|---|---|---|---|
| 1 Hostile review | PASS | HOSTILE_REVIEW_SYNTHESIS.md + 5 FINAL components | 0 FATAL/MAJOR; hedged MODERATE×2, MINOR×2 | none blocking |
| 2 Hard-code/stale | PASS | HARDCODE_AUDIT.md + result_traceability.csv (19 rows) | 0 untraceable reportable values; literals are cited inputs | none |
| 3 Public reproduction | PASS | PUBLIC_REPRODUCIBILITY_AUDIT.md | fresh clone HEAD 6495cdb8; 6/6 stages OK; outputs byte-identical or ≤4.4e-16; zip byte-identical | none |
| 4 Reference existence | PASS | REFERENCE_EXISTENCE_AUDIT.md + reference_audit.csv | 60/60 verified via Crossref/publisher; 60/60 cited & claim-supported | none |
| 5 Bidirectional citations | PASS | CITATION_BIDIRECTIONAL_AUDIT.md + csv | 60 listed; 0 orphans; 0 unmatched | none |
| 6 Figure/table order | PASS | FIGURE_TABLE_CITATION_AUDIT.md | 6 figs all cited, sequential first-mention (paras 12,23,25,27,29,33); 0 tables; ≤10 cap | none |
| 7 Numeric consistency | PASS | DATA_TEXT_FIGURE_AUDIT.md | all values match derived outputs within declared rounding | cosmetic Fig.3 Mars/Io label overlap |
| 8 OMML | NOT APPLICABLE | WORD_FORMAT_AUDIT.md §OMML | 0 oMath elements; no equations requiring OMML (evidence recorded) | — |
| 9 Asterisk remnants | PASS | WORD_FORMAT_AUDIT.md §asterisks | 0 literal `*` across all docx story parts | none |
| 10 Grid/line spacing | PASS | WORD_FORMAT_AUDIT.md §grid | docGrid linePitch=360 is layout declaration only; snapToGrid absent; rendered PDF clean | none |
