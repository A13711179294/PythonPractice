from collections import deque


s = int(input())
queue = deque()

i = 1
for _ in range(1, s + 1):
    tmp = list(input().split())
    if tmp[0] == 'A':
        if tmp[1] == 'L':
            queue.appendleft(i)
            i += 1
        else:
            queue.append(i)
            i += 1
    else:
        if tmp[1] == 'L':
            for _ in range(int(tmp[2])):
                queue.popleft()
        else:
            for _ in range(int(tmp[2])):
                queue.pop()

for k in queue:
    print(k)