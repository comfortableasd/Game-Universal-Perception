# A05 — Movement Sound Recognition

## Objective
Recognize running, jumping, landing, swimming, climbing and movement-related sounds.

## Applicable games
FPS, TPS, horror, survival, action: DOOM, Subnautica, ARK, Resident Evil, action RPGs.

## Proposed baseline
Temporal audio classifier + event localization.

## Evaluation
Macro-F1, event timing error and cross-game generalization.

## Annotation and data requirements
Record source game/version/mode, capture method, sample rate, channel layout, codec, duration, language, audio settings, voice-chat status, session ID and timestamp origin. Preserve original audio. Label event boundaries, overlaps, ambiguous cases and audibility. Keep hidden game state and controller input separate from audible evidence.

## Status
**Planned specification.** No trained weights or validated game support claims yet.
