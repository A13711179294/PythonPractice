N = int(input())
Maxnumber = list(map(int, input().split()))
Maxnumber.sort()
tmp = 1
sum1 = 1
for i in range(N):
    sum1 *= Maxnumber[i] - i
print(sum1 % 1000000007)