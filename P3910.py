from math import sqrt

n, m = map(int, input().split())
for i in range(int(sqrt(2 * m)), 0, -1):
    if 2 * m % i != 0 or ((2 * m // i) - i + 1) % 2 != 0:
        continue
    a = ((2 * m // i) - i + 1) // 2
    if a < 1 or a + i - 1 > n:
        continue
    print('[%d,%d]' % (a, a + i - 1))
