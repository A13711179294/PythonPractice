n = int(input())
temp = n
ground = [[] for _ in range(n)]
while temp > 0:
    a, b, x_len, y_len = map(int, input().strip().split())
    ground[temp - 1].extend([a, b, a + x_len, b + y_len])
    temp -= 1
x, y = map(int, input().strip().split())

flag = 0
for i in range(n):
    if ground[i][0] <= x <= ground[i][2] and ground[i][1] <= y <= ground[i][3]:
        flag = 1
        print(n - i)
        break
if flag == 0:
    print(-1)
