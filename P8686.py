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


N = int(input())
pre = [0]
for i in range(1, 1000001):
    pre.append(i)

A = [0]
A.extend(list(map(int, input().split())))
for i in range(1, N + 1):
    A[i] = find(A[i])
    pre[A[i]] = find(pre[A[i]] + 1)

for i in A[1::]:
    print(i, end=' ')