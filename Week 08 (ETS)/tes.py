A = int(input())

for i in range (A+2):
    for j in range (A+2):
        if (i == 0) or (i == (A+1)):
            print("+" + ("-" * ((A * 2) + 1) + "+"))
        if ((i > 0) and (i < (A+1))):
            if (j == 0):
                print("|", end="")
            elif(j == (A+1)):
                print("|", end="")
            else:
                if ((i+j) % 2 == 0):
                    print("v", end="")
                else:
                    print(". ", end="")
    print("")