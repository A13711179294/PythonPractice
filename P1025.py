def dfs(n1, k1, last):
    if k1 == 1:
        return 1
    ret = 0
    for i in range(last, n1 // k1 + 1):
        ret += dfs(n1 - i, k1 - 1, i)
    return ret


n, k = map(int, input().split())

print(dfs(n, k, 1))
