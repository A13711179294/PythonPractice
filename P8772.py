n = int(input())
a = list(map(int, input().split()))
ans = 0
sum = 0
for i in range(1, n):
    sum += a[i - 1]
    ans += sum * a[i]

print(ans)