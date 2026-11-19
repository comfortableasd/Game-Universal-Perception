# M15 — Map Objects

## Objective
Detect units, buildings, markers, resources, routes and regions within map interfaces.

## Applicable game families and examples
RTS, 4X, open-world, survival and racing. Examples: StarCraft II, Age of Empires IV, Civilization VI, GTA V, ARK, Forza Horizon 5.

## Proposed baseline
Map ROI segmentation + icon/object detection + coordinate transforms.

## Label scope
Define positive, negative, ambiguous, occluded, absent and not-applicable states. Keep visual observations separate from hidden game state or player input.

## Evaluation
AP and localization error; map symbols require a documented ontology.

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
