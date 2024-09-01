Jumlah = int(input("Masukkan Jumlah siwa => "))
Sisa = Jumlah % 30
Kelas = Jumlah - Sisa
JumlahKelas = round(Kelas / 30)
print("Jumlah Kelas yang ada adalah",JumlahKelas,"Kelas\nSiswa tersisa adalah",Sisa,"Siswa")