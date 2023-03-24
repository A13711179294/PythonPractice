s, a, b = map(int, input().split())
t = (b + a) * s / (b + 3 * a)
print('%.6f' % (t / b + (s - t) / a))
