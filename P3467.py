from collections import deque

n = int(input())
q = deque()
ans = n
for _ in range(n):
    w, h = map(int, input().split())
    while q and q[0] >= h:
        if q[0] == h:
            ans -= 1
        q.popleft()
    q.appendleft(h)

print(ans)
