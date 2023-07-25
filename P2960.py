from collections import deque


def bfs():
    global ans
    dir_x = [0, 1, 1, 1, 0, -1, -1, -1]
    dir_y = [1, 1, 0, -1, -1, -1, 0, 1]
    q = deque()
    vis = [[False for _ in range(x + 1)] for _ in range(y + 1)]
    vis[my][mx] = True
    q.append((my, mx, 0))
    while q:
        cur = q.popleft()
        for i in range(8):
            next_x = cur[0] + dir_x[i]
            next_y = cur[1] + dir_y[i]
            if 0 < next_x <= y and 0 < next_y <= x and not vis[next_x][next_y] and graph[next_x][next_y] == '.':
                vis[next_x][next_y] = True
                ans = max(ans, cur[2] + 1)
                q.append((next_x, next_y, cur[2] + 1))


x, y, mx, my = map(int, input().strip().split())
graph = [['.' for _ in range(x + 1)] for _ in range(y + 1)]
for i in range(y, 0, -1):
    tmp = ['.'] + list(input())
    for j in range(1, x + 1):
        graph[i][j] = tmp[j]

ans = 0
bfs()
print(ans)
