# EPSL FINAL READINESS — planetary circulation manuscript

## Artifact identity
- Submission ZIP: `submission/EPSL_submission_package_FINAL_10GATE_AUDITED.zip`
- ZIP SHA-256: `a813a52cc73dc81ca8dbbd4f08ad29fe0a2b472e4d85d41420e1658f4cacca8f`
- Wip commit: `de2ab26ddf01beb03fcc4f1030464c06aca8609b` (PR bougtoir/wip#696)
- Public repo: https://github.com/bougtoir/planetary_circulation
- Public HEAD: `6495cdb8f3d0dbe68ec3ea6ef1e97e825f0ba749` (current revision; public zip byte-identical to canonical zip)

## Format facts
- Main-text words: ~4,515 (EPSL cap 6,500); Abstract: 247 (cap 250)
- Bibliography: 60 entries (cap 70); 0 orphans, 0 unmatched citations
- Figures: 6; Tables: 0; combined 6 ≤ 10 cap
- Highlights: separate file, 5 bullets ≤82 chars (cap 85, "highlights" in name)
- Supplement: **none** (not required by EPSL; provenance lives in Methods + repo)
- Data availability: Option C — public repository (verified reachable + reproducing)
- Remaining author-only fields: `[TO COMPLETE]` placeholders for author names,
  affiliations, and corresponding-author email on the title page (author fills).

## Public regeneration
Fresh clone `/tmp/pc_fresh` at public HEAD 6495cdb8 ran the documented
6-stage pipeline cleanly; derived outputs matched THIS submission (byte-identical
for MC/network/coverage artifacts; ≤4.4e-16 float noise on pca_loo/analysis_summary;
manuscript docx text identical; submission zip byte-identical).

## Gate results
1. Hostile review — PASS (0 FATAL/MAJOR)
2. Hard-code/stale — PASS (0 untraceable values)
3. Public reproduction — PASS (public HEAD current; byte-identical zip)
4. Reference existence — PASS (60/60)
5. Bidirectional citations — PASS (0/0)
6. Figure/table order — PASS (6 figs, sequential; 0 tables)
7. Numeric consistency — PASS
8. OMML — NOT APPLICABLE (no equations; evidence recorded)
9. Asterisk remnants — PASS (0)
10. Grid/line spacing — PASS (docGrid benign; snapToGrid absent)

Non-scientific residuals: author fills `[TO COMPLETE]` title-page fields;
optional cosmetic Fig.3 label overlap.

## Final decision
**READY** — every applicable gate PASSes, Gate 8 recorded NOT APPLICABLE with
evidence, and the only remaining items are non-scientific author-completion
fields and one cosmetic label note.
