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


n, m, p = map(int, input().split())
pre = [0]
for i in range(1, n + 1):
    pre.append(i)

relation = []

tmp = m
while tmp > 0:
    people1, people2 = map(int, input().split())
    join(people1, people2)
    tmp -= 1

tmp = p
while tmp > 0:
    relation.append(tuple(map(int, input().split())))
    tmp -= 1

for i in relation:
    if find(i[0]) == find(i[1]):
        print('Yes')
    else:
        print('No')
