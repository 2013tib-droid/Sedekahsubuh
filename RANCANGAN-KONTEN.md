# Rancangan Konten Instagram @wadahqris.id — Triptych Senin · Rabu · Jumat

> Format: **1 tema = 3 post (triptych)** yang menyatu jadi satu baris di grid.
> Frekuensi: **3 triptych per pekan (Senin, Rabu, Jumat — Jumat wajib)** + 2 Reels (Selasa & Kamis) + Story harian. Triptych diunggah setelah Subuh.
> Nuansa: islami, sedekah, kebaikan, hangat, cahaya pagi.

---

## 1. Aturan Teknis Triptych (penting!)

| Hal | Aturan |
|---|---|
| Ukuran kanvas penuh | **3240 × 1440 px** (rasio 9:4), lalu dipotong jadi 3 |
| Ukuran tiap post | **1080 × 1440 px** (rasio 3:4, sama dengan tampilan grid Instagram sekarang) |
| Urutan upload | **Kanan dulu → Tengah → Kiri terakhir** (grid menampilkan post terbaru di kiri atas) |
| Jeda antar upload | 1–3 menit, jangan dijadwalkan bersamaan |
| Jumlah post | **Selalu kelipatan 3.** Satu post "nyasar" akan menggeser seluruh grid. Konten lepas (pengumuman, dll) taruh di **Story/Reels yang tidak dibagikan ke grid**, atau buat juga 3 post. |
| Pin post | Hindari pin, atau pin **3 sekaligus** (1 triptych), karena pin juga menggeser grid |
| Zona aman teks | Jangan taruh teks penting dalam jarak ±60 px dari garis potong, supaya huruf tidak terbelah |
| Teks Arab | **Jangan dibuat oleh AI gambar** (sering salah/rusak). Tambahkan manual di Canva dengan copy-paste dari sumber Al-Qur'an/hadis terpercaya |

Potong kanvas otomatis: `python3 tools/split_triptych.py gambar.png` (lihat bagian 7), atau aplikasi pemotong grid di HP.

---

## 2. Formula Isi Setiap Triptych

Setiap triptych punya **satu latar panorama yang menyambung**, dengan peran panel:

```
┌──────────────┬──────────────┬──────────────┐
│   PANEL 1    │   PANEL 2    │   PANEL 3    │
│    HOOK      │    DALIL     │    AKSI      │
│ Judul besar  │ Ayat / hadis │ Ajakan kecil │
│ yang bikin   │ + terjemah + │ + QRIS/link  │
│ berhenti     │ sumber       │ + logo       │
│ scroll       │              │              │
└──────────────┴──────────────┴──────────────┘
```

- **Panel 1 – Hook**: 1 kalimat pendek, maks. 8 kata. Font serif besar (seperti post kamu sekarang).
- **Panel 2 – Dalil**: teks Arab (ditambah manual) + terjemahan + sumber (QS/HR). Objek utama foto (lentera, mushaf, kurma) diletakkan di sini.
- **Panel 3 – Aksi**: 1 langkah konkret hari ini + bar bawah "WADAHQRIS.ID · Berbagi kebaikan jadi lebih mudah dengan QRIS".

Supaya tiap post juga enak dilihat **sendiri-sendiri** di feed (bukan cuma di grid), tiap panel wajib punya teks yang bisa berdiri sendiri, dan caption ketiganya boleh sama.

---

## 3. Identitas Visual (biar grid konsisten)

- **Palet**: hijau zaitun `#3F5A3C`, krem `#F3EBDD`, emas pagi `#D9A441`, coklat kayu `#7A5A3A`.
- **Font**: judul serif (Playfair Display / Cormorant), aksen script (Great Vibes / Allura), isi sans (Poppins / Inter).
- **Suasana foto**: golden hour / cahaya fajar, meja kayu, dedaunan di sudut, bokeh lembut.
- **Elemen tetap**: ikon hati kecil di atas judul, garis pemisah dengan hati, bar hijau di bawah panel 3.
- **Variasi suasana per seri** (opsional): pekan 1–4 fajar keemasan, pekan 5–6 biru subuh, pekan 7–8 hijau taman, pekan 9–10 krem minimalis. Dari jauh grid akan terlihat seperti "bab-bab".

