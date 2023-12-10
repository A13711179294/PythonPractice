s1 = list(input().strip())
s2 = list(reversed(s1))
l = len(s1)
s1.insert(0, 0)
s2.insert(0, 0)

dp = [[0] * (l + 1) for _ in range(l + 1)]
for i in range(1, l + 1):
    for j in range(1, l + 1):
        if s1[i] == s2[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

print(l - dp[l][l])
