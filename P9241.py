from sys import setrecursionlimit

setrecursionlimit(10000000)


def dfs(step, last):
    global flag
    if step == n + 1:
        flag = True
        return 0
    if flag:
        return 0
    for i in range(1, n + 1):
        if not vis[i]:
            if t[i] + d[i] < last:
                return 0
            vis[i] = 1
            s = t[i]
            if s < last:
                s = last
            dfs(step + 1, s + l[i])
            vis[i] = 0


for _ in range(int(input())):
    n = int(input())
    vis = [0] * (n + 1)
    flag = False
    t = [0]
    d = [0]
    l = [0]
    for _ in range(n):
        a, b, c = map(int, input().split())
        t.append(a)
        d.append(b)
        l.append(c)
    dfs(1, -1)
    if flag:
        print('YES')
    else:
        print('NO')
