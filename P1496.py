n = int(input())
li = []
for _ in range(n):
    li.append(tuple(map(int, input().split())))
li.sort(key=lambda x: (x[0], x[1]))

start = li[0][0]
end = li[0][1]
ans = end - start
for i in range(1, n):
    if end >= li[i][0]:
        if end <= li[i][1]:
            ans += li[i][1] - end
            end = li[i][1]
    else:
        start = li[i][0]
        end = li[i][1]
        ans += end - start
print(ans)
