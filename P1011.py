a, n, m, x = map(int, input().split())

up = [1, 1, 2]
down = [0, 0, 0]

for i in range(3, n):
    up.append(up[i - 1] + up[i - 2] - 1)
for i in range(3, n):
    down.append(down[i - 1] + down[i - 2] + 1)

z = -((up[n - 2] * a - m) / down[n - 2])

print(int(up[x - 1] * a + down[x - 1] * z))
