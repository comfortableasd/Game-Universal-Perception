# M18 — Rhythm Recognition

## Objective
Detect notes, lanes, hit lines, judgments, combo and timing events.

## Applicable game families and examples
Rhythm games and rhythm-based modes. Examples: Beat Saber, DJMAX, Muse Dash, osu!, Taiko no Tatsujin.

## Proposed baseline
Real-time note detector + lane geometry + temporal event matching.

## Label scope
Define positive, negative, ambiguous, occluded, absent and not-applicable states. Keep visual observations separate from hidden game state or player input.

## Evaluation
Event F1 and timing error in ms; evaluate each game mode and speed.

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
