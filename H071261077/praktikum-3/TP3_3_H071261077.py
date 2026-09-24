print("--- Sistem Reservasi PO BUS ---")

while True:
    try:
        input_kursi = input("Masukkan maksimal kursi bus: ")
        N = int(input_kursi)
        if N <= 0:
            print("Jumlah kursi harus lebih dari 0!")
            continue
        break
    except:
        print("Input jumlah kursi harus berupa angka!")

print("--- Sistem Reservasi PO BUS Dimulai ---")

total_pendapatan = 0

while N > 0:
    print(f"Sisa kursi: {N}")
    
    input_umur = input("Masukkan umur penumpang: ")
    
    try:
        umur = int(input_umur)
    except:
        print("Input umur harus berupa angka!")
        continue
        
    if umur < 0:
        print("Umur tidak valid!")
        continue
        
    if umur <= 5:
        kategori = "Balita - Tiket Gratis"
        harga = 0
    elif umur <= 12:
        kategori = "Anak - Harga"
        harga = 50000
    else:
        kategori = "Dewasa - Harga"
        harga = 100000
        
    print(f"Kategori: {kategori} Rp {harga:,}".replace(",", "."))
    
    total_pendapatan += harga
    N -= 1

print("======================================")
print("-- SEMUA KURSI TELAH TERISI PENUH --")
print(f"Total Pendapatan Perjalanan: Rp {total_pendapatan:,}".replace(",", "."))
print("======================================")
