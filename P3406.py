n, m = map(int, input().split())
p = [0] + list(map(int, input().split()))
li = [0]
for _ in range(n - 1):
    li.append(tuple(map(int, input().split())))

d = [0] * (n + 1)
p1 = p[1]
for p2 in p[2:]:
    if p1 < p2:
        d[p1] += 1
        d[p2] -= 1
    else:
        d[p2] += 1
        d[p1] -= 1
    p1 = p2

for i in range(1, n + 1):
    d[i] = d[i - 1] + d[i]

ans = 0
for i in range(1, n):
    ans += min(li[i][0] * d[i], li[i][1] * d[i] + li[i][2])

print(ans)
