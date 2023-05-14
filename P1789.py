n, m, k = map(int, input().split())
graph = [[0 for _ in range(n + 4)] for _ in range(n + 4)]

tmp = m
while tmp > 0:
    x, y = map(int, input().split())
    graph[x + 1][y + 1] = 1
    graph[x + 1][y] = 1
    graph[x + 1][y - 1] = 1
    graph[x + 1][y + 2] = 1
    graph[x + 1][y + 3] = 1

    graph[x + 2][y + 1] = 1
    graph[x + 3][y + 1] = 1
    graph[x][y + 1] = 1
    graph[x - 1][y + 1] = 1

    graph[x][y] = 1
    graph[x][y + 2] = 1
    graph[x + 2][y] = 1
    graph[x + 2][y + 2] = 1

    tmp -= 1

tmp = k
while tmp > 0:
    x, y = map(int, input().split())

    for i in range(x - 1, x + 4):
        for j in range(y - 1, y + 4):
            graph[i][j] = 1

    tmp -= 1

sum1 = 0
for i in graph[2:-2]:
    sum1 += i[2:-2].count(0)
print(sum1)
