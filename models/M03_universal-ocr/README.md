# M03 — Universal OCR

## Objective
Read digits and text in ammo, timers, scores, resources, speed, levels and other HUD fields.

## Applicable game families and examples
Nearly all UI-rich genres: FPS, RPG, MOBA, RTS, racing, sports, simulation and strategy.

## Proposed baseline
Text/region detection + OCR recognizer + field-specific parser and temporal validation.

## Label scope
Define positive, negative, ambiguous, occluded, absent and not-applicable states. Keep visual observations separate from hidden game state or player input.

## Evaluation
CER, exact sequence match and field accuracy; report language/font/scale subsets.

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
