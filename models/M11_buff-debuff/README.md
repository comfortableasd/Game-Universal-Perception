# M11 — Buff/Debuff

## Objective
Recognize status icons, stacks, duration and state transitions.

## Applicable game families and examples
MMORPG, MOBA, ARPG, survival and action RPG. Examples: WoW, FFXIV, LoL, Diablo IV, Elden Ring, Black Desert.

## Proposed baseline
Icon detection/embedding + classifier + OCR + tracking.

## Label scope
Define positive, negative, ambiguous, occluded, absent and not-applicable states. Keep visual observations separate from hidden game state or player input.

## Evaluation
Macro-F1 and duration error; semantic mapping may be game-specific.

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
