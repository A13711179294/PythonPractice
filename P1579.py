def is_prime(x):
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            return 0
    else:
        return 1


n = int(input())
flag = 0
for i in range(2, n - 3):
    if is_prime(i) == 1:
        for j in range(i, n - i - 1):
            if is_prime(j) and is_prime(n - i - j):
                print(i, j, n - i - j)
                flag = 1
                break
    if flag == 1:
        break
