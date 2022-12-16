n = int(input())
a_list = list(map(int, input().split()))
count_list = [0]
list_len = len(a_list)

count = 0

for i in range(0, len(a_list) - 1):
    if a_list[i]+1 == a_list[i+1]:
        count += 1
        count_list.append(count)
    else:
        count = 0

print(max(count_list)+1)
