K = int(input())
flag = 0
for i in range(10000, 30001):
    temp_str = str(i)
    sub1 = int(temp_str[0] + temp_str[1] + temp_str[2])
    sub2 = int(temp_str[1] + temp_str[2] + temp_str[3])
    sub3 = int(temp_str[2] + temp_str[3] + temp_str[4])
    if sub1 % K == sub2 % K == sub3 % K == 0:
        flag = 1
        print(i)
if flag == 0:
    print('No')
