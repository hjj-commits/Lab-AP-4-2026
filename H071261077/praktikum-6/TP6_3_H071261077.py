#TP6_3_H071261077
# Soal 3: Sistem Manajemen Playlist Musik "PlayTune"


def format_durasi(detik):
    return f"{detik // 60}:{detik % 60:02d}"


def tambah_lagu(playlist, genre_set, judul, artis, genre, durasi):
    # samakan penulisan genre dengan yang sudah ada (tidak peka huruf besar/kecil)
    for g in genre_set:
        if g.lower() == genre.lower():
            genre = g
            break
    lagu = (judul, artis, genre, durasi)  # tuple
    playlist.append(lagu)
    genre_set.add(genre)
    print(f"Lagu '{judul}' oleh {artis} berhasil ditambahkan!")


def tampilkan_playlist(playlist):
    if not playlist:
        print("Playlist masih kosong.")
        return
    print("=" * 55)
    print(f"{'No':<4}{'Judul':<22}{'Artis':<15}{'Genre':<9}{'Durasi':<6}")
    print("=" * 55)
    for i, (judul, artis, genre, durasi) in enumerate(playlist, 1):
        print(f"{i:<4}{judul:<22}{artis:<15}{genre:<9}{format_durasi(durasi):<6}")
    print("=" * 55)
    total = sum(lagu[3] for lagu in playlist)
    print(f"Total durasi playlist: {total // 60} menit {total % 60} detik")


def filter_genre(playlist, genre_target):
    return [lagu for lagu in playlist if lagu[2].lower() == genre_target.lower()]


def hapus_lagu(playlist, nomor):
    if 1 <= nomor <= len(playlist):
        lagu = playlist.pop(nomor - 1)
        print(f"Lagu '{lagu[0]}' berhasil dihapus!")
        return True
    print("Error: Nomor lagu tidak valid!")
    return False


def statistik_playlist(playlist, genre_set):
    print("=" * 40)
    print(" STATISTIK PLAYLIST PLAYTUNE")
    print("=" * 40)
    if not playlist:
        print(" Playlist masih kosong.")
        print("=" * 40)
        return

    distribusi = {}
    for lagu in playlist:
        distribusi[lagu[2]] = distribusi.get(lagu[2], 0) + 1

    terpanjang = max(playlist, key=lambda l: l[3])
    terpendek = min(playlist, key=lambda l: l[3])

    print(f" Total lagu : {len(playlist)}")
    print(f" Jumlah genre : {len(genre_set)}")
    print(f" Daftar genre : {genre_set}")
    print(" Distribusi genre:")
    for genre, jumlah in distribusi.items():
        print(f" {genre} : {'#' * jumlah} ({jumlah})")
    print(f" Lagu terpanjang : {terpanjang[0]} ({format_durasi(terpanjang[3])})")
    print(f" Lagu terpendek : {terpendek[0]} ({format_durasi(terpendek[3])})")
    print("=" * 40)


def tampilkan_menu():
    print("Menu:")
    print("1. Tambah Lagu")
    print("2. Tampilkan Playlist")
    print("3. Filter berdasarkan Genre")
    print("4. Hapus Lagu")
    print("5. Statistik Playlist")
    print("6. Keluar")


def main():
    playlist = []
    genre_set = set()

    print("=" * 40)
    print(" PLAYLIST MUSIK - PLAYTUNE")
    print("=" * 40)

    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-6): ").strip()

        if pilihan == "1":
            judul = input("Judul lagu: ").strip()
            artis = input("Artis: ").strip()
            genre = input("Genre (Pop/Rock/Jazz/RnB/Dangdut): ").strip()
            try:
                durasi = int(input("Durasi (dalam detik): "))
                if durasi <= 0:
                    raise ValueError
            except ValueError:
                print("Error: Durasi harus berupa angka positif!")
                continue
            tambah_lagu(playlist, genre_set, judul, artis, genre, durasi)

        elif pilihan == "2":
            tampilkan_playlist(playlist)

        elif pilihan == "3":
            if not playlist:
                print("Playlist masih kosong.")
                continue
            print(f"Genre tersedia: {genre_set}")
            target = input("Masukkan genre yang ingin difilter: ").strip()
            hasil = filter_genre(playlist, target)
            if hasil:
                print(f"Lagu bergenre '{target}':")
                for i, (judul, artis, _, durasi) in enumerate(hasil, 1):
                    print(f" {i}. {judul} - {artis} ({format_durasi(durasi)})")
            else:
                print(f"Tidak ada lagu bergenre '{target}'.")

        elif pilihan == "4":
            if not playlist:
                print("Playlist masih kosong.")
                continue
            tampilkan_playlist(playlist)
            try:
                nomor = int(input("Nomor lagu yang ingin dihapus: "))
            except ValueError:
                print("Error: Masukkan nomor berupa angka!")
                continue
            hapus_lagu(playlist, nomor)

        elif pilihan == "5":
            statistik_playlist(playlist, genre_set)

        elif pilihan == "6":
            print("Terima kasih telah menggunakan PlayTune!")
            break

        else:
            print("Pilihan tidak valid! Masukkan angka 1-6.")


if __name__ == "__main__":
    main()