k = int(input())
a1 = 1
a2 = 1
sn = 0
while sn <= k:
    sn += a1 / a2
    a2 += 1
print(a2 - 1)
