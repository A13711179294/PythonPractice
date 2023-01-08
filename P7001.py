str1 = input()
n = int(input())

string_list = []
tmp = n
while tmp > 0:
    temp = input()
    string_list.append(temp)
    tmp -= 1

right = []
count2 = 0

for i in range(n):
    count1 = 0
    for j in range(len(str1)):
        if string_list[i][j] == str1[j] or str1[j] == '*':
            count1 += 1
    if count1 == len(str1):
        right.append(string_list[i])
        count2 += 1

print(count2)
for i in range(count2):
    print(right[i])