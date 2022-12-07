n_list = list(map(int, input().split()))
n_length = len(n_list) - 1

sub_list = []
flag = 0

for i in range(1, n_length):
    temp = abs(n_list[i] - n_list[i + 1])
    sub_list.append(temp)

for i in range(1, n_length):
    if i not in sub_list:
        flag = 1

if flag == 1:
    print('Not jolly')
else:
    print('Jolly')
