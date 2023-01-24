T, M = map(int, input().split())
n = M
time = []
value = []
while n > 0:
    t, v = map(int, input().split())
    time.append(t)
    value.append(v)
    n -= 1

dp = [[0 for _ in range(T + 1)] for _ in range(M + 1)]

for i in range(1, M + 1):
    for j in range(1, T + 1):
        if j >= time[i - 1]:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - time[i - 1]] + value[i - 1])
        else:
            dp[i][j] = dp[i - 1][j]
print(dp[M][T])
