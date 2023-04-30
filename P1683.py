def dfs(x, y):
    global ans
    for k in range(5):
        if 0 <= x + dir_x[k] < h and 0 <= y + dir_y[k] < w and visit[x + dir_x[k]][y + dir_y[k]] == 0 and graph[x + dir_x[k]][y + dir_y[k]] == '.':
            visit[x + dir_x[k]][y + dir_y[k]] = 1
            ans += 1
            dfs(x + dir_x[k], y + dir_y[k])


w, h = map(int, input().split())
visit = [[0 for _ in range(w)] for _ in range(h)]
dir_x = [0, 0, 1, 0, -1]
dir_y = [0, 1, 0, -1, 0]
graph = []
for _ in range(h):
    graph.append(list(input()))

# for i in graph:
#     print(i)

ans = 1
for i in range(h):
    for j in range(w):
        if graph[i][j] == '@':
            dfs(i, j)

print(ans)