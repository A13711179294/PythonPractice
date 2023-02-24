# def partition(li, left, right):
#     tmp = li[left]
#     while left < right:
#         while left < right and tmp <= li[right]:
#             right -= 1
#         li[left] = li[right]
#         while left < right and tmp >= li[left]:
#             left += 1
#         li[right] = li[left]
#     li[left] = tmp
#     return left
#
#
# def q_sort(li, left, right):
#     if left < right:
#         mid = partition(li, left, right)
#         q_sort(li, 0, mid - 1)
#         q_sort(li, mid + 1, right)
#

n = int(input())
li = list(map(int, input().split()))
#q_sort(li, 0, n - 1)
li.sort()
print(*li)
