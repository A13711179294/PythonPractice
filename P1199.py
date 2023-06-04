n = int(input())
graph = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(1, n):
    t = [0] * (i + 1) + list(map(int, input().split()))
    for j in range(i + 1, n + 1):
        graph[i][j] = graph[j][i] = t[j]

ans = 0
for i in range(1, n + 1):
    graph[i].sort()
    if graph[i][n - 1] > ans:
        ans = graph[i][n - 1]

print('1', ans, sep='\n')
