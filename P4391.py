l = int(input())
s = ' ' + input()
kmp = [0] * (l + 1)

j = 0
for i in range(2, l + 1):
    while j and s[j + 1] != s[i]:
        j = kmp[j]
    if s[j + 1] == s[i]:
        j += 1
    kmp[i] = j

print(l - kmp[l])