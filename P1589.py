n, L = map(int, input().split())
tmp = n
road = []
while tmp > 0:
    road.append(tuple(map(int, input().split())))
    tmp -= 1

road.sort(key=lambda x: x[0])
left = 0
count1 = 0
for i in range(n):
    left = max(road[i][0], left)
    while left < road[i][1]:
        left += L
        count1 += 1
print(count1)
