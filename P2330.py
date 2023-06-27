class Node:
    def __init__(self, l, r, s):
        self.l = l
        self.r = r
        self.s = s


def find(x):
    if pre[x] == x:
        return x
    pre[x] = find(pre[x])
    return pre[x]


def kruskal():
    count1 = 0
    for i in range(1, len(Node_list)):
        fx = find(Node_list[i].l)
        fy = find(Node_list[i].r)
        if fx != fy:
            pre[fx] = fy
            count1 += 1
        if count1 == n - 1:
            return Node_list[i].s


n, m = map(int, input().split())
pre = [i for i in range(n + 1)]
Node_list = [Node(0, 0, 0)]
for _ in range(m):
    u, v, w = map(int, input().split())
    Node_list.append(Node(u, v, w))

Node_list.sort(key=lambda k: k.s)
print(n - 1, kruskal())
