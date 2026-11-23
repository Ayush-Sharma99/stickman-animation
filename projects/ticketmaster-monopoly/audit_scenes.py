import csv, os
from PIL import Image

proj = r"c:\Users\Lenovo\Downloads\stickman-animation\projects\ticketmaster-monopoly"
shots = {r['id']: r for r in csv.DictReader(open(os.path.join(proj, 'SHOTS.tsv'), encoding='utf-8'), delimiter='\t')}
scenes = list(csv.reader(open(os.path.join(proj, 'SCENES.tsv'), encoding='utf-8'), delimiter='\t'))

for i, r in enumerate(scenes):
    if r and r[0].startswith('+'):
        prev = scenes[i-1]
        cue = prev[0]
        img_file = prev[1]
        sid = img_file.replace('img/s', '').replace('.jpg', '')
        sh = shots.get(sid, {})
        space = sh.get('space', '-')
        print(f"Scene {cue:5s} | Shot {sid}: space={space:6s} | text: {prev[2]:30s} pos: {prev[3]:6s} | sticker: {r[1]:20s} pos: {r[3]}")
