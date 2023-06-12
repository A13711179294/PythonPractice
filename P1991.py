from math import sqrt


class Node:
    def __init__(self, l, r, w):
        self.l = l
        self.r = r
        self.w = w


def find(x):
    if pre[x] == x:
        return x
    pre[x] = find(pre[x])
    return pre[x]


def kruskal():
    count1 = 0
    ans = 0
    for i in range(0, len(Node_list) - 1):
        fx = find(Node_list[i].l)
        fy = find(Node_list[i].r)
        if fx != fy:
            pre[fx] = fy
            count1 += 1
        if count1 == p - s:
            ans = Node_list[i].w
            break
    return ans


s, p = map(int, input().split())
pre = [i for i in range(p + 1)]
Node_list = [Node(0, 0, 0)]
station = [0]

for _ in range(p):
    station.append(tuple(map(int, input().split())))

for i in range(1, p + 1):
    for j in range(i + 1, p + 1):
        Node_list.append(
            Node(i, j, (sqrt(pow(station[i][0] - station[j][0], 2) + pow(station[i][1] - station[j][1], 2)))))

Node_list.sort(key=lambda k: k.w)
print('%.2f' % kruskal())
