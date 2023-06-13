from math import gcd

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

tmp1 = gcd(y2 - y1, x2 - x1)
if ((y2 - y1) // tmp1) % ((x2 - x1) // tmp1) == 0:
    k = '%s' % (((y2 - y1) // tmp1) // ((x2 - x1) // tmp1))
else:
    if ((y2 - y1) // tmp1) >= 0 > ((x2 - x1) // tmp1):
        k = '-%s/%s' % ((y2 - y1) // tmp1, -(x2 - x1) // tmp1)
    elif ((x2 - x1) // tmp1) > 0 > ((y2 - y1) // tmp1):
        k = '-%s/%s' % (-(y2 - y1) // tmp1, (x2 - x1) // tmp1)
    elif ((y2 - y1) // tmp1) > 0 and ((x2 - x1) // tmp1) > 0:
        k = '%s/%s' % ((y2 - y1) // tmp1, (x2 - x1) // tmp1)
    else:
        k = '%s/%s' % (-(y2 - y1) // tmp1, -(x2 - x1) // tmp1)

tmp2 = gcd(y2 * x1 - y1 * x2, x1 - x2)
if ((y2 * x1 - y1 * x2) // tmp2) % ((x1 - x2) // tmp2) == 0:
    b = '%s' % (((y2 * x1 - y1 * x2) // tmp2) // ((x1 - x2) // tmp2))

else:
    if ((y2 * x1 - y1 * x2) // tmp2) >= 0 > ((x1 - x2) // tmp2):
        b = '-%s/%s' % (((y2 * x1 - y1 * x2) // tmp2), -((x1 - x2) // tmp2))
    elif ((x1 - x2) // tmp2) > 0 > ((y2 * x1 - y1 * x2) // tmp2):
        b = '-%s/%s' % (-((y2 * x1 - y1 * x2) // tmp2), ((x1 - x2) // tmp2))
    elif ((y2 * x1 - y1 * x2) // tmp2) > 0 and ((x1 - x2) // tmp2) > 0:
        b = '%s/%s' % (((y2 * x1 - y1 * x2) // tmp2), ((x1 - x2) // tmp2))
    else:
        b = '%s/%s' % (-((y2 * x1 - y1 * x2) // tmp2), -((x1 - x2) // tmp2))

if int(eval(k)) != eval(k) and eval(b) > 0:
    print('y={}*x+{}'.format(k, b))
elif int(eval(k)) != eval(k) and eval(b) < 0:
    print('y={}*x{}'.format(k, b))
elif int(eval(k)) != eval(k) and eval(b) == 0:
    print('y={}*x'.format(k))
elif eval(k) == 1 and eval(b) > 0:
    print('y=x+{}'.format(b))
elif eval(k) == 1 and eval(b) < 0:
    print('y=x{}'.format(b))
elif eval(k) != 1 and eval(b) < 0:
    print('y={}x{}'.format(k, b))
elif eval(k) != 1 and eval(b) == 0:
    print('y={}x'.format(k))
else:
    print('y={}x+{}'.format(k, b))
