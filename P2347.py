num = [0, 1, 2, 3, 5, 10, 20]
a = [0]
a.extend(list(map(int, input().strip().split())))
nums = [0]
for i in range(1, 7):
    for j in range(a[i]):
        nums.append(num[i])

max_sum = 0
for i in range(1, 7):
    max_sum += num[i] * a[i]

dp = [0 for _ in range(max_sum + 1)]
dp[0] = 1

for i in range(1, len(nums)):
    for j in range(max_sum, nums[i] - 1, -1):
        dp[j] += dp[j - nums[i]]

ans = 0
for i in dp[1:max_sum + 1]:
    if i:
        ans += 1
print('Total=%d' % ans)
