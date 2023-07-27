N = int(input())
a = []
tmp = N
while tmp > 0:
    a.append(int(input()))
    tmp -= 1

ans = a[0]
for i in range(N - 1):
    if a[i] < a[i + 1]:
        ans += a[i + 1] - a[i]
print(ans)