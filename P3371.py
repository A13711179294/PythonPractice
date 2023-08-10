from heapq import heappush, heappop
from collections import defaultdict
from sys import stdin, stdout


def main():
    def dijkstra():
        inf = (1 << 31) - 1
        dirs = [inf] * (n + 1)
        dirs[s] = 0
        visit = [False] * (n + 1)
        pq = []
        heappush(pq, (0, s))

        while pq:
            _, u = heappop(pq)
            if visit[u]:
                continue
            else:
                visit[u] = True
            for v, w in graph[u]:
                t = dirs[u] + w
                if t < dirs[v]:
                    dirs[v] = t
                    if not visit[v]:
                        heappush(pq, (t, v))
        return dirs

    n, m, s = map(int, stdin.readline().split())
    graph = defaultdict(list)
    for _ in range(m):
        u, v, w = map(int, stdin.readline().split())
        graph[u].append((v, w))

    stdout.write(' '.join(map(str, dijkstra()[1:])))


main()
