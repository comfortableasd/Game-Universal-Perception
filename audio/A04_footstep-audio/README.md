# A04 — Footstep Sound Recognition

## Objective
Detect footsteps and classify surface/material when supported by evidence.

## Applicable games
FPS, TPS, horror, survival: Metro Exodus, Resident Evil, Rust, DayZ, Subnautica.

## Proposed baseline
Audio event detection + metric-learning classifier.

## Evaluation
Event F1, surface macro-F1, false alarms/min; player vs NPC attribution separately.

## Annotation and data requirements
Record source game/version/mode, capture method, sample rate, channel layout, codec, duration, language, audio settings, voice-chat status, session ID and timestamp origin. Preserve original audio. Label event boundaries, overlaps, ambiguous cases and audibility. Keep hidden game state and controller input separate from audible evidence.

## Status
**Planned specification.** No trained weights or validated game support claims yet.
