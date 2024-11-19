r, c, N = map(int, input("").split())
hutan = []
i, j = 0, 0
mentok = False

for k in range(r):
    hutan.append(list(map(int, input().split())))

emas = hutan[i][j]

langkah = list(input().split())

for l in langkah:
    if l == "L":
        j -= 1
    elif l == "D":
        i += 1
    elif l == "R":
        j += 1
    elif l == "U":
        i -= 1

    if i < 0 or i >= r or j < 0 or j >= c:
        print(emas)
        print("gerakanmu salah bung!")
        mentok = True
        break

    if l == "L" or l == "D":
        emas -= 2
    elif l == "R" or l == "U":
        emas += 3

    emas += hutan[i][j]

if not (mentok):
    print(emas)