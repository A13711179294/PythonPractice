n, m = map(int, input().split())
ni = []
for i in range(1, n + 1):
    ni.append(i)
left = 0
for i in range(n):
    print(ni.pop((left + m - 1) % n), end=' ')
    left = (left + m - 1) % n
    n -= 1
