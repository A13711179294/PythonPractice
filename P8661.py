from collections import deque

q = deque()
n, d, k = map(int, input().strip().split())

a = [(0, 0)]
cnt = [0] * 100001
ans = [False] * 100001
for _ in range(n):
    a.append(tuple(map(int, input().strip().split())))

a.sort(key=lambda x: x[0])

for i in range(1, n + 1):

    while q and a[q[0]][0] + d <= a[i][0]:
        cnt[a[q[0]][1]] -= 1
        q.popleft()

    q.append(i)
    cnt[a[i][1]] += 1

    if cnt[a[i][1]] >= k:
        ans[a[i][1]] = True

for i in range(0, 100001):
    if ans[i]:
        print(i)
