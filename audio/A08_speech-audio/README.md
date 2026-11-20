# A08 — Speech Recognition

## Objective
Transcribe spoken dialogue and optionally detect language and voice activity.

## Applicable games
Narrative RPG, MMO, sports and games with voice chat: Baldur's Gate 3, Cyberpunk 2077, The Witcher 3, Mass Effect.

## Proposed baseline
VAD + ASR; diarization is a separate optional task.

## Evaluation
WER/CER, VAD miss/false alarm, language-wise metrics; privacy/consent controls.

## Annotation and data requirements
Record source game/version/mode, capture method, sample rate, channel layout, codec, duration, language, audio settings, voice-chat status, session ID and timestamp origin. Preserve original audio. Label event boundaries, overlaps, ambiguous cases and audibility. Keep hidden game state and controller input separate from audible evidence.

## Status
**Planned specification.** No trained weights or validated game support claims yet.
