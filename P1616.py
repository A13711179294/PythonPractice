def main():
    t, m = map(int, input().split())
    dp = [0 for _ in range(t + 1)]
    if m == 1:
        a, b = map(int, input().split())
        print(t // a * b)
    else:
        tmp = m
        while tmp > 0:
            a, b = map(int, input().split())
            for j in range(a, t + 1):
                dp[j] = max(dp[j], dp[j - a] + b)
            tmp -= 1
        print(dp[t])


if __name__ == '__main__':
    main()
