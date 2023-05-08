n, m = map(int, input().split())
val = list(map(int, input().split()))

dp = [[float('inf') for _ in range(n)] for _ in range(n)]
for i in range(n):
    dp[i][i] = 0

for _ in range(m):
    a, b, w = map(int, input().split())
    dp[a][b] = dp[b][a] = w

now = 0
for _ in range(int(input())):
    x, y, t = map(int, input().split())
    while now < n and val[now] <= t:
        for i in range(n):
            for j in range(n):
                if dp[i][j] > dp[i][now] + dp[j][now]:
                    dp[i][j] = dp[j][i] = dp[i][now] + dp[j][now]
        now += 1
    if val[x] > t or val[y] > t:
        print('-1')
    elif dp[x][y] == float('inf'):
        print(-1)
    else:
        print(dp[x][y])