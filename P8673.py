from collections import deque


def bfs():
    q = deque()
    dir_x = [0, 1, 0, -1]
    dir_y = [1, 0, -1, 0]
    vis = [[-1 for _ in range(n)] for _ in range(n)]
    vis[0][0] = 0
    q.append((0, 0, 0, 0))
    while q:
        cur = q.popleft()
        for i in range(4):
            next_x = cur[0] + dir_x[i]
            next_y = cur[1] + dir_y[i]
            if 0 <= next_x < n and 0 <= next_y < n:
                if next_x == n - 1 and next_y == n - 1:
                    return cur[3] + 1
                elif graph[next_x][next_y] == 'X' and cur[2] == 0:
                    continue

                magic = max(0, cur[2] - 1)
                if graph[next_x][next_y] == '%':
                    magic = k
                if graph[next_x][next_y] != '#' and vis[next_x][next_y] < magic:
                    vis[next_x][next_y] = magic
                    q.append((next_x, next_y, magic, cur[3] + 1))

    return -1


n, k = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(input()))

# for i in graph:
#     print(i)

print(bfs())
