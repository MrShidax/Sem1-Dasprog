A = list(map(int(input("Masukkan Urutan Kucing : ").split())))
B = int(input("Masukkan Jumlah Kucing yang melompat : "))
C = int(input("Masukkan berapa banyak lompatan yang terjadi"))
D, E, F = list(map(int(input("Masukkan 3 Angka urutan Kucing yang ingin diketahui : ").split())))

for _ in range(C):
    A = A[-B:] + A[:-B]aa