from collections import deque

n, k = map(int, input().split())
vis = [0] * (n + 1)
cnt = [0] * (n + 1)
q = deque()

vis[0] = 1
q.append(0)
ans = 0
while q:
    cur = q.popleft()
    t1 = (cur + 1) % n
    t2 = (cur + k) % n
    ans = max(ans, cnt[cur])
    if not vis[t1]:
        vis[t1] = 1
        cnt[t1] = cnt[cur] + 1
        q.append(t1)

    if not vis[t2]:
        vis[t2] = 1
        cnt[t2] = cnt[cur] + 1
        q.append(t2)

print(ans)