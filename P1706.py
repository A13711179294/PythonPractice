from itertools import permutations

n = int(input())
list1 = []
for i in range(1, n + 1):
    list1.append(i)
res = list(permutations(list1))
for i in res:
    for j in i:
        print('%5d' % j, end='')
    print()
