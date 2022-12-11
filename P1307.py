N = input()
if N != '0':
    N = N.rstrip('0')
N = int(N)

flag = 0
if N < 0:
    N = N * (-1)
    flag = 1

list1 = list(reversed(str(N)))

if flag == 1:
    print('-' + ''.join(list1))
else:
    print(''.join(list1))
