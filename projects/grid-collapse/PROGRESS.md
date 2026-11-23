# STICKMAN SYSTEMS: EPISODE #07 PRODUCTION PIPELINE

**Episode Title:** *Power Grid Collapse: 30 Days Locked in a US Suburb When 60.00 Hz Fails (Day 1 to Day 30)*  
**Slug:** `grid-collapse`  
**Framework:** Stickman Systems 2.0 (Simulation Storytelling & Outlier Engine)  
**Status:** Complete — Final Render & QC 100% Verified  

---

## 1. Episode Specifications
- **Script Length:** 93 lines (2,046 words)
- **Voice Actor:** Kokoro (`am_michael`, US English, natural documentary speed)
- **Audio Target:** Master mix `mix.wav` (982.17s / 16:22.2, 28 cues, -14.0 LUFS integrated)
- **Words Aligned:** `WORDS.tsv` via faster-whisper (`tiny`)
- **Visual Engine:** Google Flow (Nano Banana 2)
- **Visual Palette:** Slate Blueprint (`#0F172A`), Cyan Line Art (`#38BDF8`), Emerald Green (`#10B981`), Crimson Red (`#EF4444`), Amber Warning (`#F59E0B`)
- **Shots:** 34 background scenes (`SHOTS.tsv`) — 100% Ingested
- **Cutout Elements:** 20 transparent stickers (`ELEMENTS.tsv`) — 100% Keyed

---

## 2. Stage Progress Tracker
- [x] Stage 1: Titles (A/B/C) + 3 Upgraded Thumbnails + 0:00–0:08 Hook-Sync (`Thumbnail/PROMPTS.txt`)
- [x] Stage 2: Verbatim 93-line Script (`LINES.tsv` — 2,046 words) adhering to 2.0 rules
- [x] Stage 3A: Flow Prompts (`SHOTS.tsv` 34 shots, `ELEMENTS.tsv` 20 stickers)
- [x] Stage 3B: Audio Generation (`VO.wav`, `VO.tsv`, `WORDS.tsv` — 93 takes, 2,046 words aligned, 981.17s)
- [x] Stage 3C: Storyboard Matrix (`SCENES.tsv` 113 rows, `cues.tsv` 28 cues — 100% validated)
- [x] Stage 3D: Audio Mix (`mix.wav` — 982.17s, -14.0 LUFS integrated)
- [x] Stage 3E: Visual Generation (54 Flow jobs: 34 shots + 20 elements) — COMPLETED
- [x] Stage 3F: Ingestion & Keying (`ingest_shots.py`, `ingest_elements.py`) — COMPLETED
- [x] Stage 3G: Forensic Collision Audit (`debug_overlays.py` -> 0 collisions) — VERIFIED 0 COLLISIONS
- [x] Stage 3H: Final Video Render (`render.py` -> `grid-collapse.mp4`) — 362.2 MB, 982.13s, 30 fps
- [x] Stage 4: YouTube Studio Package (`YT_PACKAGE.md`)

---

## 3. Collision Audit Guarantee
- Enforce strict opposite-corner placement (`0.82` right vs `0.18` left).
- Ensure all overlay cuts in `SCENES.tsv` have empty text tags (`text=""`).
- Pre-render automated collision verification with `debug_overlays.py`.
