# A06 — Enemy & Creature Audio

**Objective:** Detect and classify audible enemy alerts, growls, roars, calls and creature vocalizations.

**Applicable games:** horror, FPS, survival and action games. Candidates: Resident Evil, Subnautica, ARK, Monster Hunter and Metro Exodus.

**Baseline:** sound event classification + temporal detection + optional source/event tracking.

**Evaluation:** per-class event F1, false alarms per minute, onset/offset error and held-out-game species/creature generalization.

**Caution:** do not assign an audio event to a visible entity unless audio-visual evidence supports the association.

**Status:** Planned specification.
