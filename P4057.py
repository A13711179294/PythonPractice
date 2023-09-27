from math import gcd

time = list(map(int, input().split()))
time.sort()
m = time[0]
n = time[1]
for _ in range(2):
    n = m * n // gcd(m, n)
    m = time[2]
print(n)
