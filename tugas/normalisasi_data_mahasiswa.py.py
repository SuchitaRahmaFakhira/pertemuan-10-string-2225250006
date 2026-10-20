def normalisasi_nama(nama):
    return nama.strip().title()


def buat_inisial(nama):
    kata = nama.split()
    inisial = ""

    for k in kata:
        inisial += k[0].upper()

    return inisial


def normalisasi_kode(kode):
    kata = kode.strip().upper().split()
    return "-".join(kata)


nama = input("Nama: ")
kode = input("Kode kelas: ")

nama_bersih = normalisasi_nama(nama)
kode_bersih = normalisasi_kode(kode)
jumlah_kata = len(nama_bersih.split())
inisial = buat_inisial(nama_bersih)

print(f"Nama bersih : {nama_bersih}")
print(f"Kode kelas : {kode_bersih}")
print(f"Jumlah kata : {jumlah_kata}")
print(f"Inisial     : {inisial}")