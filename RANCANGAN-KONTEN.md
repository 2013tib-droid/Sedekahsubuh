# Rancangan Konten Instagram @wadahqris.id — Triptych Harian

> Format: **1 tema = 3 post (triptych)** yang menyatu jadi satu baris di grid.
> Frekuensi: **1 triptych per hari**, diunggah setelah Subuh.
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

Potong kanvas otomatis: `python3 tools/split_triptych.py gambar.png` (lihat bagian 7), atau di Canva pakai 3 halaman 1080×1440 dengan gambar yang digeser.

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
- **Variasi warna per pekan** (opsional): pekan 1 fajar keemasan, pekan 2 biru subuh, pekan 3 hijau taman, pekan 4 krem minimalis. Dari jauh grid akan terlihat seperti "bab-bab".

---

## 4. Pilar Konten Mingguan

| Hari | Pilar | Isi |
|---|---|---|
| Senin | **Dalil Sedekah** | Ayat/hadis keutamaan sedekah |
| Selasa | **Kisah Teladan** | Kisah Nabi ﷺ, sahabat, orang saleh yang dermawan |
| Rabu | **Kebaikan Kecil** | Sedekah non-materi: senyum, menolong, ilmu |
| Kamis | **Amalan Sunnah** | Puasa Senin-Kamis, dzikir pagi, persiapan Jumat |
| Jumat | **Jumat Berkah** | Ajakan sedekah Jumat, Al-Kahfi, shalawat |
| Sabtu | **Edukasi Praktis** | Cara sedekah via QRIS, adab berbagi, niat |
| Minggu | **Refleksi & Transparansi** | Muhasabah pekan ini + laporan/penyaluran donasi (jika ada) |

---

## 5. Kalender 30 Hari

> Sebelum posting, **cek ulang teks Arab & terjemahan** di sumber resmi (Qur'an Kemenag: quran.kemenag.go.id; hadis: nomor sesuai kitab yang disebut). Nomor hadis di bawah mengikuti penomoran umum (Fu'ad Abdul Baqi / Tirmidzi Syakir).

### Pekan 1 — "Pagi yang Berkah" (fajar keemasan)

**Hari 1 (Sen) — Dua Malaikat di Waktu Pagi**
- P1: *Setiap pagi, ada doa yang turun untukmu.*
- P2: HR. Bukhari 1442 & Muslim 1010 — "Tidak ada satu hari pun ketika hamba berada di pagi hari, kecuali dua malaikat turun. Salah satunya berdoa: 'Ya Allah, berilah ganti bagi orang yang berinfak.' Yang lain berdoa: 'Ya Allah, berilah kehancuran bagi orang yang menahan (hartanya).'"
- P3: *Jadikan sedekah pertamamu hari ini sebelum matahari terbit.*
- Visual: jendela masjid saat fajar, cahaya masuk, sajadah.

**Hari 2 (Sel) — Kurma Setengah Butir**
- P1: *Tak punya banyak? Setengah kurma pun cukup.*
- P2: HR. Bukhari 1417 & Muslim 1016 — "Jagalah diri kalian dari api neraka walau hanya dengan (bersedekah) separuh kurma."
- P3: *Mulai dari Rp1.000. Yang penting istiqamah.*
- Visual: piring kayu berisi kurma, gelas air, cahaya pagi.

**Hari 3 (Rab) — Senyum Itu Sedekah**
- P1: *Sedekah paling ringan ada di wajahmu.*
- P2: HR. Tirmidzi 1956 — "Senyummu di hadapan saudaramu adalah sedekah bagimu."
- P3: *Hari ini: senyumi 3 orang yang kamu temui.*
- Visual: dua cangkir teh berhadapan di teras, bunga kecil.

