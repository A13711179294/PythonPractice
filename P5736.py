def isprime(x):
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            return False
    return True


n = int(input())
ni = list(map(int, input().split()))
for i in ni:
    if (i % 2 != 0 or i == 2) and i != 1:
        if isprime(i):
            print(i, end=' ')
