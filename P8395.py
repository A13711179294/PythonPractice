n = int(input().strip())

ans = 0
for i in range(0, n + 1):
    if (n - 5 * i) < 0:
        break
    if (n - 5 * i) % 4 == 0:
        ans += 1
print(ans)