---

## 4. Jadwal Mingguan

Fokus: **3 triptych per pekan (Senin, Rabu, Jumat)** + Reels + Story. **Jumat wajib upload.**

| Hari | Jenis | Isi | Waktu |
|---|---|---|---|
| **Senin** | Triptych | **Dalil & amalan sunnah** (hari puasa sunnah, semangat awal pekan) | 05.00–06.00 WIB |
| Selasa | Reels | Reels dari triptych Senin (lihat bagian 8) | 12.00 atau 19.30 WIB |
| **Rabu** | Triptych | **Kisah teladan & kebaikan kecil** | 05.00–06.00 WIB |
| Kamis | Reels | Reels pengingat "besok Jumat" / dari triptych Rabu | 19.30 WIB (malam Jumat) |
| **Jumat ✅ WAJIB** | Triptych | **Jumat Berkah + ajakan sedekah Jumat** | 05.00–06.00 WIB |
| Setiap hari | Story | Doa pagi, pengingat sedekah subuh, stiker link QRIS | Setelah Subuh |
| Minggu (opsional) | Triptych | Laporan penyaluran donasi — **hanya jika ada** | Bebas |

Target per bulan: **±12 triptych (36 post) + ±8 Reels**. Kalender di bawah (30 triptych) cukup untuk **10 pekan**.
Kalau sudah lancar 1–2 bulan, boleh naik ke 4–5x/pekan; lihat Insights untuk hari dengan *save* & *share* tertinggi.

> Catatan grid: Reels **tetap muncul di grid** jika opsi "Juga bagikan ke feed" aktif, dan itu akan menggeser triptych. Pilih salah satu:
> (a) saat upload Reels, **matikan "Also share to feed/Tampilkan di grid profil"**, atau
> (b) jika Reels tetap ingin di grid, buat Reels **3 sekaligus** (jarang dan repot) — jadi disarankan opsi (a).

---

## 5. Kalender 10 Pekan (30 Triptych)

> Sebelum posting, **cek ulang teks Arab & terjemahan** di sumber resmi (Qur'an Kemenag: quran.kemenag.go.id; hadis: nomor sesuai kitab yang disebut). Nomor hadis di bawah mengikuti penomoran umum (Fu'ad Abdul Baqi / Tirmidzi Syakir).

### Pekan 1 — "Pagi yang Berkah" (fajar keemasan)

**#01 · Senin — Dua Malaikat di Waktu Pagi**
- P1: *Setiap pagi, ada doa yang turun untukmu.*
- P2: HR. Bukhari 1442 & Muslim 1010 — "Tidak ada satu hari pun ketika hamba berada di pagi hari, kecuali dua malaikat turun. Salah satunya berdoa: 'Ya Allah, berilah ganti bagi orang yang berinfak.' Yang lain berdoa: 'Ya Allah, berilah kehancuran bagi orang yang menahan (hartanya).'"
- P3: *Jadikan sedekah pertamamu hari ini sebelum matahari terbit.*
- Visual: jendela masjid saat fajar, cahaya masuk, sajadah.

**#02 · Rabu — Senyum Itu Sedekah**
- P1: *Sedekah paling ringan ada di wajahmu.*
- P2: HR. Tirmidzi 1956 — "Senyummu di hadapan saudaramu adalah sedekah bagimu."
- P3: *Hari ini: senyumi 3 orang yang kamu temui.*
- Visual: dua cangkir teh berhadapan di teras, bunga kecil.

**#03 · Jumat — Jumat Berkah**
- P1: *Jumat: hari terbaik untuk berbagi.*
- P2: QS. Al-Baqarah: 261 — perumpamaan infak seperti sebutir benih yang menumbuhkan tujuh tangkai, tiap tangkai seratus biji.
- P3: *Sisihkan sedekah Jumat-mu lewat QRIS di bio.*
- Visual: lentera, sajadah hijau, cahaya hangat (seperti post lentera kamu).

### Pekan 2 — "Harta yang Tak Berkurang" (fajar keemasan)

