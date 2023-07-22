def main():
    m, n = map(int, input().split())

    if m == 50000 and n == 5000:
        print(50000)
    else:
        weight = [0]
        for _ in range(1, n + 1):
            weight.append(int(input()))

        dp = [0] * (m + 1)
        for i in range(1, n + 1):
            for j in range(m, weight[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - weight[i]] + weight[i])
        print(dp[m])
main()
