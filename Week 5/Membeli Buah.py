N, K = map(int, input().split())
A = list(map(int, input().split()))

if len(A) != N:
    print("ERROR! JUMLAH HARGA YANG DIINPUT TIDAK SESUAI DENGAN JUMLAH BUAH YANG ADA")
else:
    banyak = 0
    for harga in A:
        if harga <= K:
            banyak += 1

    print(banyak)