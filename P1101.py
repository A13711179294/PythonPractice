n = int(input())
matrix = [[0 for _ in range(n)] for i in range(n)]
book = [[0 for _ in range(n)] for _ in range(n)]

tmp = 0
while tmp < n:
    row = list(input())
    matrix[tmp] = row
    tmp += 1

tmp = 'yizhong'


def dfs(i, j, index, direction):
    if 0 <= i < n and 0 <= j < n:
        if matrix[i][j] == tmp[index]:
            if index == 6:
                book[i][j] = 1
                return 1
            else:
                if direction == 0:
                    if dfs(i, j - 1, index + 1, 1):
                        book[i][j] = 1
                    if dfs(i - 1, j - 1, index + 1, 2):
                        book[i][j] = 1
                    if dfs(i - 1, j, index + 1, 3):
                        book[i][j] = 1
                    if dfs(i - 1, j + 1, index + 1, 4):
                        book[i][j] = 1
                    if dfs(i, j + 1, index + 1, 5):
                        book[i][j] = 1
                    if dfs(i + 1, j + 1, index + 1, 6):
                        book[i][j] = 1
                    if dfs(i + 1, j, index + 1, 7):
                        book[i][j] = 1
                    if dfs(i + 1, j - 1, index + 1, 8):
                        book[i][j] = 1
                elif direction == 1:
                    if dfs(i, j - 1, index + 1, 1):
                        book[i][j] = 1
                        return 1
                    else:
                        return 0
                elif direction == 2:
                    if dfs(i - 1, j - 1, index + 1, 2):
                        book[i][j] = 1
                        return 1
                    else:
                        return 0
                elif direction == 3:
                    if dfs(i - 1, j, index + 1, 3):
                        book[i][j] = 1
                        return 1
                    else:
                        return 0
                elif direction == 4:
                    if dfs(i - 1, j + 1, index + 1, 4):
                        book[i][j] = 1
                        return 1
                    else:
                        return 0
                elif direction == 5:
                    if dfs(i, j + 1, index + 1, 5):
                        book[i][j] = 1
                        return 1
                    else:
                        return 0
                elif direction == 6:
                    if dfs(i + 1, j + 1, index + 1, 6):
                        book[i][j] = 1
                        return 1
                    else:
                        return 0
                elif direction == 7:
                    if dfs(i + 1, j, index + 1, 7):
                        book[i][j] = 1
                        return 1
                    else:
                        return 0
                elif direction == 8:
                    if dfs(i + 1, j - 1, index + 1, 8):
                        book[i][j] = 1
                        return 1
                    else:
                        return 0
        else:
            return 0
    else:
        return 0


for i in range(n):
    for j in range(n):
        if matrix[i][j] == 'y':
            dfs(i, j, 0, 0)

for i in range(n):
    for j in range(n):
        if book[i][j] != 1:
            matrix[i][j] = '*'

for i in range(n):
    print(''.join(matrix[i]))
