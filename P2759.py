from math import log10
n = int(input())
n -= 1

left = 1
right = int(3e8)
while left < right:
    mid = (left + right) >> 1
    if mid * log10(mid) < n:
        left = mid + 1
    else:
        right = mid

print(left)