n, m = map(int, input().split())
bomb_map = [['?' for j in range(m + 2)] for i in range(n + 2)]
tmp = n
row = 1
while tmp > 0:
    bomb_map[row] = list('?' + input() + '?')
    row += 1
    tmp -= 1

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if bomb_map[i][j] != '*':
            count1 = 0
            if bomb_map[i][j - 1] == '*':
                count1 += 1
            if bomb_map[i - 1][j - 1] == '*':
                count1 += 1
            if bomb_map[i - 1][j] == '*':
                count1 += 1
            if bomb_map[i - 1][j + 1] == '*':
                count1 += 1
            if bomb_map[i][j + 1] == '*':
                count1 += 1
            if bomb_map[i + 1][j + 1] == '*':
                count1 += 1
            if bomb_map[i + 1][j] == '*':
                count1 += 1
            if bomb_map[i + 1][j - 1] == '*':
                count1 += 1
            bomb_map[i][j] = count1

for i in bomb_map[1:n + 1]:
    for j in i[1:m + 1]:
        print(j, end='')
    print()