**Hari 4 (Kam) — Doa Setelah Subuh**
- P1: *Tiga hal yang diminta Nabi ﷺ setiap pagi.*
- P2: HR. Ibnu Majah 925 — "Allahumma innī as'aluka 'ilman nāfi'an, wa rizqan ṭayyiban, wa 'amalan mutaqabbalan." (Ya Allah, aku memohon ilmu yang bermanfaat, rezeki yang baik, dan amal yang diterima.)
- P3: *Baca selepas salam Subuh. Simpan post ini sebagai pengingat.*
- Visual: tangan menengadah berdoa (siluet), tasbih, mushaf.

**Hari 5 (Jum) — Jumat Berkah**
- P1: *Jumat: hari terbaik untuk berbagi.*
- P2: QS. Al-Baqarah: 261 — perumpamaan infak seperti sebutir benih yang menumbuhkan tujuh tangkai, tiap tangkai seratus biji.
- P3: *Sisihkan sedekah Jumat-mu lewat QRIS di bio.*
- Visual: lentera, sajadah hijau, cahaya hangat (seperti post lentera kamu).

**Hari 6 (Sab) — Cara Sedekah via QRIS**
- P1: *Sedekah cuma butuh 10 detik.*
- P2: Langkah: buka e-wallet/m-banking → scan QRIS → isi nominal → niatkan karena Allah.
- P3: *Scan, niat, kirim. Pahala mengalir.* + mockup ponsel dengan QRIS.
- Visual: ponsel di meja kayu, secangkir kopi, notes.

**Hari 7 (Min) — Muhasabah Pekan Ini**
- P1: *Sudah berapa kebaikan kita pekan ini?*
- P2: QS. Az-Zalzalah: 7 — "Barangsiapa mengerjakan kebaikan seberat zarrah, niscaya dia akan melihat (balasan)nya."
- P3: *Tulis 1 kebaikan yang ingin kamu lanjutkan pekan depan di kolom komentar.*
- Visual: jurnal terbuka, pena, daun kering, sinar pagi.

### Pekan 2 — "Harta yang Tak Pernah Berkurang" (biru subuh)

**Hari 8 (Sen) — Sedekah Tidak Mengurangi Harta**
- P1: *Memberi tidak akan membuatmu miskin.*
- P2: HR. Muslim 2588 — "Sedekah tidak akan mengurangi harta."
- P3: *Percayakan hitungannya kepada Allah.*
- Visual: toples kaca berisi koin, tanaman tumbuh dari dalamnya.

**Hari 9 (Sel) — Kisah Abu Bakar & Umar**
- P1: *Umar memberi separuh. Abu Bakar memberi semuanya.*
- P2: Kisah infak Perang Tabuk (HR. Abu Dawud 1678, Tirmidzi 3675): "Apa yang kau sisakan untuk keluargamu?" — "Aku sisakan untuk mereka Allah dan Rasul-Nya."
- P3: *Kita mungkin tak sanggup semuanya. Tapi bisa mulai dari sebagian.*
- Visual: gurun saat fajar, siluet unta di kejauhan.

**Hari 10 (Rab) — Setiap Sendi Ada Sedekahnya**
- P1: *Tubuhmu punya "tagihan" sedekah setiap hari.*
- P2: HR. Bukhari 2989 & Muslim 1009 — setiap persendian wajib bersedekah setiap hari; mendamaikan dua orang, membantu orang naik kendaraan, kata yang baik, menyingkirkan gangguan dari jalan adalah sedekah.
- P3: *Hari ini: singkirkan satu gangguan dari jalan.*
- Visual: jalan setapak pagi berkabut, daun berguguran.

**Hari 11 (Kam) — Puasa Senin-Kamis**
- P1: *Amal diangkat hari Senin & Kamis.*
- P2: HR. Tirmidzi 747 — "Amal-amal diperlihatkan (kepada Allah) setiap Senin dan Kamis, maka aku suka amalku diperlihatkan saat aku berpuasa."
- P3: *Puasa + sedekah = paket lengkap hari ini.*
- Visual: meja sahur sederhana, lampu temaram, jam menunjukkan 04.15.

