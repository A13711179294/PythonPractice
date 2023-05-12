n = int(input())
s = [0] + list(map(int, input().split()))
dp = [[float('inf') for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    dp[i][i] = 0
    s[i] += s[i - 1]

for i in range(2, n + 1):
    for j in range(1, n - i + 1 + 1):
        e = j + i - 1
        dp[j][e] = min(dp[j][k] + dp[k + 1][e] for k in range(j, e)) + s[e] - s[j - 1]

print(dp[1][n])
