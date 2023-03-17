n = int(input())
t = list(map(int, input().split()))
t.insert(0, 0)
t.append(0)
dp = [[0] * (n + 2) for _ in range(2)]

for i in range(1, n + 1):
    for j in range(0, i):
        if t[i] > t[j]:
            dp[0][i] = max(dp[0][i], dp[0][j] + 1)

for i in range(n, 0, -1):
    for j in range(n + 1, i, -1):
        if t[i] > t[j]:
            dp[1][i] = max(dp[1][i], dp[1][j] + 1)

# for i in dp:
#     print(i)

ans = 0
for i in range(1, n + 1):
    ans = max(dp[0][i] + dp[1][i] - 1, ans)

print(n - ans)
