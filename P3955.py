n, q = map(int, input().split())
m = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000]
nums = [0]

for _ in range(n):
    nums.append(int(input()))
nums.sort()

for _ in range(q):
    a, b = map(int, input().split())
    ans = -1
    for i in range(1, n + 1):
        tmp = nums[i] % m[a]
        if tmp == b:
            ans = nums[i]
            break
    print(ans)
