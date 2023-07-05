from math import sqrt
import heapq

def find(x):
    if pre[x] == x:
        return x
    pre[x] = find(pre[x])
    return pre[x]


def kruskal():
    count1 = 0
    cnt = 0
    while count1 < n - 1:
        cur = heapq.heappop(Node_list)
        fx = find(cur[1])
        fy = find(cur[2])
        if fx != fy:
            pre[fx] = fy
            count1 += 1
            cnt = max(cnt, cur[0])
    return cnt


M = int(input())
monkey = list(map(int, input().split()))
n = int(input())
pre = [i for i in range(n + 1)]
Node_list = []
li = [(0, 0)]
for _ in range(n):
    li.append(tuple(map(int, input().split())))

for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        heapq.heappush(Node_list, (sqrt(pow(li[i][0] - li[j][0], 2) + pow(li[i][1] - li[j][1], 2)), i, j))

ret = kruskal()
ans = 0
for k in range(M):
    if ret <= monkey[k]:
        ans += 1
print(ans)
