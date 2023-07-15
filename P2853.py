from collections import defaultdict


def dfs(now):
    vis[now] = True
    b[now] += 1
    for x in graph[now]:
        if not vis[x]:
            vis[x] = True
            dfs(x)


k, n, m = map(int, input().split())

graph = defaultdict(list)
a = [0]
b = [0] * (n + 1)
for _ in range(k):
    a.append(int(input()))

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

for i in range(1, k + 1):
    vis = [False] * (n + 1)
    dfs(a[i])

ans = 0
for i in range(1, n + 1):
    if b[i] == k:
        ans += 1
print(ans)
