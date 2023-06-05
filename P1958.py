a, b = map(int, input().split())
dp = [[0 for _ in range(b + 2)] for _ in range(a + 2)]
visit = [[0 for _ in range(b + 2)] for _ in range(a + 2)]

n = int(input())
for _ in range(n):
    t1, t2 = map(int, input().split())
    visit[t1][t2] = 1

dp[1][0] = 1
for i in range(1, a + 1):
    for j in range(1, b + 1):
        if visit[i][j] != 1:
            dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

# for i in dp:
#     print(i)
print(dp[a][b])