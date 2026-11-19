# A02 — Gunshot & Reload Audio

**Objective:** Detect audible gunshots, bursts, weapon cycling, reload cues and empty-fire clicks.

**Applicable games:** FPS, TPS and survival shooters. Candidates: DOOM Eternal, Metro Exodus, Borderlands 3, Far Cry 6, GTA V, Red Dead Redemption 2, Rust and Remnant II.

**Baseline:** log-mel features + temporal event detector; compare pretrained audio embeddings and lightweight CNN/Transformer models.

**Labels:** shot_single, shot_burst, shot_auto, reload, weapon_cycle, empty_fire, impact_confounder, unknown.

**Evaluation:** event precision/recall/F1, onset/offset error, false alarms per minute, robustness to music/voice chat and per-game macro metrics.

**Caution:** audible shot detection is not equivalent to trigger-input detection. Suppressors, distance, mix settings and occlusion may alter or remove cues.

**Status:** Planned specification.
