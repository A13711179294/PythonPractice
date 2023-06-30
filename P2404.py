def dfs(now, sum1, last):
    if sum1 > n or now > n + 1:
        return
    elif sum1 == n:
        tmp = '+'.join(nums[1:now])
        print(tmp.rstrip('+'))
        return
    for i in range(last, n):
        nums[now] = str(i)
        dfs(now + 1, sum1 + i, i)


n = int(input())
nums = [0] * (n + 1)
dfs(1, 0, 1)
