n, m, k = map(int, input().split())
count = list(map(int, input().split()))
tmp = n
food = []

while tmp > 0:
    food.append(tuple(map(int, input().split())))
    tmp -= 1
food.sort(key=lambda x: x[0], reverse=True)

sum1 = 0
for i in food:
    if count[i[1] - 1] > 0 and m > 0:
        sum1 += i[0]
        count[i[1] - 1] -= 1
        m -= 1
print(sum1)
