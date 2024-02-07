def trans(num):
    if num % p < 10:
        return num % p
    return chr(num % p + ord('A') - 10)


def test(x):
    a = []
    while x > 0:
        a.append(trans(x))
        x //= p
    a.reverse()
    return a


p = int(input())

for i in range(1, p):
    for j in range(1, i + 1):
        print(*test(i), '*', *test(j), '=', *test(i * j), sep='', end=' ')
    print()
