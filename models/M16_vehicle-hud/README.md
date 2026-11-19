# M16 — Vehicle HUD

## Objective
Read speed, RPM, gear, fuel, battery, temperature, damage and gauge state.

## Applicable game families and examples
Racing, driving simulation and selected open-world games. Examples: Forza Horizon 5, Gran Turismo 7, ACC, ETS2, BeamNG.drive.

## Proposed baseline
OCR + gauge/keypoint geometry + temporal filtering.

## Label scope
Define positive, negative, ambiguous, occluded, absent and not-applicable states. Keep visual observations separate from hidden game state or player input.

## Evaluation
Numeric exact match, gauge MAE and latency; separate metric/imperial units.

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
