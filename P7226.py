n = int(input().strip())
tmp = n
digit = []
while tmp > 0:
    digit.append(input().strip())
    tmp -= 1
sum1 = 0
for i in range(n):
    sum1 += pow(int(digit[i][:len(digit[i])-1]), int(digit[i][-1]))
print(sum1)
