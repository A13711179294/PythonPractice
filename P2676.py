n, b = map(int, input().split())
a = []
for _ in range(n):
    a.append(int(input()))

a.sort(reverse=True)
ans = 0
sum1 = 0
# rint(a)
for i in range(n):
    if sum1 + a[i] < b:
        sum1 += a[i]
        ans += 1
    else:
        ans += 1
        break

print(ans)
