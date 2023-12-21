n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

if m == 0:
    print(sum(nums))
else:
    ans = nums[-1] - nums[0]
    print(nums[1:-1])
    for i in nums[1:-1]:
        ans += abs(i)
    print(ans)
