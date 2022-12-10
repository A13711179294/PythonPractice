def prime(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


N = int(input())
for x in range(4, N + 1, 2):
    for y in range(2, N):
        if x > y and prime(y) == True and prime(x - y) == True:
            print('%d=%d+%d' % (x, y, x - y))
            break
