# M13 — Inventory

## Objective
Parse item grids, equipment slots, item classes, stack quantities and selected item state.

## Applicable game families and examples
RPG, survival, horror and management. Examples: Resident Evil 4, Escape from Tarkov, Rust, ARK, Diablo IV, Baldur's Gate 3.

## Proposed baseline
Grid/layout parsing + item detector/classifier + OCR.

## Label scope
Define positive, negative, ambiguous, occluded, absent and not-applicable states. Keep visual observations separate from hidden game state or player input.

## Evaluation
Item macro-F1, slot localization and quantity exact match; game-specific item ontology is an adapter.

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
