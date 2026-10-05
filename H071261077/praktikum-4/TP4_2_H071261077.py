def rekap_nilai(*args):
    if len(args) == 0:
        return None

    rata_rata = sum(args) / len(args)
    tertinggi = max(args)
    terendah = min(args)

    return rata_rata, tertinggi, terendah


nilai = []

while True:
    input_nilai = input(
        "Masukkan nilai ujian siswa (kosongkan untuk selesai): "
    )

    if input_nilai == "":
        break

    nilai.append(float(input_nilai))


hasil = rekap_nilai(*nilai)

if hasil is None:
    print("Data nilai tidak tersedia.")
else:
    rata_rata, tertinggi, terendah = hasil

    print(f"Rata-rata kelas: {rata_rata}")
    print(f"Nilai tertinggi: {tertinggi}")
    print(f"Nilai terendah: {terendah:g}")