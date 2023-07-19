n, m = map(int, input().split())
a = [0]
for _ in range(m):
    a.append(int(input()))

dis = [[0] * (n + 1)]
for _ in range(n):
    dis.append([0] + list(map(int, input().split())))

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dis[i][j] = min(dis[i][k] + dis[k][j], dis[i][j])

ans = 0
for i in range(2, m + 1):
    ans += dis[a[i - 1]][a[i]]

print(ans)