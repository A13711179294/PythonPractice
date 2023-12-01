from collections import defaultdict


def dfs(cur, deep):
    global ans
    if deep >= d:
        return
    for x in tree[cur]:
        if not vis[x]:
            vis[cur] = True
            ans += 1
            dfs(x, deep + 1)


tree = defaultdict(list)
n, d = map(int, input().split())
vis = [False] * (n + 1)
for _ in range(n - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

ans = 0
dfs(1, 0)
print(ans)
