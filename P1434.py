def dfs(x, y):
    if s[x][y]:
        return s[x][y]
    s[x][y] = 1
    for dir in range(4):
        t1 = x + dx[dir]
        t2 = y + dy[dir]
        if 0 <= t1 < r and 0 <= t2 < c and graph[x][y] > graph[t1][t2]:
            dfs(t1, t2)
            s[x][y] = max(s[x][y], s[t1][t2] + 1)
    return s[x][y]


r, c = map(int, input().split())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
s = [[0 for _ in range(c)] for _ in range(r)]
graph = []
for _ in range(r):
    graph.append(list(map(int, input().split())))

ans = 0
for i in range(r):
    for j in range(c):
        ans = max(ans, dfs(i, j))

print(ans)