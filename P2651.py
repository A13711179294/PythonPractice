from math import gcd

for _ in range(int(input())):
    n = int(input())
    a = [0] + list(map(int, input().split()))
    for i in range(1, n + 1):
        if i != 2:
            a[2] //= gcd(a[2], a[i])
    if a[2] == 1:
        print('Yes')
    else:
        print('No')