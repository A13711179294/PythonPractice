n, m = map(int, input().split())
w = list(map(int, input().split()))
c = list(map(int, input().split()))
w.sort()
c.sort()
print(c)
print(w)

i = 0
j = 0
ans = 0
while i < n and j < m:
    if w[i] >= c[j]:
        ans += 1
        i += 1
        j += 1
    elif w[i] < c[j]:
        i += 1
print(ans)