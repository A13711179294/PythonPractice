str1 = input()
left_symbol = []
right_symbol = []
flag = 0
for i in str1:
    if i == '(':
        left_symbol.append(i)
    if i == ')':
        try:
            left_symbol.pop()
        except:
            flag = 1

if flag == 0 and len(left_symbol) == 0:
    print('YES')
else:
    print('NO')
