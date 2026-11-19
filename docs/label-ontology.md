# Label Ontology

Shared visibility states: `visible`, `occluded`, `unreadable`, `absent`, `not_applicable`, `unknown`.

## Health bars
`player_hp`, `enemy_hp`, `boss_hp`, `shield`, `stamina`, `mana`, `oxygen`, `resource_bar`. Do not infer semantic type from color alone.

## Skill states
`visible`, `unlocked`, `cooldown`, `ready`, `resource_blocked`, `locked`, `charges`, `remaining_time`. A displayed icon is not proof of readiness.

## Shooting events
`idle`, `aim`, `fire_single`, `fire_burst`, `fire_auto`, `empty_fire`, `reload`, `weapon_switch`, `melee`. Visual firing is distinct from hidden trigger input.

## Character actions
`idle`, `walk`, `run`, `jump`, `attack`, `heavy_attack`, `block`, `parry`, `dodge`, `hit_reaction`, `fall`, `interact`.

Task ontologies may extend these labels through versioned schemas. Do not silently change label meaning across games.
