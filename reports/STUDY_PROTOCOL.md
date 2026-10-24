# STUDY_PROTOCOL.md — frozen design (Phase 0)

Project: network framework for comparing circulation architectures across planetary bodies.
Target journal: EPSL (see JOURNAL_REQUIREMENTS.md).
Canonical tree: bougtoir/wip/planetary_circulation/ → synced public repo bougtoir/planetary_circulation.

## Core question
Are planetary dynamical states better represented as heterogeneous architectures of coupled
circulation processes than as a single scalar active/inactive state? The framework is a
hypothesis under test, not a premise.

## Frozen pilot body set (n = 8)
Earth (strongly coupled reference), Venus (atmosphere-rich, hydrology-poor terrestrial),
Mars (residual/intermediate terrestrial), Moon (low-current-circulation reference),
Mercury (small body retaining intrinsic dynamo), Io (tidal-magmatic extreme),
Europa (tidal/subsurface-ocean), Titan (atmosphere–surface condensable-fluid).
No additions to the primary set; extra bodies only as labelled exploratory validation.

## Frozen reservoir/node ontology (7)
Core; Mantle; Crust/Ice Shell; Subsurface Liquid; Surface; Atmosphere; Space.
Structural absence ≠ missing data — recorded explicitly per body.

## Frozen edge/process ontology (7)
E1 Interior→Surface (volcanism, cryovolcanism, magmatic transport, advective/conductive heat);
E2 Crust/Ice deformation & recycling (tectonics, faulting, seismic deformation, resurfacing);
E3 Surface↔Atmosphere (evap/cond/precip/sublim/degassing — NOT H2O-only; Titan CH4 included);
E4 Subsurface Liquid↔Crust/Ice/Surface (ocean–ice exchange, groundwater, brine, hydrothermal);
E5 Atmosphere→Surface deposition (aerosol, photochemical delivery, chemical precipitation);
E6 Planet→Space (escape, sputtering, volcanic/plasma loss);
E7 Chemical/redox recycling (mineral–fluid reactions, photochemistry, disequilibrium processing).
Body-specific processes map into this common ontology; no silent splitting.

## Dynamo rule
Magnetic dynamo is NOT a circulation edge; it is an internal-state observable. Separate
variables: intrinsic_magnetic_field, dynamo_evidence, remanent_magnetization_evidence,
induced_magnetic_response. Induced fields (e.g. Europa) are not intrinsic-dynamo evidence.

## Three distinct data objects
- A(body, process) — Current Activity Matrix (evidence for current activity).
- P(body, process) — Persistence Matrix; persistence_fraction = duration / body_age;
  still-active processes are right-censored, never assigned arbitrary end dates.
- O(body, process) — Observability Matrix; O0 none / O1 model-dependent or single indirect /
  O2 multiple independent indirect or strong paleo / O3 direct contemporary or strong
  quantitative measurement. Observability ≠ activity.

## Measurement tiers (per body×process cell)
A: direct quantitative measurement or strong contemporary quantitative constraint.
B: quantitative proxy or defensible physically based estimate.
C: state/evidence only, no comparable quantitative flux.
D: unconstrained for comparative purposes.
Tier ≠ activity; a well-measured near-zero is Tier A.

## Energy-source variables (per body)
primordial/internal residual heat; radiogenic; tidal; stellar. Quantitative where defensible;
else qualitative metadata — labels never converted to fake scores.

## No-fabrication rule
No invented values. Missing cells stay missing (state + tier + observability + evidence
recorded). Missingness beats invented precision.

## Hypotheses
H1 Multidimensionality — state not adequately represented by one latent scalar.
H2 Asynchronous persistence — within-body processes persist for different history fractions
beyond dating uncertainty.
H3 Network decoupling — bodies differ in connectivity, not only in process disappearance.
H4 Multiple energy architectures — architecture not reducible to age or internal heat alone.

## Null comparisons (descriptive, n=8 — no overfit regressions)
age alone; mass alone; internal-heat/heat-flow proxy alone; age+mass+dominant energy source.

## Coverage gate (Phase 3)
GO: ≥70% of 56 cells Tier A–C AND ≥5 bodies with ≥4 evaluable process classes.
CONDITIONAL GO: 50–70% → identify two weakest edge classes, minimal ontology consolidation only.
NO-GO: <50% or misleading overlap → pivot to framework/feasibility paper (outcome E).

## Analysis plan
- Activity: quantitative subset (6A) + evidence-state matrix for all cells (6B).
- Dimensionality: PCA/ordination on quantitative subset only; report explained variance,
  loadings; bootstrap + leave-one-body-out (Earth, Io, Titan, Europa); no predeclared PC1
  cutoff; no proof claims from small-sample PCA.
- Persistence: fractions with censoring + date-interval uncertainty; API = IQR of persistence
  fractions (exploratory, not headline unless robust); Monte Carlo over age intervals.
- Network: binary/evidence networks per body; edges, density, components, LCC, fragmentation;
  weighted networks only where weights commensurate; modularity exploratory only.
- Energy: internally/radiogenic vs tidal vs stellar vs mixed; test monotonic age→weak
  trajectory; no causal claims from cross-sectional data.

## Robustness (mandatory)
leave-Earth/Io/Europa/Titan-out; direct-evidence-only subset; Tier-C removal; persistence-date
uncertainty; alternative normalizations. Material changes reported prominently.

## Output contract
manuscript/ (docx+pdf main, supplement, highlights.txt, cover_letter.docx, graphical abstract),
figures/, tables/, data/ (measurement_dictionary + master + 3 matrices), analysis/,
literature/ (novelty_matrix, reference_audit), reports/ (this file + JOURNAL_REQUIREMENTS,
NOVELTY_AUDIT, COVERAGE_GATE, DATA_QC, HOSTILE_REVIEW, EPSL_FIT_AUDIT, FINAL_AUDIT,
FINAL_HANDOFF), submission/EPSL_submission_package_FINAL.zip.

## Source hierarchy
PDS/mission archives > USGS products > other official mission products > primary papers >
peer-reviewed reviews. Outreach pages for discovery only. Every numeric claim keeps unit,
epoch, uncertainty, observed-vs-inferred, exact source.

## Deviations recorded here
(none yet — will be appended)
