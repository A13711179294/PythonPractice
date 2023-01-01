k = int(input())

sum1 = 0
count = 1
money = 0
day = 0

while True:

    money = count * count
    sum1 += money
    day += count

    if day == k:
        break
    elif day > k:
        sum1 -= (day - k) * count
        break
    count += 1

print(sum1)
