# Audio Perception and Multimodal Research Plan

GUP treats audio as a first-class modality, alongside screenshots and video. Audio-only models and synchronized audio-visual models must be evaluated separately.

## Eight audio model directions

| ID | Model | Main game families | Example tasks | Candidate methods |
|---|---|---|---|---|
| A01 | Audio Event Recognition | all genres | classify sound effects, ambience and event categories | log-mel + audio encoder / event classifier |
| A02 | Gunshot & Reload Audio | FPS, TPS, survival shooters | shots, bursts, reload, empty-fire sounds | event detection + temporal localization |
| A03 | Footstep & Movement Audio | FPS, TPS, horror, survival | footsteps, running, jumping, landing, surface cues | audio event model + temporal classifier |
| A04 | Ability & UI Sound | RPG, MOBA, MMO, action | ability activation, cooldown-ready cues, warnings and menu sounds | audio embeddings + event classifier |
| A05 | Speech & Dialogue Audio | RPG, narrative, MMO, sports | voice activity, transcription, speaker turns and language | ASR + VAD; diarization only when required |
| A06 | Enemy & Creature Audio | horror, FPS, survival, action | growls, roars, alerts and creature sound classes | sound event classification + temporal detection |
| A07 | Music & Game-State Audio | rhythm, sports, racing, action | music segments, intensity, transitions, beat/onset | music/audio event analysis |
| A08 | Audio-Visual Event Association | FPS, TPS, racing, rhythm and multimodal games | associate audible events with visible firing, impacts, UI cues and events | synchronized audio-video encoders / late fusion |

## Audio data requirements
Record source game/version/mode, capture method, sample rate, channel count/layout, codec, duration, language, game audio settings, voice chat status, capture session, timestamp origin and audio-video synchronization offset. Preserve original audio; store resampled or mono versions as reproducible derivatives.

Annotations should include event class, start/end time, overlap, ambiguity, confidence and whether the label is actually audible. Do not equate a sound with hidden controller input or internal game state without independent evidence.

## Benchmark requirements
- Event detection: event precision/recall/F1, onset/offset error, class-wise AP and false alarms per minute.
- Speech: WER/CER and VAD miss/false alarm.
- Audio-visual association: matched-event precision/recall and timestamp alignment error.
- Robustness: game mix, music/effects volume, voice chat, language, sample rate, codec, mono/stereo/spatial audio, compression, noise and overlapping sounds.
- Compare audio-only, video-only and fused systems on identical held-out games/clips.

## Recommended order
1. A01 general sound event baseline.
2. A02 gunshot/reload and A03 movement events.
3. A04 ability/UI cues and A06 creature sounds.
4. A05 speech and A07 music analysis.
5. A08 synchronized audio-visual event association.

## Limitations
A sound may be absent, masked, changed by user audio settings, or shared by multiple actions. Audio can improve confidence but does not guarantee a unique game-state interpretation. Use UNKNOWN when evidence is ambiguous.
