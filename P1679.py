from math import sqrt, ceil

m = int(input())
dp = [float('inf') for _ in range(m + 1)]
value = [0]
n = ceil(sqrt(sqrt(m)))
for i in range(1, n + 1):
    value.append(i ** 4)

dp[0] = 0
for i in range(1, n + 1):
    for j in range(value[i], m + 1):
        dp[j] = min(dp[j], dp[j - value[i]] + 1)

print(dp[m])