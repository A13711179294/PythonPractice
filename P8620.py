from math import factorial
s = list(input().strip())
l = len(s)

ans = 0
i = 0
while True:
    cur = s[i]
    a = 0
    for j in range(i + 1, l):
        if s[j] < cur:
            a += 1
    ans += a * factorial(l - i - 1)

    i += 1
    if i == l:
        break

print(ans)