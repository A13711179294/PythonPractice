from collections import deque


def bfs():
    q = deque()
    vis = [[False for _ in range(310)] for _ in range(310)]
    q.append((0, 0, 0))
    vis[0][0] = True
    while q:
        cur = q.popleft()
        for i in range(1, 5):
            next_x = cur[0] + dx[i]
            next_y = cur[1] + dy[i]
            if 0 <= next_x <= 301 and 0 <= next_y <= 301 and not vis[next_x][next_y]:
                if graph[next_x][next_y] == -1:
                    return cur[2] + 1
                elif graph[next_x][next_y] > cur[2] + 1:
                    vis[next_x][next_y] = True
                    q.append((next_x, next_y, cur[2] + 1))
    return -1


m = int(input())
dx = [0, 0, 0, 1, -1]
dy = [0, 1, -1, 0, 0]
graph = [[-1 for _ in range(310)] for _ in range(310)]
for _ in range(m):
    a, b, c = map(int, input().split())
    for j in range(5):
        if 0 <= a + dx[j] <= 300 and 0 <= b + dy[j] <= 300:
            if graph[a + dx[j]][b + dy[j]] == -1 or graph[a + dx[j]][b + dy[j]] > c:
                graph[a + dx[j]][b + dy[j]] = c

print(bfs())
