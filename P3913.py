from sys import stdin

n, k = map(int, stdin.readline().split())
row = set()
col = set()
for _ in range(k):
    x, y = stdin.readline().split()
    row.add(x)
    col.add(y)
print((len(col) + len(row)) * n - len(col) * len(row))
