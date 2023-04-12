from collections import deque


def bfs():
    queue.append((x1 - 1, y1 - 1, 1))
    ans[x1 - 1][y1 - 1] = 0
    vis[x1 - 1][y1 - 1] = True
    while queue:
        cur = queue.popleft()
        for i in range(8):
            next_x = cur[0] + x_dir[i]
            next_y = cur[1] + y_dir[i]
            if 0 <= next_x < n and 0 <= next_y < m and not vis[next_x][next_y]:
                vis[next_x][next_y] = True
                queue.append((next_x, next_y, cur[2] + 1))
                ans[next_x][next_y] = cur[2]


n, m, x1, y1 = map(int, input().split())
queue = deque()
x_dir = [-1, -2, -2, -1, 1, 2, 2, 1]
y_dir = [2, 1, -1, -2, 2, 1, -1, -2]
graph = [[0 for _ in range(m)] for _ in range(n)]
ans = [[-1 for _ in range(m)] for _ in range(n)]
vis = [[False for _ in range(m)] for _ in range(n)]
bfs()

for i in range(n):
    for j in range(m):
        print('%-5d' % ans[i][j], end='')
    print()
