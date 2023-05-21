from math import sqrt
N = int(input())
for i in range(1, int(sqrt(N)) + 1):
    if i * i <= N:
        print(i * i, end=' ')
