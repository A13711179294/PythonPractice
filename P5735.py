from math import sqrt

li = []
for _ in range(3):
    li.append(tuple(map(eval, input().split())))

ans = 0
for i in range(3):
    for j in range(i + 1, 3):
        ans += sqrt(pow(li[i][0] - li[j][0], 2) + pow(li[i][1] - li[j][1], 2))

print('%.2f' % ans)