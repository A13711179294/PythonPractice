w1 = 0
l1 = 0
w2 = 0
l2 = 0
ans1 = []
ans2 = []
flag = 0
while True:
    tmp = input().strip()
    for i in tmp:
        if i == 'W':
            w1 += 1
            w2 += 1
        elif i == 'L':
            l1 += 1
            l2 += 1
        if (w1 >= 11 and w1 - l1 >= 2) or (l1 >= 11 and l1 - w1 >= 2):
            ans1.append('%s:%s' % (w1, l1))
            w1 = 0
            l1 = 0
        if (w2 >= 21 and w2 - l2 >= 2) or (l2 >= 21 and l2 - w2 >= 2):
            ans2.append('%s:%s' % (w2, l2))
            w2 = 0
            l2 = 0
        if i == 'E':
            flag = 1
            break
    if flag == 1:
        break
ans1.append('%s:%s' % (w1, l1))
ans2.append('%s:%s' % (w2, l2))

for i in ans1:
    print(i)
print()
for i in ans2:
    print(i)
