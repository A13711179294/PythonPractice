n = int(input())
sum1 = [0]
sum2 = 0
tmp = 1
while tmp <= n:
    num = int(input())
    sum2 += num
    sum1.append(sum2)
    tmp += 1

if sum1[n] < 0:
    print('Impossible')
else:
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(0, i):
            if sum1[i] >= 0 and sum1[i] - sum1[j] >= 0:
                dp[i] = max(dp[j] + 1, dp[i])
    print(dp[n])
