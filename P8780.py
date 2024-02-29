a, b, n = map(int, input().split())
ans = 0
count = 0
day = 1
while count < n:
    if day == 8:
        day = 1
    if day != 6 and day != 7:
        count += a
        day += 1
        ans += 1
    else:
        count += b
        day += 1
        ans += 1
print(ans)
