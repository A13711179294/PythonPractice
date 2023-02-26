n, m = map(int, input().strip().split())
city = [[0 for _ in range(m + 2)] for _ in range(n + 2)]
tmp = 1
while tmp <= n:
    j = 1
    for i in tuple(input().strip()):
        city[tmp][j] = int(i)
        j += 1
    tmp += 1

# for i in city:
#     print(i)

sum1 = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if city[i][j] != 0:
            sum1 += 2
            if city[i][j] > city[i][j - 1]:
                sum1 += city[i][j] - city[i][j - 1]
            if city[i][j] > city[i - 1][j]:
                sum1 += city[i][j] - city[i - 1][j]
            if city[i][j] > city[i][j + 1]:
                sum1 += city[i][j] - city[i][j + 1]
            if city[i][j] > city[i + 1][j]:
                sum1 += city[i][j] - city[i + 1][j]
        else:
            continue

print(sum1)