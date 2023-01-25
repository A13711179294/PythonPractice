n = input().strip()
tmp = 0
for i in range(len(n)):
    if n[i] == '=':
        tmp = i
        break

left = n[:tmp]
right = n[tmp + 1:]

left_symbol = []
right_symbol = []

for i in left:
    if i == '+' or i == '-':
        left_symbol.append(i)
for i in right:
    if i == '+' or i == '-':
        right_symbol.append(i)

left_digit = list(left.replace('-', ' ').replace('+', ' ').split())
right_digit = list(right.replace('-', ' ').replace('+', ' ').split())

if len(left_symbol) + 1 == len(left_digit):
    left_symbol.insert(0, '+')
if len(right_symbol) + 1 == len(right_digit):
    right_symbol.insert(0, '+')

digit = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
flag = 0
tmp_x = ''
for i in left_digit:
    for j in str(i):
        if j not in digit:
            tmp_x = j
            flag = 1
            break
if flag == 0:
    for i in right_digit:
        for j in str(i):
            if j not in digit:
                tmp_x = j
                break

left_sum = 0
left_x_sum = 0
for i in range(len(left_digit)):
    if tmp_x not in str(left_digit[i]):
        if left_symbol[i] == '+':
            left_sum += int(left_digit[i])
        elif left_symbol[i] == '-':
            left_sum -= int(left_digit[i])
    else:
        if left_symbol[i] == '+':
            if left_digit[i][:-1] != '':
                left_x_sum += int(left_digit[i][:-1])
            else:
                left_x_sum += 1
        elif left_symbol[i] == '-':
            if left_digit[i][:-1] != '':
                left_x_sum -= int(left_digit[i][:-1])
            else:
                left_x_sum -= 1

right_sum = 0
right_x_sum = 0
for i in range(len(right_digit)):
    if tmp_x not in str(right_digit[i]):
        if right_symbol[i] == '+':
            right_sum += int(right_digit[i])
        elif right_symbol[i] == '-':
            right_sum -= int(right_digit[i])
    else:
        if right_symbol[i] == '+':
            if right_digit[i][:-1] != '':
                right_x_sum += int(right_digit[i][:-1])
            else:
                right_x_sum += 1
        elif right_symbol[i] == '-':
            if right_digit[i][:-1] != '':
                right_x_sum -= int(right_digit[i][:-1])
            else:
                right_x_sum -= 1

tmp_sum = right_sum - left_sum
tmp_x_sum = left_x_sum - right_x_sum
if tmp_sum == 0:
    ans = 0
else:
    ans = tmp_sum / tmp_x_sum
print('{}={:.3f}'.format(tmp_x, ans))
