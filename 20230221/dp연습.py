
T = int(input())

for _ in range(T):
    N = int(input())
    coins = [int(input()) for _ in range(N)]
    M = int(input())
    dp = [0 for i in range(M)]

    for i in coins:
        for j in range(i, M+1):
            if j-i >= 0:
                dp[j] += dp[j-i]
    print(dp[M])