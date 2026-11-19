# Model Catalogue and Game Applicability

Applicability is a research hypothesis, not a support claim. A title is supported only after the task is present and validated on that title/version.

| ID | Model | Main game families | Example titles | Primary approach |
|---|---|---|---|---|
| M01 | Health HUD | FPS, TPS, ARPG, MMO, MOBA, fighting, survival | DOOM Eternal, GTA V, Elden Ring, WoW, Dota 2, Street Fighter 6, Rust | detector + segmentation + bar geometry |
| M02 | Skill Cooldown | MOBA, MMO, ARPG, action RPG, selected TPS/FPS | LoL, Dota 2, FFXIV, Nioh 2, Hogwarts Legacy, Warframe | icon classification + state logic + OCR |
| M03 | Universal OCR | nearly all UI-rich genres | Forza Horizon 5, DOOM, Civilization VI, EA SPORTS FC, Cities: Skylines II | text detection + OCR + parser |
| M04 | Minimap & Compass | FPS, TPS, open-world, racing, survival, RTS | GTA V, RDR2, Far Cry 6, Forza Horizon 5, Rust, StarCraft II | ROI + marker/keypoint detection + geometry |
| M05 | Weapon Recognition | FPS, TPS, survival shooters, shooter RPG | Borderlands 3, Metro Exodus, Far Cry 6, GTA V, Rust, Cyberpunk 2077 | detection + visual embedding |
| M06 | Shooting Recognition | FPS, TPS, survival shooters | DOOM Eternal, Metro Exodus, Borderlands 3, GTA V, RDR2, Remnant II | temporal event classifier |
| M07 | Reload Recognition | FPS, TPS, survival shooters | Metro Exodus, Far Cry 6, Borderlands 3, The Division 2, Rust | weapon ROI + TCN/Transformer |
| M08 | Character Action | TPS, action RPG, fighting, sports, selected FPS | Sekiro, Black Myth: Wukong, God of War Ragnarök, Tekken 8, NBA 2K | video encoder + temporal head |
| M09 | Target Detection | FPS, TPS, RPG, MOBA, RTS, survival | DOOM, Horizon Forbidden West, Witcher 3, Dota 2, StarCraft II, ARK | detector + tracking |
| M10 | Boss Bar | action RPG, soulslike, ARPG, selected shooters | Elden Ring, Sekiro, Lies of P, Black Myth: Wukong, Nioh 2 | bar features + OCR + phase tracking |
| M11 | Buff/Debuff | MMO, MOBA, ARPG, survival, action RPG | WoW, FFXIV, LoL, Diablo IV, Elden Ring, Black Desert | icon embedding + OCR + tracking |
| M12 | Interaction Prompt | FPS, TPS, RPG, adventure, survival, puzzle | Cyberpunk 2077, RDR2, RE4, Skyrim, Portal 2, Subnautica | prompt detection + OCR |
| M13 | Inventory | RPG, survival, horror, management | RE4, Escape from Tarkov, Rust, ARK, Diablo IV, Baldur's Gate 3 | grid parsing + item classifier |
| M14 | Dialogue | RPG, narrative adventure, open-world, strategy | Baldur's Gate 3, Detroit: Become Human, Cyberpunk 2077, Witcher 3, Mass Effect | OCR + text tracking |
| M15 | Map Objects | RTS, 4X, open-world, survival, racing | StarCraft II, AoE IV, Civilization VI, GTA V, ARK, Forza Horizon 5 | map segmentation + icon detection |
| M16 | Vehicle HUD | racing, driving simulation, selected open-world | Forza Horizon 5, GT7, ACC, ETS2, BeamNG.drive | OCR + gauge geometry |
| M17 | Scoreboard | sports, fighting, racing, FPS, strategy | EA SPORTS FC, NBA 2K, Street Fighter 6, Tekken 8, F1 | panel parsing + OCR |
| M18 | Rhythm | rhythm games and rhythm mechanics | Beat Saber, DJMAX, Muse Dash, osu!, Taiko no Tatsujin | note detection + temporal matching |
| M19 | Warning | games with explicit warning UI | Resident Evil, Subnautica, DOOM, Cities: Skylines II, Farming Simulator | icon/text detection + state machine |
| M20 | Spatial UI | TPS, RPG, MMO, action, survival | Horizon Forbidden West, Monster Hunter, Witcher 3, ARK, Elden Ring | UI detection + entity association |

## Scope boundaries
- M01 handles general bars; M10 specializes in boss identity and phases.
- M04 requires observable heading references; do not infer absolute north if none is shown.
- M06 detects visible firing, not hidden trigger input.
- M08 first-person hand actions and third-person full-body actions are separate evaluation domains.
- M20 handles world-anchored UI; M01 handles screen HUD.
