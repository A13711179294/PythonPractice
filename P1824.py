def binary_search():
    left = 0
    right = 2 ** 30
    while left + 1 < right:
        mid = (left + right) >> 1
        now = nums[1]
        j = 1
        for i in range(2, n + 1):
            if nums[i] - now >= mid:
                now = nums[i]
                j += 1
            if j >= c:
                break
        if j < c:
            right = mid
        else:
            left = mid
    return left


n, c = map(int, input().split())
nums = [0]
for _ in range(n):
    nums.append(int(input()))

nums.sort()
print(binary_search())