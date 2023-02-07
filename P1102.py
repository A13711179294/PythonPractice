N, C = map(int,input().split())
a = list(map(int, input().split()))
mapn = {}

for i in a:
    mapn[i] = mapn.get(i, 0) + 1

for i in range(len(a)):
    a[i] -= C

cnt = 0
for i in a:
    if i in mapn:
        cnt += mapn[i]

print(cnt)
