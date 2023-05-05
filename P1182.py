def binary_search():
    left = max(a)
    right = sum(a)
    while left <= right:
        mid = left + right >> 1
        if check(mid):
            left = mid + 1
        else:
            right = mid - 1
    return left


def check(t):
    tmp = 0
    count1 = 0
    for i in range(1, n + 1):
        if tmp + a[i] <= t:
            tmp += a[i]
        else:
            count1 += 1
            tmp = a[i]
    return count1 >= m


n, m = map(int, input().split())
a = [0] + list(map(int, input().split()))
ret = binary_search()
print(ret)
