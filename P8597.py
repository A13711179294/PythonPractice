s1 = list(input().strip())
s2 = list(input().strip())
ans = 0
for i in range(len(s1)):
    if s1[i] != s2[i]:
        ans += 1
        if s1[i + 1] == 'o':
            s1[i + 1] = '*'
        else:
            s1[i + 1] = 'o'
print(ans)