def printf(l, r):
    if l > r:
        return
    print(root[l][r], end=' ')
    if l == r:
        return
    printf(l, root[l][r] - 1)
    printf(root[l][r] + 1, r)


n = int(input())
a = [0] + list(map(int, input().split()))

dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
root = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    dp[i][i] = a[i]
    root[i][i] = i

for l in range(1, n):
    for i in range(1, n - l + 1):
        j = i + l
        dp[i][j] = dp[i + 1][j] + dp[i][i]
        root[i][j] = i
        for k in range(i + 1, j):
            if dp[i][j] < dp[i][k - 1] * dp[k + 1][j] + dp[k][k]:
                dp[i][j] = dp[i][k - 1] * dp[k + 1][j] + dp[k][k]
                root[i][j] = k

print(dp[1][n])
printf(1, n)