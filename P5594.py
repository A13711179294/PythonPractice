n, m, k = map(int, input().split())
tmp = 0
a = [[0 for j in range(k)] for i in range(n)]

while tmp < n:
    b = list(map(int, input().split()))
    count1 = 1
    for i in b:
        a[tmp][i - 1] = count1
        count1 += 1
    tmp += 1

d = []
for i in range(k):
    c = []
    for j in range(n):
        if a[j][i] != 0:
            c.append(a[j][i])
    d.append(len(set(c)))

for i in d:
    print(i, end=' ')
