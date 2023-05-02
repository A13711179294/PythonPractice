def matrix_add(ind):
    t1 = matrix1[ind]
    ind += 1
    while ind + 1 <= n + 1:
        t2 = matrix1[ind]
        t1 = matrix_sum(t1, t2)
        dp_func(t1)
        ind += 1
    return t1


def matrix_sum(li1, li2):
    li3 = [0]
    for i in range(1, n + 1):
        li3.append(li1[i] + li2[i])
    return li3


def dp_func(a):
    max1 = -128
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = max(dp[i - 1] + a[i], a[i])
        if dp[i] > max1:
            max1 = dp[i]
    #print(dp)
    ans.append(max1)


n = int(input())
matrix1 = [[0] for _ in range(n + 1)]
ans = []
nums = []
while len(nums) < n * n:
    num = list(map(int, input().split()))
    nums.extend(num)

i = 1
count1 = 0
for j in nums:
    matrix1[i].append(j)
    count1 += 1
    if count1 == n:
        count1 = 0
        i += 1

# for i in matrix1:
#     print(i)

for i in range(1, n + 1):
    dp_func(matrix1[i])
    matrix_add(i)

print(max(ans))
