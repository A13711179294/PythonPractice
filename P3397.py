n, m = map(int, input().split())
flag = [[0 for _ in range(n+1)] for _ in range(n)]
real = [[0 for _ in range(n+1)] for _ in range(n)]
tmp = m
while tmp > 0:
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1 - 1, x2):
        flag[i][y1 - 1] += 1
        flag[i][y2] -= 1
    tmp -= 1

# for i in flag:
#     print(*i)

for i in range(n):
    sum = 0
    for j in range(n):
        sum += flag[i][j]
        real[i][j] = sum

for i in real:
    for j in i[0:-1]:
        print(j, end=' ')
    print()
