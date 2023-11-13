def dfs(now):
    if now == k+1:
        print(*val[1:])
        return

    for i in range(1, n + 1):
        if vis[i] == 0:
            val[now] = i
            vis[i] = 1
            dfs(now + 1)
            vis[i] = 0


n, k = map(int, input().split())
vis = [0 for _ in range(n + 1)]
val = [0 for _ in range(k + 1)]
dfs(1)
