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


m, n = map(int, input().split())
k = int(input())

pre = [0]
for i in range(1, n * m + 1):
    pre.append(i)

tmp = k
while tmp > 0:
    a, b = map(int, input().split())
    join(a, b)
    tmp -= 1

ans = 0
for i in range(1, m * n + 1):
    if pre[i] != i:
        ans += 1
print(n * m - ans)
