def fun(x):
    return x - (x + 2) // 4


l, r = map(int, input().split())
print(fun(r) - fun(l - 1))
