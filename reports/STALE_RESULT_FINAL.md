# STALE-RESULT AUDIT — FINAL (10-gate QC, Gate 2)

## Checks run (this session, same VM)
1. `data/processed/*` and `analysis/derived/*` timestamps vs the manuscript
   build time — derived artifacts regenerated after the last code change;
   no derived file older than the script that produces it.
2. Re-verified every reported number against the live JSON/CSV outputs
   (result_traceability_final.csv): all match.
3. Stale artifacts on disk:
   - `archive/pre_no_supplement/` — prior zip + supplement files (quarantined, out of package).
   - `archive/pre_hostile_review/` — pre-review docx/zip (quarantined).
   - `submission/EPSL_submission_package_FINAL.zip` (older lineage zip) — superseded;
     the current package is `EPSL_submission_package_FINAL_NO_SUPPLEMENT.zip`.
   - `manuscript/EPSL_supplement.docx/.pdf` — removed from the manuscript dir earlier;
     supplement section deleted from build script (public clone still carries the
     old files — public mirror is one sync cycle behind; see PUBLIC_REPRO_FINAL.md).
4. Abstract word count re-verified after trim: 247 words (was 299 > 250 cap) —
   the NO_SUPPLEMENT zip was rebuilt after the trim so the archived docx matches.

## Known STALE exposure
- Public mirror `bougtoir/planetary_circulation` HEAD (audit time) = ab2bb9e
  (2026-10-17), i.e. the pre-expansion tree with supplement files. The wip sync
  branch is pushed; mirror updates on the hourly cron (manual dispatch not
  permitted by token). Recorded as a residual issue in the readiness table, not
  hidden: the data-availability statement becomes fully true on next sync.

## Disposition
**PASS with one recorded residual (public mirror lag, self-healing on next cron).**
