import os, sys, csv
import numpy as np
from PIL import Image, ImageDraw

sys.path.insert(0, r"C:\Users\Lenovo\.claude\skills\stickman-hybrid\scripts")
import render

proj = r"c:\Users\Lenovo\Downloads\stickman-animation\projects\dealership-trap"
os.chdir(proj)
out_dir = os.path.join(proj, "test_scenes")
os.makedirs(out_dir, exist_ok=True)

words = {r['line'] + '.' + r['i']: float(r['start']) for r in csv.DictReader(open('WORDS.tsv', encoding='utf-8'), delimiter='\t')}
rows = [r for r in csv.reader(open('SCENES.tsv', encoding='utf-8'), delimiter='\t') if r and not r[0].startswith('#') and r[0] != 'cue']

render.set_look('night')
SPACE = {}
if os.path.exists('SHOTS.tsv'):
    for r in csv.DictReader(open('SHOTS.tsv', encoding='utf-8'), delimiter='\t'):
        sid = f"s{int(r['id']):02d}"
        if (r.get('space') or '').strip().lower() in ('left', 'right', 'top'):
            SPACE[sid] = r['space'].strip().lower()

scenes = []
for r in rows:
    r += [''] * (5 - len(r))
    cue = r[0].strip()
    if cue.startswith('+'):
        c = cue[1:]
        pos = r[3].strip() or 'auto'
        x, y, h = (None, None, min(0.34, float(pos.split(',')[1]) if ',' in pos else 0.3)) if pos.startswith('auto') else (float(v) for v in pos.split(','))
        mo = r[4].strip() or 'pop'
        scenes[-1]['ov'].append(dict(t=words[c], img=r[1].strip(), text=r[2].strip(), x=x, y=y, h=h, motion=mo, plain='plain' in mo))
    else:
        scenes.append(dict(t0=words[cue] if scenes else 0.0, row=r, ov=[]))

