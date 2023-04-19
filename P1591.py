from math import factorial
t = int(input())
b = []
while t > 0:
    n, a = map(int, input().split())
    b.append(str(factorial(n)).count(str(a)))
    t -= 1
for i in b:
    print(i)
