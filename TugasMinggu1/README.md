# H1D024093-PraktikumKB-Pertemuan1
Program Python untuk menganalisis data suhu harian. Data disimpan dalam file CSV, dilengkapi fitur statistik deskriptif, visualisasi grafik, dan regresi linear untuk melihat tren suhu.

## Konsep yang Diimplementasikan
- **Struktur kontrol**: if-elif-else, loop while, for, break
- **Struktur data**: list, dictionary, set
- **Library eksternal**:
  - `numpy` : pembangkitan data dummy dan regresi linear
  - `matplotlib` : visualisasi grafik suhu
- **Library bawaan**: csv, statistics, datetime, os

## Fitur
- Tambah data suhu manual (dengan validasi tanggal)
- Generate data dummy 30 hari terakhir (menggunakan numpy.random.normal)
- Tampilkan semua data dalam bentuk tabel rapi
- Statistik deskriptif (rata-rata, median, modus, max, min, rentang, standar deviasi)
- Grafik suhu harian + garis tren linear (regresi)
- Ubah data pada tanggal tertentu
- Hapus data pada tanggal tertentu
- Data otomatis tersimpan dalam file `data_cuaca.csv`

## Instalasi
1. Python 3
2. Install library yang diperlukan:
   ```bash
   pip install numpy matplotlib
