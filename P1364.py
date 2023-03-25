n = int(input())
dp = [[float('inf') for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    dp[i][i] = 0
w = [0]
for i in range(1, n + 1):
    t, u, v = map(int, input().split())
    w.append(t)
    if u > 0:
        dp[i][u] = dp[u][i] = 1
    if v > 0:
        dp[i][v] = dp[v][i] = 1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != k and j != k and dp[i][j] > dp[i][k] + dp[k][j]:
                dp[i][j] = dp[i][k] + dp[k][j]

# for i in dp:
#     print(i)

min1 = float('inf')
for i in range(1, n + 1):
    tmp = 0
    for j in range(1, n + 1):
        tmp += dp[i][j] * w[j]
    if tmp < min1:
        min1 = tmp

print(min1)