from collections import deque


def bfs(x, y):
    visit[x][y] = 1
    map1[x][y] = 3
    queue.append((x, y))
    while queue:
        cur_node = queue.popleft()
        for dir in dirs:
            next_node = dir(cur_node[0], cur_node[1])
            if (0 <= next_node[0] < n) and (0 <= next_node[1] < n) and visit[next_node[0]][next_node[1]] == 0 and map1[next_node[0]][next_node[1]] == 0:
                queue.append((next_node[0], next_node[1]))
                visit[next_node[0]][next_node[1]] = 1
                map1[next_node[0]][next_node[1]] = 3
            else:
                continue


n = int(input())
visit = [[0 for _ in range(n)] for _ in range(n)]
dirs = [lambda x, y: (x + 1, y),
        lambda x, y: (x, y + 1),
        lambda x, y: (x - 1, y),
        lambda x, y: (x, y - 1)]

queue = deque()
map1 = []
tmp = n
while tmp > 0:
    map1.append(list(map(int, input().split())))
    tmp -= 1


for j in range(n):
    if map1[0][j] == 0:
        bfs(0, j)
    if map1[n - 1][j] == 0:
        bfs(n - 1, j)
for i in range(n):
    if map1[i][0] == 0:
        bfs(i, 0)
    if map1[i][n - 1] == 0:
        bfs(i, n - 1)

# for i in map1:
#     print(i)

for i in range(n):
    for j in range(n):
        if map1[i][j] == 3:
            print(0, end=' ')
        elif map1[i][j] == 1:
            print(1, end=' ')
        else:
            print(2, end=' ')
    print()
