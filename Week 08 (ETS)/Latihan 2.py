#    1
#   1 1
#  1 2 1
# 1 3 3 1
#1 4 6 4 1
A = int(input())
B = 1
C = 1
for i in range(A+1):
    print(((A-i)*" "), end="")
    for j in range(i):
        print(("1" if j == 0 else "") + " " + (str(j) if (j != 0) else ""), end="")
    print("")