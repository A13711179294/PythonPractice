a, b, c = map(int, input().split())

count1 = 3
time = [0] * 101

while count1 > 0:
    temp1, temp2 = map(int, input().split())
    for i in range(temp1, temp2):
        time[i] += 1
    count1 -= 1

print(time.count(1) * a + time.count(2) * b * 2 + time.count(3) * c * 3)
