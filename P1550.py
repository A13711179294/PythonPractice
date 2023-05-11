class Node:
    def __init__(self, start, end, length):
        self.start = start
        self.end = end
        self.length = length


def find(x):
    if pre[x] == x:
        return x
    pre[x] = find(pre[x])
    return pre[x]


def kruskal():
    cnt = 0
    li.sort(key=lambda x: x.length)
    for i in range(1, len(li)):
        t1 = find(li[i].start)
        t2 = find(li[i].end)
        if t1 == t2:
            continue
        pre[t1] = t2
        cnt += li[i].length
    return cnt


n = int(input())
pre = [i for i in range(n + 2)]
w = [0]
for _ in range(n):
    w.append(int(input()))

val = [[0] * (n + 1)]
for _ in range(n):
    val.append([0] + list(map(int, input().split())))

li = [Node(0, 0, 0)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i != j:
            li.append(Node(i, j, val[i][j]))
            li.append(Node(j, i, val[i][j]))

for i in range(1, n + 1):
    li.append(Node(i, n + 1, w[i]))
    li.append(Node(n + 1, i, w[i]))

ret = kruskal()
print(ret)
