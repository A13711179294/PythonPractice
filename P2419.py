n, m = map(int, input().split())
dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    dp[a][b] = 1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dp[i][j] |= dp[i][k] & dp[k][j]

ans = 0
for i in range(1, n + 1):
    cnt = 1
    for j in range(1, n + 1):
        if i == j:
            continue
        cnt = cnt & (dp[i][j] | dp[j][i])
    ans += cnt

print(ans)
