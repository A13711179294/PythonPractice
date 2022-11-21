from math import factorial

n = int(input())
s = 0
for i in range(1, n + 1):
    ret = factorial(i)
    s += ret
print(s)
