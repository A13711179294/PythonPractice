n = int(input())
count1 = 1
for i in range(n):
    for j in range(n):
        print('{:0>2d}'.format(count1), end='')
        count1 += 1
    print()
print()
count1 = 1
for i in range(n):
    for j in range(n - i - 1):
        print('  '.format(count1), end='')
    for j in range(i + 1):
        print('{:0>2d}'.format(count1), end='')
        count1 += 1
    print()
