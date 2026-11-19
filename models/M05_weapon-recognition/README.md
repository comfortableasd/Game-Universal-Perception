# M05 — Weapon Recognition

## Objective
Detect first-/third-person weapons and classify weapon families or game-specific variants.

## Applicable game families and examples
FPS, TPS, survival shooters and shooter RPGs. Examples: Borderlands 3, Metro Exodus, Far Cry 6, GTA V, Rust, Cyberpunk 2077.

## Proposed baseline
Detection + DINOv3 embeddings + hierarchical category classifier.

## Label scope
Define positive, negative, ambiguous, occluded, absent and not-applicable states. Keep visual observations separate from hidden game state or player input.

## Evaluation
Per-game macro-F1 and AP; separate weapon-family recognition from exact model identification.

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
