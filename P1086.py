m, n, k = map(int, input().split())
map1 = []
tmp = m
while tmp > 0:
    map1.append(list(map(int, input().split())))
    tmp -= 1

location = []
for i in range(m):
    for j in range(n):
        if map1[i][j] != 0:
            location.append((map1[i][j], i, j))

k -= 2
if k > 0 and len(location) > 0:
    ans = 0
    location.sort(key=lambda x: x[0], reverse=True)
    if location[0][1] * 2 < k:
        k -= location[0][1] + 1
        ans += location[0][0]
        for i in range(1, len(location)):
            time = abs(location[i][1] - location[i - 1][1]) + abs(location[i][2] - location[i - 1][2])
            if time + location[i][1] + 1 > k:
                break
            else:
                k -= time + 1
                ans += location[i][0]
    print(ans)
else:
    print(0)
