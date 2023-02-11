def find(x):
    if pre[x] == x:
        return x
    pre[x] = find(pre[x])
    return pre[x]


def join(x, y):
    t1 = find(x)
    t2 = find(y)
    if t1 != t2:
        pre[t1] = t2
        return True


N, M = map(int, input().split())
pre = [0]
for i in range(1, N + 1):
    pre.append(i)

tmp = M
road = []
while tmp > 0:
    road.append(tuple(map(int, input().split())))
    tmp -= 1

road.sort(key=lambda x: x[2])

ans = -1
count = N
for i in range(M):
    if count > 1:
        ret = join(road[i][0], road[i][1])
        if ret:
            count -= 1
        if count == 1:
            ans = road[i][2]
            break

print(ans)
