# Acceptance Criteria

The following are proposed initial targets for defined benchmark conditions, not measured results or universal guarantees.

| Model | Main metric | Initial target |
|---|---|---:|
| M01 Health HUD | precision/recall; value MAE | P/R >= 0.99; <=2 percentage points |
| M02 Skill Cooldown | READY precision; macro-F1 | >=0.995; >=0.99 |
| M03 OCR | numeric exact sequence match | >=0.995 on defined subset |
| M04 Minimap | wrapped angular MAE | <5 degrees where heading is observable |
| M05 Weapon | category macro-F1 | >=0.98 |
| M06 Shooting | event F1 | >=0.98 |
| M07 Reload | event F1 | >=0.98 |
| M08 Action | macro-F1 | >=0.95 |
| M09 Target | AP50 | >=0.95 |
| M10 Boss Bar | detection recall | >=0.99 |
| M11 Buff/Debuff | macro-F1 | >=0.95 |
| M12 Interaction | precision/recall | >=0.99 |
| M13 Inventory | item macro-F1 | >=0.95 |
| M14 Dialogue | CER | <=0.01 on defined subset |
| M15 Map Objects | AP50 | >=0.95 |
| M16 Vehicle HUD | numeric exact match | >=0.99 on defined fields |
| M17 Scoreboard | numeric field exact match | >=0.995 |
| M18 Rhythm | event F1 | >=0.99 |
| M19 Warning | precision/recall | >=0.99 |
| M20 Spatial UI | detection recall | >=0.98 |

Report per-game metrics, macro average, confidence intervals, support conditions, thresholds, calibration, abstention, latency and failure cases. Never claim universal performance.
