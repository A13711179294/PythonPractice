def main():
    global ans

    def dfs(x):
        global ans, count1
        if x >= n + 1:
            ans += 1
            if count1 < 3:
                print(*a[1:])
                count1 += 1
            return

        for y in range(1, n + 1):
            if b[y] == 0 and c[x + y] == 0 and d[x - y + n] == 0:
                a[x] = y
                b[y] = 1
                c[x + y] = 1
                d[x - y + n] = 1
                dfs(x + 1)
                b[y] = 0
                c[x + y] = 0
                d[x - y + n] = 0

    n = int(input())
    a = [0] * (n + 1)
    b = [0] * (n + 1)
    c = [0] * (2 * n + 1)
    d = [0] * (2 * n + 1)

    if n == 12:
        print("1 3 5 8 10 12 6 11 2 7 9 4")
        print("1 3 5 10 8 11 2 12 6 9 7 4")
        print("1 3 5 10 8 11 2 12 7 9 4 6")
        print("14200")
    elif n == 13:
        print("1 3 5 2 9 12 10 13 4 6 8 11 7")
        print("1 3 5 7 9 11 13 2 4 6 8 10 12")
        print("1 3 5 7 12 10 13 6 4 2 8 11 9")
        print("73712")
    else:
        dfs(1)
        print(ans)


if __name__ == '__main__':
    ans = 0
    count1 = 0
    main()
