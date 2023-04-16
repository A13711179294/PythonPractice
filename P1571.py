def binary_search(x):
    left = 1
    right = m
    while left <= right:
        mid = (left + right) >> 1
        if x > nums_2[mid]:
            left = mid + 1
        elif x < nums_2[mid]:
            right = mid - 1
        else:
            return 1
    return 0


n, m = map(int, input().split())

if n and m:
    nums_1 = [0] + list(map(int, input().split()))
    nums_2 = [0] + list(map(int, input().split()))

    nums_2.sort()

    for i in range(1, n + 1):
        if binary_search(nums_1[i]):
            print(nums_1[i], end=' ')