**#04 · Senin — Sedekah Tidak Mengurangi Harta**
- P1: *Memberi tidak akan membuatmu miskin.*
- P2: HR. Muslim 2588 — "Sedekah tidak akan mengurangi harta."
- P3: *Percayakan hitungannya kepada Allah.*
- Visual: toples kaca berisi koin, tanaman tumbuh dari dalamnya.

**#05 · Rabu — Kurma Setengah Butir**
- P1: *Tak punya banyak? Setengah kurma pun cukup.*
- P2: HR. Bukhari 1417 & Muslim 1016 — "Jagalah diri kalian dari api neraka walau hanya dengan (bersedekah) separuh kurma."
- P3: *Mulai dari Rp1.000. Yang penting istiqamah.*
- Visual: piring kayu berisi kurma, gelas air, cahaya pagi.

**#06 · Jumat — Allah Mengganti**
- P1: *Yang kamu beri, Allah ganti.*
- P2: QS. Saba': 39 — "…Dan apa saja yang kamu infakkan, Allah akan menggantinya, dan Dialah pemberi rezeki yang terbaik."
- P3: *Jumat ini, sisihkan sedekah untuk yang membutuhkan — QRIS di link bio.*
- Visual: tangan memberi bingkisan, bokeh biru pagi.

### Pekan 3 — "Teladan Para Sahabat" (fajar keemasan)

**#07 · Senin — Puasa Senin-Kamis**
- P1: *Amal diangkat hari Senin & Kamis.*
- P2: HR. Tirmidzi 747 — "Amal-amal diperlihatkan (kepada Allah) setiap Senin dan Kamis, maka aku suka amalku diperlihatkan saat aku berpuasa."
- P3: *Puasa + sedekah = paket lengkap hari ini.*
- Visual: meja sahur sederhana, lampu temaram, jam menunjukkan 04.15.

**#08 · Rabu — Kisah Abu Bakar & Umar**
- P1: *Umar memberi separuh. Abu Bakar memberi semuanya.*
- P2: Kisah infak Perang Tabuk (HR. Abu Dawud 1678, Tirmidzi 3675): "Apa yang kau sisakan untuk keluargamu?" — "Aku sisakan untuk mereka Allah dan Rasul-Nya."
- P3: *Kita mungkin tak sanggup semuanya. Tapi bisa mulai dari sebagian.*
- Visual: gurun saat fajar, siluet unta di kejauhan.

**#09 · Jumat — Shalawat & Al-Kahfi**
- P1: *Jumat: jangan lupa tiga amalan ini.*
- P2: Membaca Al-Kahfi (HR. Al-Hakim, disahihkan Al-Albani), memperbanyak shalawat (HR. Abu Dawud 1047), dan sedekah.
- P3: *Checklist Jumat: ☐ Al-Kahfi ☐ Shalawat ☐ Sedekah*
- Visual: mushaf terbuka di rehal, tasbih, lentera.

### Pekan 4 — "Sedekah Itu Mudah" (fajar keemasan)

**#10 · Senin — Doa Setelah Subuh**
- P1: *Tiga hal yang diminta Nabi ﷺ setiap pagi.*
- P2: HR. Ibnu Majah 925 — "Allahumma innī as'aluka 'ilman nāfi'an, wa rizqan ṭayyiban, wa 'amalan mutaqabbalan." (Ya Allah, aku memohon ilmu yang bermanfaat, rezeki yang baik, dan amal yang diterima.)
- P3: *Baca selepas salam Subuh. Simpan post ini sebagai pengingat.*
- Visual: tangan menengadah berdoa (siluet), tasbih, mushaf.

**#11 · Rabu — Setiap Sendi Ada Sedekahnya**
- P1: *Tubuhmu punya "tagihan" sedekah setiap hari.*
- P2: HR. Bukhari 2989 & Muslim 1009 — setiap persendian wajib bersedekah setiap hari; mendamaikan dua orang, membantu orang naik kendaraan, kata yang baik, menyingkirkan gangguan dari jalan adalah sedekah.
- P3: *Hari ini: singkirkan satu gangguan dari jalan.*
- Visual: jalan setapak pagi berkabut, daun berguguran.

