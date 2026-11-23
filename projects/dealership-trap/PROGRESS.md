# STICKMAN SYSTEMS: EPISODE #06 PRODUCTION PIPELINE

**Episode Title:** *Why Car Dealerships Don't Want You Paying Cash (4 Hours Locked in the Finance Office)*  
**Slug:** `dealership-trap`  
**Framework:** Stickman Systems 2.0 (Simulation Storytelling & Outlier Engine)  
**Status:** Complete — Final Render & QC 100% Verified  

---

## 1. Episode Specifications
- **Script Length:** 92 lines (1,910 words)
- **Voice Actor:** Kokoro (`am_michael`, US English, natural documentary speed)
- **Audio Mix:** Complete — `mix.wav` (1004.70s / 16:44.7, 29 cues, -14.0 LUFS integrated)
- **Words Aligned:** 2,292 words (`WORDS.tsv`)
- **Storyboard Matrix:** 92 scenes + 20 sticker overlays (`SCENES.tsv` — 100% validated)
- **Visual Engine:** Google Flow (Nano Banana 2 / 2.1)
- **Visual Palette:** Slate Blueprint (`#0F172A`), Cyan Line Art (`#38BDF8`), Emerald Green (`#10B981`), Crimson Red (`#EF4444`), Amber Warning (`#F59E0B`)
- **Shots:** 34 background scenes (`SHOTS.tsv`) — Active in Flow
- **Cutout Elements:** 20 transparent stickers (`ELEMENTS.tsv`) — Active in Flow

---

## 2. Stage Progress Tracker
- [x] Stage 1: Titles (A/B/C) + 3 Upgraded Thumbnails + 0:00–0:08 Hook-Sync (`Thumbnail/PROMPTS.txt`)
- [x] Stage 2: Verbatim 92-line Script (`LINES.tsv`) adhering to 2.0 rules
- [x] Stage 3A: Flow Prompts (`SHOTS.tsv`, `ELEMENTS.tsv`)
- [x] Stage 3B: Audio Generation (`VO.wav`, `VO.tsv`, `WORDS.tsv` — 92 takes, 2,292 words aligned)
- [x] Stage 3C: Storyboard Matrix (`SCENES.tsv`, `cues.tsv` — 100% validated)
- [x] Stage 3D: Audio Mix (`mix.wav` — 1004.70s, -14.0 LUFS integrated)
- [x] Stage 3E: Visual Generation (54 Flow jobs) — COMPLETED (34 shots + 20 elements)
- [x] Stage 3F: Ingestion & Keying (`ingest_shots.py`, `ingest_elements.py`) — COMPLETED
- [x] Stage 3G: Forensic Collision Audit (`debug_overlays.py` -> 0 collisions) — VERIFIED 0 COLLISIONS
- [x] Stage 3H: Final Video Render (`render.py` -> `dealership-trap.mp4`) — 305.8 MB, 1004.70s, 30 fps
- [x] Stage 4: YouTube Studio Package (`YT_PACKAGE.md`)

---

## 3. Collision Audit Guarantee
- Prior episodes experienced rare collisions between auto-placed stickers and text labels.
- In Episode #06, all 20 overlay cuts follow:
  1. Zero redundant text tags on overlay cuts.
  2. Strict opposite-corner separation (`0.82` right vs `0.18` left).
  3. Pre-render collision verification with `debug_overlays.py`.
