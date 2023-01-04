n = int(input())
a = [[] for i in range(n + 1)]
for i in range(n + 1):
    for _ in range(n + 1):
        a[i].append(0)

a[0][0] = 1
for i in range(1, n + 1):
    for j in range(1, n + 1):
        a[i][j] = a[i-1][j-1] + a[i-1][j]

for i in a[1:]:
    for j in i:
        if j != 0:
            print(j, end=' ')
    print()