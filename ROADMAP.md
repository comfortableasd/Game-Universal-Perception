# GUP Roadmap

| Phase | Weeks | Scope | Exit evidence |
|---|---:|---|---|
| P0 | 1–4 | Taxonomy, schemas, capture pipeline, DINOv3 feature inspection | Versioned manifest and reproducible feature extraction |
| P1 | 5–8 | M01 Health HUD, M02 Skill Cooldown, M03 OCR | Baselines and per-game reports |
| P2 | 9–12 | M04 Minimap, M05 Weapon, M06 Shooting, M07 Reload, M08 Action | Held-out-game and temporal event tests |
| P3 | 13–16 | M09 Target, M10 Boss Bar, M11 Buff/Debuff, M12 Interaction, M13 Inventory | Model cards and failure analysis |
| P4 | 17–20 | M14 Dialogue, M15 Map Objects, M16 Vehicle HUD, M17 Scoreboard, M18 Rhythm | Task-specific benchmarks |
| P5 | 21–24 | M19 Warning, M20 Spatial UI, runtime integration | Regression suite and compatibility matrix |

These are proposed planning windows, not performance or delivery guarantees. A title is supported only after a named game/version/configuration passes its published evaluation protocol.


## Audio expansion

After the visual baseline is stable, add A01–A08 as a parallel workstream: begin with A01 sound-event recognition and A02 gunshot/reload audio; then footsteps, ability/UI cues, speech, creature sounds, music-state analysis and synchronized audio-visual association. Keep audio-only and fused results separate.
