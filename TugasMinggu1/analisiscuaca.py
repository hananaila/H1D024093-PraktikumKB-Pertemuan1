import csv
import statistics
import datetime
import os
import numpy as np
import matplotlib.pyplot as plt

FILE_NAME = "data_cuaca.csv"

def init_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Tanggal", "Suhu"])

def baca_data():
    data = []
    with open(FILE_NAME, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['Suhu'] = float(row['Suhu'])
            data.append(row)
    return data

def simpan_data(data):
    with open(FILE_NAME, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["Tanggal", "Suhu"])
        writer.writeheader()
        writer.writerows(data)

def tambah_data_manual():
    data = baca_data()
    tanggal_set = {d['Tanggal'] for d in data}
    print("\n--- Tambah Data Manual ---")
    while True:
        tanggal = input("Masukkan tanggal (YYYY-MM-DD) atau 'selesai': ")
        if tanggal.lower() == 'selesai':
            break
        try:
            datetime.datetime.strptime(tanggal, "%Y-%m-%d")
        except ValueError:
            print("Format tanggal salah! Gunakan YYYY-MM-DD.")
            continue
        if tanggal in tanggal_set:
            print("Tanggal sudah ada, gunakan fitur ubah jika ingin mengubah.")
            continue
        try:
            suhu = float(input(f"Masukkan suhu untuk {tanggal} (°C): "))
        except ValueError:
            print("Suhu harus angka.")
            continue
        data.append({"Tanggal": tanggal, "Suhu": suhu})
        tanggal_set.add(tanggal)
        print("Data ditambahkan.")
    simpan_data(data)
    print("Data tersimpan.")

def generate_data_dummy():
    data = baca_data()
    tanggal_set = {d['Tanggal'] for d in data}
    today = datetime.date.today()
    baru = 0
    for i in range(30, 0, -1):
        tanggal = (today - datetime.timedelta(days=i)).isoformat()
        if tanggal not in tanggal_set:
            suhu = np.random.normal(28, 5)
            data.append({"Tanggal": tanggal, "Suhu": round(suhu, 1)})
            tanggal_set.add(tanggal)
            baru += 1
    simpan_data(data)
    print(f"{baru} data dummy berhasil ditambahkan.")

def tampil_data():
    data = baca_data()
    if not data:
        print("Belum ada data.")
        return

    lebar_no = 4
    lebar_tgl = max(len(d['Tanggal']) for d in data)
    lebar_tgl = max(lebar_tgl, len("Tanggal"))
    lebar_suhu = max(len(f"{d['Suhu']:.1f}") for d in data)
    lebar_suhu = max(lebar_suhu, len("Suhu (°C)"))

    print("\n--- Data Cuaca Harian ---")
    header = (f"{'No':<{lebar_no}} | {'Tanggal':<{lebar_tgl}} | {'Suhu (°C)':<{lebar_suhu}}")
    print(header)
    print("-" * len(header))

    for i, d in enumerate(data, 1):
        suhu_str = f"{d['Suhu']:.1f}"
        print(f"{i:<{lebar_no}} | {d['Tanggal']:<{lebar_tgl}} | {suhu_str:<{lebar_suhu}}")
    print()

def statistik_data():
    data = baca_data()
    if len(data) < 2:
        print("Minimal 2 data untuk statistik.")
        return
    suhu_list = [d['Suhu'] for d in data]
    print("\n--- Statistik Suhu ---")
    print(f"Jumlah data: {len(suhu_list)}")
    print(f"Rata-rata   : {statistics.mean(suhu_list):.2f} °C")
    print(f"Median      : {statistics.median(suhu_list):.2f} °C")
    try:
        modus = statistics.mode(suhu_list)
        print(f"Modus       : {modus:.2f} °C")
    except statistics.StatisticsError:
        print("Modus       : Tidak ada modus tunggal")
    print(f"Max         : {max(suhu_list):.2f} °C")
    print(f"Min         : {min(suhu_list):.2f} °C")
    print(f"Rentang     : {max(suhu_list)-min(suhu_list):.2f} °C")
    print(f"Standar dev : {statistics.stdev(suhu_list):.2f} °C")

def plot_data():
    data = baca_data()
    if len(data) < 2:
        print("Minimal 2 data untuk plot.")
        return
    data.sort(key=lambda x: x['Tanggal'])
    tanggal = [d['Tanggal'] for d in data]
    suhu = [d['Suhu'] for d in data]

    x = np.arange(len(tanggal))
    y = np.array(suhu)
    koef = np.polyfit(x, y, 1)
    trend = np.polyval(koef, x)

    plt.figure(figsize=(10, 5))
    plt.plot(tanggal, suhu, 'o-', label='Suhu harian', color='blue')
    plt.plot(tanggal, trend, 'r--', label=f'Tren linear (slope={koef[0]:.2f})')
    plt.xlabel('Tanggal')
    plt.ylabel('Suhu (°C)')
    plt.title('Grafik Suhu Harian')
    plt.xticks(rotation=45)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.tight_layout()
    plt.show()

def ubah_data():
    data = baca_data()
    if not data:
        print("Belum ada data.")
        return
    tampil_data()
    tanggal = input("Masukkan tanggal yang akan diubah (YYYY-MM-DD): ")
    for d in data:
        if d['Tanggal'] == tanggal:
            try:
                suhu_baru = float(input(f"Masukkan suhu baru untuk {tanggal}: "))
            except ValueError:
                print("Suhu harus angka.")
                return
            d['Suhu'] = suhu_baru
            simpan_data(data)
            print("Data berhasil diubah.")
            return
    print("Tanggal tidak ditemukan.")

def hapus_data():
    data = baca_data()
    if not data:
        print("Belum ada data.")
        return
    tampil_data()
    tanggal = input("Masukkan tanggal yang akan dihapus (YYYY-MM-DD): ")
    for i, d in enumerate(data):
        if d['Tanggal'] == tanggal:
            del data[i]
            simpan_data(data)
            print("Data berhasil dihapus.")
            return
    print("Tanggal tidak ditemukan.")

def main():
    init_file()
    while True:
        print("\n=== ANALISIS DATA CUACA HARIAN ===")
        print("1. Tambah data manual")
        print("2. Generate data dummy (30 hari terakhir)")
        print("3. Tampilkan semua data")
        print("4. Tampilkan statistik")
        print("5. Tampilkan grafik (dengan tren linear)")
        print("6. Ubah data")
        print("7. Hapus data")
        print("8. Keluar")
        pilih = input("Pilih menu (1-8): ")

        if pilih == '1':
            tambah_data_manual()
        elif pilih == '2':
            generate_data_dummy()
        elif pilih == '3':
            tampil_data()
        elif pilih == '4':
            statistik_data()
        elif pilih == '5':
            plot_data()
        elif pilih == '6':
            ubah_data()
        elif pilih == '7':
            hapus_data()
        elif pilih == '8':
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

if __name__ == "__main__":
    main()
