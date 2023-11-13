queue = [0 for _ in range(10001)]
head = tail = 0

n = int(input())
for _ in range(n):
    tmp = list(map(int, input().split()))
    if len(tmp) == 2:
        queue[tail] = tmp[1]
        tail += 1
    else:
        if tmp[0] == 2:
            if tail == head:
                print('ERR_CANNOT_POP')
            else:
                head += 1
        elif tmp[0] == 3:
            if tail == head:
                print('ERR_CANNOT_QUERY')
            else:
                print(queue[head])
        else:
            print(tail - head)

