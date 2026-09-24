#Soal No 1
print("---Rekapitulasi Transaksi Dins Store---")
print("Ketik '0' untuk menutup toko dan mengakhiri sesi")

while True:
    try:
        a = int(input("Masukkan nilai : "))
        if a > 0:
            if a >= 0 and a <= 100:
                 print(f"Transaksi {a} item berhasil!")
            elif a > 100:
                 print("Maksimal 100 item per transaksi")
        elif a < 0:
             print("Jumlah tidak boleh negatif")
        elif a == 0:
            print ("Toko ditutup sesi rekap selesai")
            break
    except:
        print("Input harus berupa angka")
        
    

    
