n = int(input())
tmp = n
time = []
while tmp > 0:
    time.append(tuple(map(int, input().split())))
    tmp -= 1
time.sort(key=lambda x: x[0])
start = time[0][0]
end = time[0][1]
least_one = [end - start]
no_one = [0]
for i in time[1::]:

    if i[0] <= end:
        if i[1] <= end:
            least_one.append(i[1] - start)
        else:
            least_one.append(i[1] - start)
            end = i[1]
    elif i[0] > end:
        no_one.append(i[0] - end)
        start = i[0]
        end = i[1]

print(max(least_one), max(no_one), sep=' ')
