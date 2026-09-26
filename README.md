# Sedekah Subuh — Rancangan Konten @wadahqris.id

Isi utama ada di [`RANCANGAN-KONTEN.md`](RANCANGAN-KONTEN.md): aturan triptych, jadwal Senin–Rabu–Jumat, kalender 30 triptych, prompt gambar & caption, panduan Reels, dan strategi Threads (bagian 11).

## Web

**<https://2013tib-droid.github.io/Sedekahsubuh/>**

Versi web dari `RANCANGAN-KONTEN.md`, enak dibuka di HP:

- **Hari Ini** — apa yang harus dikerjakan hari ini (triptych, Reels, produksi Minggu, atau Story saja), lengkap dengan teks panel dan tombol salin, plus konten Threads hari itu (utas triptych, pertanyaan Selasa, pengingat Kamis, polling Sabtu — diambil bergiliran dari bagian 11d–11f). Atur sekali tanggal Senin saat triptych #01 diunggah; tanggal disimpan di browser itu saja.
- **Kalender** — 30 triptych per pekan, bisa difilter Senin/Rabu/Jumat. Setiap kartu punya tombol *Salin prompt gambar* (prompt master 6a sudah terisi visual dan suasana pekannya), *Salin prompt caption*, *Salin prompt Reels*, *Salin utas Threads* (utas 3 bagian siap posting dari P1/P2/P3), dan *Salin prompt utas*.
- **Panduan** — seluruh isi `RANCANGAN-KONTEN.md` dengan daftar isi dan tombol salin di setiap blok prompt.

Web membaca `RANCANGAN-KONTEN.md` langsung, jadi cukup edit file itu. Workflow [`web.yml`](.github/workflows/web.yml) men-deploy ulang otomatis setiap kali `RANCANGAN-KONTEN.md` atau folder `web/` berubah di branch default. Kalau run pertama gagal di langkah "Aktifkan & konfigurasi GitHub Pages", aktifkan sekali lewat **Settings → Pages → Source: GitHub Actions**, lalu jalankan ulang workflow-nya.

Agar kalender tetap terbaca, pertahankan format penulisannya: `### Pekan N — "Judul" (suasana)`, `**#NN · Hari — Judul**`, lalu baris `- P1:`, `- P2:`, `- P3:`, `- Visual:`.

Lihat di komputer sendiri:

```
mkdir -p _site && cp -r web/. _site/ && cp RANCANGAN-KONTEN.md _site/
cd _site && python3 -m http.server 8000   # buka http://localhost:8000
```

## Alat

- [`tools/split_triptych.py`](tools/split_triptych.py) — potong panorama 3240×1440 jadi 3 post 1080×1440.
