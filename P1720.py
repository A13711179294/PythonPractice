from math import sqrt, pow

n = int(input())
Fn = (pow((1 + sqrt(5)) / 2, n) - pow((1 - sqrt(5)) / 2, n)) / sqrt(5)
print('%.2f' % Fn)
