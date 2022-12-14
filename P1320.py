N_list = list(input().strip())
count = 1
temp = len(N_list)
while count < temp:
    N_list.extend(list(input().strip()))
    count += 1

sum0 = 0
sum1 = 0
flag = 1
count_list = [temp]

for i in N_list:
    if i == '0':
        sum0 += 1
        flag = 0
        if sum1 != 0:
            count_list.append(sum1)
            sum1 = 0
    else:
        if flag == 1:
            count_list.append(0)
        flag = 0
        sum1 += 1
        if sum0 != 0:
            count_list.append(sum0)
            sum0 = 0

if sum0 != 0:
    count_list.append(sum0)
if sum1 != 0:
    count_list.append(sum1)
for i in count_list:
    print(i, end=" ")
