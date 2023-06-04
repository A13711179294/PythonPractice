from collections import defaultdict


def dfs(u):
    if f[u]:
        return f[u]
    for v in edge[u]:
        f[u] = max(f[u], dfs(v))
    f[u] += a[u]
    return f[u]


n = int(input())
f = [0] * (n + 1)
edge = defaultdict(list)
a = [0]
for i in range(1, n + 1):
    tmp = list(map(int, input().split()))
    a.append(tmp[1])
    for j in range(2, len(tmp) - 1):
        edge[tmp[j]].append(i)

ans = 0
for i in range(1, n + 1):
    ans = max(ans, dfs(i))

print(ans)
