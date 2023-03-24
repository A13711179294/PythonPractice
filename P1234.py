n, m = map(int, input().split())

graph = [[0 for _ in range(m + 6)] for _ in range(n + 6)]

for i in range(3, n + 3):
    j = 3
    for k in list(input()):
        graph[i][j] = k
        j += 1

# for g in graph:
#     print(g)

ans = 0
for i in range(3, n + 3):
    for j in range(3, m + 3):
        if graph[i][j] == 'h' and graph[i][j + 1] == 'e' and graph[i][j + 2] == 'h' and graph[i][j + 3] == 'e':
            ans += 1
        if graph[i][j] == 'h' and graph[i][j - 1] == 'e' and graph[i][j - 2] == 'h' and graph[i][j - 3] == 'e':
            ans += 1
        if graph[i][j] == 'h' and graph[i + 1][j] == 'e' and graph[i + 2][j] == 'h' and graph[i + 3][j] == 'e':
            ans += 1
        if graph[i][j] == 'h' and graph[i - 1][j] == 'e' and graph[i - 2][j] == 'h' and graph[i - 3][j] == 'e':
            ans += 1

print(ans)