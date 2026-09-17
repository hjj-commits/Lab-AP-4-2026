#Soal No 3
nilai = int(input("Masukkan Nilai tes                      : ") ) 

match nilai: 
     
    case nilai if nilai >= 80:
         print("Lolos Ke Tahap Wawancara")  
 
    case nilai if nilai < 80 and nilai >= 65:
        pengalaman = int(input("Masukkan Pengalaman Kerja (tahun)       : "))

        if pengalaman >= 2:
                print("Lolos Bersyarat")
        else:
            print("Tidak lolos")   
        
    case _:
        print("Nilai tidak valid")