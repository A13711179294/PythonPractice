s = '0' + input()
l = len(s)
pre = [0] * (l + 1)
next = [0] * (l + 1)
index = [0] * 27


for i in range(1, l):
    pre[i] = index[ord(s[i]) - 97 + 1]
    index[ord(s[i]) - 97 + 1] = i

index = [l] * 27

for i in range(l - 1, 0, -1):
    next[i] = index[ord(s[i]) - 97 + 1]
    index[ord(s[i]) - 97 + 1] = i

ans = 0
for i in range(1, l):
    ans += (i - pre[i]) * (next[i] - i)

# print(pre)
# print(next)
print(ans)