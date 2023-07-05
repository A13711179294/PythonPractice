n, k = map(int, input().split())
L = []
tmp = n
while tmp > 0:
    L.append(int(input()))
    tmp -= 1

l = 0
r = 100000001

while l + 1 < r:
    mid = (l + r) // 2
    cnt = 0
    for i in range(n):
        cnt += L[i] // mid
    if cnt >= k:
        l = mid
    else:
        r = mid

print(l)
