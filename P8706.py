n = list(input())
ans = ''
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
for i in range(len(n)):
    if n[i].isdigit():
        ans += n[i - 1] * (int(n[i]) - 1)
    elif n[i] not in num:
        ans += n[i]
print(ans)
