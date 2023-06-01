from collections import deque, defaultdict
from sys import stdin


def main():
    def spfa():
        q = deque()
        vis = [False] * (3 * n + 1)
        dis = [float('-inf')] * (3 * n + 1)
        dis[1] = 0
        q.append(1)
        vis[1] = True
        while q:
            cur = q.popleft()
            vis[cur] = False
            for v, w in edge[cur]:
                tmp = dis[cur] + w
                if tmp > dis[v]:
                    dis[v] = tmp
                    if not vis[v]:
                        q.append(v)
                        vis[v] = True
        return dis[3 * n]

    n, m = map(int, stdin.readline().split())
    edge = defaultdict(list)
    a = [0] + list(map(int, stdin.readline().split()))

    for i in range(1, n + 1):
        edge[i].append((i + n, -a[i]))
        edge[i + n].append((i + 2 * n, a[i]))

    for _ in range(m):
        x, y, z = map(int, stdin.readline().split())
        if z == 1:
            edge[x].append((y, 0))
            edge[x + n].append((y + n, 0))
            edge[x + 2 * n].append((y + 2 * n, 0))
        else:
            edge[x].append((y, 0))
            edge[y].append((x, 0))
            edge[x + n].append((y + n, 0))
            edge[x + 2 * n].append((y + 2 * n, 0))
            edge[y + n].append((x + n, 0))
            edge[y + 2 * n].append((x + 2 * n, 0))

    ret = spfa()
    if ret > 0:
        print(ret)
    else:
        print('0')


main()
