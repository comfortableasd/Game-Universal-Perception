# M06 — Shooting Recognition

## Objective
Detect visible firing events and localize event boundaries; classify single, burst and automatic fire where observable.

## Applicable game families and examples
FPS, TPS and survival shooters. Examples: DOOM Eternal, Metro Exodus, Borderlands 3, GTA V, RDR2, Remnant II.

## Proposed baseline
Patch features + motion/frame differences + TCN or temporal Transformer.

## Label scope
Define positive, negative, ambiguous, occluded, absent and not-applicable states. Keep visual observations separate from hidden game state or player input.

## Evaluation
Event precision/recall/F1 and onset/offset error; visual firing is not hidden trigger input.

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
