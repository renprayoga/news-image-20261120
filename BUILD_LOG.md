# BUILD LOG — news-image-20261120

Entry: "The World in One Image" — Friday 20 November 2026.
Bounty: news-image-20261120, $250, 50 places paid.
Deadline: Saturday 22 November 2026, 07:00 WIB (2026-11-22T00:00:00Z).

## 1. Analisis rubrik (Protokol Top 5 — langkah 1)

Syarat gate: PNG/JPEG utuh, ≤ 1 MiB, ≤ 1024×1024 px, program jalan 2x
dengan byte identik, tanpa network, stdlib saja.

Kriteria juri (berurutan, paling penting dulu):
1. **Namakan harinya** — gambar harus menyebut tanggalnya dan berisi
   peristiwa spesifik hari itu. Gambar tanpa tanggal, atau tentang hari
   sebelum 13 Nov 2026, kalah dari gambar mana pun yang memenuhi.
   → Masthead + bar tanggal hitam besar "FRIDAY 20 NOVEMBER 2026" di
   posisi paling atas, mustahil terlewat.
2. **Seleksi & keluasan** — cerita paling berdampak, lintas wilayah dan
   bidang, bukan satu negara atau satu beat.
   → 4 cerita: hukum internasional (Den Haag), geopolitik AS–Iran,
   bencana alam India, hiburan global (GTA 6) + strip ALSO (Timur Tengah,
   Ukraina). Lima wilayah, empat bidang.
3. **Terbaca** — orang yang ketinggalan berita hari itu bisa paham hanya
   dari gambar; tiap cerita jelas dari gambar + label pendek; tidak ada
   yang kontradiktif atau salah.
   → Satu cerita hero besar + tiga baris dengan judul tebal dan 1–2 baris
   subteks faktual; tiap baris punya ikon geometris yang menjelaskan
   isinya (timbangan, jam pasir, siklon, kontroler game).
4. **Setia pada fakta** — apa yang terjadi, seperti dilaporkan, tanpa hype
   atau spekulasi sebagai fakta.
   → Semua angka dan kutipan diambil dari laporan yang terverifikasi
   (lihat daftar fakta di bawah); tidak ada prediksi atau klaim tambahan.
5. **Kerapian** — satu komposisi jelas, terbaca pada ~300 px, tanpa noda
   atau teks kacau.
   → Grid koran kaku (masthead → hero → 3 baris → ALSO → footer),
   kontras tinggi (tinta gelap di kertas krem, panel hero navy dengan
   teks putih), semua teks diukur dengan `textlength` dan di-wrap agar
   tidak pernah terpotong.

## 2. Optimasi algoritma (langkah 2)

- Renderer `draw.py` murni prosedural: semua koordinat, warna, dan teks
  adalah konstanta; tidak ada pencarian, tidak ada brute force, tidak ada
  perulangan atas data. Kompleksitas O(piksel) sekali jalan — menggambar
  1024×1024 langsung, tanpa pass tambahan.
- `main.py` tidak me-render ulang: hanya `shutil.copyfile` byte demi byte.
  Ini menghilangkan seluruh kelas risiko non-determinisme (font, antialias,
  versi Pillow) dari dua run grader: byte yang disubmit adalah byte yang
  sudah diverifikasi di sini.
- PNG ditulis tanpa metadata waktu (Pillow tidak menulis tEXt/chunk waktu
  secara default), sehingga render ulang menghasilkan byte identik.
- Ikon digambar dari primitif PIL (polygon, pieslice, arc,
  rounded_rectangle) — nol aset eksternal, nol hak cipta pihak ketiga,
  nol dependensi font di runtime grader (font hanya dipakai saat render
  di sini, bukan saat `main.py` jalan).

## 3. Uji kasus ekstrem (langkah 3)

- **Tanpa network:** tidak ada satu pun panggilan network di `draw.py`
  maupun `main.py`; font dibaca dari path sistem lokal saat render.
- **Tanpa randomness:** tidak ada `random`, `time`, atau `os.urandom`;
  tidak ada dict/set yang urutannya memengaruhi output.
- **Byte-identik:** `main.py` dijalankan 2x ke dua folder berbeda;
  sha256 keduanya harus sama (dicatat di bawah). Render `draw.py` dua
  kali juga menghasilkan byte yang sama.
- **Batas ukuran:** entry.png harus tepat 1024×1024 dan ≤ 1.048.576 byte
  (dicatat di bawah; PNG datar dengan palet terbatas jauh di bawah batas).
- **Teks terpotong:** semua teks di-wrap dengan pengukuran `textlength`
  terhadap lebar kolom yang tersedia; subteks dibatasi 2–3 baris dan
  headline hero 3 baris pendek yang sudah diukur muat.
- **Keterbacaan 300 px:** headline hero 56 px, judul baris 29 px, subteks
  21 px — pada skala 300 px headline ≈ 16 px, masih terbaca; bar tanggal
  26 px tebal putih di atas hitam.
