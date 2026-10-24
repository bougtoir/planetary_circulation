# HOSTILE_REVIEW.md — Phase 11 (adversarial self-review as EPSL referee)

## Fatal? — verdicts

1. **Arbitrary ontology** — serious but survivable. The 7-reservoir/7-process ontology is a
   declared instrument; coverage gate passed at 94.6% and structural absences are signal, not
   noise. Manuscript states the ontology is an analysis choice and shows robustness to the
   E4-absence interpretation. *Calibrated, not fatal.*
2. **Incompatible quantities across bodies** — the quantitative subset is thin (heat flow,
   escape, magma rates unavailable for several bodies). Mitigation: quantitative subset and
   evidence-state matrix are kept separate; ordination is done on evidence states, which is
   explicitly labelled exploratory. *Calibrated.*
3. **Cherry-picked bodies** — frozen a priori for architectural diversity (contract). Stated
   in Methods; not tunable post hoc. *Defensible.*
4. **Earth-centric normalization** — none used; Earth is a row, not a denominator. *OK.*
5. **Observational bias** — genuinely dangerous: Moon has Apollo data, Europa contested
   plumes. Mitigation: the observability matrix is a separate data object and Tier/O classes
   are shown in Fig. 2; Mars volcanism is only "probable" despite heavy exploration, and
   Europa "probable" cells are observability-flagged, not activity-boosted. *Calibrated.*
6. **Mission-coverage bias** — same as (5); acknowledged as fundamental limit; O-classes
   reported per cell in Supplement. *Calibrated.*
7. **Inventory/flux confusion** — explicitly policed (DATA_QC, measurement dictionary).
8. **Pseudo-quantification** — avoided: 32/56 cells carry numbers, the rest carry state only.
9. **Age uncertainty** — cessation intervals used (e.g., Moon dynamo 1.0–3.5 Ga); Monte Carlo
   over intervals. *OK.*
10. **n = 8** — descriptive statistics + sensitivity only; no regression claims; Spearman
    nulls are illustrative. *Calibrated.*
11. **PCA overuse** — PCA is exploratory on ordinal evidence states; we report that PC1
    explains ~56% and do NOT claim proof of multidimensionality. *Calibrated.*
12. **Network metrics on tiny graphs** — we report only interpretable properties (supported
    process edges, components, LCC); no invented indices. *OK.*
13. **Circular reasoning** — checked: activity states entered independently of hypotheses;
    the framework can fail (GO gate could have failed).
14. **Novelty vs existing literature** — see NOVELTY_AUDIT; claims restricted to the common
    matrix + asynchronous-persistence test + connectivity descriptor.
15. **"Vitality" metaphor** — demoted to umbrella term; not an index; no ranking.
16. **"Planetary death" framing** — banished from claims; at most one careful phrase.
17. **Geological cessation overclaim** — youngest-unit ≠ cessation: Mars E1 coded probable
    (units <10 Ma but magma presence debated); Moon IMPs debated noted.
18. **Dynamo ≠ circulation** — enforced; dynamo used only as internal-state indicator in the
    persistence spectrum.
19. **Induced vs intrinsic fields** — Europa induction separated (Kivelson 2000).
20. **Current vs paleo conflation** — censored/ceased encoding enforced.

## Material changes made because of this review
- Reported PC1 ~56% as a *dominant-but-not-exclusive* gradient rather than either
  "one-dimensional" or "multidimensional" — the honest reading of the evidence-state data.
- Added process-edge support count (0–7) as the primary network descriptor instead of the
  more abstract fragmentation fraction.
- Europa/Titan cryovolcanism and plumes held at probable/O1–O2 throughout.

## Resulting headline claims allowed
1. A common reservoir/process ontology is operationalizable across 8 diverse bodies at 95%
   cell coverage.
2. Comparative dynamical state has a dominant activity gradient (~56% of evidence-state
   variance) but a substantial multidimensional residual (~44%); not reducible to one axis.
3. Within-body cessation is asynchronous on Mars/Mercury/Moon (persistence spreads 0.44–0.99
   of body age) vs synchronous persistence on Earth/Io/Europa/Titan.
4. Supported process-edge counts (4–7) and component structure differ among bodies in ways
   not predicted by age (Spearman rho ≈ −0.04) or mass (rho ≈ 0.35, n.s.).
