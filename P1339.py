from collections import defaultdict
import heapq

def dirjkstra():
    dirs = [float('inf')] * (n + 1)
    dirs[start] = 0
    visit = [0] * (n + 1)

    pq = []
    heapq.heappush(pq, (0, start))
    while pq:
        _, u = heapq.heappop(pq)
        visit[u] = True

        next_node_list = graph[u]
        for v, w in next_node_list:
            tmp = dirs[u] + w
            if tmp < dirs[v]:
                dirs[v] = tmp
                if not visit[v]:
                    heapq.heappush(pq, (tmp, v))

    if dirs[t] == float('inf'):
        return -1
    else:
        return dirs[t]


n, m, s, t = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

start = s
ret = dirjkstra()
print(ret)