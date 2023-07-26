from collections import deque, defaultdict


def spfa():
    q = deque()
    dis = [0] * (n + 1)
    for i in range(1, n + 1):
        if deg[i] == 0:
            q.append(i)
            dis[i] = time[i]
    while q:
        u = q.popleft()
        for v in edge[u]:
            deg[v] -= 1
            tmp = dis[u] + time[v]
            if dis[v] < tmp:
                dis[v] = tmp
            if deg[v] == 0:
                q.append(v)
    return dis[1:]


edge = defaultdict(list)
n, m = map(int, input().split())
time = [0]
deg = [0] * (n + 1)
for i in range(1, n + 1):
    time.append(int(input()))

for i in range(1, m + 1):
    x, y = map(int, input().split())
    edge[x].append(y)
    deg[y] += 1

ans = 0
for x in spfa():
    ans = max(ans, x)

print(ans)
