n, m = map(int, input().split())
d = [0] * (n + 1)
u = [0] * (m + 1)
v = [0] * (m + 1)

tmp = 1
while tmp <= m:
    u1, v1 = map(int, input().split())
    u[tmp] = u1
    v[tmp] = v1
    d[u1] += 1
    d[v1] += 1
    tmp += 1

ans = 0
for i in range(1, m + 1):
    if d[u[i]] > 1 and d[v[i]] > 1:
        ans += (d[u[i]] - 1) * (d[v[i]]-1) * 2

print(ans)
