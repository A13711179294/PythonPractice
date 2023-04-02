from sys import setrecursionlimit

setrecursionlimit(1000000)
def dfs(x):
    for j in range(64, 125):
        if graph[x][j]:
            graph[x][j] = graph[j][x] = 0
            dfs(j)
    ans.append(chr(x))

def find(x):
    if pre[x] == x:
        return x
    pre[x] = find(pre[x])
    return pre[x]

def join(x, y):
    fx = find(x)
    fy = find(y)
    if fx != fy:
        pre[fx] = fy

n = int(input().strip())
graph = [[0 for _ in range(125)] for _ in range(125)]
ans = []
pre = [i for i in range(125)]
depth = [0] * 125

for _ in range(n):
    tmp = list(input().strip())
    graph[ord(tmp[0])][ord(tmp[1])] = 1
    graph[ord(tmp[1])][ord(tmp[0])] = 1
    join(ord(tmp[0]), ord(tmp[1]))
    depth[ord(tmp[0])] += 1
    depth[ord(tmp[1])] += 1

cnt = 0
for i in range(64, 125):
    if depth[i] and pre[i] == i:
        cnt += 1

if cnt != 1:
    print('No Solution')
    exit(0)

cnt = 0
head = 0
for i in range(64, 125):
    if depth[i] & 1:
        cnt += 1
        if not head:
            head = i

if cnt and cnt != 2:
    print('No Solution')
    exit(0)

if not head:
    for i in range(64, 125):
        if depth[i]:
            head = i
            break

dfs(head)
print(''.join(ans[::-1]))