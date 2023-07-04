m, n = map(int, input().split())
road = [0 for _ in range(n)]
road[m - 1] = 1
road[m] = 1
for i in range(m + 1, n):
    road[i] = road[i-1]+road[i-2]

print(road[n-1])
