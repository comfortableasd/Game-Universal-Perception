# A07 — UI Sound Recognition

## Objective
Recognize menu navigation, notifications, confirmations, warnings and interface sound effects.

## Applicable games
All genres with UI audio: RPG, strategy, sports, racing, action.

## Proposed baseline
Audio event classifier + temporal decoder.

## Evaluation
Macro-F1, event F1 and robustness to custom audio settings.

## Annotation and data requirements
Record source game/version/mode, capture method, sample rate, channel layout, codec, duration, language, audio settings, voice-chat status, session ID and timestamp origin. Preserve original audio. Label event boundaries, overlaps, ambiguous cases and audibility. Keep hidden game state and controller input separate from audible evidence.

## Status
**Planned specification.** No trained weights or validated game support claims yet.
