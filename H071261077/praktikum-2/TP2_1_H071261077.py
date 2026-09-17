#Soal no 1
pedas = (int(input("Masukkan Presentase Pedas: ")))

if  pedas >= 0 and pedas <= 10:
    print("Level Aman")
elif pedas >= 11 and pedas <= 40:
    print("Level Sedang")
elif pedas >= 41 and pedas <= 70:
    print("Level Panas")
elif pedas >= 71 : 
    print ("Level Ekstrem")
else:
    print("Input tidak valid")