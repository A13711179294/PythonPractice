from collections import deque

n, m = map(int, input().strip().split())
graph = [[float('inf') for _ in range(n + 1)]for _ in range(n + 1)]
for i in range(1, n + 1):
    graph[i][i] = 0

# for i in graph:
#     print(i)

for _ in range(m):
    a, b = map(int, input().strip().split())
    graph[a][b] = graph[b][a] = 1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j or i == k or j == k:
                continue
            graph[j][i] = graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

t = int(input().strip())
q = deque()
for _ in range(t):
    v, u = map(int, input().strip().split())
    for i in range(1, n + 1):
        if graph[v][u] == graph[v][i] + graph[i][u]:
            q.append(i)

    while q:
        print(q.popleft(), end=' ')
    print()
