def dfs(num, s):
    global ans
    if num >= 11:
        if s == n:
            ans += 1
            tmp = nums.copy()
            ans_list.append(tmp)
        return
    for i in range(1, 4):
        nums[num] = i
        dfs(num + 1, s + i)


n = int(input())
nums = [0] * 11
ans = 0
ans_list = []
dfs(1, 0)
if ans != 0:
    print(ans)
    for i in ans_list:
        print(*i[1:])
else:
    print('0')