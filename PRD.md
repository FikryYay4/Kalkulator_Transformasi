# prd.md

# Product Requirements Document (PRD)
## Aplikasi Web Kalkulator Canggih Berbasis Flask

---

# 1. Visi Produk

Membangun aplikasi web kalkulator modern berbasis Flask yang mampu melakukan:
- Operasi matematika lanjutan
- Operasi logika digital
- Transformasi dan konversi bilangan
- Menampilkan langkah-langkah penyelesaian secara edukatif

Aplikasi ditujukan untuk tugas kuliah Teknik Informatika semester 2 dengan tampilan profesional, responsif, dan mudah dipahami.

---

# 2. Tujuan Produk

## Tujuan Utama
- Membantu mahasiswa memahami proses perhitungan matematika dan logika.
- Menyediakan kalkulator multifungsi dalam satu aplikasi web.
- Menampilkan langkah-langkah penyelesaian secara detail.
- Menjadi project tugas akhir yang siap presentasi dan siap cetak laporan.

## Target Outcome
- Semua fitur berjalan tanpa error di localhost.
- UI responsif desktop dan mobile.
- Dark/Light mode berjalan dengan baik.
- Riwayat perhitungan tersimpan selama sesi aplikasi berjalan.

---

# 3. Target Pengguna

## Pengguna Utama
- Mahasiswa Teknik Informatika semester awal.
- Dosen penguji tugas pemrograman web.
- Pengguna umum yang membutuhkan kalkulator multifungsi.

## Karakteristik Pengguna
- Familiar dengan operasi matematika dasar.
- Membutuhkan visualisasi langkah perhitungan.
- Mengakses aplikasi melalui laptop maupun smartphone.

---

# 4. Scope MVP

## Fitur Wajib

### 4.1 Operasi Aritmatika
Aplikasi wajib mendukung:
- Penjumlahan (+)
- Pengurangan (-)
- Perkalian (×)
- Pembagian (÷)
- Pangkat
- Akar
- Modulus
- Floor Division

### 4.2 Operator Logika
Aplikasi wajib mendukung:
- AND
- OR
- NOT
- XOR
- NAND
- NOR

### 4.3 Transformasi Bilangan

#### Konversi Basis
- Decimal ↔ Binary
- Decimal ↔ Octal
- Decimal ↔ Hexadecimal

#### Konversi Suhu
- Celsius
- Fahrenheit
- Kelvin
- Réaumur

#### Konversi Mata Uang
Menggunakan kurs statis:
- IDR → USD
- IDR → EUR
- IDR → SGD
- IDR → MYR

### 4.4 Fitur Bonus
- Faktorial
- Deret Fibonacci

### 4.5 Riwayat Perhitungan
Setiap hasil wajib:
- Menampilkan rumus
- Menampilkan langkah penyelesaian
- Menyimpan histori perhitungan

### 4.6 UI/UX
- Dark mode & light mode
- Mobile responsive
- Navigasi sederhana
- Bootstrap 5 interface

---

# 5. Kebutuhan Fungsional

## RF-01: Input Perhitungan
Pengguna dapat memasukkan angka dan memilih operasi.

## RF-02: Hasil Perhitungan
Sistem menampilkan:
- Hasil akhir
- Formula yang digunakan
- Langkah-langkah penyelesaian

## RF-03: Riwayat
Sistem menyimpan histori perhitungan selama sesi aktif.

## RF-04: Konversi Bilangan
Pengguna dapat mengubah basis bilangan.

## RF-05: Konversi Suhu
Pengguna dapat mengubah satuan suhu.

## RF-06: Konversi Mata Uang
Pengguna dapat menghitung nilai tukar berdasarkan rate statis.

## RF-07: Dark/Light Mode
Pengguna dapat mengganti tema tampilan.

## RF-08: Responsive Layout
Tampilan harus menyesuaikan ukuran layar.

---

# 6. Kebutuhan Non-Fungsional

## Performance
- Respon kalkulasi < 1 detik.

## Compatibility
- Chrome
- Edge
- Firefox

## Security
- Validasi input angka.
- Mencegah crash akibat input kosong.

## Maintainability
- Struktur folder rapi.
- Modular Flask routes.

## Accessibility
- Kontras warna memadai.
- Tombol mudah diakses pada mobile.

---

# 7. Arsitektur Sistem

## Backend
- Python 3
- Flask

## Frontend
- HTML5
- CSS3
- Bootstrap 5
- JavaScript
- Jinja2

## Struktur MVC Sederhana
- app.py → controller + logic
- templates/ → view
- static/ → assets

---

# 8. User Flow

## Flow Utama
1. User membuka aplikasi.
2. User memilih kategori kalkulator.
3. User memasukkan nilai input.
4. User menekan tombol hitung.
5. Sistem menampilkan:
   - hasil
   - rumus
   - langkah
   - histori

---

# 9. Desain Antarmuka

## Halaman Utama
- Navbar
- Menu kategori
- Card fitur
- Riwayat perhitungan

## Halaman Perhitungan
- Form input
- Tombol proses
- Area hasil
- Penjelasan langkah

## Tema
- Dark mode
- Light mode

---

# 10. Roadmap Pengembangan

## Minggu 1
- Setup Flask
- Struktur project
- Routing dasar

## Minggu 2
- Implementasi operasi aritmatika
- Implementasi logika

## Minggu 3
- Implementasi transformasi bilangan
- Riwayat perhitungan

## Minggu 4
- Styling Bootstrap
- Dark mode
- Responsive testing
- Penyusunan laporan

---

# 11. Future Improvements

- Grafik matematika
- Scientific calculator
- Penyimpanan database
- Login user
- Export PDF hasil perhitungan
- API kurs realtime

---

# 12. Success Metrics

Aplikasi dianggap berhasil jika:
- Semua fitur wajib berjalan.
- Tidak ada error saat testing.
- UI responsive.
- Dark mode aktif.
- Histori tampil.
- Dapat dijalankan di localhost menggunakan Flask.

---

# 13. Acceptance Criteria

## Aplikasi dinyatakan selesai apabila:
- Semua operasi aritmatika valid.
- Semua operator logika berjalan.
- Konversi basis akurat.
- Konversi suhu akurat.
- Konversi mata uang sesuai rate statis.
- Riwayat tampil otomatis.
- Penjelasan langkah muncul.
- Bootstrap responsive aktif.
- Dark/light mode berjalan normal.