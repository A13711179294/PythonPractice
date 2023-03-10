n, k = map(int, input().split())
dp = [[99999 for _ in range(n - k + 1)] for _ in range(n + 1)]
a = [(0, 0)]
for _ in range(n):
    a.append(tuple(map(int, input().split())))

a.sort(key=lambda x: x[0])

for i in range(1, n + 1):
    dp[i][1] = 0

for i in range(2, n + 1):
    for j in range(2, min(i, n - k) + 1):
        for t in range(j - 1,  i):
            dp[i][j] = min(dp[i][j], dp[t][j - 1] + abs(a[i][1] - a[t][1]))

for v in dp:
    print(v)

ans = 999999
for i in range(n - k, n + 1):
    ans = min(ans, dp[i][n - k])
print(ans)