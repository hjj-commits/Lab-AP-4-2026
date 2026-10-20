#TP6_2_H071261077
# Soal 2: Sistem Pemilihan Ketua Kelas "VoteClass"


def daftar_kandidat(kandidat_set, nama):
    nama = nama.strip().capitalize()
    if nama in kandidat_set:
        print(f"'{nama}' sudah terdaftar sebagai kandidat!")
        return False
    kandidat_set.add(nama)
    print(f"'{nama}' berhasil didaftarkan sebagai kandidat!")
    return True


def berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan):
    kunci = nama_pemilih.strip().lower()
    nama_tampil = nama_pemilih.strip().capitalize()
    pilihan = pilihan.strip().capitalize()

    if kunci in rekap_suara:
        print(f"'{nama_tampil}' sudah memberikan suara sebelumnya!")
        return False
    if pilihan not in kandidat_set:
        print(f"Error: Kandidat '{pilihan}' tidak ada! Suara tidak dicatat.")
        return False

    rekap_suara[kunci] = pilihan
    print(f"Suara '{nama_tampil}' untuk '{pilihan}' berhasil dicatat!")
    return True


def hitung_suara(rekap_suara, kandidat_set):
    perolehan = {kandidat: 0 for kandidat in sorted(kandidat_set)}
    for pilihan in rekap_suara.values():
        perolehan[pilihan] += 1
    return perolehan


def tampilkan_hasil(perolehan):
    print("=" * 40)
    print(" HASIL PEMILIHAN KETUA KELAS")
    print("=" * 40)
    for kandidat, jumlah in perolehan.items():
        print(f" {kandidat}: {jumlah} suara")

    total = sum(perolehan.values())
    print(f"Total suara masuk: {total}")

    if total == 0:
        print("Belum ada suara yang masuk.")
    else:
        tertinggi = max(perolehan.values())
        pemenang = [k for k, v in perolehan.items() if v == tertinggi]
        if len(pemenang) > 1:
            print(f"Hasil SERI antara: {', '.join(pemenang)}")
            print("Perlu dilakukan pemilihan ulang!")
        else:
            print(f"PEMENANG: {pemenang[0]} dengan {tertinggi} suara!")
    print("=" * 40)


def main():
    kandidat_set = set()
    rekap_suara = {}

    print("=" * 40)
    print(" SISTEM PEMILIHAN KETUA KELAS")
    print("=" * 40)

    # Fase pendaftaran
    print("--- FASE PENDAFTARAN KANDIDAT ---")
    while True:
        nama = input("Masukkan nama kandidat (kosongkan untuk selesai): ").strip()
        if nama == "":
            if len(kandidat_set) < 2:
                print("Minimal harus ada 2 kandidat sebelum lanjut!")
                continue
            break
        daftar_kandidat(kandidat_set, nama)
    print(f"Kandidat terdaftar: {kandidat_set}")

    # Fase pemungutan suara
    print("--- FASE PEMUNGUTAN SUARA ---")
    while True:
        nama_pemilih = input("Nama pemilih (kosongkan untuk selesai): ").strip()
        if nama_pemilih == "":
            break
        print(f"Kandidat yang tersedia: {kandidat_set}")
        pilihan = input("Pilih kandidat: ")
        berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan)

    perolehan = hitung_suara(rekap_suara, kandidat_set)
    tampilkan_hasil(perolehan)


if __name__ == "__main__":
    main()