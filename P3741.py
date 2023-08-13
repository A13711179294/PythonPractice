n = int(input())
s = list(input())

ans = 0
for i in range(n - 1):
    if s[i] == 'V' and s[i + 1] == 'K':
        s[i] = s[i + 1] = 'X'
        ans += 1

for i in range(n - 1):
    if s[i] == 'V' and s[i + 1] == 'V':
        ans += 1
        break
    elif s[i] == 'K' and s[i + 1] == 'K':
        ans += 1
        break

print(ans)