n, m, x, y = map(int, input().strip().split())

ground = [[] for _ in range(m)]
for i in range(m):
    for j in range(n):
        ground[i].append(0)

count_x = []
count_y = []
temp = x

while temp > 0:
    x1, y1, x2, y2 = map(int, input().strip().split())
    count_x.append(x1)
    count_x.append(x2)
    count_y.append(y1)
    count_y.append(y2)

    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            ground[i - 1][j - 1] += 1
    temp -= 1

temp = y
boom_x = []
boom_y = []
sequence = []

while temp > 0:
    tmp_x, tmp_y = map(int, input().strip().split())
    boom_x.append(tmp_x)
    boom_y.append(tmp_y)
    temp -= 1

for j1, j2 in zip(boom_x, boom_y):
    for i in range(2 * x - 2, -1, -2):
        if count_x[i] <= j1 <= count_x[i+1] and count_y[i] <= j2 <= count_y[i+1]:
            sequence.append(int(i//2+1))
            break

for i in range(y):
    if ground[boom_x[i] - 1][boom_y[i] - 1] == 0:
        print('N')
    else:
        print('Y', ground[boom_x[i] - 1][boom_y[i] - 1], sequence[i])
