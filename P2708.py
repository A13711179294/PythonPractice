s = input().strip()
m = len(s)
k = m - 1
for i in range(1, m):
    if s[i] == s[i - 1]:
        k -= 1

if s[-1] == '0':
    k += 1

print(k)
