n, k = map(int, input().split())
tmp = bin(k).lstrip('0b')
sum1 = 0
for i in range(len(tmp)):
    sum1 += int(tmp[len(tmp) - 1 - i]) * (n ** i)
print(sum1)
