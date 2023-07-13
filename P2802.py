from collections import deque


def bfs(x, y, h, s):
    global ans
    visit[x][y] = h
    queue.append((x, y, h, s))
    flag = 0
    while queue:
        cur_node = queue.popleft()
        if flag == 1:
            break
        for dir in dirs:
            next_node = dir(cur_node[0], cur_node[1], cur_node[2] - 1, cur_node[3] + 1)
            if 0 <= next_node[0] < n and 0 <= next_node[1] < m and visit[next_node[0]][next_node[1]] < next_node[2]:
                if graph[next_node[0]][next_node[1]] == 0:
                    pass
                elif graph[next_node[0]][next_node[1]] == 1:
                    visit[next_node[0]][next_node[1]] = next_node[2]
                    queue.append((next_node[0], next_node[1], next_node[2], next_node[3]))
                elif graph[next_node[0]][next_node[1]] == 4:
                    visit[next_node[0]][next_node[1]] = 6
                    queue.append((next_node[0], next_node[1], 6, next_node[3]))
                elif graph[next_node[0]][next_node[1]] == 3:
                    ans = next_node[3]
                    flag = 1
                    break


n, m = map(int, input().split())
queue = deque()
dirs = [lambda x, y, z, k: (x, y + 1, z, k),
        lambda x, y, z, k: (x + 1, y, z, k),
        lambda x, y, z, k: (x, y - 1, z, k),
        lambda x, y, z, k: (x - 1, y, z, k)]
visit = [[0 for _ in range(m)] for _ in range(n)]
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

start_x = 0
start_y = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            start_x = i
            start_y = j
            break

ans = 99999999
bfs(start_x, start_y, 6, 0)

if ans != 99999999:
    print(ans)
else:
    print('-1')
