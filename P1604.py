dic = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
B = int(input().strip())
a = list(input().strip())
b = list(input().strip())
a.reverse()
b.reverse()

la = len(a)
lb = len(b)

if la > lb:
    for _ in range(la - lb):
        b.append('0')
        lb = la
elif la < lb:
    for _ in range(lb - la):
        a.append('0')
        la = lb

i = 0
tmp2 = 0
c = []
while i < la:
    tmp1 = dic.index(a[i]) + dic.index(b[i]) + tmp2
    if tmp1 >= B:
        c.append(dic[tmp1 % B])
        tmp2 = tmp1 // B
    else:
        c.append(dic[tmp1])
        tmp2 = 0
    i += 1

if tmp2 != 0:
    c.append(dic[tmp2])
c.reverse()
print(*c, sep='')
