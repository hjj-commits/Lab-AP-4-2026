#Soal no 4
tujuan      = input("Masukkan Tujuan (Pantai/Pegunungan/Kota) : ")

match tujuan:

    case "Pantai":
        waktu = input("Masukkan Waktu (Pagi/Malam)              : ")
        if waktu == "Pagi":
            pengunjung  = input("Masukkan Tipe Pengunjung (Anak/Dewasa)   : ")
            if pengunjung == "Dewasa" "Anak":
                print("Paket Rekomendasi                         : Paket A")
            else:
                print("Tidak Ada Paket yang Cocok")
        elif waktu == "Malam":
                pengunjung  = input("Masukkan Tipe Pengunjung (Anak/Dewasa)   : ")
                print("Paket Rekomendasi                         : Paket C")
        else:
             print("Tidak Ada Paket yang Cocok")

    case "Pegunungan":
            waktu = input("Masukkan Waktu (Pagi/Malam)              : ")
            if waktu == "Pagi":
                pengunjung  = input("Masukkan Tipe Pengunjung (Anak/Dewasa)   : ")
                if pengunjung == "Dewasa":
                    print("Paket Rekomendasi                         : Paket B")
                else:
                    print("Tidak Ada Paket yang Cocok")
            elif waktu == "Malam":
                pengunjung  = input("Masukkan Tipe Pengunjung (Anak/Dewasa)   : ")
                if pengunjung == "Dewasa":
                    print("Paket Rekomendasi                         : Paket C")
                else:
                    print("Tidak Ada Paket yang Cocok")
            else:
                 print("Tidak Ada Paket yang Cocok")

    case "Kota":
            waktu = input("Masukkan Waktu (Pagi/Malam)              : ")
            if waktu == "Malam":
                pengunjung  = input("Masukkan Tipe Pengunjung (Anak/Dewasa)   : ")
                if pengunjung == "Dewasa" and "Anak":
                        print("Paket Rekomendasi                         : Paket C")
                else:
                        print("Tidak Ada Paket yang Cocok")
            else:
                     print("Tidak Ada Paket yang Cocok")

    case _:
        print("Tidak Ada Paket yang Cocok")

        
        