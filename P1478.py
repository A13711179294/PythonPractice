n, s = map(int, input().split())
a, b = map(int, input().split())
tmp = n
appletree = []
while tmp > 0:
    appletree.append(tuple(map(int, input().split())))
    tmp -= 1
appletree.sort(key=lambda x: x[1])
count1 = 0
for i in appletree:
    if s < i[1]:
        break
    if i[0] <= a + b and s >= i[1]:
        count1 += 1
        s -= i[1]
print(count1)
