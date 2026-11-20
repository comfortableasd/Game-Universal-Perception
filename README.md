# Game Universal Perception (GUP)

**A cross-game visual perception framework for video games.**

GUP is an open-source research and engineering project that studies reusable visual models for understanding gameplay across different games, genres, HUD designs, resolutions, and visual styles.

> **Research status:** GUP is a planned framework and benchmark. The model catalogue and targets in this repository are specifications, not claims of achieved performance. No universal 100% accuracy guarantee is made.

## Project goals

- Build reusable visual perception tasks rather than one model per game.
- Share visual encoders where appropriate and use task-specific heads.
- Combine detection, segmentation, OCR, classification, tracking, and temporal modeling.
- Evaluate generalization on games excluded from training.
- Publish reproducible datasets, protocols, baselines, and deployment interfaces.

## Model catalogue

| ID | Model | Primary tasks |
|---|---|---|
| M01 | Health HUD | Player, enemy, boss bars; bar segmentation and value estimation |
| M02 | Skill Cooldown | Skill visibility, unlock state, cooldown, readiness and charges |
| M03 | Universal OCR | Digits, timers, ammo, score, resources and text |
| M04 | Minimap & Compass | Minimap localization, player marker, north indicator and heading |
| M05 | Weapon Recognition | First-/third-person weapon localization and category recognition |
| M06 | Shooting Recognition | Visual firing-event detection and temporal localization |
| M07 | Reload Recognition | Reload start, phases, completion and reload type |
| M08 | Character Action | Attack, dodge, block, jump, run and hit reactions |
| M09 | Target Detection | Enemies, allies, NPCs, bosses and interactive entities |
| M10 | Boss Bar | Boss health bars, phases, names and defeat state |
| M11 | Buff/Debuff | Status icons, stacks, durations and state changes |
| M12 | Interaction Prompt | Interaction prompts, input glyphs and action labels |
| M13 | Inventory | Item grids, equipment slots, item classes and quantities |
| M14 | Dialogue | Dialogue panels, subtitles, speaker labels and choices |
| M15 | Map Objects | Units, buildings, markers, resources and routes on maps |
| M16 | Vehicle HUD | Speed, RPM, gear, fuel, temperature and damage indicators |
| M17 | Scoreboard | Scores, ranks, rounds, kills and match timers |
| M18 | Rhythm | Notes, lanes, hit lines, judgments and combo counters |
| M19 | Warning | Low-health, oxygen, ammo, resource and system warnings |
| M20 | Spatial UI | World-anchored bars, labels, markers and entity association |

See [docs/model-catalog.md](docs/model-catalog.md) for detailed specifications and applicability.

## Architecture

A modular architecture is preferred:

1. RGB frame/video ingestion and metadata.
2. Preprocessing, optional ROI proposals and resolution normalization.
3. Shared visual encoders (DINOv3 and task-appropriate alternatives).
4. Task heads for detection, segmentation, OCR, classification and regression.
5. Temporal modules for events and changing states.
6. Tracking, state fusion, confidence calibration and abstention.
7. A stable output API with game-agnostic schemas.

DINOv3 is an encoder candidate, not a mandatory solution for every task. Patch tokens are appropriate for spatial features; CLS tokens provide global image context. PCA-to-RGB is intended for feature inspection and visualization, not as a replacement for the original high-dimensional features.

## Repository structure

- `docs/`: architecture, taxonomy, model specifications, data and evaluation protocols.
- `models/M01...M20/`: independent model specifications and implementation scaffolds.
- `shared/`: encoders, feature extraction, PCA visualization and temporal utilities.
- `datasets/`: dataset documentation, schemas, splits and governance; no copyrighted game captures are bundled.
- `training/`: baseline and fine-tuning entry points.
- `evaluation/`: same-game, cross-game, leave-one-game-out and robustness evaluation.
- `deployment/`: ONNX, TensorRT and inference integration.
- `tools/`: collection, annotation, inspection and error analysis.

## Getting started

This initial commit establishes the research specifications and project scaffolding. Executable training pipelines and benchmark results will be added only after datasets, labels, dependencies and reproducible baselines are defined.

Read in this order:

1. [Research plan](docs/research-plan.md)
2. [Game and UI taxonomy](docs/game-and-ui-taxonomy.md)
3. [Model catalogue](docs/model-catalog.md)
4. [Architecture](docs/architecture.md)
5. [Dataset and annotation standard](docs/data-standard.md)
6. [Evaluation protocol](docs/evaluation-protocol.md)
7. [24-week roadmap](docs/roadmap.md)
8. [中文项目说明](README_CN.md)

## Responsible use and data policy

Use lawfully obtained gameplay captures and respect each game's terms, platform rules, privacy, and applicable copyright. Do not distribute game assets, proprietary UI files, or third-party datasets unless their licenses permit redistribution. Keep source provenance and license metadata for every dataset.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Contributions should include reproducible evaluation and clearly state which games and conditions were tested.

## License

Apache-2.0. This license applies to original project code and documentation. It does not relicense third-party game assets, datasets, pretrained weights, or dependencies.

## Audio and multimodal perception

GUP is not limited to screenshots or video. Audio is a first-class input modality. The roadmap expands the catalogue with audio event recognition, gunshot/reload cues, footsteps and movement, ability/UI sound cues, speech/transcription, enemy vocalizations, music-state analysis and audio-visual event association. See [audio perception plan](docs/audio-perception.md). Audio models must be evaluated across game mixes, languages, codecs, spatial audio and sound settings; sound cues are not guaranteed to be unique or present in every title.

## Independent-model principle

Each model represents one narrowly defined recognition task and is trained, evaluated, versioned and released independently. Cross-game generalization is pursued within that task; unrelated tasks must not be merged merely to reduce model count. Encoders, data tooling and evaluation infrastructure may be shared, but task heads/checkpoints remain independent unless controlled ablations show no loss in task performance.

## Audio model catalogue

Audio is a first-class modality. The project now specifies 13 independent audio models (A01–A13), including sound-event classification, gunshot recognition, reload-sound recognition, footsteps, movement, ability sounds, UI sounds, speech, creature vocalizations, ambience, music, source direction and audio-visual event association. See [audio model catalogue](audio/README.md) and [audio research plan](docs/audio-perception.md).
