k = int(input())
size = 1
c = 0
while size < k:
    size *= 2
if size == k:
    print(k, c)
else:
    print(size, end=' ')
    while k > 0:
        size //= 2
        k %= size
        c += 1
    print(c)
