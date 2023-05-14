n = int(input())
tmp1 = n
person = []
index1 = 1
while tmp1 > 0:
    tmp2 = (index1, int(input()))
    person.append(tmp2)
    tmp1 -= 1
    index1 += 1

ret = max(person, key=lambda x: x[1])
for i in ret:
    print(i)