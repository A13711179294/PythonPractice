def find(x):
    # while pre[x] != x:
    #     x = pre[x]
    # return x
    if pre[x] == x:
        return x
    pre[x] = find(pre[x])
    return pre[x]


def join(x, y):
    t1 = find(x)
    t2 = find(y)
    if t1 != t2:
        pre[t1] = t2


N, M = map(int, input().split())
pre = [0]
for i in range(1, N + 1):
    pre.append(i)

ans = []

tmp = M
while tmp > 0:
    z, x, y = map(int, input().split())
    if z == 1:
        join(x, y)
    elif z == 2:
        t1 = find(x)
        t2 = find(y)
        if t1 != t2:
            ans.append('N')
        else:
            ans.append('Y')
    tmp -= 1
for i in ans:
    print(i)
