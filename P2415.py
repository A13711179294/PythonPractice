n = list(map(int, input().split()))
nl = len(n)
sum1 = 0
for i in n:
    sum1 += i * pow(2, nl - 1)

print(sum1)
