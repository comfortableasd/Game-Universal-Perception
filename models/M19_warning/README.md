# M19 — Warning Recognition

## Objective
Recognize explicit warnings such as low health, oxygen, ammo, resources, system failures and hazards.

## Applicable game families and examples
Any genre with explicit warning UI: Resident Evil, Subnautica, DOOM, Cities: Skylines II, Farming Simulator.

## Proposed baseline
Icon/text detection + OCR + temporal state machine.

## Label scope
Define positive, negative, ambiguous, occluded, absent and not-applicable states. Keep visual observations separate from hidden game state or player input.

## Evaluation
Precision/recall at operating point; do not infer danger without a visible cue.

## Implementation status
**Planned.** This directory contains a specification, not a trained model or validated game support claim.

## Required deliverables
- [ ] Versioned ontology and annotation guide
- [ ] Dataset manifest with provenance and license
- [ ] Reproducible baseline and config
- [ ] Same-game and held-out-game evaluation
- [ ] Per-game metrics and failure analysis
- [ ] Model card, latency and memory report
- [ ] Inference API and regression tests
