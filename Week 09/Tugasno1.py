def prima(N):
    if N <= 1:
        return False
    if N <= 3:
        return True
    akarN = int(N ** 0.5)
    for i in range(2, akarN + 1):
        if N % i == 0:
            return False
    return True

N = int(input())
if prima(N):
    print(f"{N} adalah prima")
else:
    print(f"{N} bukan prima")