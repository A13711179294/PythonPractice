n = int(input().strip())
a = list(map(int, input().split()))
a.sort()
d = 100001
for i in range(n - 1):
    tmp = a[i + 1] - a[i]
    if tmp < d:
        d = tmp
if d != 0:
    print((a[-1] - a[0])//d + 1)
else:
    print(n)