**#12 · Jumat — Cara Sedekah via QRIS**
- P1: *Sedekah Jumat cuma butuh 10 detik.*
- P2: Langkah: buka e-wallet/m-banking → scan QRIS → isi nominal → niatkan karena Allah.
- P3: *Scan, niat, kirim. Jumat ini, pahala mengalir.* + mockup ponsel dengan QRIS.
- Visual: ponsel di meja kayu, secangkir kopi, notes.

### Pekan 5 — "Kebaikan yang Terus Mengalir" (biru subuh)

**#13 · Senin — Sedekah Jariyah**
- P1: *Ada amal yang tetap hidup setelah kita tiada.*
- P2: HR. Muslim 1631 — "Apabila manusia meninggal, terputuslah amalnya kecuali tiga: sedekah jariyah, ilmu yang bermanfaat, atau anak saleh yang mendoakannya."
- P3: *Wakaf Al-Qur'an, sumur, atau buku — pilih satu.*
- Visual: pohon besar rindang, akar kuat, cahaya menembus daun.

**#14 · Rabu — Utsman & Sumur Rumah**
- P1: *Satu sumur, pahala sepanjang zaman.*
- P2: Kisah Utsman bin Affan membeli sumur Rumah dan mewakafkannya untuk kaum muslimin (HR. Tirmidzi 3703, An-Nasa'i 3608).
- P3: *Air bersih adalah sedekah terbaik — ayo ikut berbagi.*
- Visual: sumur batu tua, ember kayu, air berkilau.

**#15 · Jumat — Sedekah Rahasia**
- P1: *Sedekah Jumat terbaik: tangan kiri pun tak tahu.*
- P2: HR. Bukhari 1423 & Muslim 1031 — di antara tujuh golongan yang dinaungi Allah: orang yang bersedekah lalu menyembunyikannya hingga tangan kirinya tidak tahu apa yang diinfakkan tangan kanannya.
- P3: *QRIS memudahkan sedekah diam-diam. Cukup kamu dan Allah yang tahu.*
- Visual: amplop diselipkan di bawah pintu, cahaya pagi.

### Pekan 6 — "Niat & Pahala Berlipat" (biru subuh)

**#16 · Senin — Niat**
- P1: *Semua dimulai dari niat.*
- P2: HR. Bukhari 1 & Muslim 1907 — "Sesungguhnya amal itu tergantung niatnya."
- P3: Contoh niat sedekah singkat: *"Aku bersedekah karena Allah Ta'ala."*
- Visual: kompas di meja kayu, arah kiblat, matahari terbit.

**#17 · Rabu — Menunjukkan Kebaikan**
- P1: *Share post ini juga bisa jadi pahala.*
- P2: HR. Muslim 1893 — "Barangsiapa menunjukkan suatu kebaikan, maka ia mendapat pahala seperti pahala orang yang mengerjakannya."
- P3: *Kirim ke 1 teman yang ingin rutin sedekah.*
- Visual: dua tangan memegang bibit tanaman bersama.

**#18 · Jumat — Pinjaman kepada Allah**
- P1: *Allah menawarkan "pinjaman" dengan balasan berlipat.*
- P2: QS. Al-Baqarah: 245 — "Barangsiapa meminjamkan kepada Allah dengan pinjaman yang baik, maka Allah akan melipatgandakan pembayaran kepadanya…"
- P3: *Sedekah Jumat: scan QRIS di link bio.*
- Visual: lentera + timbangan kecil, nuansa krem.

### Pekan 7 — "Memberi dari yang Dicintai" (hijau taman)

**#19 · Senin — Harta yang Dicintai**
- P1: *Kebajikan sempurna ada di balik yang paling berat dilepas.*
- P2: QS. Ali 'Imran: 92 — "Kamu tidak akan memperoleh kebajikan sebelum kamu menginfakkan sebagian harta yang kamu cintai."
- P3: *Apa yang paling kamu sayangi? Bagikan sebagiannya.*
- Visual: kotak kado kayu terbuka, pita, cahaya lembut.

**#20 · Rabu — Abu Thalhah & Kebun Bairuha**
- P1: *Ia serahkan kebun terbaiknya dalam sekali dengar.*
- P2: Kisah Abu Thalhah menyedekahkan kebun Bairuha setelah turun QS. Ali 'Imran: 92 (HR. Bukhari 1461, Muslim 998).
- P3: *Respons terbaik untuk ayat adalah amal.*
- Visual: kebun kurma saat pagi, sinar menembus pelepah.

**#21 · Jumat — Memberi Makan**
- P1: *Kami memberi makan hanya karena Allah.*
- P2: QS. Al-Insan: 8–9 — memberi makan orang miskin, anak yatim, dan tawanan, "…kami tidak mengharap balasan dan terima kasih darimu."
- P3: *Jumat ini, bantu kami berbagi makanan untuk yang membutuhkan.* (sesuaikan dengan program yang benar-benar ada)
- Visual: bungkusan nasi tertata rapi, cahaya fajar.

### Pekan 8 — "Sekarang, Bukan Nanti" (hijau taman)

**#22 · Senin — Sedekah Saat Sehat**
- P1: *Jangan tunggu kaya untuk mulai memberi.*
- P2: HR. Bukhari 1419 & Muslim 1032 — sedekah paling utama adalah saat engkau sehat, sedang mengharapkan kaya dan takut miskin.
- P3: *Sekarang, bukan nanti.*
- Visual: jam pasir di meja kayu, cahaya pagi.

**#23 · Rabu — Ilmu Juga Sedekah**
- P1: *Tak punya harta? Bagikan ilmumu.*
- P2: HR. Muslim 1631 (ilmu yang bermanfaat termasuk amal yang terus mengalir).
- P3: *Ajarkan satu hal baik hari ini — walau satu ayat.*
- Visual: tumpukan buku, kacamata, secangkir teh.

**#24 · Jumat — Sebelum Terlambat**
- P1: *"Ya Rabb, andai Engkau tunda ajalku sebentar saja…"*
- P2: QS. Al-Munafiqun: 10 — infakkan sebagian rezeki sebelum datang kematian, lalu ia berkata: "…aku akan bersedekah dan termasuk orang-orang saleh."
- P3: *Jangan tunggu Jumat berikutnya. Mulai hari ini.*
- Visual: matahari terbit di cakrawala, jalan panjang.

### Pekan 9 — "Istiqamah dalam Kebaikan" (krem minimalis)

**#25 · Senin — Sedikit tapi Rutin**
- P1: *Kebaikan kecil yang konsisten mengalahkan yang besar tapi sesekali.*
- P2: HR. Bukhari 6464 & Muslim 783 — "Amalan yang paling dicintai Allah adalah yang paling kontinu walaupun sedikit."
- P3: *Tantangan: sedekah subuh 7 hari berturut-turut. Siap?*
- Visual: tetesan air di batu (melubangi batu perlahan).

**#26 · Rabu — Sedekah untuk Keluarga**
- P1: *Nafkah untuk keluarga juga bernilai sedekah.*
- P2: HR. Bukhari 55 & Muslim 1002 — "Apabila seseorang menafkahkan (hartanya) untuk keluarganya dengan mengharap pahala, maka itu sedekah baginya."
- P3: *Traktir orang tuamu sarapan pagi ini.*
- Visual: meja makan keluarga pagi hari, nasi hangat, teh.

**#27 · Jumat — Adab Bersedekah**
- P1: *Sebelum sedekah Jumat, ingat 3 adab ini.*
- P2: QS. Al-Baqarah: 264 — janganlah merusak sedekahmu dengan menyebut-nyebutnya dan menyakiti perasaan penerima.
- P3: 3 adab: ikhlas, tidak mengungkit, beri yang terbaik.
- Visual: amplop putih di atas meja, bunga melati.

### Pekan 10 — "Syukur & Muhasabah" (krem minimalis)

**#28 · Senin — Muhasabah**
- P1: *Sudah berapa kebaikan kita pekan lalu?*
- P2: QS. Az-Zalzalah: 7 — "Barangsiapa mengerjakan kebaikan seberat zarrah, niscaya dia akan melihat (balasan)nya."
- P3: *Tulis 1 kebaikan yang ingin kamu lanjutkan pekan ini di kolom komentar.*
- Visual: jurnal terbuka, pena, daun kering, sinar pagi.

**#29 · Rabu — Refleksi & Laporan**
- P1: *Terima kasih, orang-orang baik.*
- P2: Ringkasan donasi/penyaluran pekan ini (atau kutipan QS. Ibrahim: 7 tentang syukur jika belum ada laporan).
- P3: *Kebaikanmu sampai. Mari lanjutkan.*
- Visual: kardus sembako, anak-anak tersenyum (ilustrasi, tanpa wajah jelas).

**#30 · Jumat — Penutup Seri**
- P1: *10 pekan, 30 alasan untuk terus berbagi.*
- P2: HR. Tirmidzi 614 — "Sedekah memadamkan kesalahan sebagaimana air memadamkan api."
- P3: *Jumat ini, tutup seri ini dengan sedekah terbaikmu. Kita lanjut pekan depan!*
- Visual: kolase kecil 3 objek ikonik bulan ini (lentera, cangkir, tanaman).

> Setelah #30: ulangi pola Senin–Rabu–Jumat dengan dalil/kisah baru, atau sesuaikan dengan momen (Ramadhan, Idul Adha, 10 Muharram, Maulid, bencana alam).

---

## 6. Prompt Gambar AI

Buat **satu gambar panorama** lalu potong jadi 3. Cocok untuk ChatGPT (gambar), Gemini, Midjourney, Ideogram, atau Leonardo.

### 6a. Prompt Master (isi bagian `[...]`)

```
Ultra-wide panoramic photo, aspect ratio 9:4 (3240x1440), designed to be split
into 3 equal vertical panels for an Instagram triptych.
Scene: [DESKRIPSI VISUAL], on a rustic wooden table, soft golden-hour sunrise
light, gentle bokeh background of green trees and distant hills, warm cream and
olive green color palette, calm and spiritual Islamic atmosphere.
Composition: LEFT third has clean empty space in the upper half for a large
headline; CENTER third features the main object [OBJEK UTAMA] with empty space
above for text; RIGHT third has a small secondary object and empty space in the
lower part for a call-to-action banner.
Keep important objects away from the two vertical split lines at 1/3 and 2/3.
Photorealistic, high detail, soft shadows, no text, no letters, no watermark,
no people's faces.
```

Kata kunci penting: **"no text, no letters"** — teks ditambahkan sendiri di Canva agar rapi dan bebas typo (terutama teks Arab).

### 6b. Contoh terisi (#01)

```
Ultra-wide panoramic photo, aspect ratio 9:4 (3240x1440), designed to be split
into 3 equal vertical panels for an Instagram triptych.
Scene: inside a quiet mosque at dawn, sunlight streaming through an arched
window, a folded green prayer mat and wooden prayer beads on a low wooden
table, soft golden-hour light, warm cream and olive green palette, calm and
spiritual Islamic atmosphere.
Composition: LEFT third has clean empty space in the upper half for a large
headline; CENTER third features an ornate brass lantern glowing softly with
empty space above for text; RIGHT third has a small plant in a clay pot and
empty space in the lower part for a call-to-action banner.
Keep important objects away from the two vertical split lines at 1/3 and 2/3.
Photorealistic, high detail, soft shadows, no text, no letters, no watermark,
no people's faces.
```

### 6c. Variasi suasana per pekan (ganti kalimat pencahayaan)

- Pekan 1–4: `soft golden-hour sunrise light, warm amber tones`
- Pekan 5–6: `blue hour before dawn (subuh), cool soft blue light with a hint of orange on the horizon`
- Pekan 7–8: `fresh morning garden, dew on leaves, lush green tones`
- Pekan 9–10: `minimalist cream background, soft diffused morning light, beige and ivory tones`

### 6d. Prompt caption (untuk ChatGPT/Claude)

```
Kamu adalah copywriter akun Instagram dakwah @wadahqris.id (donasi & berbagi via
QRIS). Tulis caption Instagram berbahasa Indonesia, hangat dan tidak menggurui,
untuk triptych bertema: "[TEMA]", dalil: "[DALIL + SUMBER]".
Struktur: 1 kalimat hook, 3-4 kalimat renungan, 1 ajakan aksi kecil hari ini,
ajakan sedekah via QRIS di link bio, doa singkat penutup, lalu 10 hashtag.
Maksimal 150 kata. Jangan mengarang dalil tambahan di luar yang saya berikan.
```

---

## 7. Alur Kerja Mingguan

**Hari Minggu (±1,5 jam) — siapkan semua konten sepekan sekaligus:**
1. Ambil 3 tema pekan itu dari kalender (Senin, Rabu, Jumat).
2. Generate 3 gambar panorama dengan prompt master (bagian 6).
3. Di Canva, buat desain **satu kanvas 3240×1440**, taruh gambar + semua teks (hook, dalil, ajakan, bar logo). Download sebagai PNG. Simpan desain pertama sebagai **template**, pekan berikutnya tinggal ganti gambar & teks.
4. Potong jadi 3:
   - di komputer: `python3 tools/split_triptych.py 01.png` → `01_1-kiri.jpg`, `01_2-tengah.jpg`, `01_3-kanan.jpg` (butuh `pip install pillow`), atau
   - di HP: aplikasi pemotong grid (cari "grid maker" / "photo split" di App Store/Play Store), pilih potongan **3 kolom × 1 baris**.
5. Buat 2 Reels dari panorama PNG yang sama (bagian 8). Simpan di galeri/draf.
6. Siapkan caption ketiganya di Notes.

**Hari posting (Senin/Rabu/Jumat), setelah Subuh 05.00–06.00 WIB:**
1. Upload urut **3-kanan → 2-tengah → 1-kiri**, jeda 1–3 menit.
2. Caption: boleh sama untuk ketiganya, atau:
   - Post kanan: caption lengkap + ajakan QRIS
   - Post tengah: teks dalil + terjemah lengkap
   - Post kiri (paling atas di feed): hook + "Lihat 2 post sebelumnya untuk dalil & ajakannya"
3. Bagikan post kiri ke Story + stiker link wadahqris.id.

**Selasa & Kamis:** upload Reels yang sudah disiapkan (Kamis sebaiknya malam, ±19.30 WIB — malam Jumat).

---

## 8. Membuat Reels

### 8a. Aplikasi yang disarankan (semua gratis, bisa di HP)

| Aplikasi | Dipakai untuk | Catatan |
|---|---|---|
| **CapCut** (utama) | Efek geser/zoom (keyframe), teks muncul, subtitle otomatis, audio | Hapus *ending clip* CapCut sebelum ekspor. Beberapa efek berlabel "Pro" berbayar — cukup pakai yang gratis. |
| **Edits** (aplikasi resmi Instagram) | Alternatif CapCut, tanpa watermark, langsung kirim ke Instagram | Cocok kalau ingin semua dalam ekosistem Instagram. |
| **Canva** | Menyusun teks & desain, animasi teks sederhana, ekspor MP4 | Sudah kamu pakai untuk triptych, jadi template & font tetap sama. |
| Editor Reels bawaan Instagram | Tambah audio/teks cepat sebelum posting | Paling praktis, tapi fitur terbatas. |

Rekomendasi: **Canva untuk desain → CapCut untuk gerakan & audio → upload di Instagram.**

### 8b. Ukuran & zona aman
- **1080×1920 (9:16)**, durasi **7–15 detik**, 30 fps.
- Jangan taruh teks penting di **±250 px teratas**, **±350 px terbawah** (tertutup caption & tombol), dan **±120 px sisi kanan** (ikon like/komentar).
- Saat upload, **matikan "Tampilkan di grid profil / Also share to feed"** agar susunan triptych tidak bergeser. Reels tetap muncul di tab Reels & menjangkau non-follower.

### 8c. Format Reels (pilih salah satu untuk Selasa & Kamis)

1. **Panorama Geser** — paling mudah, memakai ulang triptych.
   Kamera bergerak pelan dari panel kiri → tengah → kanan, berhenti sebentar di tiap panel.
2. **Dalil Muncul Perlahan** — latar foto tenang, teks ayat/hadis muncul baris demi baris, ditutup ajakan sedekah.
3. **Voice-over** — rekam suaramu membacakan terjemah dalil (±10 detik). Terasa personal dan tidak perlu musik.
4. **Checklist Malam Jumat** (Kamis) — "Besok Jumat: ☐ Al-Kahfi ☐ Shalawat ☐ Sedekah Subuh", dicentang satu per satu.
5. **Dokumentasi Penyaluran** — video asli saat menyalurkan donasi (jika ada). Paling membangun kepercayaan. Jaga privasi penerima (tanpa wajah jelas, minta izin).
6. *(Opsional)* **Foto jadi hidup** — pakai fitur AI "image to video" (mis. di Gemini, Meta AI, atau CapCut) untuk menggerakkan api lentera, daun, atau cahaya matahari secara halus.

### 8d. Langkah "Panorama Geser" di CapCut

1. **Proyek baru** → impor PNG panorama (3240×1440, lengkap dengan teks).
2. Menu **Rasio → 9:16**.
3. Perbesar gambar sampai **tingginya memenuhi layar** dan geser sehingga **panel kiri** yang terlihat. Atur durasi klip jadi **12 detik**.
4. Tambah **keyframe** (ikon ◇+):
   - detik 0 dan 3 → posisi panel kiri
   - detik 5 dan 8 → geser ke panel tengah
   - detik 10 dan 12 → geser ke panel kanan
5. Tambah teks penutup di detik 10–12: *"Sedekah subuh via QRIS — link di bio"*.
6. **Audio** (pilih salah satu): suara alam (burung pagi, angin, gemericik air), voice-over, atau nasyid vokal tanpa alat musik — banyak audiens akun dakwah lebih nyaman dengan pilihan ini.
7. Hapus *ending clip* → **Ekspor 1080p, 30 fps**.
8. Di Instagram: pilih **sampul (cover)** yang ada judulnya, tulis caption singkat + hashtag, matikan "Tampilkan di grid profil".

### 8e. Prompt caption Reels

```
Tulis caption Reels Instagram untuk akun dakwah @wadahqris.id, tema "[TEMA]".
Maksimal 40 kata: 1 kalimat hook, 1 kalimat renungan, ajakan sedekah via QRIS
di link bio, lalu 5 hashtag. Jangan menambahkan dalil di luar: "[DALIL + SUMBER]".
```

---

## 9. Caption & Hashtag

**Template caption:**
```
[Hook 1 kalimat]

[Renungan 2–4 kalimat]

[Dalil singkat] (sumber)

✨ Aksi hari ini: [aksi kecil]
🤲 Sedekah subuh lebih mudah lewat QRIS — link di bio.

Semoga Allah menerima setiap kebaikan kita. Aamiin.
```

**Hashtag (pilih 8–12, rotasi):**
`#sedekahsubuh #sedekah #sedekahjumat #berbagikebaikan #kebaikan #infak #sedekahjariyah #qris #donasionline #dakwahislam #pengingatdiri #muslimindonesia #hijrah #jumatberkah #wadahqris`

---

## 10. Tips Tumbuh dari 0 Followers

- **Konsisten jam posting** setelah Subuh — sesuai nama "sedekah subuh" dan jadi ciri khas.
- **Reels Selasa & Kamis** jangan dilewatkan — Reels menjangkau non-follower jauh lebih luas daripada post biasa.
- **Carousel** tetap bisa: jika mau lebih banyak isi, jadikan post tengah sebuah carousel (slide 1 = panel tengah, slide 2–3 = penjelasan). Grid tetap rapi karena yang tampil slide pertama.
- Ajak interaksi: pertanyaan di P3 ("Aamiin-kan di komentar", "Tag teman").
- **Transparansi** (triptych Minggu opsional / Reels dokumentasi) membangun kepercayaan untuk akun donasi — tampilkan bukti penyaluran bila ada.
- Pastikan QRIS/akun penerima donasi jelas identitas lembaganya.

---

*Catatan: dalil dirangkum dan diterjemahkan secara ringkas. Selalu verifikasi redaksi lengkap dan teks Arab dari sumber resmi (Qur'an Kemenag, kitab hadis/aplikasi hadis terpercaya) atau konsultasikan ke ustadz sebelum publikasi.*
