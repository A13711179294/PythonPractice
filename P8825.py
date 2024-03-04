n, k = map(int, input().split())
dp = [[0] * (k + 1) for _ in range(n + 1)]
dp[0][0] = 1
for i in range(1, n + 1):
    for j in range(1, 6 + 1):
        for l in range(0, k):
            dp[i][(l * 10 + j) % k] += dp[i - 1][l]
print(dp[n][0])
