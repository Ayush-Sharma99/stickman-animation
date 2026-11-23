# Stickman Systems: Forensic Documentary Explainer Pipeline

> Automated, documentary-grade 2D vector animation pipeline built on the **Stickman Systems 2.0** framework. Combines minimalist slate blueprint visuals (`#0F172A`), electric cyan line art (`#38BDF8`), Kokoro TTS voice tracks (`am_michael`), faster-whisper word-level alignment, and broadcast-normalized audio mixing (-14.0 LUFS EBU R128).

---

## 🎬 Episode Catalog (Episodes 01–08)

| Ep # | Project Directory | Episode Title | Duration | Status |
|:---:|:---|:---|:---:|:---:|
| **01** | `projects/printer-trap` | *How Printer Companies Legally Brick Working Machines* | 4m 32s | Complete |
| **02** | `projects/grocery-trap` | *Every Trick Grocery Stores Use to Make You Spend 40% More* | 5m 12s | Complete |
| **03** | `projects/hospital-bills` | *Why US Hospital Bills Have Fake Prices (Chargemaster Forensic)* | 7m 45s | Complete |
| **04** | `projects/fast-food-trap` | *Why Every Fast-Food Drive-Thru Changed Its Menu and Prices* | 10m 18s | Complete |
| **05** | `projects/ticketmaster-monopoly` | *How Ticketmaster Gets Paid to Be the Most Hated Company in America* | 11m 30s | Complete |
| **06** | `projects/dealership-trap` | *Why Car Dealerships Don't Want You Paying Cash* | 13m 42s | Complete |
| **07** | `projects/grid-collapse` | *Power Grid Collapse: 30 Days Locked in a US Suburb When 60.00 Hz Fails* | 18m 10s | Complete |
| **08** | `projects/hospital-bill-plans` | *You Owe $10,000 on a Fake Hospital Bill. We Tested 5 Viewer Plans to Erase It Legally.* | 18m 14s | Complete |

> **Note on Video Deliverables:**  
> Master 1080p 30fps `.mp4` video renders are published under **[GitHub Releases](https://github.com/Ayush-Sharma99/stickman-animation/releases)** to preserve system bandwidth and maintain a lightweight git repository.

---

## 🛠️ Pipeline Architecture

1. **Script & Line Pacing (`LINES.tsv`):** Verbatim 2nd-person simulation script anchored by sentence-level IDs.
2. **Visual Prompts (`SHOTS.tsv` & `ELEMENTS.tsv`):** Alternating spatial layouts (`space=left` vs `space=right`) and isolated cutout stickers on magenta backgrounds (`#FF00FF`).
3. **Voice & Alignment (`VO.wav`, `WORDS.tsv`):** Kokoro TTS (`am_michael`) joined with `vo_join.py` and aligned word-by-word with `faster-whisper`.
4. **Broadcast Audio Mix (`mix.wav`):** Dynamic ducking sidechain compression, music bed at -24 dB, SFX one-shot positioning, and two-pass EBU R128 loudness normalization to -14.0 LUFS.
5. **Zero-Collision Scene Composition (`SCENES.tsv`):** Mathematical bounding-box verification ensuring all overlay stickers and scene text banners remain in opposing frame quadrants.
6. **Master Video Render (`render.py`):** 1080p 30fps compositing with dynamic camera zooms, transparency physics, and x264 CRF 18 encoding.

---

## 📂 Project Structure

```
stickman-animation/
├── projects/
│   ├── dealership-trap/
│   ├── fast-food-trap/
│   ├── grid-collapse/
│   ├── grocery-trap/
│   ├── hospital-bill-plans/
│   ├── hospital-bills/
│   ├── printer-trap/
│   └── ticketmaster-monopoly/
│       ├── img/               # 34 ingested scene backgrounds (1080p)
│       ├── elements/cut/      # 20 auto-keyed transparent PNG stickers
│       ├── Thumbnail/         # 3 thumbnail archetype prompts
│       ├── LINES.tsv          # Full voice script
│       ├── SHOTS.tsv          # Scene generation prompts
│       ├── ELEMENTS.tsv       # Cutout sticker prompts
│       ├── SCENES.tsv         # Master cut & overlay timeline (0 collisions)
│       ├── cues.tsv           # SFX & music bed timing
│       ├── WORDS.tsv          # Faster-whisper word timestamps
│       ├── VO.tsv             # Line duration table
│       ├── YT_PACKAGE.md      # Full description, chapters, tags, sources
│       ├── STYLE.txt          # Aesthetic color blueprint
│       └── run_pipeline.py    # Automation runner
├── skills/                    # Specialized tooling & sound packs
├── Strategy-2.0.md            # Stickman Systems 2.0 bible & playbook
└── README.md
```
