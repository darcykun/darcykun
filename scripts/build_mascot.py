"""Rebuild mascot outputs: python -m pip install Pillow; python scripts/build_mascot.py.

Consumes the included original imagegen sprite sheet; no network or API calls.
"""

from pathlib import Path
from PIL import Image

base = Path(__file__).resolve().parents[1] / "assets"
source = base / "mascot-sheet.png"
sheet = Image.open(source).convert("RGBA")
frames = []
for i in range(4):
    crop = sheet.crop(
        (i * sheet.width // 4, 0, (i + 1) * sheet.width // 4, sheet.height)
    )
    bbox = crop.getchannel("A").point(lambda a: 255 if a > 40 else 0).getbbox()
    crop = crop.crop(bbox)
    crop.thumbnail((54, 60), Image.Resampling.LANCZOS)
    frame = Image.new("RGBA", (72, 72))
    frame.alpha_composite(crop, ((72 - crop.width) // 2, 66 - crop.height))
    frames.append(frame)
frames[0].save(base / "mascot-static.png")
# Use neutral, blink, and the same raised-hand pose; never alternate waving hands.
sequence = [0, 1, 0, 3, 0, 3, 0]
durations = [1300, 120, 280, 260, 180, 260, 600]
gifs = []
for n in sequence:
    f = frames[n]
    p = f.convert("RGB").quantize(colors=255)
    p.paste(255, mask=f.getchannel("A").point(lambda a: 255 if a < 128 else 0))
    p.info["transparency"] = 255
    gifs.append(p)
gifs[0].save(
    base / "mascot.gif",
    save_all=True,
    append_images=gifs[1:],
    duration=durations,
    loop=0,
    transparency=255,
    disposal=2,
    optimize=False,
)
