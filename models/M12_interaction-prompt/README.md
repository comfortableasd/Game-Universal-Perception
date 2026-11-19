# M12 — Interaction Prompt

## Objective
Detect interaction prompts, keyboard/controller glyphs and action labels; classify interaction type.

## Applicable game families and examples
FPS, TPS, RPG, adventure, survival and puzzle. Examples: Cyberpunk 2077, RDR2, Resident Evil 4, Skyrim, Portal 2, Subnautica.

## Proposed baseline
Prompt detector + OCR + glyph classifier + state tracking.

## Label scope
Define positive, negative, ambiguous, occluded, absent and not-applicable states. Keep visual observations separate from hidden game state or player input.

## Evaluation
Precision/recall and action-label exact match; distinguish prompt visibility from successful interaction.

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
