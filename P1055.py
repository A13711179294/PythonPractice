ISBN = ''.join(input().strip().split('-'))
sum1 = 0
for i in range(1, 10):
    sum1 += int(ISBN[i - 1]) * i
sum2 = str(sum1 % 11)
if sum2 == '10':
    sum2 = 'X'
if sum2 == ISBN[-1]:
    print('Right')
else:
    print(ISBN[0] + '-' + ''.join(ISBN[1:4]) + '-' + ''.join(ISBN[4:9]) + '-' + sum2)
