def main():
    h, t = map(int, input().split())
    n = int(input())
    dp = [[0 for _ in range(t + 1)] for _ in range(h + 1)]
    v = [0]
    m = [0]
    k = [0]

    tmp = n
    while tmp > 0:
        a, b, c = map(int, input().split())
        v.append(a)
        m.append(b)
        k.append(c)
        tmp -= 1

    for i in range(1, n + 1):
        for j in range(h, v[i] - 1, -1):
            for l in range(t, m[i] - 1, -1):
                dp[j][l] = max(dp[j][l], dp[j - v[i]][l - m[i]] + k[i])

    print(dp[h][t])


if __name__ == '__main__':
    main()