# A05 — Speech & Dialogue Audio

**Objective:** Voice activity detection, speech transcription, language identification and speaker-turn segmentation when relevant.

**Applicable games:** narrative RPG, MMO, sports and story-driven games. Candidates: Baldur's Gate 3, Cyberpunk 2077, The Witcher 3, Mass Effect and multiplayer titles with consented voice-chat data.

**Baseline:** VAD + ASR; diarization only for tasks that require speaker turns.

**Evaluation:** WER/CER, VAD miss/false-alarm rates, language-wise results and diarization error where applicable.

**Privacy:** voice chat can contain personal data. Require lawful collection, consent and retention controls. Do not infer real-world identity.

**Status:** Planned specification.
