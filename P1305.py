n = int(input().strip())
tmp = n - 1
pre = list(input().strip())
while tmp > 0:
    child = list(input().strip())
    for i in range(len(pre)):
        if child[0] == pre[i]:
            pre.pop(i)
            for j in child[::-1]:
                pre.insert(i, j)
    tmp -= 1
for i in pre:
    if i != '*':
        print(i, end='')
