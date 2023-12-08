from math import sqrt

n = int(input())
tmp = int(sqrt(n))
flag = 0
for i in range(0, tmp + 1):
    if flag == 0:
        for j in range(0, tmp + 1):
            if flag == 0:
                for k in range(0, tmp + 1):
                    tmp2 = n - i * i - j * j - k * k
                    if tmp2 < 0:
                        break
                    if sqrt(tmp2) == int(sqrt(tmp2)):
                        print(i, j, k, int(sqrt(tmp2)), sep=' ')
                        flag = 1
                        break
