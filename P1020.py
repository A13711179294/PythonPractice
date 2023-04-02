import bisect

a = list(map(int, input().split()))

b = [-a[0]]
j = 0
for i in range(1, len(a)):
    if b[j] <= -a[i]:
        b.append(-a[i])
        j += 1
    else:
        ind = bisect.bisect_right(b, -a[i])
        b[ind] = -a[i]

print(len(b))

c = [a[0]]
j = 0
for i in range(1, len(a)):
    if a[i] > c[j]:
        c.append(a[i])
        j += 1
    else:
        ind = bisect.bisect_left(c, a[i])
        c[ind] = a[i]

print(len(c))
