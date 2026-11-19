# M07 — Reload Recognition

## Objective
Detect reload start, phases, completion, magazine swap and per-round loading where visible.

## Applicable game families and examples
FPS, TPS and survival shooters. Examples: Metro Exodus, Far Cry 6, Borderlands 3, The Division 2, Rust.

## Proposed baseline
Weapon ROI + temporal classifier/TCN + optional ammo HUD evidence.

## Label scope
Define positive, negative, ambiguous, occluded, absent and not-applicable states. Keep visual observations separate from hidden game state or player input.

## Evaluation
Event F1 and boundary error; distinguish reload, weapon switch and inspect animations.

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
