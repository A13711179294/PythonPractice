n = int(input())
a = ['0'] + list(input().split())
dp = [0] * 12

for i in range(1, n + 1):
    dp[ord(a[i][-1]) - 48] = max(dp[ord(a[i][-1]) - 48], dp[ord(a[i][0]) - 48] + 1)

cnt = 0
for i in range(0, 10):
    cnt = max(cnt, dp[i])

print(n - cnt)
