s1 = int(input())
s2 = int(input())
d = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
ans = 0
for i in range(1, 13):
    for j in range(1, d[i] + 1):
        c = (j % 10) * 1000 + (j // 10) * 100 + (i % 10) * 10 + (i // 10)
        sum1 = c * 10000 + i * 100 + j
        if s1 <= sum1 <= s2:
            ans += 1
print(ans)
