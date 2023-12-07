from math import sqrt, ceil

n, l, r = map(int, input().split())
sum1 = r - l + 1
print(ceil(sum1 - (sqrt(r) - sqrt(l - 1))))
