tmp = 1
people = []
while tmp <= 5:
    people.append(list(map(int, input().split())))
    tmp += 1

sum1 = 0
i1 = 1
i2 = 1
i3 = 1
i4 = 1
i5 = 1
while i1 + i2 + i3 + i4 + i5 < 25:
    tmp = min(people[0][i1]-people[0][i1-1], people[1][i2]-people[1][i2-1], people[2][i3]-people[2][i3-1], people[3][i4]-people[3][i4-1], people[4][i5]-people[4][i5-1])
    if tmp == people[0][i1]-people[0][i1-1]:
        i1 += 1
    elif tmp == people[1][i2]-people[1][i2-1]:
        i2 += 1
    elif tmp == people[2][i3]-people[2][i3-1]:
        i3 += 1
    elif tmp == people[3][i4]-people[3][i4-1]:
        i4 += 1
    elif tmp == people[4][i5]-people[4][i5-1]:
        i5 += 1
sum1 = people[0][i1-1] + people[1][i2-1] + people[2][i3-1] + people[3][i4-1] + people[4][i5-1]
print(sum1)
print(i1, i2, i3, i4, i5)
