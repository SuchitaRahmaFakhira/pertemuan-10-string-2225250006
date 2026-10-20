# Pertemuan 10 - String dan Pengolahan Teks

Nama: Alfitrah Zahra Ameliya
NIM: 2225250181
Kelas: 3B

## Tujuan

Mengolah dan menormalisasi data teks dengan string Python.

## Cara Menjalankan

python3 tugas/normalisasi_data_mahasiswa.py

## Algoritma

1. Membaca nama dan kode kelas dari input pengguna.
2. Membersihkan nama menggunakan strip() untuk menghapus spasi di awal dan akhir.
3. Menggunakan title() untuk mengubah huruf awal setiap kata pada nama menjadi huruf kapital.
4. Menggunakan split() untuk memisahkan nama menjadi beberapa kata.
5. Membuat inisial dengan mengambil huruf pertama dari setiap kata dan mengubahnya menjadi huruf kapital.
6. Membersihkan kode kelas, mengubahnya menjadi huruf kapital menggunakan upper(), lalu menggabungkan setiap kata dengan tanda hubung menggunakan join().
7. Menghitung jumlah kata pada nama yang sudah dibersihkan.
8. Menampilkan nama bersih, kode kelas, jumlah kata, dan inisial.

## Test Case

| No. | Input Nama | Input Kode Kelas | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|---|---|
| 1 | aan hendrayana | pmat a 2026 | Aan Hendrayana, PMAT-A-2026, 2, AH | Aan Hendrayana, PMAT-A-2026, 2, AH | Berhasil |
| 2 | fATHIYYAH mUTHMAINNAH | kelas b | Fathiyyah Muthmainnah, KELAS-B, 2, FM | Fathiyyah Muthmainnah, KELAS-B, 2, FM | Berhasil |
| 3 | BUDI | pmtk 01 | Budi, PMTK-01, 1, B | Budi, PMTK-01, 1, B | Berhasil |
| 4 | siti nur aisyah | kelas c | Siti Nur Aisyah, KELAS-C, 3, SNA | Siti Nur Aisyah, KELAS-C, 3, SNA | Berhasil |

Keterangan:
- Angka menunjukkan jumlah kata pada nama.
- Inisial diambil dari huruf pertama setiap kata pada nama.

## Refleksi

Kesulitan yang saya temukan adalah membersihkan spasi berlebih pada teks dan menyeragamkan huruf pada nama mahasiswa. Masalah ini dapat diatasi dengan menggunakan method strip(), title(), split(), dan join() agar data lebih rapi dan mudah diolah.
