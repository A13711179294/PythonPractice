from math import sqrt

M = int(input())
k1 = int(sqrt(2 * M))
for i in range(k1, 1, -1):
    if 2 * M % i == 0 and (i + 2 * M // i) % 2:
        k2 = 2 * M // i
        print((k2-i+1)//2, (i+k2-1)//2, sep=' ')
