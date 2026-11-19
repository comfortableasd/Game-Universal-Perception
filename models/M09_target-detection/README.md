# M09 — Target Detection

## Objective
Detect enemies, allies, NPCs, bosses, units and interactive targets.

## Applicable game families and examples
FPS, TPS, RPG, MOBA, RTS and survival. Examples: DOOM, Horizon Forbidden West, The Witcher 3, Dota 2, StarCraft II, ARK.

## Proposed baseline
Object detector + tracking + HUD/marker relation cues.

## Label scope
Define positive, negative, ambiguous, occluded, absent and not-applicable states. Keep visual observations separate from hidden game state or player input.

## Evaluation
AP, per-class precision/recall and ID consistency; faction semantics need evidence.

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
