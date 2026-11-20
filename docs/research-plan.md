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

## Model design principle

Each Universal Model is a dedicated single-task model with its own ontology, training configuration, checkpoint, evaluation report and supported-game list. The goal is maximum generalization across games for that one task. Shared pretrained encoders and engineering components are allowed, but task-specific parameters remain independent unless experiments demonstrate that sharing does not reduce single-task performance.

## Audio workstream
Audio is a first-class modality with independently scoped A01–A13 models. Evaluate audio-only, visual-only and audiovisual association separately. Do not merge gunshot and reload audio into one task model.
