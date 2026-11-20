# A01 — Game Sound Event Classification

## Objective
Classify non-speech game sound events at clip level.

## Applicable games
All genres: combat, racing, sports, survival, horror, simulation.

## Proposed baseline
Audio encoder + log-mel baseline + event classifier.

## Evaluation
Macro-F1, per-game AP, false alarms/min; distinct event labels.

## Annotation and data requirements
Record source game/version/mode, capture method, sample rate, channel layout, codec, duration, language, audio settings, voice-chat status, session ID and timestamp origin. Preserve original audio. Label event boundaries, overlaps, ambiguous cases and audibility. Keep hidden game state and controller input separate from audible evidence.

## Status
**Planned specification.** No trained weights or validated game support claims yet.
