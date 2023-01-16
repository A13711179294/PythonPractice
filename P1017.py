dict1 = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'G', 17: 'H', 18: 'I', 19: 'J', 20: 'K'}
n, R = map(int, input().split())

tmp1 = n
tmp2 = R
list1 = []

while True:
    tmp = tmp1 % tmp2
    tmp1 //= tmp2

    if tmp < 0:
        tmp -= tmp2
        tmp1 += 1

    if tmp in dict1:
        list1.append(dict1[tmp])
    else:
        list1.append(tmp)
    if tmp1 == 0:
        break

print(n, '=', end='', sep='')
for i in list1[::-1]:
    print(i, end='')
print('(base{})'.format(R))
