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
    global count1
    ans = 0
    for i in range(1, len(Node_list)):
        fx = find(Node_list[i].l)
        fy = find(Node_list[i].r)
        if fx != fy:
            count1 += 1
            pre[fx] = fy
            ans += Node_list[i].s
    return ans


N, M = map(int, input().split())
count1 = 0
pre = [i for i in range(N + 1)]
Node_list = [Node(0, 0, 0)]
for _ in range(M):
    x, y, z = map(int, input().split())
    Node_list.append(Node(x, y, z))

Node_list.sort(key=lambda k: k.s)
ret = kruskal()
if count1 != N - 1:
    print('orz')
else:
    print(ret)
