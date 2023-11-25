def isprime(x):
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            return False
    return True


L = int(input())
count1 = 0
sum1 = 0
i = 2

while sum1 + i <= L:
    if isprime(i):
        print(i)
        sum1 += i
        count1 += 1
    i += 1

print(count1)
