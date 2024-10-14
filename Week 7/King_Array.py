t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    q = int(input())
    if q == 1:
        hasil = float("-inf")
    elif q == 2:
        hasil = float("inf")
    for j in range(1, k + 1):
        jumlah = sum(A[:j])
        if q == 1:
            hasil = max(hasil, jumlah)
        else:
            hasil = min(hasil, jumlah)
        for l in range(j, n):
            jumlah += A[l] - A[l - j]
            if q == 1:
                hasil = max(hasil, jumlah)
            else:
                hasil = min(hasil, jumlah)
    print(hasil)