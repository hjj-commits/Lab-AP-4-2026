DOMAIN_RESMI = (".com", ".id", ".ac.id")


def deteksi_anomali_email(email, daftar_valid=()):
    """Return list deskripsi aturan yang dilanggar (list kosong jika valid)."""
    anomali = []

    # Aturan 1: tepat satu '@'
    if email.count("@") != 1:
        anomali.append("Harus memiliki tepat satu karakter @.")
        if " " in email:
            anomali.append("Tidak boleh mengandung spasi.")
        return anomali

    local, domain = email.split("@")

    # Aturan 2: local & domain tidak kosong
    if local == "" or domain == "":
        anomali.append("Bagian sebelum @ (local) atau setelah @ (domain) tidak boleh kosong.")

    # Aturan 3: tanpa spasi
    if " " in email:
        anomali.append("Tidak boleh mengandung spasi.")

    # Aturan 4: aturan titik pada local
    if local.startswith(".") or local.endswith(".") or ".." in local:
        anomali.append("Bagian local tidak boleh diawali/diakhiri titik atau mengandung titik berurutan.")

    # Aturan 5: aturan titik pada domain
    if "." not in domain:
        anomali.append("Bagian domain wajib memiliki minimal satu titik.")
    if ".." in domain or domain.endswith("."):
        anomali.append("Bagian domain tidak boleh mengandung titik berurutan atau diakhiri titik.")

    # Aturan 7: domain resmi
    resmi = False
    for akhiran in DOMAIN_RESMI:
        if email.lower().endswith(akhiran):
            resmi = True
    if not resmi:
        anomali.append("Wajib berakhiran dengan .com, .id, atau .ac.id")

    # Aturan 6: duplikat
    for e in daftar_valid:
        if e.lower() == email.lower():
            anomali.append("Email sudah terdaftar (Duplikat).")
            break

    return anomali


def cetak_daftar(daftar_email_valid, karakter_border):
    """Bingkai teks; lebar menyesuaikan email terpanjang + padding spasi."""
    border = karakter_border[:1] or "-"
    lebar = 0
    for e in daftar_email_valid:
        if len(e) > lebar:
            lebar = len(e)

    garis = "+" + border * (lebar + 2) + "+"
    baris = [garis]
    for e in daftar_email_valid:
        baris.append("| " + e + " " * (lebar - len(e)) + " |")
    baris.append(garis)
    return "\n".join(baris)


if __name__ == "__main__":
    print("--- Sistem Pencatatan email valid ---")
    border = input("Masukkan border dengan karakter bebas: ")
    print("\nKetik 'tutup' untuk mengakhiri masukan dan mencetak email.")

    valid = []
    while True:
        email = input("Masukkan email: ")
        if email.strip().lower() == "tutup":
            break

        masalah = deteksi_anomali_email(email, valid)
        if masalah:
            print(">> Email DITOLAK karena:")
            for m in masalah:
                print("   - " + m)
        else:
            print(">> Email VALID!")
            valid.append(email)

    print("\n--- HASIL EMAIL VALID ---")
    if valid:
        print(cetak_daftar(valid, border))
    else:
        print("Tidak ada email valid.")