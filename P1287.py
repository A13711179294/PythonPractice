from math import factorial


def f(n, m):
    if m <= 0 or n < m:
        return 0
    if n == m:
        return 1
    else:
        return f(n - 1, m - 1) + f(n - 1, m) * m


n, r = map(int, input().split())
ans = f(n, r)
print(ans * factorial(r))
