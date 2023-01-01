str1 = input().strip()
symbol_list = []
for i in str1:
    if i in '+-*/':
        symbol_list.append(i)

symbol_length = len(symbol_list)
number_list = list(map(int, str1.replace('+', ' ').replace('-', ' ').replace('*', ' ').replace('/', ' ').split()))
sum1 = number_list[0]

for i in range(0, symbol_length):
    if symbol_list[i] == '+':
        sum1 += number_list[i+1]
    if symbol_list[i] == '-':
        sum1 -= number_list[i+1]
    if symbol_list[i] == '*':
        sum1 *= number_list[i+1]
    if symbol_list[i] == '/':
        sum1 /= number_list[i+1]

if sum1 != int(sum1):
    print(sum1)
else:
    print(int(sum1))
