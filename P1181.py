n, m = map(int, input().split())
a = list(map(int, input().split()))
sum1 = 0
ans = 1
for i in range(n):
    if sum1 + a[i] > m:
        sum1 = 0
        ans += 1
    sum1 += a[i]

print(ans)