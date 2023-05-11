def w(x, y, z):
    if x <= 0 or y <= 0 or z <= 0:
        return 1
    elif x > 20 or y > 20 or z > 20:
        return w(20, 20, 20)
    elif cnt[x][y][z] == 0:
        if x < y < z:
            cnt[x][y][z] = w(x, y, z - 1) + w(x, y - 1, z - 1) - w(x, y - 1, z)
        else:
            cnt[x][y][z] = w(x - 1, y, z) + w(x - 1, y - 1, z) + w(x - 1, y, z - 1) - w(x - 1, y - 1, z - 1)
    return cnt[x][y][z]


cnt = [[[0 for _ in range(30)] for _ in range(30)] for _ in range(30)]
while True:
    a, b, c = map(int, input().split())
    if a == b == c == -1:
        break
    else:
        print('w(%d, %d, %d) = %d' % (a, b, c, w(a, b, c)))
