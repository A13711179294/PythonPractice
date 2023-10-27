N = int(input())
tmp = N
count1 = 1
pre_people = 0
while tmp > 0:
    people = input()
    if pre_people != people:
        pre_people = people
        count1 += 1
    tmp -= 1

print(count1)
