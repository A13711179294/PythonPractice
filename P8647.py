n, k = map(int, input().strip().split())
a = []
tmp = n
while tmp > 0:
    a.append(tuple(map(int, input().strip().split())))
    tmp -= 1

left = 1
right = 100001

while left + 1 < right:
    mid = (left + right) // 2
    sum = 0
    for value in a:
        sum += (value[0] // mid) * (value[1] // mid)
    if sum >= k:
        left = mid
    else:
        right = mid

print(left)
