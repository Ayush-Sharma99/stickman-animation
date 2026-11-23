import os, sys, glob, re, subprocess
from PIL import Image, ImageDraw

def main():
    proj_dir = os.path.dirname(os.path.abspath(__file__))
    dl_dir = os.path.join(os.path.expanduser("~"), "Downloads", "stick_grocery-trap_el")
    raw_dir = os.path.join(proj_dir, "elements", "raw")
    cut_dir = os.path.join(proj_dir, "elements", "cut")
    os.makedirs(raw_dir, exist_ok=True)
    os.makedirs(cut_dir, exist_ok=True)

    files = glob.glob(os.path.join(dl_dir, "*.*"))
    elements = {}
    for f in files:
        base = os.path.basename(f)
        m = re.match(r"^(\d+)\s*-\s*", base)
        if m:
            elements[int(m.group(1))] = f

    print(f"Found {len(elements)} elements in {dl_dir}")
    for i in range(1, 21):
        if i in elements:
            src = elements[i]
            im = Image.open(src).convert("RGB")
            w, h = im.size
            px = im.load()
            bg = px[4, 4]
            # Wipe Flow sparkle in bottom right
            ImageDraw.Draw(im).rectangle((w - int(w * 0.12), h - int(h * 0.12), w, h), fill=bg)
            im.save(os.path.join(raw_dir, f"{i:02d}.png"))
        else:
            print(f"Missing element: {i}")

    # Run keyer
    keyer = r"C:\Users\Lenovo\.claude\skills\stickman-hybrid\scripts\key.py"
    res = subprocess.run([sys.executable, keyer, raw_dir, cut_dir], capture_output=True, text=True)
    print("Keyer output:")
    print((res.stdout or res.stderr).strip()[-800:])

    # Build preview grid
    cuts = sorted(glob.glob(os.path.join(cut_dir, "*.png")))
    print(f"Generated {len(cuts)} cutout stickers in {cut_dir}")
    if cuts:
        cols = 5
        tw, th = 300, 300
        rows = (len(cuts) + cols - 1) // cols
        grid = Image.new("RGBA", (tw * cols, th * rows), (150, 150, 150, 255))
        for idx, p in enumerate(cuts):
            st = Image.open(p).convert("RGBA")
            st.thumbnail((tw - 20, th - 20), Image.LANCZOS)
            x = (idx % cols) * tw + (tw - st.width) // 2
            y = (idx // cols) * th + (th - st.height) // 2
            grid.alpha_composite(st, (x, y))
        grid.convert("RGB").save(os.path.join(proj_dir, "cutouts.jpg"), quality=90)
        print("Created cutouts.jpg preview")

if __name__ == "__main__":
    main()
