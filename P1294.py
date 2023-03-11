def dfs(x, sum1):
    global ans
    ans = max(ans, sum1)
    for j in range(1, n + 1):
        if visit[j] == 0 and graph[x][j] != 0:
            visit[x] = 1
            dfs(j, sum1 + graph[x][j])
            visit[x] = 0


n, m = map(int, input().split())
visit = [0] * (n + 1)
graph = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c

# for i in graph:
#     print(i)

ans = 0
for i in range(1, n + 1):
    dfs(i, 0)
print(ans)
