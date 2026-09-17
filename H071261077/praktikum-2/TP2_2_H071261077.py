#Soal no 2
jarak = int(input("Masukkan Jarak Pengiriman (Km): ")  )
layanan = input("Layanan Express (ya/tidak)    : ")   

match jarak:
    case jarak if jarak > 0 and jarak < 5:
        if layanan == "tidak":
             biaya = 10000
        elif layanan == "ya":
                 biaya = 10000
                 biaya = biaya + 15000
        print("Total tarif pengiriman    : Rp.",biaya)

    case jarak if jarak >= 5 and jarak <= 20:
            if layanan == "tidak":
                 biaya = 20000
            elif layanan == "ya":
                 biaya = 20000
                 biaya = biaya + 15000

            print("Total tarif pengiriman    : Rp.",biaya)
      
    case jarak if jarak > 20:
            if layanan == "tidak":
                  biaya = 35000
            elif layanan == "ya":
                biaya = 35000
                biaya = biaya + 15000

            print("Total tarif pengiriman    : Rp.",biaya)
    case _:
        print("nilai tidak valid")


