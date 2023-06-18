from math import gcd

a, b, l = map(int, input().split())
ab = a / b
x = a
y = b
min1 = float('inf')
for i in range(1, l + 1):
    for j in range(1, l + 1):
        if gcd(i, j) == 1:
            t = i / j
            if t >= ab:
                s = t - ab
                if s < min1:
                    min1 = s
                    x = i
                    y = j

print(x, y, sep=' ')
