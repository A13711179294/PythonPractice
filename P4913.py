from sys import setrecursionlimit

setrecursionlimit(100000)


class Node:
    def __init__(self, left, right):
        self.left = left
        self.right = right


def dfs(cur, deep):
    global ans
    if not cur:
        return
    ans = max(ans, deep)
    dfs(tree[cur].left, deep + 1)
    dfs(tree[cur].right, deep + 1)


n = int(input())
tree = [Node(0, 0)]
for i in range(1, n + 1):
    l, r = map(int, input().split())
    tree.append(Node(l, r))

ans = 0
dfs(1, 1)
print(ans)
