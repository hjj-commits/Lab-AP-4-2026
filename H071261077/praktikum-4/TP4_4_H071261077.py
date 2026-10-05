def konversi_suhu(suhu, asal, tujuan):
    asal = asal.upper()
    tujuan = tujuan.upper()

    if asal not in ["C", "F", "K"] or tujuan not in ["C", "F", "K"]:
        raise ValueError("Skala suhu tidak dikenali.")

    if asal == "C":
        celsius = suhu
    elif asal == "F":
        celsius = (suhu - 32) * 5 / 9
    else:
        celsius = suhu - 273.15

    if tujuan == "C":
        hasil = celsius
    elif tujuan == "F":
        hasil = (celsius * 9 / 5) + 32
    else:
        hasil = celsius + 273.15

    return hasil

print("=== Konversi Suhu ===")

while True:
    input_suhu = input("Masukkan suhu (atau 'selesai' untuk keluar): ")

    if input_suhu.lower() == "selesai":
        break

    try:
        suhu = float(input_suhu)

        asal = input("Skala asal (C/F/K): ")
        tujuan = input("Skala tujuan (C/F/K): ")

        hasil = konversi_suhu(suhu, asal, tujuan)

        print(f"Hasil: {suhu} {asal.upper()} = {hasil} {tujuan.upper()}")

    except ValueError as e:
        if str(e) == "Skala suhu tidak dikenali.":
            print("Error: Skala suhu tidak dikenali.")
        else:
            print("Input suhu tidak valid.")