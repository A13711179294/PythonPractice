n = int(input())
a = [0] + list(map(int, input().split())) + [0]
l = [0] * (n + 2)
r = [0] * (n + 2)

for i in range(1, n + 1):
    l[i] = max(l[i - 1], a[i])

for i in range(n, 0, -1):
    r[i] = max(r[i + 1], a[i])

sum1 = 0
for i in range(1, n + 1):
    if min(l[i], r[i]) - a[i] > 0:
       sum1 += min(l[i], r[i]) - a[i]

# print(a)
# print(l)
# print(r)
print(sum1)