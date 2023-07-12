def binary_search():
    left = 0
    right = l + 1
    while left < right:
        mid = (left + right + 1) >> 1
        if check(mid):
            left = mid
        else:
            right = mid - 1
    return left


def check(x):
    total = 0
    now = 0
    i = 0
    while i < n + 1:
        i += 1
        if a[i] - a[now] < x:
            total += 1
        else:
            now = i

    if total > m:
        return False
    else:
        return True


l, n, m = map(int, input().split())
a = [0]
for _ in range(n):
    a.append(int(input()))
a.append(l)

print(binary_search())