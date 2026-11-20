# A10 — Game Ambience Recognition

## Objective
Classify environmental soundscapes such as indoor/outdoor, underwater, cave, rain, wind and machinery.

## Applicable games
Survival, horror, open-world, simulation: Subnautica, Metro Exodus, RDR2, survival titles.

## Proposed baseline
Audio scene classification + embeddings.

## Evaluation
Scene macro-F1, calibration and held-out-game evaluation.

## Annotation and data requirements
Record source game/version/mode, capture method, sample rate, channel layout, codec, duration, language, audio settings, voice-chat status, session ID and timestamp origin. Preserve original audio. Label event boundaries, overlaps, ambiguous cases and audibility. Keep hidden game state and controller input separate from audible evidence.

## Status
**Planned specification.** No trained weights or validated game support claims yet.
