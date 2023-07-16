from math import sqrt
import heapq


def find(x):
    if pre[x] == x:
        return x
    pre[x] = find(pre[x])
    return pre[x]


def kruskal():
    ans = 0
    c = 0
    while True:
        if c == n - 1:
            return ans
        cur = heapq.heappop(Node_list)
        fx = find(cur[1])
        fy = find(cur[2])
        if fx != fy:
            pre[fx] = fy
            ans += cur[0]
            c += 1


n, m = map(int, input().split())
pre = [i for i in range(n + 1)]
Node_list = []
li = [(0, 0)]
for _ in range(n):
    li.append(tuple(map(int, input().split())))

for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        heapq.heappush(Node_list, (sqrt(pow(li[i][0] - li[j][0], 2) + pow(li[i][1] - li[j][1], 2)), i, j))

for k in range(1, m + 1):
    a, b = map(int, input().split())
    heapq.heappush(Node_list, (0, a, b))

print('%.2f' % kruskal())
