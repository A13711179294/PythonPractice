def dfs(last):
    if compare():
        tmp = []
        sum2 = 0
        for j in a:
            tmp.append(j)
            sum2 += j
        if tmp:
            value.append(tmp)
    for i in range(last + 1, g + 1):
        if visit[i] != 1:
            visit[i] = 1
            a.append(i)
            dfs(i)
            a.pop()
            visit[i] = 0


def compare():
    for i in range(v):
        sum1 = 0
        for j in a:
            sum1 += nums[j][i]
        if sum1 < vi[i]:
            return False
    return True


v = int(input())
vi = list(map(int, input().split()))
g = int(input())

value = []
visit = [0] * (g + 1)
a = []
nums = [0]
tmp = g
while tmp > 0:
    nums.append(list(map(int, input().split())))
    tmp -= 1

dfs(0)
value.sort(key=lambda x: (len(x), x[0]))
print(len(value[0]), end=' ')
print(*value[0], sep=' ')
