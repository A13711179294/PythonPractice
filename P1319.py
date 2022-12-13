digital_list = list(map(int, input().split()))

length = digital_list.pop(0)
count1 = 0

i = 1
for x in digital_list:
    if i % 2 == 0:
        while x > 0:
            print('1', end='')
            count1 += 1
            if count1 == length:
                count1 = 0
                print()
            x -= 1
    else:
        while x > 0:
            print('0', end='')
            count1 += 1
            if count1 == length:
                count1 = 0
                print()
            x -= 1
    i += 1
