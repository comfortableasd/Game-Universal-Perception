# A09 — Enemy and Creature Vocalization Recognition

## Objective
Detect and classify audible enemy alerts, growls, roars and creature calls.

## Applicable games
Horror, FPS, survival, action: Resident Evil, Subnautica, ARK, Monster Hunter, Metro Exodus.

## Proposed baseline
Sound event classifier + temporal detector.

## Evaluation
Per-class event F1, false alarms/min; associate to visible entity only with evidence.

## Annotation and data requirements
Record source game/version/mode, capture method, sample rate, channel layout, codec, duration, language, audio settings, voice-chat status, session ID and timestamp origin. Preserve original audio. Label event boundaries, overlaps, ambiguous cases and audibility. Keep hidden game state and controller input separate from audible evidence.

## Status
**Planned specification.** No trained weights or validated game support claims yet.
