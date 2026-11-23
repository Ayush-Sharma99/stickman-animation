import os, glob, re
from PIL import Image, ImageDraw

def main():
    proj_dir = os.path.dirname(os.path.abspath(__file__))
    dl_dir = os.path.join(os.path.expanduser("~"), "Downloads", "stick_grid-collapse")
    img_dir = os.path.join(proj_dir, "img")
    os.makedirs(img_dir, exist_ok=True)

    files = glob.glob(os.path.join(dl_dir, "*.*"))
    shots = {}
    for f in files:
        base = os.path.basename(f)
        m = re.match(r"^(\d+)(?:\s*\(\d+\))?\s*-\s*", base)
        if m:
            s_idx = int(m.group(1))
            try:
                test_im = Image.open(f)
                px = test_im.getpixel((10, 10))
                # Skip if accidental magenta background
                if px[0] > 200 and px[2] > 200:
                    continue
                shots[s_idx] = f
            except Exception:
                shots[s_idx] = f

    print(f"Found {len(shots)} shots in {dl_dir}")
    converted = 0
    for s in range(1, 35):
        if s in shots:
            src = shots[s]
            im = Image.open(src).convert("RGB")
            dst = os.path.join(img_dir, f"s{s:02d}.jpg")
            im.save(dst, quality=95)
            converted += 1
        else:
            print(f"Missing shot: {s}")

    print(f"Successfully converted {converted}/34 shots to {img_dir}")

    # Build review.jpg contact sheet
    paths = [os.path.join(img_dir, f"s{s:02d}.jpg") for s in range(1, 35) if os.path.exists(os.path.join(img_dir, f"s{s:02d}.jpg"))]
    if paths:
        cols = 6
        tw, th = 384, 216
        rows = (len(paths) + cols - 1) // cols
        grid = Image.new("RGB", (tw * cols, th * rows), (15, 23, 42))
        for idx, p in enumerate(paths):
            im = Image.open(p).resize((tw, th), Image.LANCZOS)
            x = (idx % cols) * tw
            y = (idx // cols) * th
            grid.paste(im, (x, y))
            d = ImageDraw.Draw(grid)
            d.text((x + 10, y + 10), f"s{idx+1:02d}", fill=(255, 255, 255))
        grid.save(os.path.join(proj_dir, "review.jpg"), quality=90)
        print("Created review.jpg contact sheet")

if __name__ == "__main__":
    main()
