def dfs(li, n):
    t = sum(li)
    dp = [0 for _ in range(t)]
    for i in range(1, n + 1):
        for j in range(t // 2, li[i] - 1, - 1):
            dp[j] = max(dp[j], dp[j - li[i]] + li[i])
    return t - dp[t // 2]


nums = list(map(int, input().split()))
s = []
for i in range(4):
    s.append([0] + list(map(int, input().split())))

ans = 0
for i in range(4):
    ans += dfs(s[i], nums[i])

print(ans)
