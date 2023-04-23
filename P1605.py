def dfs(x, y):
    if x == FX and y == FY:
        return 1
    ans = 0
    for dir in dirs:
        tx = dir(x, y)[0]
        ty = dir(x, y)[1]
        if 0 < tx <= n and 0 < ty <= m and visit[tx][ty] == 0 and graph[tx][ty] == 0:
            visit[tx][ty] = 1
            ans += dfs(tx, ty)
            visit[tx][ty] = 0
    return ans


n, m, t = map(int, input().split())
graph = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
visit = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
SX, SY, FX, FY = map(int, input().split())

dirs = [lambda x, y: (x, y + 1),
        lambda x, y: (x + 1, y),
        lambda x, y: (x, y - 1),
        lambda x, y: (x - 1, y)]

for _ in range(t):
    a, b = map(int, input().split())
    graph[a][b] = 1

# for i in graph:
#     print(i)
visit[SX][SY] = 1
print(dfs(SX, SY))
