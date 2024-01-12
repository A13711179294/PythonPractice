ans = 0
n = 5
while n > 0:
    year = input()
    if year[0] == year[2] and int(year[1]) + 1 == int(year[3]):
        ans += 1
    n -= 1

print(ans)
