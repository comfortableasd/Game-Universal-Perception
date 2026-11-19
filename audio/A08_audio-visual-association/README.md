# A08 — Audio-Visual Event Association

**Objective:** Associate synchronized audible events with visible events such as firing, impacts, UI cues, footsteps and rhythm judgments.

**Applicable games:** FPS, TPS, racing, rhythm and games with synchronized audio/video. Candidates: DOOM Eternal, Metro Exodus, GTA V, Forza Horizon 5 and Beat Saber.

**Baseline:** separate audio and visual encoders, timestamp alignment, event-level late fusion; compare early fusion only with sufficient data.

**Evaluation:** audio-only vs video-only vs fused event F1, matched-event precision/recall, timestamp alignment error, missing-modality robustness and per-game macro metrics.

**Data:** record clock origin, audio/video offset, frame rate, sample rate and drift. Verify synchronization before labeling.

**Caution:** fusion can propagate errors. Preserve modality-specific predictions and confidence; support audio-only/video-only fallback.

**Status:** Planned specification.
