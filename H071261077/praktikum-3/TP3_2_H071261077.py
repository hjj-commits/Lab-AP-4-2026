#Soal 2
print("--- Setup Denah Bioskop NontonYuk ---")

while True:
    try:
        n = input("Masukkan jumlah baris: ")
        N = int(n)
        if N <= 0:
            print("Jumlah baris harus lebih dari 0!")
            continue
    except:
        print("Input baris harus berupa angka!")

while True:
    try:
        n = input("Masukkan jumlah kursi per baris: ")
        M = int(n)
        if M <= 0:
            print("Jumlah kursi harus lebih dari 0!")
            continue
        break
    except:
        print("Input kursi harus berupa angka!")


print("\n--- Daftar Kursi Tersedia ---")


for baris in range(1, N + 1):
    for kursi in range(1, M + 1):
        if kursi == 13:
            continue
            
        if baris == 1:
            if kursi % 2 == 0:
                continue
            
        print(f"Baris {baris} - Kursi {kursi}")