**Hari 12 (Jum) — Allah Mengganti**
- P1: *Yang kamu beri, Allah ganti.*
- P2: QS. Saba': 39 — "…Dan apa saja yang kamu infakkan, Allah akan menggantinya, dan Dialah pemberi rezeki yang terbaik."
- P3: *Jumat ini, berbagi untuk yang membutuhkan.*
- Visual: tangan memberi bingkisan, bokeh biru pagi.

**Hari 13 (Sab) — Adab Bersedekah**
- P1: *Sedekah yang baik punya adab.*
- P2: QS. Al-Baqarah: 264 — janganlah merusak sedekahmu dengan menyebut-nyebutnya dan menyakiti perasaan penerima.
- P3: 3 adab: ikhlas, tidak mengungkit, beri yang terbaik.
- Visual: amplop putih di atas meja, bunga melati.

**Hari 14 (Min) — Refleksi & Laporan**
- P1: *Terima kasih, orang-orang baik.*
- P2: Ringkasan donasi/penyaluran pekan ini (atau kutipan QS. Ibrahim: 7 tentang syukur jika belum ada laporan).
- P3: *Kebaikanmu sampai. Mari lanjutkan.*
- Visual: kardus sembako, anak-anak tersenyum (ilustrasi, tanpa wajah jelas).

### Pekan 3 — "Kebaikan yang Terus Mengalir" (hijau taman)

**Hari 15 (Sen) — Sedekah Jariyah**
- P1: *Ada amal yang tetap hidup setelah kita tiada.*
- P2: HR. Muslim 1631 — "Apabila manusia meninggal, terputuslah amalnya kecuali tiga: sedekah jariyah, ilmu yang bermanfaat, atau anak saleh yang mendoakannya."
- P3: *Wakaf Al-Qur'an, sumur, atau buku — pilih satu.*
- Visual: pohon besar rindang, akar kuat, cahaya menembus daun.

