from math import sqrt


class node:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.flag = False


def dis(x1, y1, x2, y2):
    return sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))


def dfs(x, y, r):
    global ans

    left = Lmid = 1
    right = n
    while left <= right:
        Lmid = left + right >> 1
        if li[Lmid].x < x - r:
            left = Lmid + 1
        else:
            right = Lmid - 1

    left = 1
    right = Rmid = n
    while left <= right:
        Rmid = left + right >> 1
        if li[Rmid].x <= x + r:
            left = Rmid + 1
        else:
            right = Rmid - 1

    for i in range(Lmid, Rmid + 1):
        if not li[i].flag and dis(x, y, li[i].x, li[i].y) <= r:
            li[i].flag = True
            ans += 1
            dfs(li[i].x, li[i].y, li[i].r)


n, m = map(int, input().split())
li = [node(0, 0, 0)]
for _ in range(n):
    a, b, c = map(int, input().split())
    li.append(node(a, b, c))

li.sort(key=lambda x: x.x)

ans = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    dfs(a, b, c)

print(ans)
