from collections import defaultdict
from sys import setrecursionlimit

setrecursionlimit(10000000)


def dfs(x):
    for i in edge[x]:
        dfs(i)
        dp[x] = max(dp[x], dp[i])
    dp[x] += len(edge[x])


n = int(input())
edge = defaultdict(list)
dp = [0 for _ in range(n + 1)]

for i in range(2, n + 1):
    edge[int(input())].append(i)

print(edge)
dfs(1)
print(dp[1])