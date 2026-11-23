# STICKMAN SYSTEMS: EPISODE #08 PRODUCTION PIPELINE

**Episode Title:** *You Owe $10,000 on a Fake Hospital Bill. We Tested 5 Viewer Plans to Erase It Legally.*  
**Slug:** `hospital-bill-plans`  
**Framework:** Stickman Systems 2.0 (Simulation Storytelling & Outlier Engine)  
**Status:** Audio Pipeline Active (Kokoro TTS Generating Takes)  

---

## 1. Episode Specifications
- **Script Length:** 93 lines (2,250 words)
- **Voice Actor:** Kokoro (`am_michael`, US English, natural documentary speed)
- **Audio Target:** Master mix `mix.wav` (~16–17 minutes, ducked music bed, -14.0 LUFS integrated)
- **Words Aligned:** `WORDS.tsv` via faster-whisper (`tiny`)
- **Visual Engine:** Google Flow (Nano Banana 2)
- **Visual Palette:** Slate Blueprint (`#0F172A`), Cyan Line Art (`#38BDF8`), Emerald Green (`#10B981`), Crimson Red (`#EF4444`), Amber Warning (`#F59E0B`)
- **Shots:** 34 background scenes (`SHOTS.tsv`) — Ready for Flow
- **Cutout Elements:** 20 transparent stickers (`ELEMENTS.tsv`) — Ready for Flow

---

## 2. Stage Progress Tracker
- [x] Stage 1: Titles (A/B/C) + 3 Upgraded Thumbnails + 0:00–0:08 Hook-Sync (`Thumbnail/PROMPTS.txt`)
- [x] Stage 2: Verbatim 93-line Script (`LINES.tsv` — 2,250 words) adhering to 2.0 rules
- [x] Stage 3A: Flow Prompts (`SHOTS.tsv` 34 shots, `ELEMENTS.tsv` 20 stickers)
- [ ] Stage 3B: Audio Generation (`VO.wav`, `VO.tsv`, `WORDS.tsv` — Actively generating takes)
- [ ] Stage 3C: Storyboard Matrix (`SCENES.tsv`, `cues.tsv` — To be generated after alignment)
- [ ] Stage 3D: Audio Mix (`mix.wav` — Ducked music bed + line SFX, -14.0 LUFS)
- [ ] Stage 3E: Visual Generation (54 Flow jobs: 34 shots + 20 elements)
- [ ] Stage 3F: Ingestion & Keying (`ingest_shots.py`, `ingest_elements.py`)
- [ ] Stage 3G: Forensic Collision Audit (`debug_overlays.py` -> 0 collisions)
- [ ] Stage 3H: Final Video Render (`render.py` -> `hospital-bill-plans.mp4`)
- [x] Stage 4: YouTube Studio Package (`YT_PACKAGE.md`)

---

## 3. Collision Audit Guarantee
- Enforce strict opposite-corner placement (`0.82` right vs `0.18` left).
- Ensure all overlay cuts in `SCENES.tsv` have empty text tags (`text=""`).
- Pre-render automated collision verification with `debug_overlays.py`.
