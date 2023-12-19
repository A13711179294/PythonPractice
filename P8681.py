n = int(input().strip())
a = list(map(int, input().strip().split()))
count1 = 1
count2 = 0
index = 0
max_sum = 0
ans1 = 1
ans2 = 1
tmp = 0

while True:
    if index == n:
        if tmp > max_sum:
            max_sum = tmp
            ans2 = ans1
        break
    if count2 < count1:
        tmp += a[index]
        count2 += 1
        index += 1
    else:
        if tmp > max_sum:
            max_sum = tmp
            ans2 = ans1
        ans1 += 1
        tmp = 0
        count1 *= 2
        count2 = 0

print(ans2)