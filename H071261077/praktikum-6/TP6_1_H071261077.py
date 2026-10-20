#TP6_1_H071261077
# Soal 1: Sistem Inventaris Toko Buku "BookNest"


def format_angka(x):
    """Tampilkan angka tanpa .0 jika bilangan bulat."""
    return int(x) if float(x).is_integer() else x


def tambah_buku(inventaris, judul, penulis, harga, stok):
    buku = {"judul": judul, "penulis": penulis, "harga": harga, "stok": stok}
    inventaris.append(buku)
    print(f"Buku '{judul}' berhasil ditambahkan!")


def cari_buku(inventaris, kata_kunci):
    kata_kunci = kata_kunci.lower()
    return [b for b in inventaris if kata_kunci in b["judul"].lower()]


def update_stok(inventaris, judul, jumlah):
    for buku in inventaris:
        if buku["judul"].lower() == judul.lower():
            stok_baru = buku["stok"] + jumlah
            if stok_baru < 0:
                print(f"Gagal! Stok '{buku['judul']}' tidak mencukupi "
                      f"(stok saat ini: {buku['stok']}).")
                return False
            buku["stok"] = stok_baru
            if jumlah >= 0:
                print(f"Stok '{buku['judul']}' bertambah {jumlah}. Stok sekarang: {stok_baru}")
            else:
                print(f"Stok '{buku['judul']}' berkurang {abs(jumlah)}. Stok sekarang: {stok_baru}")
            return True
    print(f"Error: Buku '{judul}' tidak ditemukan!")
    return False


def ringkasan_inventaris(inventaris):
    jumlah_jenis = len(inventaris)
    total_stok = sum(b["stok"] for b in inventaris)
    total_aset = sum(b["harga"] * b["stok"] for b in inventaris)

    print("=" * 40)
    print("RINGKASAN INVENTARIS BOOKNEST")
    print("=" * 40)
    print(f"Jumlah jenis buku : {jumlah_jenis}")
    print(f"Total seluruh stok: {total_stok}")
    print(f"Total nilai aset : Rp{format_angka(total_aset)}")
    if inventaris:
        termahal = max(inventaris, key=lambda b: b["harga"])
        print(f"Buku termahal : {termahal['judul']} (Rp{format_angka(termahal['harga'])})")
    else:
        print("Buku termahal : -")
    print("=" * 40)


def tampilkan_menu():
    print("Menu:")
    print("1. Tambah Buku")
    print("2. Cari Buku")
    print("3. Update Stok")
    print("4. Ringkasan Inventaris")
    print("5. Keluar")


def main():
    inventaris = []
    print("=" * 40)
    print(" SISTEM INVENTARIS TOKO BUKU BOOKNEST")
    print("=" * 40)

    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-5): ").strip()

        if pilihan == "1":
            judul = input("Judul buku: ").strip()
            penulis = input("Penulis: ").strip()
            try:
                harga = float(input("Harga: "))
                stok = int(input("Stok awal: "))
            except ValueError:
                print("Error: Harga dan stok harus berupa angka (stok bilangan bulat)!")
                continue
            if harga < 0 or stok < 0:
                print("Error: Harga dan stok tidak boleh negatif!")
                continue
            tambah_buku(inventaris, judul, penulis, format_angka(harga), stok)

        elif pilihan == "2":
            kata_kunci = input("Masukkan kata kunci judul: ").strip()
            hasil = cari_buku(inventaris, kata_kunci)
            if hasil:
                print(f"Ditemukan {len(hasil)} buku:")
                for i, b in enumerate(hasil, 1):
                    print(f" {i}. {b['judul']} - {b['penulis']} | "
                          f"Rp{b['harga']} | Stok: {b['stok']}")
            else:
                print("Buku tidak ditemukan.")

        elif pilihan == "3":
            judul = input("Judul buku yang ingin diupdate: ").strip()
            try:
                jumlah = int(input("Jumlah perubahan (positif=tambah, negatif=kurang): "))
            except ValueError:
                print("Error: Jumlah harus berupa bilangan bulat!")
                continue
            update_stok(inventaris, judul, jumlah)

        elif pilihan == "4":
            ringkasan_inventaris(inventaris)

        elif pilihan == "5":
            print("Terima kasih telah menggunakan BookNest!")
            break

        else:
            print("Pilihan tidak valid! Masukkan angka 1-5.")


if __name__ == "__main__":
    main()