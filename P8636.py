from math import gcd

n = int(input().strip())
x = list(map(int, input().strip().split()))
x = list(set(x))
x.sort()
digit = []
for i in range(len(x) - 1):
    tmp = gcd(x[i + 1], x[i])
    digit.append((x[i + 1] // tmp, x[i] // tmp))

digit = list(set(digit))
digit.sort(key=lambda y: y[0], reverse=True)

a, b = digit[0][0], digit[0][1]
for i in range(1, len(digit)):
    a //= digit[i][0]
    b //= digit[i][1]

tmp1 = digit[0][0]
tmp2 = digit[0][1]
while True:
    tmp1 = (tmp1/a)
    tmp2 = (tmp2/b)
    if tmp1 / tmp2 < a / b and tmp1 / tmp2 != 1:
        a = a // tmp1
        b = b // tmp2
    elif tmp1 / tmp2 == 1:
        break



print('%d/%d' % (a, b))
