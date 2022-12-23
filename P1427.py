list1 = list(map(int, input().split()))
for i in list1[-2:0:-1]:
    print(i, end=' ')
print(list1[0])