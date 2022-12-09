from functools import reduce

plants = list(input())
team = list(input())

plants = list(map(ord, plants))
team = list(map(ord, team))

new_plants = []
new_team = []

for i in plants:
    i -= 64
    new_plants.append(i)

for i in team:
    i -= 64
    new_team.append(i)


p_sum = reduce(lambda x, y: x * y, new_plants)
t_sum = reduce(lambda x, y: x * y, new_team)

if p_sum % 47 == t_sum % 47:
    print('GO')
else:
    print('STAY')
