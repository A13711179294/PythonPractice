n, m = map(int, input().split())
graph = [0]
w = [0] * (n + 1)
b = [0] * (n + 1)
r = [0] * (n + 1)

for i in range(1, n + 1):
    tmp = list(input())
    graph.append(tmp)
    w[i] = w[i - 1] + m - tmp.count('W')
    b[i] = b[i - 1] + m - tmp.count('B')
    r[i] = r[i - 1] + m - tmp.count('R')

ans = float('inf')
for i in range(1, n - 1):
    for j in range(i + 1, n):
        ans = min(ans, w[i] + b[j] - b[i] + r[n] - r[j])

print(ans)
