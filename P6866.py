n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
graph[0].extend(['.'] * (m + 1))

for i in range(1, n + 1):
    graph[i].extend('.' + input())

count = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if graph[i][j] == '*' and graph[i][j-1] == '.' and graph[i-1][j] == '.':
            count += 1

print(count)
