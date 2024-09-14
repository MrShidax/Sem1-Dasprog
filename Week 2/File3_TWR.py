A = (input("Masukkan Urutan Kucing : "))
A = list(map(int, A.split()))
B = int(input("Masukkan Jumlah Kucing yang melompat : "))
C = int(input("Masukkan berapa banyak lompatan yang terjadi : "))
DEF = input("Masukkan 3 Angka urutan Kucing yang ingin diketahui : ")
DEF = list(map(int, DEF.split()))
for kucing in range(C):
    A = A[-B:] + A[:-B]
Hasil = [A[i] for i in DEF if i < len(A)]
print(" ".join(map(str, Hasil)))