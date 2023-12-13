t = int(input())
for _ in range(t):
    a = input().split()
    b = input().split()

    d1 = d2 = 0
    if len(a) == 3:
        d1 = int(a[2].strip('()')) * 24 * 3600
    if len(b) == 3:
        d2 = int(b[2].strip('()')) * 24 * 3600

    t11 = list(map(int, a[0].split(':')))
    t12 = list(map(int, a[1].split(':')))
    t21 = list(map(int, b[0].split(':')))
    t22 = list(map(int, b[1].split(':')))

    cnt1 = (t12[0] - t11[0]) * 3600 + (t12[1] - t11[1]) * 60 + t12[2] - t11[2] + d1
    cnt2 = (t22[0] - t21[0]) * 3600 + (t22[1] - t21[1]) * 60 + t22[2] - t21[2] + d2

    ans = cnt1 + cnt2 >> 1
    h = ans // 3600
    ans %= 3600
    m = ans // 60
    ans %= 60
    s = ans % 60
    print('{:0>2d}:{:0>2d}:{:0>2d}'.format(h, m, s))
