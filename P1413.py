n = int(input())
ground = [[] for _ in range(6)]
tmp = n
while tmp > 0:
    d, t = map(int, input().split())
    ground[d - 1].append(t)
    tmp -= 1

count = 0
for i in range(len(ground)):
    ground[i].sort()
    if ground[i]:
        count += 1

for item in ground:
    i = 0
    j = 1
    while i + j < len(item):
        if item[i + j] - item[i] >= 60:
            i = i + j
            j = 1
            count += 1
        elif item[i + j] - item[i] < 60:
            j += 1
print(count)