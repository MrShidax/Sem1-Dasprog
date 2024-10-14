S = str(input())
N = int(len(S))
P = False
AB = False

for i in range(min(1,N), N):
    if (S[i] == S[-(i+1)]):
        P = True
    else:
        AB = True
if AB:
    print("Bukan King!")
else:
    if P:
        print("Palindrome King!")
    else:
        print("Bukan King!")