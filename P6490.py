n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))

ans = 0
for i in range(n - 1, 0, -1):
    if a[i] <= a[i - 1]:
        ans += a[i - 1] - a[i] + 1
        a[i - 1] = a[i] - 1

print(ans)
