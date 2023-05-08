from math import sqrt


def function():
    t = 0
    for x in a:
        t = max(t, x)
        m = int(sqrt(x))
        for i in range(1, m + 1):
            if x % i == 0:
                c[i] += 1
                if x != i * i:
                    c[x // i] += 1
    return t


n = int(input())
a = list(map(int, input().split()))
c = [0] * 1000001

x = function()
for i in range(1, n + 1):
    while c[x] < i:
        x -= 1
    print(x)
