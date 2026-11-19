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
