from sys import setrecursionlimit

setrecursionlimit(10000000)


def get_prime(n):
    global cnt
    is_prime[1] = False
    for i in range(1, n + 1):
        if is_prime[i]:
            cnt += 1
            Prime[cnt] = i
        j = 1
        while j <= cnt and i * Prime[j] <= n:
            is_prime[i * Prime[j]] = False
            if i % Prime[j] == 0:
                break
            j += 1


def find(x):
    if pre[x] != x:
        pre[x] = find(pre[x])
    return pre[x]


def join(x, y):
    fx = find(x)
    fy = find(y)
    if fx != fy:
        pre[fx] = fy


a, b, p = map(int, input().split())
cnt = ans = 0
Prime = [0] * (b + 1)
is_prime = [True] * (b + 1)
get_prime(b)
pre = [i for i in range(b + 1)]

q = 1
for i in range(1, cnt + 1):
    if Prime[i] >= p:
        q = i
        break

for i in range(q, cnt + 1):
    tmp = 0
    while tmp * Prime[i] < a:
        tmp += 1
    while Prime[i] * (tmp + 1) <= b:
        join(Prime[i] * tmp, Prime[i] * (tmp + 1))
        tmp += 1

for i in range(a, b + 1):
    if pre[i] == i:
        ans += 1

print(ans)
