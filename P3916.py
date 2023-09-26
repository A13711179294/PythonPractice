import sys
from collections import defaultdict


def dfs(x, d):
    if visit[x]:
        return
    visit[x] = d
    for i in graph[x]:
        if not visit[i]:
            dfs(i, d)


sys.setrecursionlimit(1000000)
n, m = map(int, input().strip().split())
visit = [0 for _ in range(n + 1)]
graph = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().strip().split())
    graph[v].append(u)

for i in range(n, 0, -1):
    if not visit[i]:
        dfs(i, i)

print(*visit[1:])
