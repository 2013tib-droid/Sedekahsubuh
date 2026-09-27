#!/usr/bin/env python3
"""Potong gambar triptych dari ChatGPT menjadi 3 post Instagram ukuran 1080x1440.

Kalau gambar punya garis/jarak polos (biasanya putih) di antara panel, garis itu
dideteksi otomatis dan dibuang: potongan tepat di tepi garis. Kalau tidak ada,
gambar dipotong sama rata di 1/3 dan 2/3 lebarnya.

Pemakaian:
    pip install pillow
    python3 tools/split_triptych.py hari01.png [folder_output]

Hasil: hari01_1-kiri.jpg, hari01_2-tengah.jpg, hari01_3-kanan.jpg
Urutan upload ke Instagram: 3-kanan -> 2-tengah -> 1-kiri.
"""
import sys
from pathlib import Path

from PIL import Image, ImageOps, ImageStat

PANEL = (1080, 1440)  # rasio 3:4
NAMES = ["1-kiri", "2-tengah", "3-kanan"]


def find_gutters(img: Image.Image):
    """Cari 2 garis vertikal polos di sekitar 1/3 dan 2/3 lebar.

    Kembalikan [(awal, akhir), (awal, akhir)] dalam piksel, atau None.
    """
    w, h = img.size
    gray = img.convert("L")
    plain = []
    for x in range(w):
        st = ImageStat.Stat(gray.crop((x, 0, x + 1, h)))
        plain.append(st.stddev[0] < 6)
    runs, start = [], None
    for x, p in enumerate(plain + [False]):
        if p and start is None:
            start = x
        elif not p and start is not None:
            runs.append((start, x))
            start = None
    gutters = []
    for lo, hi in ((0.2, 0.47), (0.53, 0.8)):
        near = [r for r in runs if lo * w <= (r[0] + r[1]) / 2 <= hi * w]
        if not near:
            return None
        gutters.append(max(near, key=lambda r: r[1] - r[0]))
    return gutters


def split(src: Path, out_dir: Path) -> None:
    img = Image.open(src).convert("RGB")
    w, h = img.size
    gutters = find_gutters(img)
    if gutters:
        (a0, a1), (b0, b1) = gutters
        boxes = [(0, a0), (a1, b0), (b1, w)]
        print(f"Garis pemisah ditemukan di x={a0}-{a1} dan x={b0}-{b1}, ikut dibuang.")
    else:
        boxes = [(round(i * w / 3), round((i + 1) * w / 3)) for i in range(3)]
        print(f"Tidak ada garis pemisah; dipotong sama rata di x={boxes[1][0]} dan x={boxes[2][0]}.")
    out_dir.mkdir(parents=True, exist_ok=True)
    for (x0, x1), name in zip(boxes, NAMES):
        piece = img.crop((x0, 0, x1, h))
        if piece.width < PANEL[0] * 0.8:
            print(f"  catatan: panel {name} hanya {piece.width}px, hasilnya diperbesar (bisa sedikit buram).")
        # Skala & crop tengah agar pas 1080x1440 tanpa distorsi.
        panel = ImageOps.fit(piece, PANEL, method=Image.LANCZOS, centering=(0.5, 0.5))
        out = out_dir / f"{src.stem}_{name}.jpg"
        panel.save(out, "JPEG", quality=95)
        print(out)
    print("Upload urut: 3-kanan -> 2-tengah -> 1-kiri")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    source = Path(sys.argv[1])
    split(source, Path(sys.argv[2]) if len(sys.argv) > 2 else source.parent)
