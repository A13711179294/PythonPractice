n, m = map(int, input().split())
dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
dp[1][0] = 1
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if i % 2 == 0 and j % 2 == 0:
            dp[i][j] = 0
        else:
            dp[i][j] = dp[i][j-1] + dp[i-1][j]
# for i in dp:
#     print(i)
print(dp[n][m])