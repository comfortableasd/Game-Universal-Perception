# Independent Audio Models

GUP audio models are task-specialized and independently trained/evaluated. Shared pretrained audio encoders may be used as initialization, but each task retains its own labels, head/checkpoint, thresholds and acceptance report.

| ID | Model | Applicable games | Task |
|---|---|---|---|
| A01 | Game Sound Event Classification | all genres | non-speech sound-event classification |
| A02 | Gunshot Audio Recognition | FPS, TPS, survival shooters | gunshot event detection/classification |
| A03 | Reload Sound Recognition | FPS, TPS, survival shooters | audible reload/cycling event detection |
| A04 | Footstep Sound Recognition | FPS, TPS, horror, survival | footsteps and supported surface cues |
| A05 | Movement Sound Recognition | FPS, TPS, horror, survival, action | running, jumping, landing, swimming |
| A06 | Ability Sound Recognition | RPG, MOBA, MMO, action | audible skill/ability cues |
| A07 | UI Sound Recognition | all genres with UI audio | menu, notification, confirmation, warning sounds |
| A08 | Speech Recognition | narrative RPG, MMO, sports, voice-chat titles | speech transcription and voice activity |
| A09 | Enemy/Creature Vocalization | horror, FPS, survival, action | creature/enemy vocalization detection |
| A10 | Game Ambience Recognition | survival, horror, open-world, simulation | environmental soundscape classification |
| A11 | Game Music Analysis | rhythm, racing, sports, action, RPG | music segments, transitions, beat/onset |
| A12 | Audio Source Direction | spatial-audio FPS, TPS, survival, horror | direction estimation from suitable multichannel audio |
| A13 | Audio-Visual Event Association | FPS, TPS, racing, rhythm and audiovisual games | synchronized audible/visible event association |

Each directory contains its task specification, candidate game families, baseline and evaluation requirements. All are **planned specifications**, not trained or validated models.

## Important boundaries
- A02 gunshot and A03 reload sound are separate models.
- A04 footsteps and A05 general movement are separate models.
- A06 ability cues and A07 UI sounds are separate models.
- A08 transcribes speech; it does not identify real-world speakers.
- A13 associates outputs from separate modality models; it does not replace them.
- Mono audio generally does not preserve reliable spatial direction. A12 requires suitable multichannel/spatial audio and metadata.

See [audio perception plan](../docs/audio-perception.md).