results = []
for idx, sc in enumerate(scenes):
    if not sc['ov']:
        continue
    render.W, render.H = 1920, 1080
    pic = render.picture(sc['row'][1].strip())
    e = render.busy(pic)
    img_name = os.path.splitext(os.path.basename(sc['row'][1].strip()))[0]
    side = SPACE.get(img_name)
    spots = [(0.86, 0.2), (0.14, 0.2), (0.86, 0.78), (0.14, 0.78), (0.5, 0.16),
             (0.76, 0.3), (0.24, 0.3), (0.78, 0.62), (0.22, 0.62), (0.5, 0.84)]
    if side == 'top':
        spots = [(0.3, 0.2), (0.7, 0.2), (0.5, 0.17), (0.16, 0.2), (0.84, 0.2)]
    elif side:
        xs = (0.8, 0.86) if side == 'right' else (0.2, 0.14)
        spots = [(xs[0], 0.3), (xs[0], 0.62), (xs[1], 0.18), (xs[1], 0.8), (xs[0], 0.46)]
    
    taken = []
    for o in sc['ov']:
        if o['x'] is None:
            hh = o['h'] * render.H
            ww = hh * 1.1
            def cost(i, xy):
                x0, y0 = xy[0] * render.W - ww / 2, xy[1] * render.H - hh / 2
                for tx, ty, th in taken:
                    if abs(tx - xy[0]) * render.W < (ww + th * render.H * 1.1) / 2 and abs(ty - xy[1]) * render.H < (hh + th * render.H) / 2:
                        return 1e9
                m = e[max(0, int(y0) // 8):int(y0 + hh) // 8, max(0, int(x0) // 8):int(x0 + ww) // 8]
                centre = 1 + 1.2 * np.exp(-((xy[0] - 0.5) ** 2 / 0.05 + (xy[1] - 0.55) ** 2 / 0.08))
                return float(m.mean()) * centre * (1 + 0.03 * i) if m.size else 1e9
            o['x'], o['y'] = min(spots, key=lambda xy: cost(spots.index(xy), xy))
            taken.append((o['x'], o['y'], o['h']))

    text = sc['row'][2].strip()
    pos = sc['row'][3].strip()
    img_path = sc['row'][1].strip()
    cue_name = sc['row'][0].strip()
    
    fr = pic.convert('RGBA')
    blocked = []
    for o in sc['ov']:
        hh = o['h'] * render.H
        ww = hh * 1.2
        blocked.append((o['x'] * render.W - ww / 2, o['y'] * render.H - hh / 2, o['x'] * render.W + ww / 2, o['y'] * render.H + hh / 2))
    
    # Check text rect
    text_rect = None
    p_use = pos or 'auto'
    if text:
        size = 70
        lines = [render.text_layer(ln, size, render.INK) for ln in text.split('|')]
        gap = int(size * 0.28)
        tw = max(l.width for l in lines)
        th = sum(l.height for l in lines) + gap * (len(lines) - 1)
        p_use = pos if pos.endswith('!') else 'auto'
        if p_use.endswith('!'):
            p_clean = p_use[:-1]
        else:
            e_sub = render.busy(fr)
            def tcost(i, p):
                cx = {'tl': 80 + tw // 2, 'bl': 80 + tw // 2, 'tr': render.W - 80 - tw // 2, 'br': render.W - 80 - tw // 2}.get(p, render.W // 2)
                cy = {'top': 70 + th // 2, 'tl': 70 + th // 2, 'tr': 70 + th // 2}.get(p, render.H - 80 - th // 2)
                x0, y0, x1, y1 = cx - tw // 2 - 34, cy - th // 2 - 22, cx + tw // 2 + 34, cy + th // 2 + 22
                if any(x0 < bx1 and bx0 < x1 and y0 < by1 and by0 < y1 for bx0, by0, bx1, by1 in blocked):
                    return 1e9
                m = e_sub[max(0, (y0 - 40) // 8):(y1 + 40) // 8, max(0, (x0 - 40) // 8):(x1 + 40) // 8]
                return float(m.mean()) * (1 + 0.04 * i)
            p_clean = min(render.SPOTS, key=lambda p: tcost(render.SPOTS.index(p), p))
        cx = {'tl': 80 + tw // 2, 'bl': 80 + tw // 2, 'tr': render.W - 80 - tw // 2, 'br': render.W - 80 - tw // 2}.get(p_clean, render.W // 2)
        cy = {'top': 70 + th // 2, 'tl': 70 + th // 2, 'tr': 70 + th // 2}.get(p_clean, render.H - 80 - th // 2)
        text_rect = (cx - tw // 2 - 34, cy - th // 2 - 22, cx + tw // 2 + 34, cy + th // 2 + 22)
        render.label(fr, text, pos if pos.endswith('!') else 'auto', blocked)
        
    for o in sc['ov']:
        st = render.sticker(o['img'], int(o['h'] * render.H), o.get('plain', False))
        render.place(fr, st, o['x'] * render.W, o['y'] * render.H, 1.0, o['motion'])
        
        # Check collision between text_rect and sticker rect
        st_rect = (o['x'] * render.W - st.width / 2, o['y'] * render.H - st.height / 2, o['x'] * render.W + st.width / 2, o['y'] * render.H + st.height / 2)
        collision = False
        if text_rect:
            # Overlap test
            if not (st_rect[2] < text_rect[0] or st_rect[0] > text_rect[2] or st_rect[3] < text_rect[1] or st_rect[1] > text_rect[3]):
                collision = True
        results.append((cue_name, img_path, text, p_use, o['img'], (o['x'], o['y']), collision))

    out_file = os.path.join(out_dir, f"scene_{cue_name.replace('.', '_')}.jpg")
    fr.convert('RGB').save(out_file, quality=85)

print("\n--- OVERLAY COLLISION REPORT ---")
collisions_found = 0
for cue_name, img_path, text, p_use, ov_img, pos_xy, collision in results:
    status = "COLLISION [!]" if collision else "OK"
    if collision:
        collisions_found += 1
    print(f"Cue {cue_name:6s} | Img {img_path:10s} | Pos {p_use:5s} | Ov {ov_img:15s} | PosXY ({pos_xy[0]:.2f}, {pos_xy[1]:.2f}) | {status} | Text: '{text}'")

print(f"\nTotal Overlays: {len(results)} | Collisions: {collisions_found}")
if collisions_found == 0:
    print("SUCCESS: 0 collisions detected across all overlay scenes!")
else:
    print(f"WARNING: {collisions_found} collisions detected! Review and fix SCENES.tsv coordinates or text placement.")
