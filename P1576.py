from collections import defaultdict
import heapq


def main():
    def dijkstra():
        dirs = [300000000] * (n + 1)
        dirs[start] = 100
        visit = [False] * (n + 1)
        pq = []
        heapq.heappush(pq, (1, start))
        while pq:
            _, u = heapq.heappop(pq)
            visit[u] = False
            for v, w in graph[u]:
                if dirs[v] > dirs[u] / (1 - 0.01 * w):
                    dirs[v] = dirs[u] / (1 - 0.01 * w)
                    if not visit[v]:
                        visit[v] = True
                        heapq.heappush(pq, (dirs[u] / (1 - 0.01 * w), v))

        return dirs[a]

    n, m = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        u1, v1, z1 = map(int, input().split())
        graph[u1].append((v1, z1))
        graph[v1].append((u1, z1))

    a, b = map(int, input().split())

    start = b
    print('%.8f' % dijkstra())


main()