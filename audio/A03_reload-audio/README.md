# A03 — Reload Sound Recognition

## Objective
Detect audible reload, magazine handling, weapon cycling and empty-click cues.

## Applicable games
FPS, TPS, survival shooters: Metro Exodus, Far Cry 6, Borderlands 3, The Division 2, Rust.

## Proposed baseline
Audio event detector + temporal classifier.

## Evaluation
Event F1 and boundary error; reload sounds may be absent or masked.

## Annotation and data requirements
Record source game/version/mode, capture method, sample rate, channel layout, codec, duration, language, audio settings, voice-chat status, session ID and timestamp origin. Preserve original audio. Label event boundaries, overlaps, ambiguous cases and audibility. Keep hidden game state and controller input separate from audible evidence.

## Status
**Planned specification.** No trained weights or validated game support claims yet.
