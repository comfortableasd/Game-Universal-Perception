# A11 — Game Music Analysis

## Objective
Detect music segments, transitions, intensity, beat and onset events.

## Applicable games
Rhythm, racing, sports, action, RPG: Beat Saber, DJMAX, Forza Horizon 5, EA SPORTS FC.

## Proposed baseline
Music information retrieval + temporal segmentation.

## Evaluation
Onset F1/timing error, segment F1 and cross-soundtrack robustness.

## Annotation and data requirements
Record source game/version/mode, capture method, sample rate, channel layout, codec, duration, language, audio settings, voice-chat status, session ID and timestamp origin. Preserve original audio. Label event boundaries, overlaps, ambiguous cases and audibility. Keep hidden game state and controller input separate from audible evidence.

## Status
**Planned specification.** No trained weights or validated game support claims yet.
