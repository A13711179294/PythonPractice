n, k = map(int, input().split())
nums = []
for _ in range(n):
    nums.append(int(input()))

nums.sort()

l = 0
r = n - 1
sign = 1
res = 1

if k % 2 != 0:
    res = nums[r]
    k -= 1
    r -= 1
    if res < 0:
        sign = -1

while k:
    t1 = nums[l] * nums[l + 1]
    t2 = nums[r] * nums[r - 1]
    if t1 * sign > t2 * sign:
        res *= t1
        l += 2
    else:
        res *= t2
        r -= 2
    k -= 2

if res < 0:
    res = 0 - ((0 - res) % (10 ** 9 + 9))
else:
    res = res % (10 ** 9 + 9)

print(res)
