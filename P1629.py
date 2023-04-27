from collections import defaultdict
import heapq

def dirjkstra(li):
    visit = [False] * (n + 1)
    dirs = [float('inf')] * (n + 1)
    dirs[start] = 0
    pq = []
    heapq.heappush(pq, (0, start))
    while pq:
        _, u = heapq.heappop(pq)
        visit[u] = True
        nodelist = li[u]
        for v, w in nodelist:
            tmp = dirs[u] + w
            if tmp < dirs[v]:
                dirs[v] = tmp
                if not visit[v]:
                    heapq.heappush(pq, (tmp, v))

    return dirs


n, m = map(int, input().split())
start = 1
graph1 = defaultdict(list)
graph2 = defaultdict(list)
for _ in range(m):
    u, v, w = map(int, input().split())
    graph1[u].append((v, w))
    graph2[v].append((u, w))

ret1 = dirjkstra(graph1)
ret2 = dirjkstra(graph2)
print(sum(ret1[1:]) + sum(ret2[1:]))
