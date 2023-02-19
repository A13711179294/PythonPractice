def dfs(num, count):
    if count == r:
        for j in used:
            print('%3d' % j, end='')
        print()
        return
    for i in range(num + 1, n + 1):
        used[count] = i
        dfs(i, count + 1)


n, r = map(int, input().strip().split())
a = [j for j in range(0, n + 1)]
used = [0 for _ in range(r)]
dfs(0, 0)
