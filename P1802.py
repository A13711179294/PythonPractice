n, x = map(int, input().split())
dp = [0 for _ in range(x + 1)]
lose = [0]
win = [0]
val = [0]

for _ in range(n):
    a, b, c = map(int, input().split())
    lose.append(a)
    win.append(b)
    val.append(c)

for i in range(1, n + 1):
    for j in range(x, val[i] - 1, -1):
        dp[j] = max(dp[j] + lose[i], dp[j - val[i]] + win[i])
    for j in range(val[i] - 1, -1, -1):
        dp[j] += lose[i]

print(5 * dp[x])