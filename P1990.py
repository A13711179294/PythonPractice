n = int(input())
mod = 10000
dp = [0] * (n + 1)
g = [0] * (n + 1)

dp[0] = dp[1] = g[1] = 1

for i in range(2, n + 1):
    dp[i] = ((dp[i - 1] + dp[i - 2]) % mod + 2 * g[i - 2] % mod) % mod
    g[i] = (g[i - 1] + dp[i - 1]) % mod


print(dp[n])