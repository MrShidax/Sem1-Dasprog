print("Aturan : 4 <= M <= N <= 100")
N, M = map(int, input("Masukkan Nilai N (Panjang) dan Nilai M (Tebal) : ").split())
if 4 <= M <= N <= 100:
    if M * 2 > N:
        print("ERROR! KETEBALAN TERLALU TEBAL UNTUK FRAME!")
    else:
        for i in range(M):
            print("*" * N)
        for i in range(N - 2 * M):
            print("*" * M + " " * (N - 2 * M) + "*" * M)
        for i in range(M):
            print("*" * N)
else:
    print("ERROR! IKUTI ATURAN YANG ADA!")