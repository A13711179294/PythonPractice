from collections import deque, defaultdict
from sys import stdin


def main():
    def bfs(s):
        q = deque()
        dirs_x = [0, 1, 0, -1]
        dirs_y = [1, 0, -1, 0]
        vis = [[False for _ in range(m + 1)] for _ in range(n + 1)]
        vis[s[0]][s[1]] = True
        q.append((s[0], s[1], 0))
        while q:
            cur = q.popleft()
            for i in range(4):
                next_x = cur[0] + dirs_x[i]
                next_y = cur[1] + dirs_y[i]
                if 0 < next_x <= n and 0 < next_y <= m:
                    if graph[next_x][next_y] == '=':
                        return cur[2] + 1
                    elif not vis[next_x][next_y] and graph[next_x][next_y].isalpha():
                        for x in door[graph[next_x][next_y]]:
                            if x != (next_x, next_y):
                                q.append((x[0], x[1], cur[2] + 1))
                    elif not vis[next_x][next_y] and graph[next_x][next_y] == '.':
                        vis[next_x][next_y] = True
                        q.append((next_x, next_y, cur[2] + 1))

    n, m = map(int, stdin.readline().strip().split())
    graph = [['#' for _ in range(m + 1)]]
    door = defaultdict(list)
    start = (1, 1)
    for i in range(1, n + 1):
        tmp = ['#'] + list(stdin.readline().strip())
        graph.append(tmp)
        for j in range(1, m + 1):
            if tmp[j] == '@':
                start = (i, j)
            elif tmp[j].isalpha():
                door[tmp[j]].append((i, j))

    print(bfs(start))


main()
