# A04 — Ability & UI Sound

**Objective:** Recognize audible ability activations, cooldown-ready cues, menu navigation, notifications and warning tones.

**Applicable games:** RPG, MOBA, MMO and action games. Candidates: World of Warcraft, Final Fantasy XIV, Dota 2, League of Legends, Diablo IV and action RPGs.

**Baseline:** audio embeddings + event classifier + temporal state decoder.

**Evaluation:** class-wise event F1, false alarms per minute, onset error and game-specific cue generalization.

**Caution:** many games allow audio cues to be muted or customized. Sound alone may not establish that an ability is currently usable.

**Status:** Planned specification.
