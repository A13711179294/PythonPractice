from collections import deque


n = int(input())
q = deque()
a = [0] + list(map(int, input().split()))

for i in range(1, (2 << (n - 1)) + 1):
    q.append((a[i], i))

while len(q) > 2:
    t1 = q.popleft()
    t2 = q.popleft()
    if t1[0] > t2[0]:
        q.append(t1)
    else:
        q.append(t2)

b1 = q.popleft()
b2 = q.popleft()
if b1[0] < b2[0]:
    print(b1[1])
else:
    print(b2[1])