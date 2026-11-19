# M04 — Minimap & Compass

## Objective
Localize minimap, player marker, north indicator and observable heading cues.

## Applicable game families and examples
FPS, TPS, open-world, racing, survival, RTS. Examples: GTA V, RDR2, Far Cry 6, Forza Horizon 5, Rust, StarCraft II.

## Proposed baseline
ROI detection + marker/keypoint detection + geometric angle estimation + temporal smoothing.

## Label scope
Define positive, negative, ambiguous, occluded, absent and not-applicable states. Keep visual observations separate from hidden game state or player input.

## Evaluation
Map localization recall and wrapped angular MAE; do not infer absolute north without a visual reference.

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
