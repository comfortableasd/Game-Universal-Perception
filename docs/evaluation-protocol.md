# Evaluation Protocol

## Required protocols
1. Same-game held-out sessions for basic task learning.
2. Leave-one-game-out (LOGO): hold out entire games.
3. Cross-genre: test on a genre absent from training.
4. Robustness: resolution, UI scale, language, brightness, compression, blur and occlusion.
5. Temporal generalization: unseen weapons, animation variants and event frequencies.

## Metrics
- Detection: AP50, AP50:95, precision, recall and per-game macro AP.
- Segmentation: mIoU, Dice and boundary F-score.
- OCR: character error rate (CER) and exact sequence match.
- Classification: macro-F1, per-class precision/recall and confusion matrix.
- Regression: MAE, RMSE and error percentiles; heading uses wrapped angular error.
- Events: event precision/recall/F1 and onset/offset error in milliseconds.
- Reliability: calibration error, false-positive rate and coverage-risk under abstention.
- Runtime: end-to-end latency, throughput, VRAM/RAM.

Report per-game scores and unweighted game-level macro averages, confidence intervals, sample counts, game versions, thresholds and failures. Targets are not results. A game is supported only for tested configurations. UNKNOWN is valid when evidence is insufficient.


## Audio and multimodal evaluation
- Audio event detection: event-based precision/recall/F1, onset/offset error, class-wise AP and false alarms per minute.
- Speech: WER/CER, VAD miss/false alarm, diarization error only when speaker identity is a task.
- Audio-visual association: matched-event precision/recall, timestamp alignment error and unmatched-event rate.
- Robustness: game mix, music/effects volume, voice chat, language, sample rate, codec, mono/stereo/spatial audio, compression, background noise and overlapping events.
- Compare audio-only, video-only and fused systems on identical held-out games and clips. Report modality ablations and missing-modality performance.

## Independent task-model evaluation

Every model must be evaluated independently against its own ontology. Report per-game results and game-level macro averages. Do not hide a weak task behind a combined multi-task score. If encoders are shared experimentally, report both shared and independent baselines and all task-specific regressions.

For audio models, report audio-only metrics separately. For A13, compare audio-only, visual-only and fused predictions on the exact same held-out clips.
