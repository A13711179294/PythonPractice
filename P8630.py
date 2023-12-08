s = list(input().strip())
n = int(input().strip())
password = []
tmp = 0
while tmp < n:
    a = list(input().strip())
    a.sort()
    password.append(a)
    tmp += 1

ans = 0
for i in range(0, len(s) - 7):
    tmp = s[i: i + 8]
    tmp.sort()
    for j in range(0, n):
        if tmp == password[j]:
            ans += 1

print(ans)
