N = int(input())
std = list(map(int, input().split()))
down, up = map(int, input().split())

sum1 = sum(std)
sum2 = 0
sum3 = 0

for i in std:
    if i > up:
        sum2 += i - up
    if i < down:
        sum3 += down - i

if up * N >= sum1 >= down * N and sum2 >= sum3:
    print(sum2)
elif up * N >= sum1 >= down * N and sum2 < sum3:
    print(sum3)
else:
    print(-1)

