from collections import deque


def bfs(x, y):
    queue.append((x, y))
    visit[x][y] = 1
    while queue:
        curNode = queue.popleft()
        for dir in dirs:
            nextNode = dir(curNode[0], curNode[1])
            if (0 <= nextNode[0] < n) and (0 <= nextNode[1] < m) and visit[nextNode[0]][nextNode[1]] == 0 and \
                    map1[nextNode[0]][nextNode[1]] == '#':
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
    map1.append(list(input().strip()))
    tmp -= 1

flag = 0
for i in range(n - 1):
    for j in range(m - 1):
        if map1[i][j] == '.' and map1[i][j+1] == '#' and map1[i+1][j] == '#' and map1[i+1][j+1] == '#':
            flag = 1
            break
        elif map1[i][j] == '#' and map1[i][j+1] == '.' and map1[i+1][j] == '#' and map1[i+1][j+1] == '#':
            flag = 1
            break
        elif map1[i][j] == '#' and map1[i][j+1] == '#' and map1[i+1][j] == '.' and map1[i+1][j+1] == '#':
            flag = 1
            break
        elif map1[i][j] == '#' and map1[i][j+1] == '#' and map1[i+1][j] == '#' and map1[i+1][j+1] == '.':
            flag = 1
            break


if flag == 1:
    print('Bad placement.')
else:
    ans = 0
    for i in range(n):
        for j in range(m):
            if visit[i][j] == 0 and map1[i][j] == '#':
                bfs(i, j)
                ans += 1
    print('There are %s ships.' % ans)


