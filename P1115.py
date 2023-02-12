n = int(input().strip())
a = [0]
a.extend(list(map(int, input().strip().split())))
dp = [0] * (n + 1)
ans = min(a[1:])
for i in range(1, n+1):
    dp[i] = max(dp[i - 1] + a[i], a[i])
    ans = max(ans, dp[i])
print(ans)
