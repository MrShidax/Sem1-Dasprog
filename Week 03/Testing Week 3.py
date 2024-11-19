x = int(input())

for i in range(x):
    for k in range(x - i - 1):
        print(" ",end="")

    for j in range(i * 2 + 1):
        print("*",end="")
    print()

for i in range(x-1):

    for k in range(i + 1):
        print(" ",end="")

    for j in range(2 * (x - i - 2) + 1):
        print("*",end="")
    print()