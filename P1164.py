N, M = map(int, input().split())
#a = list(map(int, input().split()))
a = []
while len(a) < N:
    a.extend(list(map(int, input().split())))

dp = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, M + 1):
        if j == a[i - 1]:
            dp[i][j] = dp[i - 1][j] + 1
        elif j > a[i - 1]:
            dp[i][j] = dp[i - 1][j - a[i - 1]] + dp[i - 1][j]
        elif j < a[i - 1]:
            dp[i][j] = dp[i - 1][j]
# for i in dp:
#     print(i)
print(dp[N][M])
