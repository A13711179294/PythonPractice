n = int(input())
a = list(map(int, input().split()))
sum1 = 0
for i in range(1, n):
    sum1 += max(a[i-1], a[i])
print(sum1)
