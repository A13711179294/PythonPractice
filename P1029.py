from math import gcd

x, y = map(int, input().split())
for i in range(x + 1, 0, -1):
    for z in range(y + 1, x, -1):
        if gcd(i, z) == x:
            print(i, z)
