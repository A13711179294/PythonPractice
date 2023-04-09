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


while True:
    tmp = input().strip()
    if len(tmp) == 1:
        break
    n, m = map(int, tmp.split())
    pre = [k for k in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().strip().split())
        join(u, v)

    ans = 0
    for i in range(1, n + 1):
        if pre[i] == i:
            ans += 1

    print(ans - 1)
