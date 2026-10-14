ALFABET = "abcdefghijklmnopqrstuvwxyz"


def cek_kata(teks, kata):
    """List indeks kemunculan kata (tidak peka huruf besar/kecil)."""
    hasil = []
    if kata == "":
        return hasil
    teks_kecil = teks.lower()
    kata_kecil = kata.lower()
    start = 0
    while True:
        idx = teks_kecil.find(kata_kecil, start)
        if idx == -1:
            break
        hasil.append(idx)
        start = idx + 1
    return hasil


def cek_batas_kata(teks, i, panjang):
    """True jika karakter sebelum & sesudah kata bukan huruf (tanpa isalpha)."""
    if i > 0 and teks[i - 1].lower() in ALFABET:
        return False
    akhir = i + panjang
    if akhir < len(teks) and teks[akhir].lower() in ALFABET:
        return False
    return True


def sensor_kata(teks, kata, simbol):
    """Return (teks_tersensor, jumlah_tersensor, list_indeks_awal)."""
    simbol = simbol[:1] or "*"
    panjang = len(kata)
    hasil = ""
    indeks = []
    posisi = 0  # bagian teks asli yang sudah dirakit

    for i in cek_kata(teks, kata):
        if i >= posisi and cek_batas_kata(teks, i, panjang):
            hasil = hasil + teks[posisi:i] + simbol * panjang
            posisi = i + panjang
            indeks.append(i)

    hasil = hasil + teks[posisi:]
    return (hasil, len(indeks), indeks)


if __name__ == "__main__":
    teks = input("Masukkan Teks: ")
    kata = input("Masukkan kata target: ")
    simbol = input("Masukkan simbol: ")

    tersensor, jumlah, indeks = sensor_kata(teks, kata, simbol)
    print("Hasil Teks:", tersensor)
    print("Jumlah:", jumlah, "| Indeks:", indeks)