n = int(input())
count1 = 1
for i in range(n):
    for j in range(n - i):
        print('{:0>2d}'.format(count1), end='')
        count1 += 1
    print()
