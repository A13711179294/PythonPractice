n, m = map(int, input().split())
tmp1 = m
milk = []

while tmp1 > 0:
    milk.append(tuple(map(int, input().split())))
    tmp1 -= 1

milk.sort(key=lambda x: x[0])
money = 0
sum1 = 0
count1 = 0

for i in milk:
    tmp = n - count1
    if tmp >= i[1]:
        money += i[0] * i[1]
        count1 += i[1]
    elif tmp < i[1]:
        money += i[0] * tmp
        count1 += tmp
    if tmp == 0:
        break

print(money)