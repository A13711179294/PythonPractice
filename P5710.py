n = int(input())
flag1 = 0
flag2 = 0
if n % 2 == 0:
    flag1 = 1
if 4 < n <= 12:
    flag2 = 1

if flag1 and flag2:
    print(1, end=' ')
else:
    print(0, end=' ')
if flag1 or flag2 or (flag1 and flag2):
    print(1, end=' ')
else:
    print(0, end=' ')
if (flag1 and flag2 == 0) or (flag2 and flag1 == 0):
    print(1, end=' ')
else:
    print(0, end=' ')
if flag1 == 0 and flag2 == 0:
    print(1, end=' ')
else:
    print(0, end=' ')
