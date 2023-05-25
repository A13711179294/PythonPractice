# import numpy as np
#
# n, k = map(int, input().split())
# arr = np.fromstring(input(), dtype = np.uint32, sep=' ')
# arr.sort()
# print(arr[k])


def partition(left, right):
    tmp = li[left]
    while left < right:
        while left < right and li[right] >= tmp:
            right -= 1
        li[left] = li[right]
        while left < right and li[left] <= tmp:
            left += 1
        li[right] = li[left]
    li[left] = tmp
    return left


def quick_sort(left, right):
    if left <= right:
        mid = partition(left, right)
        if mid == k:
            print(li[mid])
        elif mid > k:
            quick_sort(left, mid-1)
        else:
            quick_sort(mid+1, right)


n, k = map(int, input().split())
li = list(map(int, input().split()))
quick_sort(0, n - 1)
