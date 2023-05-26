n = int(input())
maxx = float('inf')
minn = 0
for _ in range(n):
    a, b = map(int, input().split())
    maxx = min(a//b, maxx)
    minn = max(minn, a//(b + 1) + 1)

print(minn, maxx)