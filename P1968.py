n = int(input())
t1 = 100.0
t2 = 0
for _ in range(n):
    a = float(input())
    tmp = t1
    t1 = max(t1, t2 / a * 100)
    t2 = max(t2, t1 / 100 * a)
print('%.2f' % t1)
