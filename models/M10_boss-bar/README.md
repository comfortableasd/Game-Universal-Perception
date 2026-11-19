# M10 — Boss Bar

## Objective
Detect boss bars, estimate values, read names and track phase/defeat transitions.

## Applicable game families and examples
Action RPG, soulslike, ARPG and selected shooters. Examples: Elden Ring, Sekiro, Lies of P, Black Myth: Wukong, Nioh 2.

## Proposed baseline
M01 bar features + OCR + temporal phase tracking.

## Label scope
Define positive, negative, ambiguous, occluded, absent and not-applicable states. Keep visual observations separate from hidden game state or player input.

## Evaluation
Recall, value MAE, phase/event F1; boss identity must not be inferred from bar shape alone.

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