**Hari 16 (Sel) — Utsman & Sumur Rumah**
- P1: *Satu sumur, pahala sepanjang zaman.*
- P2: Kisah Utsman bin Affan membeli sumur Rumah dan mewakafkannya untuk kaum muslimin (HR. Tirmidzi 3703, An-Nasa'i 3608).
- P3: *Air bersih adalah sedekah terbaik — ayo ikut berbagi.*
- Visual: sumur batu tua, ember kayu, air berkilau.

**Hari 17 (Rab) — Menunjukkan Kebaikan**
- P1: *Share post ini juga bisa jadi pahala.*
- P2: HR. Muslim 1893 — "Barangsiapa menunjukkan suatu kebaikan, maka ia mendapat pahala seperti pahala orang yang mengerjakannya."
- P3: *Kirim ke 1 teman yang ingin rutin sedekah.*
- Visual: dua tangan memegang bibit tanaman bersama.

**Hari 18 (Kam) — Sedekah Rahasia**
- P1: *Sedekah terbaik: tangan kiri pun tak tahu.*
- P2: HR. Bukhari 1423 & Muslim 1031 — di antara tujuh golongan yang dinaungi Allah: orang yang bersedekah lalu menyembunyikannya hingga tangan kirinya tidak tahu apa yang diinfakkan tangan kanannya.
- P3: *QRIS memudahkan sedekah diam-diam. Cukup kamu dan Allah yang tahu.*
- Visual: amplop diselipkan di bawah pintu, cahaya pagi.

**Hari 19 (Jum) — Shalawat & Al-Kahfi**
- P1: *Jumat: jangan lupa tiga amalan ini.*
- P2: Membaca Al-Kahfi (HR. Al-Hakim, disahihkan Al-Albani), memperbanyak shalawat (HR. Abu Dawud 1047), dan sedekah.
- P3: *Checklist Jumat: ☐ Al-Kahfi ☐ Shalawat ☐ Sedekah*
- Visual: mushaf terbuka di rehal, tasbih, lentera.

**Hari 20 (Sab) — Niat**
- P1: *Semua dimulai dari niat.*
- P2: HR. Bukhari 1 & Muslim 1907 — "Sesungguhnya amal itu tergantung niatnya."
- P3: Contoh niat sedekah singkat: *"Aku bersedekah karena Allah Ta'ala."*
- Visual: kompas di meja kayu, arah kiblat, matahari terbit.

**Hari 21 (Min) — Muhasabah**
- P1: *Kebaikan kecil yang konsisten mengalahkan yang besar tapi sesekali.*
- P2: HR. Bukhari 6464 & Muslim 783 — "Amalan yang paling dicintai Allah adalah yang paling kontinu walaupun sedikit."
- P3: *Tantangan: sedekah subuh 7 hari berturut-turut. Siap?*
- Visual: tetesan air di batu (melubangi batu perlahan).

### Pekan 4 — "Memberi dari yang Dicintai" (krem minimalis)

**Hari 22 (Sen) — Harta yang Dicintai**
- P1: *Kebajikan sempurna ada di balik yang paling berat dilepas.*
- P2: QS. Ali 'Imran: 92 — "Kamu tidak akan memperoleh kebajikan sebelum kamu menginfakkan sebagian harta yang kamu cintai."
- P3: *Apa yang paling kamu sayangi? Bagikan sebagiannya.*
- Visual: kotak kado kayu terbuka, pita, cahaya lembut.

**Hari 23 (Sel) — Abu Thalhah & Kebun Bairuha**
- P1: *Ia serahkan kebun terbaiknya dalam sekali dengar.*
- P2: Kisah Abu Thalhah menyedekahkan kebun Bairuha setelah turun QS. Ali 'Imran: 92 (HR. Bukhari 1461, Muslim 998).
- P3: *Respons terbaik untuk ayat adalah amal.*
- Visual: kebun kurma saat pagi, sinar menembus pelepah.

**Hari 24 (Rab) — Ilmu Juga Sedekah**
- P1: *Tak punya harta? Bagikan ilmumu.*
- P2: HR. Muslim 1631 (ilmu yang bermanfaat termasuk amal yang terus mengalir).
- P3: *Ajarkan satu hal baik hari ini — walau satu ayat.*
- Visual: tumpukan buku, kacamata, secangkir teh.

**Hari 25 (Kam) — Sedekah Saat Sehat**
- P1: *Jangan tunggu kaya untuk mulai memberi.*
- P2: HR. Bukhari 1419 & Muslim 1032 — sedekah paling utama adalah saat engkau sehat, sedang mengharapkan kaya dan takut miskin.
- P3: *Sekarang, bukan nanti.*
- Visual: jam pasir di meja kayu, cahaya pagi.

**Hari 26 (Jum) — Pinjaman kepada Allah**
- P1: *Allah menawarkan "pinjaman" dengan balasan berlipat.*
- P2: QS. Al-Baqarah: 245 — "Barangsiapa meminjamkan kepada Allah dengan pinjaman yang baik, maka Allah akan melipatgandakan pembayaran kepadanya…"
- P3: *Sedekah Jumat: scan QRIS di link bio.*
- Visual: lentera + timbangan kecil, nuansa krem.

**Hari 27 (Sab) — Sedekah untuk Keluarga**
- P1: *Nafkah untuk keluarga juga bernilai sedekah.*
- P2: HR. Bukhari 55 & Muslim 1002 — "Apabila seseorang menafkahkan (hartanya) untuk keluarganya dengan mengharap pahala, maka itu sedekah baginya."
- P3: *Traktir orang tuamu sarapan pagi ini.*
- Visual: meja makan keluarga pagi hari, nasi hangat, teh.

**Hari 28 (Min) — Memberi Makan**
- P1: *Kami memberi makan hanya karena Allah.*
- P2: QS. Al-Insan: 8–9 — memberi makan orang miskin, anak yatim, dan tawanan, "…kami tidak mengharap balasan dan terima kasih darimu."
- P3: *Pekan depan: program berbagi sarapan subuh.* (sesuaikan program nyata)
- Visual: bungkusan nasi tertata rapi, cahaya fajar.

**Hari 29 (Sen) — Sebelum Terlambat**
- P1: *"Ya Rabb, andai Engkau tunda ajalku sebentar saja…"*
- P2: QS. Al-Munafiqun: 10 — infakkan sebagian rezeki sebelum datang kematian, lalu ia berkata: "…aku akan bersedekah dan termasuk orang-orang saleh."
- P3: *Jangan jadi orang yang menyesal. Mulai hari ini.*
- Visual: matahari terbit di cakrawala, jalan panjang.

**Hari 30 (Sel) — Penutup Bulan**
- P1: *30 hari, 30 alasan untuk terus berbagi.*
- P2: HR. Tirmidzi 614 — "Sedekah memadamkan kesalahan sebagaimana air memadamkan api."
- P3: *Terima kasih sudah menemani 30 hari ini. Bulan depan kita lanjut!*
- Visual: kolase kecil 3 objek ikonik bulan ini (lentera, cangkir, tanaman).

> Hari 31 dst: ulangi pilar mingguan dengan dalil/kisah baru, atau sesuaikan dengan momen (Ramadhan, Idul Adha, 10 Muharram, Maulid, bencana alam).

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

### 6b. Contoh terisi (Hari 1)

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

- Pekan 1: `soft golden-hour sunrise light, warm amber tones`
- Pekan 2: `blue hour before dawn (subuh), cool soft blue light with a hint of orange on the horizon`
- Pekan 3: `fresh morning garden, dew on leaves, lush green tones`
- Pekan 4: `minimalist cream background, soft diffused morning light, beige and ivory tones`

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

## 7. Alur Kerja Harian (±30 menit)

1. **Malam sebelumnya**: buka kalender di atas, generate gambar dengan prompt master.
2. Potong jadi 3: `python3 tools/split_triptych.py hari01.png` → hasil `hari01_1-kiri.jpg`, `hari01_2-tengah.jpg`, `hari01_3-kanan.jpg`.
   (Butuh Pillow: `pip install pillow`.)
3. Tambahkan teks di Canva (template 1080×1440 yang disimpan, tinggal ganti teks).
4. **Setelah Subuh (05.00–06.00 WIB)** upload: **3-kanan → 2-tengah → 1-kiri**.
5. Caption: boleh sama untuk ketiganya, atau:
   - Post kanan: caption lengkap + ajakan QRIS
   - Post tengah: teks dalil + terjemah lengkap
   - Post kiri (paling terakhir, yang paling atas di feed): caption hook + "Geser ke 2 post sebelumnya untuk dalil & ajakannya"
6. Story: bagikan post kiri ke Story + stiker link ke wadahqris.id.

---

## 8. Caption & Hashtag

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

## 9. Tips Tumbuh dari 0 Followers

- **Konsisten jam posting** setelah Subuh — sesuai nama "sedekah subuh" dan jadi ciri khas.
- Aktifkan **Reels** 2–3x seminggu: video 7–10 detik dari gambar yang sama (zoom pelan + nasyid/tanpa musik + teks). Reels menjangkau non-follower jauh lebih luas.
- **Carousel** tetap bisa: jika mau lebih banyak isi, jadikan post tengah sebuah carousel (slide 1 = panel tengah, slide 2–3 = penjelasan). Grid tetap rapi karena yang tampil slide pertama.
- Ajak interaksi: pertanyaan di P3 ("Aamiin-kan di komentar", "Tag teman").
- **Transparansi** (hari Minggu) membangun kepercayaan untuk akun donasi — tampilkan bukti penyaluran bila ada.
- Pastikan QRIS/akun penerima donasi jelas identitas lembaganya.

---

*Catatan: dalil dirangkum dan diterjemahkan secara ringkas. Selalu verifikasi redaksi lengkap dan teks Arab dari sumber resmi (Qur'an Kemenag, kitab hadis/aplikasi hadis terpercaya) atau konsultasikan ke ustadz sebelum publikasi.*
