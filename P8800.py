def binary_search():
    l = min(a[1:])
    r = max(a) + max(b)
    while l < r:
        mid = l + r + 1 >> 1
        if check(mid):
            l = mid
        else:
            r = mid - 1
    return l


def check(x):
    sum1 = 0
    for i in range(1, n + 1):
        if a[i] + b[i] < x:
            return False
        if a[i] < x:
            sum1 += x - a[i]
    return sum1 <= m


n, m = map(int, input().split())
a = [0] + list(map(int, input().split()))
b = [0] + list(map(int, input().split()))
print(binary_search())
