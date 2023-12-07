from collections import defaultdict
from sys import setrecursionlimit

setrecursionlimit(10000000)


def dfs(now):
    dp[now] = value[now]
    for item in tree[now]:
        dp[now] = max(dp[now], dp[now] + dfs(item))
    return dp[now]


n = int(input())
tree = defaultdict(list)
value = [0] + list(map(int, input().split()))
dp = [0] * (n + 1)
for _ in range(n - 1):
    t1, t2 = map(int, input().split())
    if t1 > t2:
        t1, t2 = t2, t1
    tree[t1].append(t2)

dfs(1)
# print(tree)
# print(dp)

print(max(dp))
