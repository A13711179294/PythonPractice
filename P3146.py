def main():
    n = int(input())
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    ans = 0
    for i in range(1, n + 1):
        dp[i][i] = int(input())
        ans = max(ans, dp[i][i])

    for k in range(2, n + 1):
        for l in range(1, n - k + 1 + 1):
            r = l + k - 1
            for j in range(1, r):
                if dp[l][j] == dp[j + 1][r] and dp[l][j]:
                    dp[l][r] = max(dp[l][r], dp[l][j] + 1)
                    ans = max(ans, dp[l][r])

    print(ans)


main()
