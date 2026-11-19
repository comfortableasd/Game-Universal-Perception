# M02 — Universal Skill Cooldown

## Objective
Recognize skill slots and distinguish visible, unlocked, cooling down, ready, resource-blocked and charged states.

## Applicable game families and examples
MOBA, MMORPG, ARPG, action RPG and selected TPS/FPS. Examples: League of Legends, Dota 2, FFXIV, Nioh 2, Hogwarts Legacy, Warframe.

## Proposed baseline
Icon localization/embedding + state classifier + OCR + temporal state machine.

## Label scope
Define positive, negative, ambiguous, occluded, absent and not-applicable states. Keep visual observations separate from hidden game state or player input.

## Evaluation
READY precision, macro-F1, timer MAE; icon visibility is not proof of readiness.

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
