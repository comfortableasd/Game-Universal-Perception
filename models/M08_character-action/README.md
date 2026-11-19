# M08 — Character Action

## Objective
Recognize attack, heavy attack, dodge, block, parry, jump, run, hit reaction and fall.

## Applicable game families and examples
TPS, action RPG, fighting, sports and selected FPS. Examples: Sekiro, Black Myth: Wukong, God of War Ragnarök, Tekken 8, NBA 2K.

## Proposed baseline
Video encoder + temporal head; pose/hand cues where useful.

## Label scope
Define positive, negative, ambiguous, occluded, absent and not-applicable states. Keep visual observations separate from hidden game state or player input.

## Evaluation
Macro-F1, per-class recall and temporal boundaries; first-person hand actions are a separate domain.

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
