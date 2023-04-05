from collections import deque


def bfs(start_x, start_y):
    queue.append((start_x, start_y))
    visit[start_x][start_y] = 1
    while queue:
        curNode = queue.popleft()
        for dir in dirs:
            nextNode = dir(curNode[0], curNode[1])
            if (0 <= nextNode[0] < n) and (0 <= nextNode[1] < m) and visit[nextNode[0]][nextNode[1]] == 0 and map1[nextNode[0]][nextNode[1]] != 0:
                queue.append((nextNode[0], nextNode[1]))
                visit[nextNode[0]][nextNode[1]] = 1
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
    map1.append(list(map(int, input().strip())))
    tmp -= 1

ans = 0
for i in range(n):
    for j in range(m):
        if visit[i][j] == 0 and map1[i][j] != 0:
            bfs(i, j)
            ans += 1

# for i in map1:
#     print(i)

print(ans)
