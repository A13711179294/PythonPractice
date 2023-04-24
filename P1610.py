n, dist = map(int, input().split())
p = list(map(int, input().split()))
p.sort()
ans = 0
for i in range(1, n - 1):
    if p[i + 1] - p[i - 1] <= dist:
        ans += 1
        p[i] = p[i - 1]

print(ans)
