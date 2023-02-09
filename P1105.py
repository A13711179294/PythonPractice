N = int(input())
tmp = N
platform = [0]
while tmp > 0:
    platform.append(tuple(map(int, input().split())))
    tmp -= 1

for i in range(1, N + 1):
    l_ans = 0
    l_height = 0
    r_ans = 0
    r_height = 0
    for j in range(1, N + 1):
        if i != j and l_height < platform[j][0] < platform[i][0] and platform[j][1] < platform[i][1] < platform[j][2]:
            l_ans = j
            l_height = platform[j][0]
        if i != j and r_height < platform[j][0] < platform[i][0] and platform[j][2] > platform[i][2] > platform[j][1]:
            r_ans = j
            r_height = platform[j][0]
    print(l_ans, r_ans, sep=' ')
