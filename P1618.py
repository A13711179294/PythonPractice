A, B, C = map(int, input().split())
flag = 0
for i in range(1, 333):
    j = str(B * i)
    k = str(C * i)
    i = str(A * i)
    if '0' not in i and '0' not in j and '0' not in k and len(j) == len(k) == len(i) == 3:
        a = {i[0], i[1], i[2], j[0], j[1], j[2], k[0], k[1], k[2]}
        if len(a) == 9:
            print(int(i), int(j), int(k))
            flag = 1
if flag == 0:
    print('No!!!')
