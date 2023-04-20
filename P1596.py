import sys
sys.setrecursionlimit(100000)


def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return
    if field[x][y] == 'W' and visit[x][y] == 0:
        visit[x][y] = 1
        for i in range(8):
            dfs(x + x_dir[i], y + y_dir[i])


n, m = map(int, input().strip().split())
x_dir = [0, 1, 1, 1, 0, -1, -1, -1]
y_dir = [1, 1, 0, -1, -1, -1, 0, 1]
field = []
visit = [[0 for _ in range(m)] for _ in range(n)]
tmp = n
while tmp > 0:
    field.append(list(input().strip()))
    tmp -= 1

# for i in visit:
#     print(i)
ans = 0
for i in range(n):
    for j in range(m):
        if field[i][j] == 'W' and visit[i][j] == 0:
            dfs(i, j)
            ans += 1

print(ans)
