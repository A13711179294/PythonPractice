s1 = list(input().strip())
s2 = list(input().strip())
s1 += ' '
s2 += ' '

ans = 0
for i in range(len(s1) - 1):
    for j in range(1, len(s2) - 1):
        if s1[i] == s2[j] and s1[i + 1] == s2[j - 1]:
            ans += 1

print(pow(2, ans))
