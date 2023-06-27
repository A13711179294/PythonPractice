from collections import defaultdict, deque


def bfs1():
    q = deque()
    q.append(t)
    can[t] = 1
    while q:
        cur = q.popleft()
        for nex in edge2[cur]:
            if not can[nex]:
                q.append(nex)
                can[nex] = 1


def bfs2():
    q = deque()
    dis = [0] * (n + 1)
    dis[s] = 1
    q.append(s)
    while q:
        cur = q.popleft()
        for nex in edge1[cur]:
            if inroad[nex] and not dis[nex]:
                dis[nex] = dis[cur] + 1
                q.append(nex)
    return dis[t] - 1


n, m = map(int, input().split())
can = [0] * (n + 1)
inroad = [0] * (n + 1)
edge1 = defaultdict(list)
edge2 = defaultdict(list)

for _ in range(m):
    x, y = map(int, input().split())
    edge1[x].append(y)
    edge2[y].append(x)
s, t = map(int, input().split())

bfs1()
if not can[1]:
    print('-1')
else:
    for i in range(1, n + 1):
        if can[i]:
            inroad[i] = 1
            for j in edge1[i]:
                if not can[j]:
                    inroad[i] = 0
                    break

    if not inroad[s]:
        print('-1')
    else:
        ret = bfs2()
        if ret:
            print(ret)
        else:
            print('-1')
