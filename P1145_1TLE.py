k = int(input())
flag = 0
res = 0
m = k
c = 0
while flag == 0:
    i = 0
    count1 = 2 * k
    count2 = 0
    while True:
        c += 1
        i = (i + m - 1) % count1
        count1 -= 1
        count2 += 1
        if i <= k - 1:
            m += 1
            break
        elif count2 == k:
            flag = 1
            res = m
            break
print(c)
print(res)
