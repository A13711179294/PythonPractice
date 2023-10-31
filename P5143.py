from math import sqrt

n = int(input())
li = []
for _ in range(n):
    x, y, z = map(int, input().split())
    li.append((x, y, z))

li.sort(key=lambda x: x[2])

ans = 0
for i in range(n - 1):
    ans += sqrt(pow(li[i][0] - li[i + 1][0], 2) + pow(li[i][1] - li[i + 1][1], 2) + pow(li[i][2] - li[i + 1][2], 2))

print('%.3f' % ans)
