n, m = map(int, input().strip().split())
hurt_list = []
while len(hurt_list) < n:
    hurt_list.append(int(input().strip()))

sum_list = []
for i in range(0, n - m + 1):
    temp = 0
    for x in range(i, i + m):
        temp += hurt_list[x]
    sum_list.append(temp)

print(min(sum_list))
