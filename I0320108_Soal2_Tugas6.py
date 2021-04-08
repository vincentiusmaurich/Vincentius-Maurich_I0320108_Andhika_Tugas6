siswa = int(input('Masukkan jumlah siswa: '))

nilai = []

for i in range(0, siswa):
    list = int(input("Nilai siswa ke-%d : " % (i+1)))
    nilai.append(list)
    jumlah_nilai = sum(nilai)
    rata_rata = jumlah_nilai / siswa
print("Rata-rata nilai siswa adalah %0.2f" % rata_rata)
