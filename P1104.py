n = int(input())
tmp = n
inf = []
index1 = 1
while tmp > 0:
    tmp1 = list(input().split())
    tmp1.append(index1)
    inf.append(tmp1)
    tmp -= 1
    index1 += 1
for i in range(n - 1):
    for j in range(n - i-1):
        if int(inf[j][1]) > int(inf[j + 1][1]):
            inf[j], inf[j + 1] = inf[j + 1], inf[j]

for i in range(n - 1):
    for j in range(n - i-1):
        if int(inf[j][2]) > int(inf[j + 1][2]) and inf[j][1] == inf[j+1][1]:
            inf[j], inf[j + 1] = inf[j + 1], inf[j]

for i in range(n - 1):
    for j in range(n - i-1):
        if int(inf[j][3]) > int(inf[j + 1][3]) and inf[j][1] == inf[j+1][1] and inf[j+1][2] == inf[j][2]:
            inf[j], inf[j + 1] = inf[j + 1], inf[j]

for i in range(n - 1):
    for j in range(n - i-1):
        if int(inf[j][4]) < int(inf[j + 1][4]) and inf[j][1] == inf[j+1][1] and inf[j+1][2] == inf[j][2] and inf[j+1][3] == inf[j][3]:
            inf[j], inf[j + 1] = inf[j + 1], inf[j]

for i in inf:
    print(i[0])