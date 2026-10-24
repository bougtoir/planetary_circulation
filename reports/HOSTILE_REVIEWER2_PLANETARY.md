# HOSTILE REVIEWER 2 — planetary science & ontology
Date: 2026-10-17 (UTC). All 20 commissioning attack points.

| # | Attack | Severity | Disposition |
|---|--------|----------|-------------|
| 1 | Reservoir ontology arbitrary | MODERATE | Declared instrument; structural absence is treated as signal (§1). Seven reservoirs cover the transport routes used in comparative planetology. Retained. |
| 2 | Process ontology arbitrary | MODERATE | E1–E7 is coarse but complete for inter-reservoir circulation; stated as analysis choice. Retained. |
| 3 | E1/E4 overlap | **MAJOR→FIXED** | Io's asthenosphere/partial-melt layer was coded under E4 ("Subsurface Liquid"), mixing silicate melt into a volatile-liquid node already covered by E1 (interior→surface magmatic transport). Fix: E4 restricted to persistent/semi-persistent subsurface *volatile* reservoirs (water ocean, groundwater, brine, methane/ethane liquid); Io's melt-layer evidence mapped to E1 (already direct_active, Khurana et al. 2011 kept as supporting ref); Io E4 → structurally_absent. |
| 4 | E3/E5 overlap | MODERATE | Both link Surface↔Atmosphere but are physically distinct directions (exchange vs deposition); network aggregation keeps all contributing processes per link. Retained, now explicit in Methods. |
| 5 | E7 too broad | MODERATE | "Chemical/redox recycling" spans sulfur (Io), SO2 (Venus), perchlorate (Mars), photosynthesis (Earth). Heterogeneous but coded as *evidence of ongoing chemical cycling*, which is the comparable construct. Retained as limitation. |
| 6 | Dynamo as state vs edge | MINOR | Deliberate design (Methods states dynamo is an internal-state observable, not an edge); applied consistently. |
| 7 | Induced vs intrinsic fields | MINOR | Europa's induction correctly excluded from dynamo evidence (Kivelson 2000 cited). |
| 8 | Venus "lacks" E4 by definition | MODERATE | Correct: no subsurface volatile reservoir at 740 K surface; structural absence is architecture, not missing data. |
| 9 | Mars E4 active/probable/paleo | MODERATE | Coded probable_active on InSight seismic inference (Wright et al. 2024); polar basal-liquid claims flagged as disputed in the cell note. Defensible. |
| 10 | Europa plume evidence contested | MODERATE | Kept at probable/O1–O2, explicitly awaiting JUICE/Clipper (limitations §4). |
| 11 | Titan cryovolcanism overcalled | MODERATE | Kept at probable (morphology disputed; Sotin 2005 evidence flagged). |
| 12 | Io chemistry vs terrestrial redox | MODERATE | Sulfur allotrope/photolytic cycling is a real material cycle; coded residual/C/O1 — the weakest supported state, appropriately hedged. |
| 13 | "Residual activity" consistent | MINOR | Defined (weak ongoing expression); applied to Moon/Mercury contraction, Venus E3, Io E7. |
| 14 | "Current" across geological vs atmospheric timescales | MAJOR (irreducible) | Genuine ambiguity: atmospheric cycles are instantaneous-active, geological ones integrate ~Myr evidence. Mitigated by persistence being a separate axis; stated limitation. |
| 15 | Geological vs direct observation mixing | MAJOR→CALIBRATED | Evidence-state codes distinguish direct vs indirect/model via `evidence_types`; Fig. 2 letters show state, tier column shows constraint quality. Calibrated. |
| 16 | Cherry-picked bodies | MODERATE | Frozen a priori for architectural diversity (Methods); not tuned post hoc. |
| 17 | Excluding Enceladus biases conclusions | MODERATE | Would strengthen outer-Solar-System claims; acknowledged explicitly as the natural extension test (§4). Retained as limitation. |
| 18 | Earth dominates framework | MINOR | Earth is a row, not a normalizer; LOO-PCA shows structure survives Earth's removal. |
| 19 | Too many satellites vs planets | MINOR | 3 planets + 5 satellites; satellites carry the ocean-world cases the ontology must span. Frozen and justified in Methods. |
| 20 | Survival of extension to Enceladus/Ganymede/Callisto/Ceres/Triton/Pluto | MODERATE | Ontology accommodates all six (all have definable E4 status; Triton/Pluto add cryovolcanic E1); stated as future test, not claimed. |

## Judgement on the augmentation-gap paragraph
Survives hostile review only as a Discussion paragraph — it is speculative for EPSL but
bounded and clearly future-tense. **Kept, unchanged in position, not expanded.**

## Reviewer-2 verdict
The E4 ontology defect was the only major correctness issue; fixed by the volatile-reservoir
definition. Residual majors (14, 15) are inherent to comparative planetology and are stated
limits, not hidden.
