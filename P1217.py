from math import sqrt


def isprime(x):
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


a, b = map(int, input().split())
c = [5, 7, 11]
for d1 in range(1, 10, 2):  # 生成3位回文数
    for d2 in range(0, 10):
        c.append(d1 * 100 + d2 * 10 + d1)
for d1 in range(1, 10, 2):  # 生成5位回文数
    for d2 in range(0, 10):
        for d3 in range(0, 10):
            c.append(d1 * 10000 + d2 * 1000 + d3 * 100 + d2 * 10 + d1)
for d1 in range(1, 10, 2):  # 生成7位回文数
    for d2 in range(0, 10):
        for d3 in range(0, 10):
            for d4 in range(0, 10):
                c.append(d1 * 1000000 + d2 * 100000 + d3 * 10000 + d4 * 1000 + d3 * 100 + d2 * 10 + d1)
for d1 in range(1, 10, 2):  # 生成9位回文数
    for d2 in range(0, 10):
        for d3 in range(0, 10):
            for d4 in range(0, 10):
                for d5 in range(0, 10):
                    c.append(d1 * 100000000 + d2 * 10000000 + d3 * 1000000 + d4 * 100000 + d5 * 10000 + d4 * 1000 + d3 * 100 + d2 * 10 + d1)

for i in c:
    if a <= i <= b:
        if isprime(i):
            print(i)
    if i > b:
        break
