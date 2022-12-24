n = int(input())
list1 = list(map(int, input().split()))
cute_list = [0]
count = 0
for x in range(1, len(list1)):
    for y in range(0, x):
        if list1[x] > list1[y]:
            count += 1
    cute_list.append(count)
    count = 0
for i in cute_list:
    print(i, end=' ')