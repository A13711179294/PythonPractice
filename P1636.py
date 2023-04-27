n, m = map(int, input().split())
cnt = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    cnt[a] += 1
    cnt[b] += 1

ans = 0
for i in range(1, n + 1):
    if cnt[i] % 2 != 0:
        ans += 1

if ans == 0:
    print('1')
else:
    print(ans // 2)

