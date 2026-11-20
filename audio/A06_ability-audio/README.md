# A06 — Ability Sound Recognition

## Objective
Recognize audible skill, spell, ability activation and readiness cues.

## Applicable games
RPG, MOBA, MMO, action: World of Warcraft, FFXIV, Dota 2, League of Legends, Diablo IV.

## Proposed baseline
Audio embeddings + event classifier.

## Evaluation
Event F1 and false alarms/min; sound cue does not prove ability is usable.

## Annotation and data requirements
Record source game/version/mode, capture method, sample rate, channel layout, codec, duration, language, audio settings, voice-chat status, session ID and timestamp origin. Preserve original audio. Label event boundaries, overlaps, ambiguous cases and audibility. Keep hidden game state and controller input separate from audible evidence.

## Status
**Planned specification.** No trained weights or validated game support claims yet.
