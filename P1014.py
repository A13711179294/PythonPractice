N = int(input())

count1 = 0
count2 = 1
result = 0
flag = 0

while True:
    for i in range(1, count2 + 1):
        if count2 % 2 == 0:
            tmp = str(i)+'/'+str(count2 - i + 1)
            count1 += 1
            if N == count1:
                result = tmp
                flag = 1
                break
        else:
            tmp = str(count2 - i + 1) + '/' + str(i)
            count1 += 1
            if N == count1:
                result = tmp
                flag = 1
                break
    if flag == 1:
        break
    count2 += 1
print(result)
