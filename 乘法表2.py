for x in range(1, 10):
    for y in range(1, x + 1):
        print('%dx%d=%d' % (y, x, x * y), end=' ')
    print('\r')

row = 1
while row < 10:
    col = 1
    while col <= row:
        print('{}x{}={}'.format(col, row, col * row), end=' ')
        col += 1
    print()
    row += 1
