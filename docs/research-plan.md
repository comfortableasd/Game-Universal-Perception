# Research Plan

## Research question
Can reusable visual encoders and task heads recognize functionally equivalent game UI and gameplay events in games excluded from training?

## Hypotheses
1. Pretrained spatial features reduce per-game annotation needs for UI localization and icon matching.
2. Task-specific heads outperform a monolithic classifier on heterogeneous tasks.
3. Temporal features improve firing, reload, action and state-transition detection.
4. Geometry, OCR and explicit state constraints improve structured HUD reliability.
5. Leave-one-game-out tests reveal domain gaps hidden by random frame splits.

## Workstreams
Taxonomy; visual representation; temporal modeling; data provenance and annotation; cross-game evaluation; deployment and runtime scheduling.

## Experimental discipline
Record dataset version, game/version, split, input resolution, model/checkpoint hash, preprocessing, thresholds, hardware and software. Targets are not results. Never claim universal accuracy from a finite benchmark.
