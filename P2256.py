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


N, M = map(int, input().strip().split())
pre = [0]
for i in range(1, N + 1):
    pre.append(i)

name = {}
tmp = 1
while tmp <= N:
    name[input().strip()] = tmp
    tmp += 1

tmp = M
while tmp > 0:
    a, b = input().strip().split()
    join(name[a], name[b])
    tmp -= 1

K = int(input().strip())
tmp = K
while tmp > 0:
    a, b = input().strip().split()
    if a in name and b in name:
        if find(name[a]) == find(name[b]):
            print('Yes.')
        else:
            print('No.')
    else:
        print('No.')
    tmp -= 1
