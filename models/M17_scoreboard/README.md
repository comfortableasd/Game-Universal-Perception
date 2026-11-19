# M17 — Scoreboard

## Objective
Parse scores, ranks, rounds, kills, match timers and player rows.

## Applicable game families and examples
Sports, fighting, racing, FPS and strategy. Examples: EA SPORTS FC, NBA 2K, Street Fighter 6, Tekken 8, F1.

## Proposed baseline
Panel/table detection + OCR + row association + temporal tracking.

## Label scope
Define positive, negative, ambiguous, occluded, absent and not-applicable states. Keep visual observations separate from hidden game state or player input.

## Evaluation
Field exact match and row association accuracy; handle localization and layout variants.

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
