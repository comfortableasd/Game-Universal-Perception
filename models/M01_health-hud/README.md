# M01 — Universal Health HUD

## Objective
Locate and quantify player, enemy, boss and resource bars.

## Applicable game families and examples
FPS, TPS, ARPG/soulslike, MMORPG, MOBA, fighting, survival. Examples: DOOM Eternal, GTA V, Elden Ring, World of Warcraft, Dota 2, Street Fighter 6, Rust.

## Proposed baseline
Detection + segmentation + bar geometry; DINOv3 is an encoder candidate.

## Label scope
Define positive, negative, ambiguous, occluded, absent and not-applicable states. Keep visual observations separate from hidden game state or player input.

## Evaluation
Precision/recall, IoU, value MAE; distinguish HP from shield/stamina/mana/oxygen; UNKNOWN on occlusion.

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
