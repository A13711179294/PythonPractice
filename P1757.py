m, n = map(int, input().split())
dp = [0 for _ in range(m + 1)]
value = [0]
weight = [0]
count1 = [0 for _ in range(1001)]
g = [[0] * 1001 for _ in range(1001)]
i = 1
t = 1
while i <= n:
    a, b, c = map(int, input().split())
    t = max(t, c)
    weight.append(a)
    value.append(b)
    count1[c] += 1
    g[c][count1[c]] = i
    i += 1

for i in range(1, t + 1):
    for j in range(m, 0, -1):
        for k in range(1, count1[i] + 1):
            if j >= weight[g[i][k]]:
                dp[j] = max(dp[j], dp[j - weight[g[i][k]]] + value[g[i][k]])

print(dp[-1])
