class Node:
    def __init__(self, name, c1, c2, c3):
        self.name = name
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.sum1 = c1 + c2 + c3


n = int(input().strip())
li = []
for _ in range(n):
    tmp = input().strip().split()
    li.append(Node(tmp[0], int(tmp[1]), int(tmp[2]), int(tmp[3])))

li.sort(key=lambda x: x.name)

for i in range(n - 1):
    for j in range(i + 1, n):
        if abs(li[i].c1 - li[j].c1) <= 5 and abs(li[i].c2 - li[j].c2) <= 5 and abs(li[i].c3 - li[j].c3) <= 5 and abs(
                li[i].sum1 - li[j].sum1) <= 10:
            print(li[i].name, li[j].name)
