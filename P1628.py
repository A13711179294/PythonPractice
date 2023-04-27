N = int(input().strip())
tmp = N
alpha = []
while tmp > 0:
    alpha.append(input().strip())
    tmp -= 1
k = input().strip()
l = len(k)
ans = []
for i in alpha:
    if k == i[0:l]:
        ans.append(i)
ans.sort()
for i in ans:
    print(i)
