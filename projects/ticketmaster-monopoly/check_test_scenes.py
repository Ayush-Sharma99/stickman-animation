import os, sys, glob
from PIL import Image
import numpy as np

proj = r"c:\Users\Lenovo\Downloads\stickman-animation\projects\ticketmaster-monopoly"
img_dir = os.path.join(proj, "img")
test_dir = os.path.join(proj, "test_scenes")

# Let's inspect the 20 test frames and print their dimensions and visual layout
test_files = sorted(glob.glob(os.path.join(test_dir, "*.jpg")))
print(f"Found {len(test_files)} test scene frames.")
for f in test_files:
    im = Image.open(f)
    print(f"{os.path.basename(f)}: size={im.size}")
