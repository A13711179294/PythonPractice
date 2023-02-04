n = int(input())
digit = {}
tmp = n
while tmp > 0:
    tmp1 = int(input())
    digit[tmp1] = digit.get(tmp1, 0) + 1
    tmp -= 1

digit = sorted(digit.items())
for i in digit:
    print(i[0],i[1])
