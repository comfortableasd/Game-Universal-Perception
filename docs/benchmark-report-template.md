# Benchmark Report Template

## Run metadata
Model/version, code commit, dataset version, checkpoint hash, date, hardware/software, input resolution/FPS, preprocessing and thresholds.

## Protocol
Same-game / LOGO / cross-genre / robustness; train and held-out games; session/level separation; sample counts.

## Results
| Game | Samples | Precision | Recall | F1/AP/MAE | Latency | Abstention |
|---|---:|---:|---:|---:|---:|---:|

## Aggregate
Game-level macro average, confidence interval, worst-performing game, calibration and peak memory.

## Failure analysis
False positives/negatives, domain shifts, occlusions, unsupported states and representative examples.

## Support decision
Planned / Implemented / Benchmarked / Supported for explicitly listed game-version-configurations. Do not claim universal performance.
