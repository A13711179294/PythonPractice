from collections import defaultdict
from sys import stdin
import heapq


def main():
    def dijkstra(x):
        if a[1] > x:
            return False
        seen = [False] * (n + 1)
        dis = [float('inf')] * (n + 1)
        dis[1] = 0
        pq = []
        heapq.heappush(pq, (0, 1))
        while pq:
            _, u = heapq.heappop(pq)
            if seen[u]:
                continue
            seen[u] = True
            for v, w in edge[u]:
                t = dis[u] + w
                if a[v] <= x and t < dis[v]:
                    dis[v] = t
                    if not seen[v]:
                        heapq.heappush(pq, (t, v))

        return dis[n] <= b

    n, m, b = map(int, stdin.readline().split())
    edge = defaultdict(list)
    a = [0]
    for _ in range(n):
        a.append(int(stdin.readline()))

    for _ in range(m):
        ai, bi, ci = map(int, stdin.readline().split())
        edge[ai].append((bi, ci))
        edge[bi].append((ai, ci))

    l = min(a[1:])
    r = max(a[1:])
    while l < r:
        mid = l + r >> 1
        if dijkstra(mid):
            r = mid
        else:
            l = mid + 1
    if not dijkstra(l):
        print("AFK")
    else:
        print(l)


main()