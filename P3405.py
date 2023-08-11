n = int(input())
dic = {}
li = [[0 for _ in range(676)] for _ in range(676)]
ans = 0
for _ in range(n):
    a, b = input().split()
    x = (ord(a[0]) - 65) * 26 + ord(a[1]) - 65
    y = (ord(b[0]) - 65) * 26 + ord(b[1]) - 65
    if x != y:
        li[x][y] += 1
        ans += li[y][x]

print(ans)