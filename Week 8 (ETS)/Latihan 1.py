A = int(input())

for i in range(A):
    for j in range(A):
        if (((i+j) % 2) == 0):
            print("*", end=" ")
        else:
            print("#", end=" ")
    print("")