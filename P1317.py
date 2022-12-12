n = int(input())
mountain_list = list(map(int, input().split()))

i = 0
while i <= len(mountain_list) - 2:
    while mountain_list[i] == mountain_list[i + 1]:
        mountain_list.pop(i + 1)
    i += 1

count = 0
mountain_length = len(mountain_list)
for i in range(1, mountain_length - 1):
    if mountain_list[i] < mountain_list[i-1] and mountain_list[i] < mountain_list[i+1]:
        count += 1
print(count)
