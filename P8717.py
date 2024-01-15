n = int(input())
tmp = n
sum1 = 0
max1 = 0
min1 = 101
while tmp > 0:
    value = int(input())
    if value > max1:
        max1 = value
    if value < min1:
        min1 = value
    sum1 += value
    tmp -= 1
print(max1)
print(min1)
print('%.2f' % (sum1 / n))
