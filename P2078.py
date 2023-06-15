def find(x):
    if pre[x] == x:
        return x
    pre[x] = find(pre[x])
    return pre[x]


def join(x, y):
    t1 = find(pre[x])
    t2 = find(pre[y])
    if t1 != t2:
        pre[t1] = t2


N, M, P, Q = map(int, input().split())
pre = [0]
for i in range(1, N + M + 1):
    pre.append(i)

tmp = P
while tmp > 0:
    xi, yi = map(int, input().split())
    join(xi, yi)
    tmp -= 1

tmp = Q
while tmp > 0:
    xi, yi = map(int, input().split())
    join(-xi + N, -yi + N)
    tmp -= 1


ansm = 0
ansl = 0
for i in range(1, N + 1):
    if find(i) == find(1):
        ansm += 1
for i in range(N + 1, N + M + 1):
    if find(i) == find(N + 1):
        ansl += 1

print(min(ansm, ansl))
