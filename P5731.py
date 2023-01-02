n = int(input())
alist = [[] for _ in range(n)]
for i in alist:
    for _ in range(n):
        i.append(0)

row = 0
col = 0
digit = 1

while digit <= n * n:
    while col < n and alist[row][col] == 0:
        alist[row][col] = str('{:>2d}'.format(digit))
        col += 1
        digit += 1
    col -= 1
    row += 1

    while row < n and alist[row][col] == 0:
        alist[row][col] = str('{:>2d}'.format(digit))
        row += 1
        digit += 1
    row -= 1
    col -= 1

    while col >= 0 and alist[row][col] == 0:
        alist[row][col] = str('{:>2d}'.format(digit))
        col -= 1
        digit += 1
    col += 1
    row -= 1

    while row >= 0 and alist[row][col] == 0:
        alist[row][col] = str('{:>2d}'.format(digit))
        row -= 1
        digit += 1
    row += 1
    col += 1

for i in alist:
    print(' ', end='')
    for j in i:
        print(j, end=' ')
    print()
