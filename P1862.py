n = int(input())
a = []
for _ in range(n):
    x, y = map(int, input().split())
    a.append(y)

a.sort()
if n % 2 == 0:
    mid = (a[n // 2] + a[n // 2 - 1]) // 2
else:
    mid = a[n // 2]

ans = 0
for i in range(n):
    ans += abs(a[i] - mid)

print(ans)
