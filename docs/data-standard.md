# Dataset and Annotation Standard

## Manifest fields
asset_id, relative_path, media_type, sha256, game_id, title, edition, game_version, platform, mode, capture_date, capture_method, resolution, fps, language, ui_scale, source_owner, license, redistribution_allowed, split_group and annotation_version.

## Annotation principles
- Define task-specific classes and positive, negative, ambiguous states.
- Distinguish absent, occluded, unreadable and not-applicable.
- Use normalized xyxy boxes and polygons/RLE masks where appropriate.
- Store video event start/end timestamps and frame indices.
- Keep raw captures immutable; annotations are separate.
- Review benchmark test labels.

## Split policy
Hold out complete games for primary cross-game evaluation. Also hold out capture sessions, levels, modes and UI configurations. Never randomly split adjacent frames from the same clip across train/test.

## Example
```json
{
  "asset_id": "clip_0001",
  "game_id": "example_game",
  "task": "shooting_recognition",
  "fps": 60,
  "events": [
    {"start_frame": 120, "end_frame": 122, "label": "fire_single"}
  ],
  "annotation_version": "1.0"
}
```

Use lawful captures. Do not redistribute game footage or third-party data unless the license allows it. Preserve source and license metadata.


## Audio assets and annotations

Record audio asset ID, source game/version/mode, capture method, sample rate, channel count/layout, codec, bit depth where known, duration, loudness/clipping checks, language, audio settings, capture session, timestamp origin and synchronization offset to video. Preserve the original waveform; store derived resampled/mono copies as reproducible transforms.

Annotate event class, start/end time, confidence/ambiguity, overlapping events, source attribution only when visually/audio-evidentially supported, and whether the label is audio-observable. Keep game-state truth and controller input separate from audible evidence. Split by complete game and capture session to avoid soundtrack/level leakage.
