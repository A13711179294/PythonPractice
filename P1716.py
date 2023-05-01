n = int(input())
tmp = n
digit = []
while tmp > 0:
    digit.append(int(input()))
    tmp -= 1
digit.sort(reverse=True)
tmp = len(digit)
for i in range(1, tmp+1):
    if i % 2 != 0:
        print(digit[0])
        digit.pop(0)
    else:
        print(digit[-1])
        digit.pop()
