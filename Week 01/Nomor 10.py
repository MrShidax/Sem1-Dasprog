a, b = map(int, input().split())
if a % b == 0:
    c = b
else:
    c = a
d = (a * b) // c
hasil = (c * d // a) + (c * d // b)
print(hasil)