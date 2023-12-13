n, k = map(int, input().split())
t = list(map(int, input().split()))
a = [0] * 100001

for x in t:
    a[x] += 1

ans = 0
if k == 0:
    for i in range(0, 100001):
        if a[i]:
            ans += 1
    print(ans)
else:
    for i in range(0, 100001 - k):
        if a[i] < a[i + k]:
            a[i + k] -= a[i]
        else:
            a[i + k] = 0

    for i in range(0, 100001 - k):
        ans += a[i]

    print(ans)