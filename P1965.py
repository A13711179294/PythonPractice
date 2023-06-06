def func(a, b):
    ans = 1
    base = a
    while b:
        if b & 1:
            ans = ans * base % n
        base = base * base % n
        b >>= 1
    return ans


n, m, k, x = map(int, input().split())

# print((x + m * pow(10, k, n)) % n)

print((x % n + m * func(10, k) % n) % n)
