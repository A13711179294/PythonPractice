from collections import deque


class node:
    def __init__(self, s, t):
        self.s = s
        self.t = t


n = int(input())
nation = [0] * 100001
q = deque()
ans = 0
for _ in range(n):
    tmp = list(map(int, input().split()))
    while q:
        h = q[0]
        if h.t + 86400 <= tmp[0]:
            nation[h.s] -= 1
            if nation[h.s] == 0:
                ans -= 1
            q.popleft()
            continue
        break

    for x in tmp[2:]:
        q.append(node(x, tmp[0]))
        nation[x] += 1
        if nation[x] == 1:
            ans += 1

    print(ans)
