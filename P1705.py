m, r, n = map(int, input().split())
a = [0] + list(map(int, input().split()))
dp = [[0 for _ in range(3000)] for _ in range(40)]

t = sum(a)

dp[0][0] = 1
for i in range(1, m + 1):
    for j in range(r, 0, -1):
        for k in range(a[i], t + 1):
            dp[j][k] += dp[j - 1][k - a[i]]

ans = 0
for i in range(n + 1, t + 1):
    ans += dp[r][i]

print(ans)