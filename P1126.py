a, b, p = map(int, input().split())
b1 = str(bin(b).lstrip('0b'))
ans = 1
base = a
for i in b1[::-1]:
    if i == '1':
        ans = ans * base % p
    base = base * base % p
print('%d^%d mod %d=%d' % (a, b, p, ans))
