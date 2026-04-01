# Analisis Data Cuaca Harian

Program CLI (Command Line Interface) berbasis Python untuk mencatat, mengelola, menganalisis, dan memvisualisasikan data suhu cuaca harian. Program ini menyimpan data secara lokal menggunakan format CSV dan dilengkapi dengan fitur statistik dasar serta pembuatan grafik tren suhu.

## Fitur Utama

1. **Tambah Data Manual**: Memasukkan data tanggal (YYYY-MM-DD) dan suhu (°C) secara manual.
2. **Generate Data Dummy**: Menghasilkan data suhu acak (distribusi normal) untuk 30 hari terakhir secara otomatis, sangat berguna untuk keperluan pengujian (testing).
3. **Tampilkan Semua Data**: Menampilkan riwayat rekaman suhu dalam bentuk tabel yang rapi di terminal.
4. **Tampilkan Statistik**: Menghitung secara otomatis matriks statistik penting, termasuk:
   * Rata-rata (Mean)
   * Nilai tengah (Median)
   * Nilai yang sering muncul (Modus)
   * Suhu Tertinggi (Max) & Terendah (Min)
   * Rentang (Range)
   * Standar Deviasi
5. **Tampilkan Grafik**: Memvisualisasikan pergerakan suhu harian menggunakan `matplotlib`, lengkap dengan garis tren linear (linear trendline) yang dihitung menggunakan `numpy`.
6. **Ubah Data**: Memperbarui atau merevisi data suhu pada tanggal tertentu.
7. **Hapus Data**: Menghapus rekaman data pada tanggal tertentu.

## Persyaratan Sistem (Prerequisites)

Pastikan Anda telah menginstal **Python** di sistem Anda. Program ini menggunakan beberapa pustaka bawaan Python (`csv`, `statistics`, `datetime`, `os`) dan membutuhkan dua pustaka eksternal:

* `numpy` (Untuk perhitungan matematika dan pembuatan data dummy)
* `matplotlib` (Untuk visualisasi grafik)

## Instalasi & Persiapan

1. **Clone atau Unduh** file *script* Python ini ke dalam direktori lokal Anda.
2. Buka terminal atau *command prompt*.
3. Instal dependensi eksternal yang dibutuhkan dengan menjalankan perintah berikut:

    ```bash
    pip install numpy matplotlib
    ```

## Cara Penggunaan

1. Jalankan *script* Python melalui terminal:

    ```bash
    python analisiscuaca.py
    ```

2. Saat program berjalan, sistem akan secara otomatis membuat file bernama `data_cuaca.csv` di direktori yang sama (jika belum ada) untuk menyimpan data.
3. Ikuti instruksi pada menu interaktif di layar dengan mengetikkan angka `1` hingga `8`.

### Contoh Tampilan Menu Utama:
    ```text
    === ANALISIS DATA CUACA HARIAN ===
    1. Tambah data manual
    2. Generate data dummy (30 hari terakhir)
    3. Tampilkan semua data
    4. Tampilkan statistik
    5. Tampilkan grafik (dengan tren linear)
    6. Ubah data
    7. Hapus data
    8. Keluar
    Pilih menu (1-8): 
    ```

## Penyimpanan Data
Data akan disimpan dalam file `data_cuaca.csv` dengan struktur format berikut:

| Tanggal | Suhu |
| :--- | :--- |
| 2023-10-01 | 28.5 |
| 2023-10-02 | 29.1 |

Program akan membaca dan menulis pada file ini secara otomatis. Jika Anda ingin melakukan *reset* data, Anda cukup menghapus file `data_cuaca.csv` ini, dan program akan membuat file kosong baru pada saat dijalankan kembali.