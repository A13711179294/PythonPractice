from collections import deque


def bfs(x, y):
    queue.append((x, y))
    visit1[x][y] = 1
    while queue:
        curnode = queue.popleft()
        for dir in dirs:
            nextnode = dir(curnode[0], curnode[1])
            if (0 <= nextnode[0] < n) and (0 <= nextnode[1] < n) and visit1[nextnode[0]][nextnode[1]] == 0 and map1[nextnode[0]][nextnode[1]] == '#':
                visit1[nextnode[0]][nextnode[1]] = 1
                queue.append((nextnode[0], nextnode[1]))
            else:
                continue


n = int(input().strip())

queue = deque()
dirs = [lambda x, y: (x, y + 1), lambda x, y: (x + 1, y), lambda x, y: (x, y - 1), lambda x, y: (x - 1, y)]

map1 = []
tmp = n
while tmp > 0:
    map1.append(list(input().strip()))
    tmp -= 1

visit1 = [[0] * n for _ in range(n)]
ans1 = 0
for i in range(n):
    for j in range(n):
        if map1[i][j] == '#' and visit1[i][j] == 0:
            bfs(i, j)
            ans1 += 1

visit1 = [[0] * n for _ in range(n)]
ans2 = 0
for i in range(n):
    for j in range(n):
        if map1[i][j] == '#' and map1[i][j + 1] == '#' and map1[i + 1][j] == '#' and map1[i][j - 1] == '#' and map1[i - 1][j] == '#' and visit1[i][j] == 0:
            bfs(i, j)
            ans2 += 1

print(ans1 - ans2)
