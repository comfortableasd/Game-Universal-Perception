# A13 — Audio-Visual Event Association

## Objective
Associate synchronized audio events with visible events such as shots, impacts, footsteps and UI cues.

## Applicable games
FPS, TPS, racing, rhythm and other synchronized audiovisual games.

## Proposed baseline
Separate audio/visual encoders + timestamp alignment + late fusion.

## Evaluation
Matched-event precision/recall, alignment error, modality ablations and missing-modality robustness.

## Annotation and data requirements
Record source game/version/mode, capture method, sample rate, channel layout, codec, duration, language, audio settings, voice-chat status, session ID and timestamp origin. Preserve original audio. Label event boundaries, overlaps, ambiguous cases and audibility. Keep hidden game state and controller input separate from audible evidence.

## Status
**Planned specification.** No trained weights or validated game support claims yet.
