n, m = map(int, input().split())
w = [0] + list(map(int, input().split()))
t = m + 1
ans = 0
while True:
    for i in range(1, m + 1):
        if w[i] != 0:
            w[i] -= 1
        if w[i] == 0 and t <= n:
            w[i] = w[t]
            t += 1
    ans += 1
    if w[1:m + 1].count(0) == m:
        break

print(ans)