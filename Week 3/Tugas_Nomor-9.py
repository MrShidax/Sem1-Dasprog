print("ATURAN : 1 <= N <= 100 dan Hanya Aku atau Kamu")
N, M = input("Masukkan Tinggi dan juga Kata : ").split()
N = int(N)
M = M.lower()
if (1 <= N <= 100):
    if (M == "aku"):
        for i in range(N):
            for j in range(i + 1):
                if (i + j) % 2 == 0:
                    print("I", end=" ")
                else:
                    print("U", end=" ")
            print()
    elif (M == "kamu"):
        for i in range(N):
            print(" " * (2 * (N - i - 1)), end="")
            for j in range(i + 1):
                if (j % 2 == 0):
                    print("I", end=" ")
                else:
                    print("U", end=" ")
            print()
    else:
            print("ERROR! MASUKKAN KAMU ATAU AKU")
else:
    print("ERROR! IKUTI ATURAN YANG ADA!")