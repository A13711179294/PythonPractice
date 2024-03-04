def dfs(num):
    global flag
    if num == k + 1:
        if flag:
            print(*nums[1:])
            flag = 0
        return

    for i in range(1, n + 1):
        if visit[i] == 0 and a[i] - b[num] >= 0:
            visit[i] = 1
            nums[num] = i
            dfs(num + 1)
            visit[i] = 0


n, k = map(int, input().split())
ans = 0
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.insert(0, 0)
b.insert(0, 0)
visit = [0] * (n + 1)
nums = [0] * (k + 1)
flag = 1
dfs(1)
if flag:
    print('-1')
