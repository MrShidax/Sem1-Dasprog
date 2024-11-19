def last_man_standing(N, C):
    dp = [False] * (N + 1)

    if N >= 1:
        dp[1] = True
    if N >= 2:
        dp[2] = True
    if N >= 5:
        dp[5] = True

    for i in range(1, N + 1):
        if i - 1 >= 0 and not dp[i - 1]:
            dp[i] = True
        elif i - 2 >= 0 and not dp[i - 2]:
            dp[i] = True
        elif i - 5 >= 0 and not dp[i - 5]:
            dp[i] = True

    if dp[N]:
        if C == 1:
            return "Lala"
        else:
            return "Lili"
    else:
        if C == 1:
            return "Lili"
        else:
            return "Lala"

# Read inputs
N, C = map(int, input().split())
print(last_man_standing(N, C))