a, b, n = map(int, input().split())
mod = b * 1000
ans = 1
n += 2
base = 10
while n:
    if n % 2 != 0:
        ans *= base % mod
    base *= base % mod
    n >>= 1

print(a * ans % mod // b)
