from math import ceil
n = int(input())
money = []
for i in range(3):
    a, b = map(int, input().split())
    money.append(ceil(n / a) * b)

print(min(money))
