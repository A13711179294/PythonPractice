n, m = map(int, input().split())
tmp = m
thing = [0]
while tmp > 0:
    thing.append(tuple(map(int, input().split())))
    tmp -= 1
dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

for i in range(1, m + 1):
    for j in range(1, n + 1):
        if j >= thing[i][0]:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - thing[i][0]] + thing[i][0] * thing[i][1])
        else:
            dp[i][j] = dp[i - 1][j]

# for i in dp:
#     print(i)
print(dp[m][n])