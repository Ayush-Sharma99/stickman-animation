import os, glob
from PIL import Image, ImageDraw

proj = r"c:\Users\Lenovo\Downloads\stickman-animation\projects\ticketmaster-monopoly"
test_dir = os.path.join(proj, "test_scenes")
files = sorted(glob.glob(os.path.join(test_dir, "*.jpg")))

cols = 4
tw, th = 480, 270
rows = (len(files) + cols - 1) // cols
grid = Image.new("RGB", (tw * cols, th * rows), (15, 23, 42))

for idx, p in enumerate(files):
    im = Image.open(p).resize((tw, th), Image.LANCZOS)
    x = (idx % cols) * tw
    y = (idx // cols) * th
    grid.paste(im, (x, y))
    d = ImageDraw.Draw(grid)
    d.rectangle((x, y, x + 160, y + 24), fill=(0, 0, 0))
    d.text((x + 6, y + 4), os.path.basename(p), fill=(255, 255, 255))

grid.save(os.path.join(proj, "test_overlay_grid.jpg"), quality=90)
print(f"Created test_overlay_grid.jpg ({grid.width}x{grid.height})")
