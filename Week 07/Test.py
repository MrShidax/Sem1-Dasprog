N = int(input())
B = list(map(int, input().split()))

C = 0
for i in B:
    C ^= i

D = 1
for i in B:
    D *= C ^ i

print(D)