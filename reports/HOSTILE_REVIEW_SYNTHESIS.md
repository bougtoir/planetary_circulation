# HOSTILE REVIEW SYNTHESIS (Gate 1) — current artifact

Input artifact: `submission/EPSL_submission_package_FINAL_10GATE_AUDITED.zip`
(SHA-256 a813a52c…, wip commit de2ab26d). Reviews re-scoped to THIS build:
~4,515-word main text, 247-word abstract, 60 refs, 6 figures, no supplement.
Component reviews: HOSTILE_EDITOR_FINAL.md, HOSTILE_METHODS_FINAL.md,
HOSTILE_PLANETARY_FINAL.md, NOVELTY_FINAL.md, HOSTILE_SYNTHESIS_FINAL.md.

## Panel verdicts (all on the current manuscript)
- Editor (desk reject): proceed to review; no FATAL/MAJOR.
- Reviewer 1 (statistics/methods): no standing FATAL/MAJOR.
- Reviewer 2 (planetary/ontology): no FATAL/MAJOR.
- Novelty / citation ecology: claim defensible; no prior triple-object framework found.

## Standing items (classified)
- FATAL: 0. MAJOR: 0.
- MODERATE (hedged, declared in text): E1–E7 boundary conventions (3 named
  borderline conventions in Methods); augmentation gap for poorly characterized
  bodies (short cautious Discussion paragraph; observability axis carries it).
- MINOR (hedged): n=8 ordination limits (descriptive-only wording, LOO reported);
  generalized "circulation" term (definition stated up front).

## Closed this review lineage (evidence)
- Persistence-statistic inconsistency (was MAJOR): single definition now —
  max−min over dated-cessation intervals, censored excluded; verified vs live
  outputs (Mars 0.911, Mercury 0.778, Moon 0.443; MC bands 0.91–0.92 /
  0.78–0.88 / 0.32–0.75, 4,000 draws).
- Venus dynamo inference contaminating statistics (was MAJOR): excluded from
  spread math, kept flagged in Fig. 4.
- "32 of 56 quantitative cells" untraceable literal (was MAJOR): corrected to
  canonical 10 via `coverage_stats.json` (dynamic injection).
- Stale "95% coverage" literal: replaced by dynamic 92.9% (52/56, 4 tier-D).
- Fig.6 dom vs dom_driver duplication: unified on canonical `dom_driver`.
- Abstract length vs official ≤250-word cap: trimmed 299→247.

## Numeric provenance / hard-code (required adversarial section)
All reportable numbers are f-string injected from derived artifacts in
`build_manuscript.py`; traceability verified in Gate 2
(HARDCODE_AUDIT.md + result_traceability.csv). Remaining literals are
literature-sourced input constants (cessation dates, coding dicts, MC seed).

## Gate-1 status: PASS
