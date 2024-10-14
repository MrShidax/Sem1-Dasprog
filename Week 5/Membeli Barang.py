N, M = map(int, input().split())
P = list(map(int, input().split()))
C = list(map(int, input().split()))

if (len(P) != N) or (len(C) != M):
    print("ERROR! jumlah Barang dan/atau Uang yang diinput tidak sesuai")
else:
    P.sort()
    C.sort()
    if P[-1] > 0:
        Harga = 0
        for i in P:
            if i > 0:
                Harga += i
    else:
        Harga = P[-1]
    
    if C[0] < 0:
        Uang = 0
        for j in C:
            if j < 0:
                Uang += j
    else:
        Uang = C[0]
    
    print(Uang - Harga)