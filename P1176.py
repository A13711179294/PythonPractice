N, M = map(int, input().split())
tmp = M
point = []
while tmp > 0:
    point.append(tuple(map(int, input().split())))
    tmp -= 1

map1 = [[0 for i in range(N + 1)] for j in range(N + 1)]
map2 = [[0 for i in range(N + 1)] for j in range(N + 1)]

for i in point:
    map2[i[0]][i[1]] = 1

map1[1][0] = 1

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if map2[i][j] != 1:
            map1[i][j] = (map1[i][j - 1] + map1[i - 1][j]) % 100003

print(map1[N][N])