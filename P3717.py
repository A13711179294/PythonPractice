from math import sqrt

n, m, r = map(int, input().split())
a = [[0 for _ in range(n)] for _ in range(n)]

tmp = m
while tmp > 0:
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    for i in range(n):
        for j in range(n):
            r1 = sqrt((x - i) * (x - i) + (y - j) * (y - j))
            if r1 <= r:
                a[i][j] = 1
    tmp -= 1

ans = 0
for i in range(n):
    for j in range(n):
        if a[i][j] == 1:
            ans += 1
print(ans)