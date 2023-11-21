from math import ceil
m, t, s = map(int, input().split())
if t != 0 and m != 0:
    sum1 = ceil(s / t)
    if sum1 >= m:
        print(0)
    else:
        print(m - sum1)
else:
    print(0)
