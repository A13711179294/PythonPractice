class Node:
    def __init__(self, x, y, s):
        self.x = x
        self.y = y
        self.s = s


def find(x):
    if pre[x] == x:
        return x
    pre[x] = find(pre[x])
    return pre[x]


def kruskal():
    global count1
    ans = 0
    for i in range(1, n - num + 1):
        t1 = find(Node_list[i].x)
        t2 = find(Node_list[i].y)
        if t1 != t2:
            count1 += 1
            pre[t1] = t2
            ans += Node_list[i].s
    return ans


a, b = map(int, input().split())
pre = [k for k in range(b + 1)]
Node_list = [Node(0, 0, 0)]
count1 = 0
num = 0
n = 0
for i in range(1, b + 1):
    tmp = [0] + list(map(int, input().split()))
    for j in range(1, len(tmp)):
        if i >= j or tmp[j] == 0:
            continue
        Node_list.append(Node(i, j, tmp[j]))
        n += 1
        if tmp[j] > a:
            num += 1

Node_list.sort(key=lambda x: x.s)

ret = kruskal()
if count1 == b - 1:
    print(a + ret)
else:
    print((b - count1) * a + ret)

