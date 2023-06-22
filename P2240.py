n, t = map(int, input().split())
li = []
for _ in range(n):
    m, v = map(int, input().split())
    li.append((v / m, m, v))

li.sort(key=lambda x: x[0], reverse=True)

ans = 0
for i in range(n):
    if li[i][1] <= t:
        t -= li[i][1]
        ans += li[i][2]
    else:
        ans += t * li[i][0]
        break

print('%.2f' % ans)