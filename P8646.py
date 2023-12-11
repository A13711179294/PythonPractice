from math import gcd

n = int(input())
w = [0]
g = 0
tmp = n
while tmp > 0:
    num = int(input())
    g = gcd(num, g)
    w.append(num)
    tmp -= 1

if g != 1:
    print('INF')
else:
    dp = [0 for _ in range(10001)]
    dp[0] = 1
    for i in range(1, n + 1):
        for j in range(w[i], 10001):
            dp[j] = max(dp[j], dp[j - w[i]])

    print(dp.count(0))
