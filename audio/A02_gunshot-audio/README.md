# A02 — Gunshot Audio Recognition

## Objective
Detect and classify audible gunshot events and shot patterns.

## Applicable games
FPS, TPS, survival shooters: DOOM Eternal, Metro Exodus, Borderlands 3, Far Cry 6, GTA V, RDR2, Rust.

## Proposed baseline
Audio event detector + temporal localization.

## Evaluation
Event F1, onset/offset error, false alarms/min; distinguish shots from explosions and impacts.

## Annotation and data requirements
Record source game/version/mode, capture method, sample rate, channel layout, codec, duration, language, audio settings, voice-chat status, session ID and timestamp origin. Preserve original audio. Label event boundaries, overlaps, ambiguous cases and audibility. Keep hidden game state and controller input separate from audible evidence.

## Status
**Planned specification.** No trained weights or validated game support claims yet.
