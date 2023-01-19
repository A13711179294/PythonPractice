N, K = map(int, input().split())
digit = list(map(int, input().split()))


def isprime(x):
    for j in range(2, x // 2 + 1):
        if x % j == 0:
            return False
    return True


def find(i, k, sum2):
    global count1
    if k == K:
        if isprime(sum2):
            count1 += 1
        return
    for j in range(i, N):
        find(j + 1, k + 1, sum2 + digit[j])


count1 = 0
find(0, 0, 0)
print(count1)
