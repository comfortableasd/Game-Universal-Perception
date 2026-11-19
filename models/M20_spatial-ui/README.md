# M20 — Spatial UI

## Objective
Detect and associate world-anchored bars, labels, markers, names and distance indicators with entities.

## Applicable game families and examples
TPS, RPG, MMORPG, action and survival. Examples: Horizon Forbidden West, Monster Hunter, The Witcher 3, ARK, Elden Ring.

## Proposed baseline
UI detector + entity association + multi-object tracking.

## Label scope
Define positive, negative, ambiguous, occluded, absent and not-applicable states. Keep visual observations separate from hidden game state or player input.

## Evaluation
Detection recall, association accuracy and track consistency; distinguish screen HUD from world-space UI.

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
