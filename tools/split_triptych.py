#!/usr/bin/env python3
"""Potong satu gambar panorama menjadi 3 post Instagram (triptych) ukuran 1080x1440.

Pemakaian:
    pip install pillow
    python3 tools/split_triptych.py hari01.png [folder_output]

Hasil: hari01_1-kiri.jpg, hari01_2-tengah.jpg, hari01_3-kanan.jpg
Urutan upload ke Instagram: 3-kanan -> 2-tengah -> 1-kiri.
"""
import sys
from pathlib import Path

from PIL import Image, ImageOps

PANEL_W, PANEL_H = 1080, 1440
CANVAS = (PANEL_W * 3, PANEL_H)  # 3240 x 1440 (rasio 9:4)
NAMES = ["1-kiri", "2-tengah", "3-kanan"]


def split(src: Path, out_dir: Path) -> None:
    img = Image.open(src).convert("RGB")
    # Skala & crop tengah agar pas 3240x1440 tanpa distorsi.
    img = ImageOps.fit(img, CANVAS, method=Image.LANCZOS, centering=(0.5, 0.5))
    out_dir.mkdir(parents=True, exist_ok=True)
    for i, name in enumerate(NAMES):
        panel = img.crop((i * PANEL_W, 0, (i + 1) * PANEL_W, PANEL_H))
        out = out_dir / f"{src.stem}_{name}.jpg"
        panel.save(out, "JPEG", quality=95)
        print(out)
    print("Upload urut: 3-kanan -> 2-tengah -> 1-kiri")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    source = Path(sys.argv[1])
    split(source, Path(sys.argv[2]) if len(sys.argv) > 2 else source.parent)
