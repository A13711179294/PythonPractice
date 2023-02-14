# N = int(input())
# ans = 1
# for i in range(1, N + 1):
#     ans *= i
#     while ans % 10 == 0:
#         ans //= 10
#         ans %= 10000000
#
# print(ans % 10)

n = int(input())
a = [6, 8, 4, 2]
ans = 1
while n > 1:
    for i in range(1, n % 10 + 1):
        if i != 5:
            ans = ans * i % 10

    n = n // 5
    ans = ans * a[n % 4] % 10

print(ans)
