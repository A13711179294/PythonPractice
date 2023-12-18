n = int(input())
li = ['2','0','1','9']
ans = 0
for i in range(1, n + 1):
    for j in str(i):
        if j in li:
            ans += i
            break
print(ans)