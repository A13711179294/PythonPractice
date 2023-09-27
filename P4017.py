from collections import defaultdict, deque
from sys import stdin


def main():
    n, m = map(int, stdin.readline().split())
    q = deque()
    mod = 80112002
    cnt = [[0 for _ in range(2)] for _ in range(n + 1)]
    f = [0] * (n + 1)
    edge = defaultdict(list)

    for _ in range(m):
        a, b = map(int, stdin.readline().split())
        edge[a].append(b)
        cnt[a][0] += 1
        cnt[b][1] += 1

    for i in range(1, n + 1):
        if not cnt[i][1]:
            f[i] = 1
            q.append(i)

    while q:
        cur = q.popleft()
        for v in edge[cur]:
            cnt[v][1] -= 1
            f[v] = (f[v] + f[cur]) % mod
            if not cnt[v][1]:
                q.append(v)

    ans = 0
    for i in range(1, n + 1):
        if not cnt[i][0]:
            ans = (ans + f[i]) % mod

    print(ans)


main()
