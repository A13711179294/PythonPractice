n = int(input())
ans = 0
for i in range(1, n):
    if i * i % n < n / 2:
        ans += 1
print(ans)