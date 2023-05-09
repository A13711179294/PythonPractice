from collections import deque

m, n = map(int, input().split())
a = list(map(int, input().split()))
q = deque()

ans = 0
for x in a:
    if x not in q:
        if len(q) >= m:
            q.popleft()
        q.append(x)
        ans += 1

print(ans)