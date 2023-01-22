from math import gcd, sqrt

x, y = map(int, input().split())
count1 = 0
for i in range(x, int(sqrt(y * x)) + 1):
    if x * y % i == 0 and gcd(i, x * y // i) == x:
        count1 += 2

if x == y:
    count1 -= 1
print(count1)
