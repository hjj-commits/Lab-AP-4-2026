ALFABET = "abcdefghijklmnopqrstuvwxyz"

def bersihkan_teks(teks):
    """Simpan hanya huruf (cek manual ke ALFABET), lalu jadikan huruf kecil."""
    hasil = ""
    for ch in teks:
        huruf = ch.lower()
        if huruf in ALFABET:
            hasil += huruf
    return hasil

def cek_palinrome(teks):
    """Return (True, -1) jika palindrom, atau (False, indeks_pertama_beda)."""
    terbalik = "".join(reversed(teks))
    if teks == terbalik:
        return (True, -1)
    for i in range(len(teks)):
        if teks[i] != terbalik[i]:
            return (False, i)

def inti_palinrome(teks):
    """Cari palindrom terpanjang (seri -> yang paling kiri) pada teks bersih."""
    bersih = bersihkan_teks(teks)
    terbaik = {"teks": "", "panjang": 0, "indeks_awal": 0}

    for i in range(len(bersih)):
        for j in range(i + 1, len(bersih) + 1):
            sub = bersih[i:j]
            simetris, _ = cek_palinrome(sub)
            # '>' (bukan '>=') menjaga palindrom paling kiri saat panjangnya seri
            if simetris and len(sub) > terbaik["panjang"]:
                terbaik = {"teks": sub, "panjang": len(sub), "indeks_awal": i}
    return terbaik

if __name__ == "__main__":
    teks = input("Masukkan teks prasasti: ")
    print()
    print("Teks Bersih:", bersihkan_teks(teks))
    print("Output Terharap:", inti_palinrome(teks))