def binary_search():
    left = 0
    right = l
    while left < right:
        mid = left + right >> 1
        if check(mid):
            right = mid
        else:
            left = mid + 1
    return left


def check(m):
    count1 = k
    pos = 0
    i = 1
    while i < n:
        if count1 < 0:
            break
        if a[i] - pos <= m:
            pos = a[i]
        else:
            pos += m
            i -= 1
            count1 -= 1
        i += 1

    return count1 >= 0


l, n, k = map(int, input().split())
a = list(map(int, input().split()))
print(binary_search())
