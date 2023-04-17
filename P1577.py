def binary_search():
    ans = 0
    left = 0
    right = 999999999999
    while left <= right:
        mid = (left + right) >> 1
        if mid == 0:
            break
        if check(mid):
            left = mid + 1
            ans = mid
        else:
            right = mid - 1
    return ans


def check(l):
    cnt = 0
    for i in range(1, n + 1):
        cnt += a[i] // l
    if cnt >= k:
        return True
    else:
        return False


n, k = map(int, input().split())
a = [0]
for _ in range(n):
    a.append(int(float(input()) * 100))

print('%.2f' % (binary_search() / 100))
