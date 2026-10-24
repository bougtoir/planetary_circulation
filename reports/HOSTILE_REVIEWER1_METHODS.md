# HOSTILE REVIEWER 1 — methods & statistics
Date: 2026-10-17 (UTC). Every numbered attack point from the commissioning prompt, with
severity and disposition.

| # | Criticism | Severity | Disposition |
|---|-----------|----------|-------------|
| 1 | PCA on standardized ordinal evidence states | MAJOR | Retain, calibrated: PCA labelled exploratory in text + caption; headline is off-axis residual (~44%), not a dimensionality proof. Latent-variable alternative acknowledged as limitation. |
| 2 | n = 8 | MAJOR (irreducible) | Retain as limitation; descriptive statistics only; LOO sensitivity reported; no predictive modelling. |
| 3 | Pseudo-quantification | MODERATE | Already mitigated: 32/56 cells carry published numbers or measured zeros; the rest carry evidence state only. Stated in Methods. |
| 4 | Coding of D/P/R/0/absent states | MODERATE | Vocabulary defined in Methods + STUDY_PROTOCOL; Fig. 2 shows all six states including "—". |
| 5 | Structural absence in ordination | MODERATE | Currently imputed by column median — now stated explicitly in Methods. Post-E4-fix, Io's E4 becomes absent and is imputed to the column median (3 = probable), so its ordination position is unaffected; documented. |
| 6 | Unknown / O0 cells distorting analysis | MODERATE | O0-tier cells are exactly the structural absences; observability is a separate data object so low observability cannot masquerade as inactivity. Kept. |
| 7 | Leave-one-body-out stability | MINOR | Reported (PC1 46–66%); no flagship-body domination. |
| 8 | 56% + 44% overinterpretation | MODERATE | Calibrated in §3.2 and §4: "indicating further structure, not a measurement of dimensionality". |
| 9 | Multiple persistence-spread definitions | **FATAL→FIXED** | Manuscript used range(max−min incl. censored); Supplement S4 used an IQR "API" giving Mars/Mercury ≈ 0 — an apparent contradiction. Fix: ONE statistic — the within-body persistence spread = max − min over dated cessations plus right-censored cells; Monte Carlo now samples that same statistic; IQR/API removed from the package. |
| 10 | Right censoring | MODERATE | Censored=1.0 shown with arrows in Fig. 4; active processes never assigned end dates. Consistent after revision. |
| 11 | Cessation-date uncertainty | MAJOR→FIXED | Intervals carried per cessation; MC draws within [lo,hi]. New defect found: Venus's dynamo "cessation" (~4.5 Ga) has no measured date — no paleofield was ever detected; it is an inference from absence. It previously generated spread = 0.99, silently contradicting "Mars/Mercury most spread". Fix: only *empirically dated* cessations enter the spread statistic; Venus's inferred dynamo loss remains in the spectrum figure, flagged as inferred. |
| 12 | Monte Carlo implementation | MAJOR→FIXED | Old MC computed IQR draws — a different statistic from the headline. Rewritten to sample the headline statistic (range spread) over cessation intervals, 4000 draws, median + 5–95% band. |
| 13 | Spearman with n = 8 | MINOR | Descriptive label kept; recomputed after Io count change (see DATA_TEXT_FIGURE_AUDIT). |
| 14 | Process count as outcome | MODERATE | Count of supported process classes is interpretable and matches H4's wording; kept as the headline descriptor rather than an abstract index. |
| 15 | Binary networks, heterogeneous edges | MODERATE | Edges are "supported process classes", not physical fluxes — now stated; multi-process links (E3/E5/E7→Surface–Atmosphere) aggregate with strongest evidence retained, not overwritten. |
| 16 | Incommensurate process classes | MODERATE | Acknowledged limitation; the claim is comparative architecture, not flux equivalence. Quantitative subset kept separate (§3.5). |
| 17 | Latent-variable model would be better | MINOR | Plausible but heavier machinery at n=8; retained as stated limitation. |
| 18 | Qualitative matrix is the real contribution | MINOR | Partially conceded — the matrix IS a contribution, but the falsifiable H-tests are what make it a Letter. Balanced framing retained. |
| 19 | Unnecessary p-values | MINOR | Only two p-values exist (age/mass nulls) and both are labelled descriptive; kept because they answer H4 directly. |
| 20 | Evidence tiers leaking into activity | MINOR | Status vocabulary excludes tier; coverage gate counts tiers separately; no leakage observed. |

## Newly discovered defect (not in the commissioning list)
- **Selective spread reporting.** `persistence_spread.csv` contains Venus = 0.991, the largest
  value in the sample, but the text reported only Mars/Mercury/Moon and claimed Mars/Mercury
  "most spread". This was an honest subset ("bodies that show any cessation") made false by
  the inferred Venus cessation. Fixed by the dated-cessation inclusion rule (see issue 11).

## Reviewer-1 verdict
One fatal-level inconsistency (metric mismatch + Venus) — corrected. Remaining majors are
calibrated limitations appropriate to a pilot Letter.
