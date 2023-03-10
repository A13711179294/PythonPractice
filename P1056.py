M, N, K, L, D = map(int, input().strip().split())
a = [[i, 0] for i in range(N + 1)]
b = [[i, 0] for i in range(N + 1)]
for _ in range(D):
    xi, yi, pi, qi = map(int, input().strip().split())
    if xi == pi:
        if yi < qi:
            b[yi][1] += 1
        else:
            b[qi][1] += 1
    elif yi == qi:
        if xi < pi:
            a[xi][1] += 1
        else:
            a[pi][1] += 1

a.sort(key=lambda x: x[1], reverse=True)
b.sort(key=lambda x: x[1], reverse=True)

count1 = 0
count2 = 0
c = []
d = []
for i in range(0, M + 1):
    if a[i][1] != 0 and count1 < K:
        c.append(a[i][0])
        count1 += 1
for j in range(0, N + 1):
    if b[j][1] != 0 and count2 < L:
        d.append(b[j][0])
        count2 += 1

c.sort()
d.sort()
print(*c)
print(*d)