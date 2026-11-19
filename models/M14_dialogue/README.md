# M14 — Dialogue & Subtitle

## Objective
Read dialogue/subtitles, speaker labels, choice options and selected choice.

## Applicable game families and examples
RPG, narrative adventure, open-world and strategy. Examples: Baldur's Gate 3, Detroit: Become Human, Cyberpunk 2077, The Witcher 3, Mass Effect.

## Proposed baseline
Panel detection + OCR + text tracking + choice-state classifier.

## Label scope
Define positive, negative, ambiguous, occluded, absent and not-applicable states. Keep visual observations separate from hidden game state or player input.

## Evaluation
CER, choice exact match and speaker accuracy; support languages explicitly.

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
