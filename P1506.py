from collections import deque


def bfs(x, y):
    queue.append((x, y))
    visit[x][y] = 1
    map1[x][y] = '*'
    while queue:
        curNode = queue.popleft()
        for dir in dirs:
            nextNode = dir(curNode[0], curNode[1])
            if (0 <= nextNode[0] < n) and (0 <= nextNode[1] < m) and visit[nextNode[0]][nextNode[1]] == 0 and map1[nextNode[0]][nextNode[1]] == '0':
                queue.append((nextNode[0], nextNode[1]))
                visit[nextNode[0]][nextNode[1]] = 1
                map1[nextNode[0]][nextNode[1]] = '*'
            else:
                continue


n, m = map(int, input().strip().split())

dirs = [lambda x, y: (x + 1, y),
        lambda x, y: (x - 1, y),
        lambda x, y: (x, y - 1),
        lambda x, y: (x, y + 1)]

queue = deque()
visit = [[0 for _ in range(m)] for _ in range(n)]
map1 = []
tmp = n
while tmp > 0:
    map1.append(list(input().strip()))
    tmp -= 1

for j in range(m):
    if map1[0][j] == '0':
        bfs(0, j)
    if map1[n - 1][j] == '0':
        bfs(n - 1, j)
for i in range(n):
    if map1[i][0] == '0':
        bfs(i, 0)
    if map1[i][m - 1] == '0':
        bfs(i, m - 1)

ans = 0
for i in range(n):
    for j in range(m):
        if map1[i][j] != '*':
            ans += 1
print(ans)
