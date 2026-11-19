# A03 — Footstep & Movement Audio

**Objective:** Detect footsteps, running, jumping, landing, swimming and movement surface cues.

**Applicable games:** FPS, TPS, horror and survival. Candidates: Counter-Strike-style training environments only where permitted, Metro Exodus, Resident Evil, The Last of Us, Rust, DayZ and Subnautica.

**Baseline:** log-mel + temporal event classifier; optional surface/material classifier.

**Evaluation:** event F1, onset/offset error, false alarms per minute and cross-game/surface generalization.

**Caution:** distinguish player movement from NPC/enemy footsteps and background effects only when evidence supports attribution.

**Status:** Planned specification.
