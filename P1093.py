class Node:
    def __init__(self, s1, s2, s3, index1):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.sum1 = s1 + s2 + s3
        self.index1 = index1


n = int(input())
li = []
for i in range(1, n + 1):
    a, b, c = map(int, input().split())
    li.append(Node(a, b, c, i))

li.sort(key=lambda x: (x.sum1, x.s1, n - x.index1), reverse=True)

for i in range(5):
    print(li[i].index1, li[i].sum1)
