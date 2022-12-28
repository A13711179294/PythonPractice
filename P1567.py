N = int(input())
day_list = list(map(int, input().split()))
count = 1
continuous_day_list = []
for i in range(0, len(day_list) - 1):
    if day_list[i] < day_list[i + 1]:
        count += 1
    else:
        if count != 0:
            continuous_day_list.append(count)
        count = 1
continuous_day_list.append(count)
print(max(continuous_day_list))
