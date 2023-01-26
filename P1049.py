V = int(input())
n = int(input())
tmp = n
v = [0]
while tmp > 0:
    v.append(int(input()))
    tmp -= 1

dp = [[0 for _ in range(V + 1)] for _ in range(n + 1)]
for i in range(1, n+1):
    for j in range(1, V + 1):
        if j >= v[i]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-v[i]] + v[i])
        else:
            dp[i][j] = dp[i-1][j]

print(V - dp[n][V])