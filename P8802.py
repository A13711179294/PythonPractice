import heapq
from collections import defaultdict


def dijkstra():
    dirs = [float('inf')] * (n + 1)
    dirs[start] = 0
    seen = [False] * (n + 1)
    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        _, u = heapq.heappop(pq)
        if seen[u]:
            continue
        seen[u] = True
        nodeList = graph[u]
        for v, w, k in nodeList:
            t = dirs[u] + w + k
            if t < dirs[v]:
                dirs[v] = t
                if not seen[v]:
                    heapq.heappush(pq, (t, v))

    return dirs


n, m = map(int, input().split())
graph = defaultdict(list)
start = 1
time = [0] + list(map(int, input().split()))

for _ in range(m):
    u, v, c = map(int, input().split())
    graph[u].append((v, c, time[v]))
    graph[v].append((u, c, time[u]))

answer = dijkstra()
print(answer[n] - time[n])
