L = int(input())
D = int(input())
X = int(input())
digit = []

for i in range(L, D + 1):
    tmp1 = str(i)
    sum1 = 0
    for j in tmp1:
        sum1 += int(j)
    if sum1 == X:
        digit.append(i)
print(min(digit))
print(max(digit))