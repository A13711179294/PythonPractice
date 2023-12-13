x, y = map(int, input().split())
n = max(abs(x), abs(y))

if x < 0 and x == y:
    print(4 * n * (n + 1))
else:
    ans = 4 * n * (n - 1)
    if x == -n:
        tmp = y + n
    elif y == n:
        tmp = x + 3 * n
    elif x == n:
        tmp = 5 * n - y
    else:
        tmp = 7 * n - x

    print(ans + tmp)
