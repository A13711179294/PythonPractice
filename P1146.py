N = int(input())
coin_list = N * ['0']

print(N)
for x in range(0, N):
    for y in range(0, N):
        if x != y:
            if coin_list[y] == '0':
                coin_list[y] = '1'
            else:
                coin_list[y] = '0'
    print(''.join(coin_list))