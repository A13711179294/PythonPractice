tree_list = map(int, input().split())
hand = int(input())
count = 0
for i in tree_list:
    if hand + 30 >= i:
        count += 1
print(count)
