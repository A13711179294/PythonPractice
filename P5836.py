from sys import setrecursionlimit

setrecursionlimit(10000000)


def find(x):
    if pre[x] == x:
        return x
    pre[x] = find(pre[x])
    return pre[x]


def join(x, y):
    fx = find(x)
    fy = find(y)
    if fx != fy:
        pre[fx] = fy


n, m = map(int, input().split())
pre = [i for i in range(n + 1)]
s = list(' ' + input())
ans = [0] * (m + 1)

for _ in range(n - 1):
    x, y = map(int, input().split())
    if s[x] == s[y]:
        join(x, y)

cnt = 0
for _ in range(m):
    a, b, c = input().split()
    a = int(a)
    b = int(b)
    cnt += 1
    if find(a) == find(b) and s[a] != c:
        ans[cnt] = 0
    else:
        ans[cnt] = 1

for i in range(1, cnt + 1):
    print(ans[i], end='')