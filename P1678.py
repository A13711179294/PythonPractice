import bisect

m, n = map(int, input().split())
a = [float('-inf')] + list(map(int, input().split())) + [float('inf')]
b = [float('-inf')] + list(map(int, input().split()))

a.sort()

ans = 0
for i in range(1, n + 1):
    t = bisect.bisect(a, b[i])
    ans += min(abs(a[t] - b[i]), abs(b[i] - a[t - 1]))

print(ans)
