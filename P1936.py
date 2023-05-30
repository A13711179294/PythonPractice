k = int(input())
n = 1
m = 1
t = 0
while n + m <= k:
    t = n + m
    m = n
    n = t

print('m=%d' % m)
print('n=%d' % n)
