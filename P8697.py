S = input().strip()
T = input().strip()
ans = 0
j = 0
for i in range(len(S)):
    if j >= len(T):
        break
    if S[i] == T[j]:
        j += 1
        ans += 1
print(ans)
