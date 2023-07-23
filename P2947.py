n = int(input())
stack = []
ans = [0] * 100001
a = [0]
for i in range(1, n + 1):
    a.append((i, int(input())))

for j in range(1, n + 1):

    while stack and a[j][1] > stack[-1][1]:
        tmp = stack.pop()
        ans[tmp[0]] = [j][0]
    stack.append(a[j])

for i in range(1, n + 1):
    print(ans[i])
