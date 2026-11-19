# System Architecture

```text
RGB frames + metadata
  -> capture validation / resize / ROI proposals
  -> shared visual encoder(s) + task-specific specialists
  -> detection | segmentation | OCR | classification | regression
  -> temporal modules / tracking / event decoding
  -> state fusion + calibration + UNKNOWN abstention
  -> versioned game-agnostic output schema
```

## DINOv3 feature policy
- Patch tokens retain spatial layout and are suitable for dense spatial tasks.
- CLS tokens represent global image context; they are not a spatial feature map.
- Preserve high-dimensional features for downstream learning.
- PCA-to-RGB is a diagnostic visualization, not a substitute for original features. Fit a reference projection for comparable colors; independently fitted PCA images are not directly comparable.
- Compare frozen features, linear probes, adapters and fine-tuning under controlled splits.

## Task-specific alternatives
OCR, digit parsing and geometric gauge reading may work better with specialized algorithms. Backbone choice is empirical.

## Temporal path
For events, define clip length, stride, frame rate and event boundaries. Compare single-frame, frame-difference, optical-flow, TCN and Transformer baselines.

## Runtime
Schedule only relevant models, cache shared features, and report end-to-end latency and memory rather than isolated model latency.


## Audio and multimodal path

```text
Audio waveform + sample-rate/channel metadata
  -> resampling / channel policy / loudness and clipping checks
  -> log-mel or waveform representation
  -> audio encoder + event/ASR heads
  -> temporal event boundaries and confidence

Synchronized RGB + audio (when available)
  -> visual events + audio events
  -> timestamp alignment / cross-modal association
  -> calibrated fusion with modality-specific UNKNOWN states
```

Audio must not be treated as an optional feature hidden inside a video model. Preserve original timestamps, sample rate, channel layout and synchronization offset. Evaluate audio-only, video-only and fused systems separately. Candidate audio encoders include general audio event and contrastive audio-text models; ASR systems are separate components. Model and dataset licenses must be checked before use.
