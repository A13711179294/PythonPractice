n = int(input().strip())
time = []
tmp = n
while tmp > 0:
    t = tuple(map(int, input().strip().split()))
    time.append(t)
    tmp -= 1
time.sort(key=lambda x: x[1])

start = 0
end = 0
count = 0
for i in range(0, n):
    if time[i][0] >= end:
        start = time[i][0]
        end = time[i][1]
        count += 1
print(count)
