from sys import setrecursionlimit

setrecursionlimit(10000000)


def check(s, m, k):
    lens = len(s)
    for i in range(k):
        if s[lens - k + i] != m[i]:
            return False
    return True


def add(s, m, k):
    for i in range(k, len(m)):
        s += m[i]
    return s


def dfs(now):
    global ans
    ans = max(ans, len(now))
    for i in range(1, n + 1):
        if used[i] >= 2:
            continue
        for j in range(1, min(len(li[i]), len(now)) + 1):
            if check(now, li[i], j):
                tmp = add(now, li[i], j)
                if tmp == now:
                    continue
                used[i] += 1
                dfs(tmp)
                used[i] -= 1


n = int(input().strip())
used = [0] * (n + 1)
li = ['']
for _ in range(n):
    li.append(input().strip())

ans = 0
dfs(input().strip())
print(ans)
