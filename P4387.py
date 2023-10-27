q = int(input())
for _ in range(q):
    stack = []
    l = int(input())
    pushed = [0] + list(map(int, input().split()))
    poped = [0] + list(map(int, input().split()))
    i = 1
    head = 1
    flag = 1
    while True:
        stack.append(pushed[i])
        while stack and stack[-1] == poped[head]:
            stack.pop()
            head += 1
        i += 1
        if i == l + 1:
            if head != l + 1:
                flag = 0
            break

    if flag:
        print('Yes')
    else:
        print('No')