- **Edge case input:** tidak ada input eksternal sama sekali — program
  tidak membaca file selain `entry.png` yang sudah ada di repo.

## 4. Cara kerja kode

- `draw.py:render()` membangun `Image` RGB 1024×1024 warna kertas,
  lalu menggambar berurutan: masthead serif tebal, garis merah + hitam,
  bar tanggal hitam, panel hero navy (ikon timbangan keadilan dari
  `draw_scales`, kicker emas, headline 3 baris, subteks ter-wrap,
  baris fakta), tiga baris berita (`draw_row`: kotak ikon tinted +
  kicker merah + judul + subteks), strip ALSO navy gelap, footer sumber.
- `draw.py:wrap()` melakukan greedy word-wrap berdasarkan lebar piksel
  sebenarnya dari font yang dipakai.
- `main.py` membaca `MAKEFUN_OUTPUT_DIR` (default `./output/`), membuat
  folder bila belum ada, lalu `shutil.copyfile(entry.png → entry.png)`.

## 5. Fakta & sumber tiap cerita

| Cerita | Fakta yang dipakai | Sumber |
|---|---|---|
| ICJ: Myanmar bersalah genosida Rohingya | Putusan Kamis 19 Nov 2026, Den Haag; voting 9–6; pertama kali dalam 80 tahun ICJ sebuah negara dinyatakan bertanggung jawab atas genosida; ~10.000 Rohingya dibunuh dalam "clearance operations" 2017 di Rakhine; reparasi diperintahkan + laporan dalam 2 tahun; kasus diajukan Gambia (2019) | CNN, Le Monde, Reuters |
| Trump: no new Iran strikes before 2027 | Kamis 19 Nov, dari Air Force One sepulang China; "We'll see what happens after the beginning of the year" / "I am not rushing into any decision"; Israel menekan serangan baru; keputusan ditunda ke tahun depan | Reuters, Axios |
| Cyclone Akvan hits Odisha | Jumat 20 Nov ~tengah hari IST, mendarat dekat Gopalpur; angin 90–100 km/jam (gust 110); 105.304 orang dievakuasi ke 1.224 shelter; target zero-casualty; red alert di 11 distrik | IMD, The Hindu |
| GTA 6 sales pass $1.8 billion | Penjualan minggu peluncuran (rilis sedunia 19 Nov, PS5/Xbox) melampaui $1,80 miliar; melewati total box office global film The Odyssey | (laporan penjualan peluncuran) |
| ALSO | Houthi serang Riyadh, menara Saudi PIF rusak; serangan Rusia merusak kedutaan Austria & Belanda di Kyiv; Eropa siap berunding dengan Rusia soal akhir perang Ukraina | BBC |

## 6. Verifikasi

- `python3 draw.py` → entry.png 1024×1024, **141.306 byte** (≤ 1.048.576),
  sha256 `cef8fd6aea363ad6c684fcfb2061967e971dd8d0dda3ad70ad4ed0c33d337f67`.
- Render deterministik: `draw.py` dijalankan 3x (render ulang via modul)
  menghasilkan sha256 yang sama persis.
- `main.py` 2x ke `/tmp/outA` dan `/tmp/outB` → sha256 **identik**
  `cef8fd6a…337f67` di kedua folder dan sama dengan `entry.png` di repo.
- Inspeksi visual (2x baca entry.png sebagai gambar):
  - Render pertama: baris fakta hero terpotong ("CASE BROUGHT BY TH…")
    dan strip ALSO kehilangan kata terakhir ("war") — keduanya karena
    teks melebihi lebar kolom.
  - Revisi (thinking_revised): baris fakta diperpendek dan font diturunkan
    ke 17 px setelah diukur muat 596/658 px; teks ALSO diperpendek
    ("Russian strikes damage embassies in Kyiv") sehingga muat 2 baris.
  - Render kedua: SEMUA teks lengkap dan terbaca — masthead, bar tanggal,
    headline hero + subteks 3 baris + baris fakta, ketiga baris cerita
    (judul + 2 baris subteks), strip ALSO 2 baris lengkap, footer sumber.
    Tidak ada teks terpotong, tertutup, atau bertumpuk.
- File di `entry/`: tepat 7 file yang diminta (`.makefun/owner.json`,
  `BUILD_LOG.md`, `LICENSE`, `README.md`, `draw.py`, `entry.png`,
  `main.py`) — tidak ada file kit starter, tidak ada file edisi lama.
  (`__pycache__` yang sempat muncul dari cek determinisme sudah dihapus.)
- README: 3 badge, semuanya terbungkus link ke
  `https://make.fun/bounty/news-image-20261120`; 0 badge telanjang.
- LICENSE: baris pertama `SPDX-License-Identifier: MIT`, copyright 2026
  renprayoga.
- `.makefun/owner.json`: satu baris JSON, wallet
  `6VezNKQwb6Shp7gfHiD89FPLxkegXn2Mfah4csHZtNuc`.
