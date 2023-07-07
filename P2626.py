def func(x):
    t1 = 0
    t2 = 1
    for i in range(2, N + 1):
        t1, t2 = t2, t1 + t2
    return t2


N = int(input())
ret = func(N)
ret %= 2 ** 31
n = ret
p = [0] * 1000
g = [0] * 1000
cnt = 0
i = 2
while i * i <= n:
    if n % i == 0:
        cnt += 1
    while n % i == 0:
        p[cnt] = i
        g[cnt] += 1
        n //= i
    i += 1

if n > 1:
    cnt += 1
    p[cnt] = n
    g[cnt] += 1

# print(p)
# print(g)

ans = str(ret) + '='
for k in range(1, cnt + 1):
    for v in range(g[k]):
        ans += str(p[k]) + '*'

print(ans.rstrip('*'))

