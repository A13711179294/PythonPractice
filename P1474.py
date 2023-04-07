V, N = map(int, input().split())
v = []
while len(v) < V:
    v.extend(list(map(int, input().split())))
dp = [[0 for _ in range(N + 1)] for _ in range(V + 1)]
dp[0][0] = 1
for i in range(1, V + 1):
    for j in range(N + 1):
        if j >= v[i - 1]:
            dp[i][j] = dp[i][j - v[i - 1]] + dp[i - 1][j]
        else:
            dp[i][j] = dp[i - 1][j]
# for i in dp:
#     print(i)
print(dp[V][N])
