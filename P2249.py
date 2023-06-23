def binary_search(x):
    left = 1
    right = n
    while left < right:
        mid = (right + left) >> 1
        if a[mid] >= x:
            right = mid
        else:
            left = mid + 1
    if a[left] == x:
        return left
    else:
        return -1


n, m = map(int, input().split())
a = [0] + list(map(int, input().split()))
b = list(map(int, input().split()))

for i in b:
    print(binary_search(i), end=' ')
