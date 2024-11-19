N, r, c = map(int, input().split())
mapkelas = [[0] * c for i in range(r)]

for j in range(N):
    x, a, b = map(int, input().split())
    mapkelas[a-1][b-1] = x

for k in range(N+1):
    for i in range(r):
        for j in range(c):
            if mapkelas[i][j] == k+1:
                if j > 0:
                    kiri = mapkelas[i][j - 1]
                else:
                    kiri = 0
                if j < c - 1:
                    kanan = mapkelas[i][j + 1]
                else: 
                    kanan = 0

                if kiri != 0:
                    print(kiri)
                elif kanan != 0:
                    print(kanan)
                else:
                    print(0)