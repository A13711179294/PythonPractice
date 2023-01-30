player1 = {}
n, m = map(int, input().strip().split())
tmp = n

while tmp > 0:
    Id, score = map(int, input().strip().split())
    player1[Id] = score
    tmp -= 1

player = sorted(player1.items(), key=lambda x: x[0], reverse=True)
player = sorted(player, key=lambda x: x[1])
tmp = n - int(m * 1.5)
line = player[tmp][1]

count1 = 0
list1 = []

for i in player[::-1]:
    if i[1] >= line:
        list1.append(i)
        count1 += 1

print(line, count1)
for i in list1:
    print(i[0], i[1])
