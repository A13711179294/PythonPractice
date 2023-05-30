n = int(input())
flag = 0
for _ in range(n):
    a = list(input().split())
    if len(a) == 3:
        if a[0] == 'a':
            flag = 1
        elif a[0] == 'b':
            flag = 2
        else:
            flag = 3
    else:
        a.insert(0, 0)
    a[1] = int(a[1])
    a[2] = int(a[2])
    if flag == 1:
        print('%d+%d=%d' % (a[1], a[2], a[1] + a[2]))
        print(len(str(a[1]) + str(a[2]) + str(a[1] + a[2])) + 2)
    elif flag == 2:
        print('%d-%d=%d' % (a[1], a[2], a[1] - a[2]))
        print(len(str(a[1]) + str(a[2]) + str(a[1] - a[2])) + 2)
    else:
        print('%d*%d=%d' % (a[1], a[2], a[1] * a[2]))
        print(len(str(a[1]) + str(a[2]) + str(a[1] * a[2])) + 2)
