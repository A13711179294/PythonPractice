from sys import stdin, stdout


def binary_search():
    left = 0
    right = 1e10
    while right - left > 1e-4:
        mid = (left + right) / 2
        if check(mid):
            left = mid
        else:
            right = mid
    return left


def check(m):
    if cnt3 < m:
        return False
    q = p * m
    for i in range(n):
        if ab[i][0] * m > ab[i][1]:
            q -= ab[i][0] * m - ab[i][1]
    if q >= 0:
        return True
    return False


n, p = map(int, stdin.readline().split())
ab = []
cnt1 = 0
cnt2 = 0
for _ in range(n):
    t1, t2 = map(int, stdin.readline().split())
    cnt1 += t1
    cnt2 += t2
    ab.append([t1, t2])

if cnt1 <= p:
    stdout.write('-1')
else:
    cnt3 = cnt2 / (cnt1 - p)
    # print(cnt3)
    print('%.10f' % binary_search())
