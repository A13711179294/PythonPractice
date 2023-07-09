x, y = map(int, input().split())
ans = 0
while x:
    ans += 4 * x * (y // x)
    x, y = y % x, x

print(ans)