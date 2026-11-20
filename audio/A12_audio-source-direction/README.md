# A12 — Audio Source Direction Estimation

## Objective
Estimate direction of audible sources from multi-channel/spatial audio where channel metadata supports it.

## Applicable games
FPS, TPS, survival, horror with stereo/binaural/spatial audio.

## Proposed baseline
Multi-channel spatial audio features + direction regression/classification.

## Evaluation
Angular MAE, confidence/coverage; mono downmix generally removes reliable spatial cues.

## Annotation and data requirements
Record source game/version/mode, capture method, sample rate, channel layout, codec, duration, language, audio settings, voice-chat status, session ID and timestamp origin. Preserve original audio. Label event boundaries, overlaps, ambiguous cases and audibility. Keep hidden game state and controller input separate from audible evidence.

## Status
**Planned specification.** No trained weights or validated game support claims yet.
