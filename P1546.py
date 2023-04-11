N = int(input().strip())
tmp = N
distance = [[] for _ in range(N)]
r = 0
c = 0
while len(distance[N - 1]) != N:
    for i in list(map(int, input().strip().split())):
        if c < N:
            distance[r].append(i)
            c += 1
        if c == N:
            c = 0
            r += 1

visit = [0 for _ in range(N)]
visit[0] = 1
ans = 0
tmp = 0
count1 = 1

while True:
    min_dis = 99999

    for i in range(N):
        if visit[i] == 1:
            for j in range(N):
                if distance[i][j] < min_dis and distance[i][j] != 0 and visit[j] != 1:
                    min_dis = distance[i][j]
                    tmp = j
        else:
            continue
    count1 += 1
    ans += min_dis
    visit[tmp] = 1

    if count1 == N:
        break

print(ans)
