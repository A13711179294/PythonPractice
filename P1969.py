N = int(input())
a = list(map(int, input().split()))
ans = a[0]
for i in range(N - 1):
    if a[i] < a[i + 1]:
        ans += a[i + 1] - a[i]
print(ans)
