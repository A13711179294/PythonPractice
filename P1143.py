num_dict1 = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12,
             'D': 13, 'E': 14, 'F': 15}
num_dict2 = {'0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9', '10': 'A', '11': 'B',
             '12': 'C', '13': 'D', '14': 'E', '15': 'F'}

n = int(input().strip())
value = input().strip()
m = int(input().strip())

n_length = len(value)

sum1 = 0
temp = n
for i in range(0, n_length):
    sum1 += num_dict1[value[i]] * pow(temp, (n_length - 1) - i)

if sum1 == 0:
    print('0')
else:
    count = 0
    list1 = []
    while sum1 > 0:
        count = sum1 - m * (sum1 // m)
        sum1 = sum1 // m
        list1.append(str(num_dict2[str(count)]))

    list1.reverse()
    print(''.join(list1))
