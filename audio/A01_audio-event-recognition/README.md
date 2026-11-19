# A01 — Audio Event Recognition

**Objective:** General-purpose classification and temporal detection of game sound events and ambience.

**Applicable games:** FPS, TPS, RPG, MMO, MOBA, RTS, racing, sports, survival, horror, simulation and rhythm games. Candidate examples include DOOM Eternal, Metro Exodus, Elden Ring, World of Warcraft, Forza Horizon 5, Subnautica and Resident Evil.

**Tasks:** sound effect class, ambience, impact, explosion, interface sound, environmental event, event boundaries.

**Baseline:** log-mel spectrogram + CNN/Audio Transformer; compare waveform encoders and pretrained audio embeddings.

**Evaluation:** macro-F1, class-wise AP, event F1, onset/offset error, false alarms per minute, per-game macro average.

**Status:** Planned specification; no trained weights or validated support claims.
