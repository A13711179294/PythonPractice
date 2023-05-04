def find(x):
    for i in range(1, s // 2 + 1):
        for j in range(2, s // i + 1):
            num[i * j] += i


s = int(input())
num = [0] * (s + 1)
dp = [0 for _ in range(s + 1)]
find(s)
for i in range(2, s + 1):
    for j in range(s, i - 1,-1):
        dp[j] = max(dp[j], dp[j - i] + num[i])
        #print(dp[1:])

print(dp[s])
