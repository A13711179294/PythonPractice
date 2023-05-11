from collections import deque, defaultdict
from math import sqrt


def Spfa():
    vis = [False] * (n + 1)
    vis[start] = True
    dirs = [float('inf')] * (n + 1)
    dirs[start] = 0
    queue = deque()
    queue.append(start)
    while queue:
        cur = queue.popleft()
        vis[cur] = False
        for v, w in li[cur]:
            tmp = dirs[cur] + w
            if dirs[v] > tmp:
                dirs[v] = tmp
                if not vis[v]:
                    queue.append(v)
                    vis[v] = True
    return dirs[t]


def distance(x1, y1, x2, y2):
    return sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))


li = defaultdict(list)

n = int(input())
node = [(0, 0)]
for _ in range(n):
    node.append(tuple(map(int, input().split())))

for _ in range(int(input())):
    a, b = map(int, input().split())
    tmp_len = distance(node[a][0], node[a][1], node[b][0], node[b][1])
    li[a].append((b, tmp_len))
    li[b].append((a, tmp_len))

s, t = map(int, input().split())

start = s
print('%.2f' % Spfa())
