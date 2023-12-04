n = int(input())
b = []
a = [0] * n
for _ in range(n):
    b.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        a[i] |= b[i][j]

print(*a)