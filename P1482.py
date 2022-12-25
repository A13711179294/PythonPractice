from math import gcd

a1, a2 = map(int, input().split('/'))
b1, b2 = map(int, input().split('/'))

ret = gcd(a1 * b1, a2 * b2)

r = (a1 * b1) // ret
c = (a2 * b2) // ret

print(c, r)
