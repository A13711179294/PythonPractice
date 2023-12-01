from collections import deque, defaultdict


def spfa():
    q = deque()
    dis = [0] * (n + 1)
    q.append(0)
    while q:
        u = q.popleft()
        for v, w in edge[u]:
            dep[v] -= 1
            dis[v] = max(dis[v], dis[u] + w)
            if dep[v] == 0:
                q.append(v)

    return dis


edge = defaultdict(list)
n, m, c = map(int, input().split())
dep = [0] * (n + 1)
s = [0] + list(map(int, input().split()))

for i in range(1, n + 1):
    edge[0].append((i, s[i]))
    dep[i] += 1

for _ in range(c):
    a, b, x = map(int, input().split())
    edge[a].append((b, x))
    dep[b] += 1

ret = spfa()
for i in ret[1:]:
    print(i)
