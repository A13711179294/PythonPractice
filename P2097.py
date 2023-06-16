def find(x):
    if pre[x] == x:
        return x
    pre[x] = find(pre[x])
    return pre[x]


def join(x, y):
    pre[find(x)] = find(y)


n, m = map(int, input().strip().split())
pre = [k for k in range(n + 1)]
for _ in range(m):
    p, q = map(int, input().strip().split())
    join(p, q)

ans = 0
for i in range(1, n + 1):
    if pre[i] == i:
        ans += 1
print(ans)
