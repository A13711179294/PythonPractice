n = int(input().strip())
sum1 = sum(list(map(int, input().split())))
if sum1 % 2 == 0:
    print('Bob')
else:
    print('Alice')