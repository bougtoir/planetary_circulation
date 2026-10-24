# HOSTILE PLANETARY-SCIENCE / ONTOLOGY REVIEW — FINAL (10-gate QC, Gate 1)

## P1. E4 ontology — "subsurface" ambiguity (Io melt layer)
- Resolved earlier and re-verified: E4 codes only *volatile* subsurface reservoirs.
  Io's silicate melt layer is E1 (internal heat/engine activity) evidence;
  Io E4 = structurally_absent. Supported count Io = 6 (was 7 pre-fix).
- Manuscript states this convention explicitly. Disposition: **cleared.**

## P2. Process-class boundary conventions (E1–E7)
- Three named borderline conventions declared in Methods
  (e.g., dynamo as internal-state observable, not an edge; Io melt → E1).
- No hidden coding decisions discovered in the audit of `build_data.py` /
  `derive_matrices.py` coding dicts — they match the text.
- Disposition: **cleared.**

## P3. Body selection — "why these 8?"
- Rationale in Methods (terrestrial planets + geologically characterized satellites,
  spanning radiogenic, tidal, and stellar-dominated engines; DeMets/Anderson/Peale/
  Kivelson/Stofan/Horst cited for the cases).
- An editor may still ask "why not Enceladus/Callisto?" — text acknowledges the
  observability axis exists precisely for that: poorly characterized bodies score
  low on tier A–C coverage rather than being silently excluded.
- Disposition: **cleared — MODERATE(negative), framing defensible.**

## P4. Dated cessation values
- Mars ~4.1 Ga, Moon ~1.0–3.5 Ga band, Venus inferred-not-dated — all literature-
  sourced literals (Langseth/Tarduno/Lillis/Vervelidou/Weiss/Mighani), consistent
  with refs now in the 60-item bibliography.
- Disposition: **cleared.**

## P5. Energy-source table (dom_driver)
- `dom_driver` = dominant circulation-driving energy source; stellar-dominated
  mislabeling resolved. Fig. 6 reads the canonical `dom_driver` mapping.
- Disposition: **cleared.**

## P6. Habitability paragraph scope
- ~150-word bounded paragraph; no astrobiology over-claim (E7 is *potential*,
  not occurrence). Hand/Horst citations support the framing.
- Disposition: **cleared.**

## P7. "Circulation" definition stretched beyond atmospheres?
- Ontology figure (Fig. 1) and Intro define circulation as mass/energy exchange
  across the 7-reservoir architecture — internal convection included by design.
  A purist could object the term usually denotes fluid envelopes; the manuscript
  states its generalization up front rather than smuggling it.
- Disposition: **cleared — MINOR(negative), declared definition.**

## Reviewer verdict (simulated)
No FATAL/MAJOR. Ontology is self-consistent and conventions are declared.
**Gate-1 (planetary/ontology) disposition: PASS**
