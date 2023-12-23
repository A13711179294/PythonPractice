# from math import pow
# N = int(input().strip())
# N -= 1
# ans = 1
# for i in range(1, N):
#     ans += pow((N - i + 1), 2)
#     ans %= (10e9 + 7)
#     for j in range(1, N - i + 1):
#         ans += pow((N - (i + j) + 1), 2)
#         ans %= (10e9 + 7)
# print(int(ans))

N = int(input())
res = 0
for i in range(N - 1):
    res += pow((N - (i + 1)), 2) * (i + 1)
    res = res % 1000000007
print(res)
