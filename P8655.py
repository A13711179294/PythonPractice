from collections import defaultdict


def dfs(u):
    if u == t2:
        for i in range(1, n + 1):
            if vis[i]:
                print(i, end=' ')
    for v in graph[u]:
        if not vis[v]:
            vis[v] = True
            dfs(v)
            vis[v] = False


def find(x):
    if pre[x] == x:
        return x
    pre[x] = find(pre[x])
    return pre[x]


def join(x, y):
    fx = find(x)
    fy = find(y)
    if fx != fy:
        pre[fx] = fy


n = int(input())
pre = [i for i in range(n + 1)]
vis = [False] * (n + 1)
graph = defaultdict(list)
t1 = t2 = 1
for _ in range(n):
    a, b = map(int, input().split())
    if find(a) == find(b):
        t1 = a
        t2 = b
    else:
        graph[a].append(b)
        graph[b].append(a)
        join(a, b)
    #print(pre)
#print(graph)
vis[t1] = True
dfs(t1)
