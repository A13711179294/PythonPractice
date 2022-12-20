x, n = map(int, input().split())
count = x
sum1 = 0
while n > 0:
    if count == 6:
        count += 1
        n -= 1
        continue
    if count == 7:
        n -= 1
        count = 1
        continue
    sum1 += 250
    count += 1
    n -= 1
print(sum1)
