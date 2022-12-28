dict1 = {'a': '0', 'b': '0', 'c': '0'}
value_list = list(input().replace(':=', '').replace(';', ' ').strip().split())

for i in value_list:
    if i[0] != i[-1]:
        dict1[i[0]] = i[-1]

    if i[-1].isalpha():
        for x in dict1.keys():
            if x == i[-1]:
                dict1[i[0]] = dict1[x]

    if i[-1].isdigit():
        for x, y in dict1.items():
            if y == i[0]:
                dict1[x] = i[-1]

for x, y in dict1.items():
    if y.isalpha():
        print(0, end=' ')
    else:
        print(y, end=' ')

