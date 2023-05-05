from collections import defaultdict
from sys import setrecursionlimit

setrecursionlimit(1000000)


def dfs(u, fa):
    li[u] = value[u]
    for i in graph[u]:
        if i != fa:
            dfs(i, u)
            if li[i] > 0:
                li[u] += li[i]


graph = defaultdict(list)
n = int(input())
li = [0] * (n + 1)
value = [0] + list(map(int, input().split()))
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1, 0)
ans = float('-inf')
for k in range(1, n + 1):
    ans = max(ans, li[k])

print(ans)
