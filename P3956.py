from queue import PriorityQueue


def bfs():
    q = PriorityQueue()
    dx = [0, 1, 0, -1, 1, 1, -1, -1, 0, 2, 0, -2]
    dy = [1, 0, -1, 0, 1, -1, 1, -1, 2, 0, -2, 0]
    dw = [0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2]
    dis[1][1] = 0
    q.put((dis[1][1], color[1][1], 1, 1))
    while not q.empty():
        cur = q.get()
        cur_c = cur[1]
        if dis[cur[2]][cur[3]] < cur[0]:
            continue
        for i in range(12):
            next_w, next_x, next_y = cur[0] + dw[i], cur[2] + dx[i], cur[3] + dy[i]
            if 0 < next_x <= m and 0 < next_y <= m:
                next_c = color[next_x][next_y]
                if not next_c:
                    continue
                if next_c != cur_c:
                    next_w += 1
                if dis[next_x][next_y] > next_w:
                    dis[next_x][next_y] = next_w
                    q.put((next_w, next_c, next_x, next_y))


m, n = map(int, input().split())
color = [[0 for _ in range(m + 1)] for _ in range(m + 1)]
dis = [[float('inf') for _ in range(m + 1)] for _ in range(m + 1)]
for _ in range(n):
    x, y, c = map(int, input().split())
    color[x][y] = c + 1

bfs()
if not color[m][m]:
    ans = min(dis[m][m - 1], dis[m - 1][m]) + 2
    if ans >= float('inf'):
        print('-1')
    else:
        print(ans)
else:
    if dis[m][m] == float('inf'):
        print('-1')
    else:
        print(dis[m][m])
