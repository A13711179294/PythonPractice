from math import sqrt

a, b, c = map(float, input().split())
p = (a + b + c) / 2
s = sqrt(p * (p - a) * (p - b) * (p - c))
print('%.1f' % s)
