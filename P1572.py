from math import gcd

n = input()
nums = list(n.replace('-', ' ').replace('+', ' ').split())
for i in range(len(nums)):
    nums[i] = tuple(nums[i].split('/'))
symbol = []
for i in n:
    if i == '+' or i == '-':
        symbol.append(i)

flag = 0
if len(symbol) == len(nums):
    flag = 1
tmp = list(nums[0])

if flag == 1:
    t = 1
    tmp[0][0] *= -1
else:
    t = 0

for i in range(1, len(nums)):
    if symbol[t] == '+':
        tmp[0] = int(tmp[0]) * int(nums[i][1]) + int(nums[i][0]) * int(tmp[1])
        tmp[1] = int(tmp[1]) * int(nums[i][1])
    elif symbol[t] == '-':
        tmp[0] = int(tmp[0]) * int(nums[i][1]) - int(nums[i][0]) * int(tmp[1])
        tmp[1] = int(tmp[1]) * int(nums[i][1])
    t += 1

if tmp[0] == tmp[1]:
    print(1)
elif tmp[0] == -tmp[1]:
    print(-1)
elif tmp[0] == 0:
    print(0)
else:
    g = gcd(tmp[0], tmp[1])
    if tmp[1]//g == 1:
        print(tmp[0] // g)
    else:
        print(tmp[0] // g, '/', tmp[1] // g, sep='')
