def dfs(num):
    global ans
    visit[num] = 1
    ans += 1
    for i in range(1, k + 1):
        if a[i] == num and visit[b[i]] == 0:
            dfs(b[i])


n, k = input().split()
k = int(k)
n = '0' + n
a = [0]
b = [0]

tmp = k
while tmp > 0:
    before, after = map(int, input().split())
    a.append(before)
    b.append(after)
    tmp -= 1

flag = 0
sum1 = 1
for i in range(1, len(n)):
    visit = [0] * 10
    ans = 0
    dfs(int(n[i]))
    if ans != 0:
        flag = 1
        sum1 *= ans

if flag == 1:
    print(sum1)
else:
    print(0)