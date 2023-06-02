n, m = map(int, input().split())
dp = [[0 for _ in range(102)] for _ in range(102)]
a = [0] + list(map(int, input().split()))

dp[0][0] = 1
for i in range(1, n + 1):
    for j in range(0, m + 1):
        for k in range(0, min(j, a[i]) + 1):
            dp[i][j] = (dp[i][j] + dp[i - 1][j - k]) % 1000007

print(dp[n][m])
