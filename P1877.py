n, beginLevel, maxLevel = map(int, input().split())
c = list(map(int, input().split()))
c.insert(0, 0)
dp = [[0 for _ in range(maxLevel + 1)] for _ in range(n + 1)]

dp[0][beginLevel] = 1
for i in range(1, n + 1):
    for j in range(0, maxLevel + 1):
        if dp[i - 1][j] and j + c[i] <= maxLevel:
            dp[i][j + c[i]] = 1
        if dp[i - 1][j] and j - c[i] >= 0:
            dp[i][j - c[i]] = 1

# for i in dp:
#     print(i)
flag = 0
for i in range(maxLevel, -1, -1):
    if dp[n][i]:
        flag = 1
        print(i)
        break

if flag == 0:
    print('-1')