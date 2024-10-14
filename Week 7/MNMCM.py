N = int(input())
B = list(map(int,input().split()))
if len(set(B)) <  N:
    print(0)
else:
    C = 1
    for i in range(N):
        for j in range (i):
            C *= B[i] ^ B[j]
    print(C)